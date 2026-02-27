<script>
    import { whiteboardStore } from "../stores/whiteboardStore";

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

    // Default colors for physics
    const colors = [
        { name: "Black", hex: "#0f172a" },
        { name: "Red", hex: "#ef4444" },
        { name: "Blue", hex: "#3b82f6" },
        { name: "Green", hex: "#10b981" },
    ];
    // File logic
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
        const exportFileDefaultName = `physics_notes_${timestamp}.json`;

        let linkElement = document.createElement("a");
        linkElement.setAttribute("href", dataUri);
        linkElement.setAttribute("download", exportFileDefaultName);
        linkElement.click();
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
                alert("필기 데이터를 성공적으로 불러왔습니다!");
            } catch (error) {
                alert("잘못된 필기 파일입니다.");
                console.error("Import error:", error);
            }
        };
        reader.readAsText(file);

        // Reset input so the same file can be loaded again if needed
        event.target.value = "";
    }
</script>

<div class="toolbar-container" class:active={state.isDrawingMode}>
    <!-- Hidden File Input for Import -->
    <input
        type="file"
        accept=".json"
        bind:this={fileInput}
        on:change={handleImport}
        style="display: none;"
    />

    <!-- Main Toggle Buttons -->
    <div class="main-toggles">
        <button
            class="toggle-btn"
            class:is-active={state.isDrawingMode}
            on:click={toggleDrawingMode}
            title={state.isDrawingMode ? "필기 끄기 (보기 모드)" : "필기 켜기"}
        >
            {#if state.isDrawingMode}
                ✏️
            {:else}
                📖
            {/if}
        </button>

        <button
            class="toggle-btn"
            on:click={() => {
                if (!document.fullscreenElement) {
                    document.documentElement
                        .requestFullscreen()
                        .catch((err) => {
                            console.error(
                                `Error attempting to enable full-screen mode: ${err.message} (${err.name})`,
                            );
                        });
                } else {
                    document.exitFullscreen();
                }
            }}
            title="전체화면 전환"
        >
            🔲
        </button>
    </div>

    {#if state.isDrawingMode}
        <div class="tools-panel">
            <!-- Data Management (Export/Import) -->
            <div class="tool-group action-group">
                <button
                    class="action-btn"
                    on:click={exportDrawings}
                    title="필기 저장하기 (Export)"
                >
                    💾
                </button>
                <div class="divider"></div>
                <button
                    class="action-btn"
                    on:click={triggerImport}
                    title="필기 불러오기 (Import)"
                >
                    📂
                </button>
            </div>

            <!-- Tools -->
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

            <!-- Colors (Only show if PEN or HIGHLIGHTER) -->
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
        </div>
    {/if}
</div>

<style>
    .toolbar-container {
        position: fixed;
        bottom: 2rem;
        right: 2rem;
        z-index: 9999;
        display: flex;
        flex-direction: column-reverse;
        align-items: flex-end;
        gap: 1rem;
        font-family:
            "Pretendard",
            -apple-system,
            sans-serif;
    }

    .main-toggles {
        display: flex;
        gap: 0.5rem;
    }

    .toggle-btn {
        background: #1e293b;
        color: #f8fafc;
        border: 2px solid #334155;
        border-radius: 50%;
        width: 3.5rem;
        height: 3.5rem;
        font-size: 1.5rem;
        display: flex;
        justify-content: center;
        align-items: center;
        cursor: pointer;
        box-shadow: 0 8px 20px -5px rgba(0, 0, 0, 0.5);
        transition: all 0.2s ease;
    }

    .toggle-btn:hover {
        transform: translateY(-2px);
        box-shadow: 0 15px 30px -5px rgba(0, 0, 0, 0.6);
        border-color: #475569;
    }

    .toggle-btn.is-active {
        background: linear-gradient(135deg, #4f46e5 0%, #a855f7 100%);
        border-color: transparent;
        box-shadow: 0 10px 25px rgba(79, 70, 229, 0.4);
    }

    .tools-panel {
        background: rgba(15, 23, 42, 0.95);
        backdrop-filter: blur(10px);
        border: 1px solid #334155;
        border-radius: 12px;
        padding: 0.75rem;
        display: flex;
        flex-direction: column;
        gap: 0.75rem;
        box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.6);
        animation: slideUp 0.3s cubic-bezier(0.16, 1, 0.3, 1);
    }

    .tool-group {
        display: flex;
        gap: 0.5rem;
        background: #1e293b;
        padding: 0.5rem;
        border-radius: 12px;
    }

    .action-group {
        justify-content: space-around;
        padding: 0.5rem;
    }

    .action-btn {
        background: transparent;
        border: none;
        color: #e2e8f0;
        font-size: 1.5rem;
        padding: 0.5rem;
        border-radius: 8px;
        cursor: pointer;
        transition: all 0.2s;
        display: flex;
        align-items: center;
        justify-content: center;
        flex: 1;
    }

    .action-btn:hover {
        background: rgba(255, 255, 255, 0.1);
        color: #fff;
    }

    .divider {
        width: 1px;
        background: #334155;
        margin: 0.2rem 0;
    }

    .tool-btn {
        background: transparent;
        border: none;
        color: #94a3b8;
        font-size: 1.5rem;
        width: 3rem;
        height: 3rem;
        border-radius: 8px;
        cursor: pointer;
        transition: all 0.2s;
        display: flex;
        align-items: center;
        justify-content: center;
    }

    .tool-btn:hover {
        background: rgba(255, 255, 255, 0.1);
        color: #f8fafc;
    }

    .tool-btn.active {
        background: #334155;
        color: #fff;
        box-shadow: inset 0 2px 4px rgba(0, 0, 0, 0.2);
    }

    .color-picker {
        display: flex;
        gap: 0.8rem;
        justify-content: center;
        padding: 0.5rem;
    }

    .color-swatch {
        width: 2rem;
        height: 2rem;
        border-radius: 50%;
        border: 2px solid #1e293b;
        cursor: pointer;
        transition: all 0.2s;
        outline: none;
    }

    .color-swatch:hover {
        transform: scale(1.15);
    }

    .color-swatch.active {
        border-color: #fff;
        transform: scale(1.15);
        box-shadow: 0 0 10px rgba(255, 255, 255, 0.4);
    }

    @keyframes slideUp {
        from {
            opacity: 0;
            transform: translateY(20px) scale(0.95);
        }
        to {
            opacity: 1;
            transform: translateY(0) scale(1);
        }
    }

    @media (max-width: 768px) {
        .toolbar-container {
            bottom: 1.5rem;
            right: 1.5rem;
            /* In mobile, if LecturePage scrubber is at the bottom, we might need to place this higher */
        }
    }
</style>
