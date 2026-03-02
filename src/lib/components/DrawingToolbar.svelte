<script>
    import { whiteboardStore, clearDrawing } from "../stores/whiteboardStore";

    $: state = $whiteboardStore;

    function toggleDrawingMode() {
        whiteboardStore.update((s) => ({
            ...s,
            isDrawingMode: !s.isDrawingMode,
        }));
    }

    function changeTool(tool) {
        whiteboardStore.update((s) => ({ ...s, currentTool: tool }));
    }

    function changeColor(color) {
        whiteboardStore.update((s) => ({
            ...s,
            activeColor: color,
            currentTool: "pen",
        }));
    }

    function clearCurrentSlide() {
        if (state.currentLectureId && state.currentSlideIndex) {
            clearDrawing(state.currentLectureId, state.currentSlideIndex);
        }
    }

    function toggleFullscreen() {
        if (!document.fullscreenElement) {
            document.documentElement.requestFullscreen().catch(() => {});
        } else {
            document.exitFullscreen();
        }
    }

    const colors = [
        { name: "검정", hex: "#0f172a" },
        { name: "빨강", hex: "#ef4444" },
        { name: "파랑", hex: "#3b82f6" },
        { name: "초록", hex: "#10b981" },
    ];

    let fileInput;

    function exportDrawings() {
        const dataStr = JSON.stringify(state.slideDrawings);
        const dataUri =
            "data:application/json;charset=utf-8," +
            encodeURIComponent(dataStr);
        const timestamp = new Date()
            .toISOString()
            .replace(/T/, "_")
            .replace(/:/g, "-")
            .split(".")[0];
        let a = document.createElement("a");
        a.setAttribute("href", dataUri);
        a.setAttribute("download", `physics_notes_${timestamp}.json`);
        a.click();
    }

    function triggerImport() {
        if (fileInput) fileInput.click();
    }

    function handleImport(event) {
        const file = event.target.files[0];
        if (!file) return;
        const reader = new FileReader();
        reader.onload = (e) => {
            try {
                const importedData = JSON.parse(
                    String(e.target?.result || "{}"),
                );
                whiteboardStore.update((s) => {
                    const mergedData = { ...s.slideDrawings, ...importedData };
                    localStorage.setItem(
                        "textbookLayoutDrawings",
                        JSON.stringify(mergedData),
                    );
                    return { ...s, slideDrawings: mergedData };
                });
                showToast("필기를 불러왔습니다 ✅");
            } catch {
                showToast("잘못된 파일입니다 ❌");
            }
        };
        reader.readAsText(file);
        event.target.value = "";
    }

    // Toast notification
    let toastMsg = "";
    let toastTimer;
    function showToast(msg) {
        toastMsg = msg;
        clearTimeout(toastTimer);
        toastTimer = setTimeout(() => (toastMsg = ""), 2500);
    }

    $: hasCurrentSlideDrawing =
        state.currentLectureId &&
        state.currentSlideIndex &&
        !!state.slideDrawings[
            `${state.currentLectureId}_${state.currentSlideIndex}`
        ];
</script>

<!-- Hidden File Input -->
<input
    type="file"
    accept=".json"
    bind:this={fileInput}
    on:change={handleImport}
    style="display:none;"
/>

<!-- Toast -->
{#if toastMsg}
    <div class="toast">{toastMsg}</div>
{/if}

<div class="toolbar-container" class:active={state.isDrawingMode}>
    <!-- Main Toggle Buttons -->
    <div class="main-toggles">
        <button
            class="toggle-btn"
            class:is-active={state.isDrawingMode}
            on:click={toggleDrawingMode}
            title={state.isDrawingMode ? "필기 끄기 [D]" : "필기 켜기 [D]"}
        >
            {#if state.isDrawingMode}✏️{:else}📖{/if}
        </button>

        <button
            class="toggle-btn"
            on:click={toggleFullscreen}
            title="전체화면 [F]"
        >
            🔲
        </button>
    </div>

    {#if state.isDrawingMode}
        <div class="tools-panel">
            <!-- Row 1: save / load / clear current slide -->
            <div class="tool-group action-group">
                <button
                    class="action-btn"
                    on:click={exportDrawings}
                    title="필기 저장 (JSON)"
                >
                    💾
                </button>
                <div class="divider"></div>
                <button
                    class="action-btn"
                    on:click={triggerImport}
                    title="필기 불러오기"
                >
                    📂
                </button>
                {#if hasCurrentSlideDrawing}
                    <div class="divider"></div>
                    <button
                        class="action-btn danger"
                        on:click={clearCurrentSlide}
                        title="이 슬라이드 필기 지우기"
                    >
                        🗑️
                    </button>
                {/if}
            </div>

            <!-- Row 2: Tools -->
            <div class="tool-group">
                <button
                    class="tool-btn"
                    class:active={state.currentTool === "pen"}
                    on:click={() => changeTool("pen")}
                    title="펜"
                >
                    🖋️
                </button>
                <button
                    class="tool-btn"
                    class:active={state.currentTool === "highlighter"}
                    on:click={() => changeTool("highlighter")}
                    title="형광펜"
                >
                    🖍️
                </button>
                <button
                    class="tool-btn"
                    class:active={state.currentTool === "eraser"}
                    on:click={() => changeTool("eraser")}
                    title="지우개"
                >
                    🧽
                </button>
            </div>

            <!-- Row 3: Colors (when not eraser) -->
            {#if state.currentTool !== "eraser"}
                <div class="color-picker">
                    {#each colors as color}
                        <button
                            class="color-swatch"
                            class:active={state.activeColor === color.hex}
                            style="background-color: {color.hex};"
                            on:click={() => changeColor(color.hex)}
                            title={color.name}
                            aria-label={color.name}
                        ></button>
                    {/each}
                </div>
            {/if}

            <!-- Shortcut hints -->
            <div class="shortcut-hints">
                <span>D: 필기 켜기/끄기</span>
                <span>F: 전체화면</span>
            </div>
        </div>
    {/if}
</div>

<style>
    .toolbar-container {
        position: fixed;
        bottom: 5.5rem; /* Clear the lecture scrubber (≈80px) */
        right: 1.5rem;
        z-index: 9999;
        display: flex;
        flex-direction: column-reverse;
        align-items: flex-end;
        gap: 0.75rem;
        font-family:
            "Pretendard",
            -apple-system,
            sans-serif;
    }

    /* On pages without a scrubber (home), keep near the bottom */
    .toolbar-container:not(.active) {
        bottom: 1.5rem;
    }

    .main-toggles {
        display: flex;
        gap: 0.4rem;
    }

    .toggle-btn {
        background: #1e293b;
        color: #f8fafc;
        border: 2px solid #334155;
        border-radius: 50%;
        width: 3rem;
        height: 3rem;
        font-size: 1.3rem;
        display: flex;
        justify-content: center;
        align-items: center;
        cursor: pointer;
        box-shadow: 0 6px 16px -4px rgba(0, 0, 0, 0.5);
        transition: all 0.2s ease;
    }

    .toggle-btn:hover {
        transform: translateY(-2px);
        border-color: #475569;
    }

    .toggle-btn.is-active {
        background: linear-gradient(135deg, #4f46e5, #a855f7);
        border-color: transparent;
        box-shadow: 0 8px 20px rgba(79, 70, 229, 0.45);
    }

    .tools-panel {
        background: rgba(15, 23, 42, 0.96);
        backdrop-filter: blur(10px);
        border: 1px solid #334155;
        border-radius: 12px;
        padding: 0.6rem;
        display: flex;
        flex-direction: column;
        gap: 0.5rem;
        box-shadow: 0 8px 24px -4px rgba(0, 0, 0, 0.6);
        animation: slideUp 0.25s cubic-bezier(0.16, 1, 0.3, 1);
    }

    .tool-group {
        display: flex;
        gap: 0.35rem;
        background: #1e293b;
        padding: 0.4rem;
        border-radius: 10px;
    }

    .action-group {
        justify-content: space-around;
    }

    .action-btn {
        background: transparent;
        border: none;
        font-size: 1.2rem;
        padding: 0.35rem;
        border-radius: 8px;
        cursor: pointer;
        transition: background 0.15s;
        flex: 1;
        display: flex;
        align-items: center;
        justify-content: center;
    }

    .action-btn:hover {
        background: rgba(255, 255, 255, 0.1);
    }

    .action-btn.danger:hover {
        background: rgba(239, 68, 68, 0.2);
    }

    .divider {
        width: 1px;
        background: #334155;
        margin: 0.15rem 0;
    }

    .tool-btn {
        background: transparent;
        border: none;
        font-size: 1.3rem;
        width: 2.6rem;
        height: 2.6rem;
        border-radius: 8px;
        cursor: pointer;
        transition: all 0.15s;
        display: flex;
        align-items: center;
        justify-content: center;
        color: #94a3b8;
    }

    .tool-btn:hover {
        background: rgba(255, 255, 255, 0.08);
        color: #f8fafc;
    }

    .tool-btn.active {
        background: #334155;
        color: #fff;
    }

    .color-picker {
        display: flex;
        gap: 0.5rem;
        justify-content: center;
        padding: 0.3rem 0.4rem;
    }

    .color-swatch {
        width: 1.6rem;
        height: 1.6rem;
        border-radius: 50%;
        border: 2px solid #1e293b;
        cursor: pointer;
        transition: all 0.15s;
        outline: none;
    }

    .color-swatch:hover {
        transform: scale(1.18);
    }

    .color-swatch.active {
        border-color: #fff;
        transform: scale(1.18);
        box-shadow: 0 0 8px rgba(255, 255, 255, 0.4);
    }

    .shortcut-hints {
        display: flex;
        gap: 0.5rem;
        padding: 0.2rem 0.4rem;
        justify-content: center;
        flex-wrap: wrap;
    }

    .shortcut-hints span {
        font-size: 0.62rem;
        color: #475569;
        font-weight: 500;
        letter-spacing: 0.2px;
    }

    /* Toast */
    .toast {
        position: fixed;
        bottom: 9rem;
        right: 1.5rem;
        background: #1e293b;
        color: #f8fafc;
        border: 1px solid #334155;
        border-radius: 10px;
        padding: 0.5rem 1rem;
        font-size: 0.9rem;
        z-index: 10000;
        box-shadow: 0 4px 16px rgba(0, 0, 0, 0.4);
        animation: slideUp 0.2s ease;
    }

    @keyframes slideUp {
        from {
            opacity: 0;
            transform: translateY(12px) scale(0.96);
        }
        to {
            opacity: 1;
            transform: translateY(0) scale(1);
        }
    }

    /* Tablet: already compact by default. On large desktops, slightly bigger */
    @media (min-width: 1280px) {
        .toggle-btn {
            width: 3.5rem;
            height: 3.5rem;
            font-size: 1.5rem;
        }
        .tool-btn {
            width: 3rem;
            height: 3rem;
            font-size: 1.5rem;
        }
        .action-btn {
            font-size: 1.4rem;
        }
        .color-swatch {
            width: 2rem;
            height: 2rem;
        }
        .toolbar-container {
            right: 2rem;
            bottom: 6rem;
        }
        .toolbar-container:not(.active) {
            bottom: 2rem;
        }
    }
</style>
