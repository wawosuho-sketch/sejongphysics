<script>
    import { onMount, onDestroy } from "svelte";
    import {
        whiteboardStore,
        saveDrawing,
        readDrawing,
        migrateDrawing,
    } from "../stores/whiteboardStore";

    export let drawingKey;
    export let legacyKey = null;

    let canvas;
    let ctx;
    let isDrawing = false;
    let container;
    let lastLoadedDataUrl = null;

    // Default configuration for different tools
    const toolConfig = {
        pen: {
            globalCompositeOperation: "source-over",
            getStrokeStyle: (color) => color,
            getLineWidth: (width) => width,
        },
        highlighter: {
            // Use standard blending since the canvas sits on top of DOM elements
            globalCompositeOperation: "source-over",
            // Always return a very light yellow transparent color to prevent blocking text
            getStrokeStyle: () => "rgba(255, 255, 0, 0.03)",
            getLineWidth: (width) => width * 4, // Thicker stroke for highlighting
        },
        eraser: {
            // "destination-out" removes pixels from the canvas to make it transparent
            globalCompositeOperation: "destination-out",
            getStrokeStyle: () => "rgba(0,0,0,1)",
            getLineWidth: (width) => width * 4, // 지우개 두께를 형광펜과 비슷하게 설정
        },
    };

    $: storeState = $whiteboardStore;

    $: savedDataUrl = readDrawing(
        storeState.slideDrawings,
        drawingKey,
        legacyKey,
    );

    // Reactive statement: Whenever savedDataUrl changes, load it into canvas
    // Wait for ctx and canvas to be ready
    $: if (ctx && canvas) {
        if (savedDataUrl && savedDataUrl !== lastLoadedDataUrl) {
            lastLoadedDataUrl = savedDataUrl;
            loadDrawing(savedDataUrl);
        } else if (!savedDataUrl) {
            lastLoadedDataUrl = null;
            // Clear canvas if no data
            clearCanvas();
        }
    }

    let resizeObserver;

    onMount(() => {
        // Use ResizeObserver instead of window resize to catch container size changes (e.g. image loads)
        resizeObserver = new ResizeObserver((entries) => {
            for (let entry of entries) {
                if (entry.target === container) {
                    handleResize();
                }
            }
        });

        if (container) {
            resizeObserver.observe(container);
        }

        migrateDrawing(drawingKey, legacyKey);
    });

    onDestroy(() => {
        if (resizeObserver) resizeObserver.disconnect();
    });

    // Handle container resizing (e.g., when the underlying image finally loads and sets height)
    function handleResize() {
        if (!container || !canvas) return;

        const rect = container.getBoundingClientRect();

        // Skip if dimensions are too small (e.g., before image load complete)
        if (rect.width < 10 || rect.height < 10) return;

        // If dimensions haven't changed, skip to avoid erasing
        if (
            canvas.width === Math.floor(rect.width) &&
            canvas.height === Math.floor(rect.height)
        )
            return;

        // Save current data (could be user drawing or just empty)
        const currentData = isDrawing ? canvas.toDataURL() : savedDataUrl;

        canvas.width = rect.width;
        canvas.height = rect.height;

        // Setup context strokes again
        ctx = canvas.getContext("2d");
        ctx.lineCap = "round";
        ctx.lineJoin = "round";

        // Restore image data scaled to new canvas
        if (currentData) {
            loadDrawing(currentData);
        }
    }

    function loadDrawing(dataUrl) {
        if (!ctx || !canvas || canvas.width === 0 || canvas.height === 0)
            return;

        const img = new Image();
        img.onload = () => {
            const tempComposite = ctx.globalCompositeOperation;
            ctx.globalCompositeOperation = "source-over"; // Reset for drawing image

            clearCanvas(); // Clear before drawing new image
            // Draw image scaled to fit current canvas size
            ctx.drawImage(img, 0, 0, canvas.width, canvas.height);

            ctx.globalCompositeOperation = tempComposite; // Restore
        };
        img.src = dataUrl;
    }

    function clearCanvas() {
        if (ctx && canvas) {
            ctx.clearRect(0, 0, canvas.width, canvas.height);
        }
    }

    function getCoords(e) {
        const rect = canvas.getBoundingClientRect();
        // Handle both touch and mouse events
        if (e.touches && e.touches.length > 0) {
            return {
                x: e.touches[0].clientX - rect.left,
                y: e.touches[0].clientY - rect.top,
            };
        }
        return {
            x: e.clientX - rect.left,
            y: e.clientY - rect.top,
        };
    }

    function startDrawing(e) {
        if (!storeState.isDrawingMode) return;

        // Allow 2-finger scroll
        if (e.touches && e.touches.length > 1) {
            isDrawing = false; // Cancel any active drawing
            return; // Let browser handle scroll
        }

        // Only left mouse button or single touch
        if (e.type === "mousedown" && e.button !== 0) return;

        e.preventDefault(); // Prevent scrolling on single touch drawing
        isDrawing = true;

        const { x, y } = getCoords(e);

        // Apply tool specific configuration
        const tool = toolConfig[storeState.currentTool] || toolConfig.pen;
        ctx.globalCompositeOperation = tool.globalCompositeOperation;
        ctx.strokeStyle = tool.getStrokeStyle(storeState.activeColor);
        ctx.lineWidth = tool.getLineWidth(storeState.activeWidth);

        ctx.beginPath();
        ctx.moveTo(x, y);
        // 그려지는 점을 위해 아주 짧은 선을 하나 그립니다 (클릭만 해도 점이 찍히거나 지워짐)
        ctx.lineTo(x, y + 0.1);
        ctx.stroke();
    }

    function draw(e) {
        if (!isDrawing || !storeState.isDrawingMode) return;

        // If it becomes a multi-touch gesture mid-draw, cancel drawing
        if (e.touches && e.touches.length > 1) {
            isDrawing = false;
            ctx.closePath();
            return;
        }

        e.preventDefault();

        const { x, y } = getCoords(e);
        ctx.lineTo(x, y);
        ctx.stroke();
    }

    function stopDrawing() {
        if (!isDrawing) return;
        isDrawing = false;
        ctx.closePath();

        const dataUrl = exportDrawing(canvas);
        lastLoadedDataUrl = dataUrl;
        saveDrawing(drawingKey, legacyKey, dataUrl);
    }

    function exportDrawing(source) {
        if (!source.width || !source.height) return source.toDataURL("image/png");
        const maxWidth = 1400;
        const scale = Math.min(1, maxWidth / source.width);
        const width = Math.max(1, Math.round(source.width * scale));
        const height = Math.max(1, Math.round(source.height * scale));
        const copy = document.createElement("canvas");
        copy.width = width;
        copy.height = height;
        copy.getContext("2d").drawImage(source, 0, 0, width, height);
        const webp = copy.toDataURL("image/webp", 0.8);
        if (webp.startsWith("data:image/webp")) return webp;
        return copy.toDataURL("image/png");
    }
</script>

<div
    class="canvas-container"
    bind:this={container}
    class:drawing-mode={storeState.isDrawingMode}
>
    <!-- svelte-ignore a11y-no-static-element-interactions -->
    <canvas
        bind:this={canvas}
        on:mousedown={startDrawing}
        on:mousemove={draw}
        on:mouseup={stopDrawing}
        on:mouseleave={stopDrawing}
        on:touchstart|nonpassive={startDrawing}
        on:touchmove|nonpassive={draw}
        on:touchend={stopDrawing}
        on:touchcancel={stopDrawing}
    ></canvas>
</div>

<style>
    .canvas-container {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        z-index: 50;
        /* Let clicks pass through when NOT drawing so underlying quizzes/videos work */
        pointer-events: none;
    }

    .canvas-container.drawing-mode {
        /* Enable interactions only in drawing mode */
        pointer-events: auto;
        cursor: crosshair;
    }

    canvas {
        display: block;
        width: 100%;
        height: 100%;
        touch-action: none; /* Prevent browser handling of pinch-zoom/pan on canvas */
    }
</style>
