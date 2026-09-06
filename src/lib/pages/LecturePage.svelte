<script>
    import { onMount, tick } from "svelte";
    import Simulation from "../components/Simulation.svelte";
    import Video from "../components/Video.svelte";
    import CanvasOverlay from "../components/CanvasOverlay.svelte";
    import ToggleQuiz from "../components/ToggleQuiz.svelte";
    import Callout from "../components/Callout.svelte";
    import {
        whiteboardStore,
        updateCurrentSlide,
    } from "../stores/whiteboardStore";

    import { getLectureMeta } from "../data/textbooks.js";

    export let navigate;
    export let lectureId = "01"; // Default or passed from App.svelte
    export let initialSlide = 1;

    let lectureData = [];
    let title = "로딩 중...";
    let subtitle = "데이터를 불러오는 중입니다.";
    let currentBookId = "physics";

    let observer;
    let lastHandledSlide = 0;

    let currentScrubberSlide = 1;
    let isScrubbing = false;

    $: {
        const meta = getLectureMeta(lectureId);
        title = meta.title;
        subtitle = meta.subtitle;
        currentBookId = meta.bookId || "physics";

        let dataFileName = lectureId;
        if (/^\d+$/.test(lectureId)) {
            dataFileName = `lecture_${lectureId.padStart(2, "0")}`;
        }

        import(`../data/${dataFileName}.js`)
            .then(async (module) => {
                lectureData = module.lectureData;
                lastHandledSlide = initialSlide;

                await tick(); // Wait for DOM to render
                setupObserver();

                if (initialSlide > 1) {
                    scrollToSlide(initialSlide);
                }
            })
            .catch((err) => {
                console.error("Lecture data not found for", dataFileName, err);
                lectureData = [];
            });
    }

    // React to browser Back/Forward updates
    $: {
        if (lectureData.length > 0 && initialSlide !== lastHandledSlide) {
            lastHandledSlide = initialSlide;
            scrollToSlide(initialSlide);
        }
    }

    function setupObserver() {
        if (observer) observer.disconnect();

        const options = {
            root: null,
            rootMargin: "0px",
            threshold: 0.5,
        };

        observer = new IntersectionObserver((entries) => {
            entries.forEach((entry) => {
                if (entry.isIntersecting) {
                    const slideIndex =
                        entry.target.getAttribute("data-slide-index");
                    if (slideIndex) {
                        const idx = parseInt(slideIndex, 10);
                        updateUrlSilently(idx);
                        updateCurrentSlide(lectureId, idx);
                        if (!isScrubbing) {
                            currentScrubberSlide = idx;
                        }
                    }
                }
            });
        }, options);

        setTimeout(() => {
            const items = document.querySelectorAll(".stream-item");
            items.forEach((item) => observer.observe(item));
        }, 100);
    }

    function scrollToSlide(index) {
        setTimeout(() => {
            const target = document.querySelector(
                `.stream-item[data-slide-index="${index}"]`,
            );
            if (target) {
                const yOffset = -120; // Account for the header
                const y =
                    target.getBoundingClientRect().top +
                    window.scrollY +
                    yOffset;
                window.scrollTo({ top: y, behavior: "smooth" });
            }
        }, 200);
    }

    function updateUrlSilently(slideIndex) {
        const url = new URL(window.location.href);
        if (url.searchParams.get("slide") !== slideIndex.toString()) {
            url.searchParams.set("slide", slideIndex);
            window.history.replaceState({}, "", url);
        }
    }

    function handleScrubInput(e) {
        currentScrubberSlide = parseInt(e.target.value, 10);
    }

    function handleScrubChange(e) {
        isScrubbing = true;
        const targetSlide = parseInt(e.target.value, 10);
        currentScrubberSlide = targetSlide;
        scrollToSlide(targetSlide);

        // Lock observer updates until scroll animation completes
        setTimeout(() => {
            isScrubbing = false;
        }, 600);
    }

    function handleKeyDown(e) {
        const tag = document.activeElement.tagName;
        const isTyping = ["INPUT", "TEXTAREA", "SELECT"].includes(tag);

        // D: toggle drawing mode (works even when total slides is 0)
        if (e.key === "d" || e.key === "D") {
            if (!isTyping) {
                e.preventDefault();
                whiteboardStore.update((s) => ({
                    ...s,
                    isDrawingMode: !s.isDrawingMode,
                }));
                return;
            }
        }

        // F: toggle fullscreen
        if (e.key === "f" || e.key === "F") {
            if (!isTyping) {
                e.preventDefault();
                if (!document.fullscreenElement) {
                    document.documentElement
                        .requestFullscreen()
                        .catch(() => {});
                } else {
                    document.exitFullscreen();
                }
                return;
            }
        }

        if (isTyping) return;

        const totalSlides = lectureData.length;
        if (totalSlides === 0) return;

        let nextSlide = currentScrubberSlide;

        switch (e.key) {
            case "ArrowRight":
            case "ArrowDown":
            case "PageDown":
            case " ":
            case "Enter":
                if (currentScrubberSlide < totalSlides) {
                    nextSlide = currentScrubberSlide + 1;
                }
                break;
            case "ArrowLeft":
            case "ArrowUp":
            case "PageUp":
            case "Backspace":
                if (currentScrubberSlide > 1) {
                    nextSlide = currentScrubberSlide - 1;
                }
                break;
            case "Home":
                nextSlide = 1;
                break;
            case "End":
                nextSlide = totalSlides;
                break;
            default:
                return;
        }

        if (nextSlide !== currentScrubberSlide) {
            e.preventDefault();
            currentScrubberSlide = nextSlide;
            scrollToSlide(nextSlide);
        }
    }

    onMount(() => {
        window.addEventListener("keydown", handleKeyDown);
        return () => {
            window.removeEventListener("keydown", handleKeyDown);
        };
    });

    import { formatMathText } from "../utils/katexHelper.js";

    // Fast-Design Aesthetic Configuration
    const theme = {
        background: "#0b0f19",
        text: "#f8fafc",
        accent: "#4f46e5",
        secondary: "#1e293b",
    };
</script>

<main style="background-color: {theme.background}; color: {theme.text}">
    <header>
        <button class="back-btn" on:click={() => navigate("home", 1, currentBookId)}>
            ← 전체 목록으로 돌아가기
        </button>
        <h1>{title}</h1>
        <p>{subtitle}</p>
    </header>

    <div class="content-stream">
        {#if lectureData.length === 0}
            <div style="text-align: center; padding: 4rem; color: #94a3b8;">
                강의 데이터를 불러오는 중이거나 찾을 수 없습니다.
            </div>
        {/if}

        {#each lectureData as item, index}
            <div
                class="stream-item"
                data-slide-index={index + 1}
                style="position: relative;"
            >
                <CanvasOverlay {lectureId} slideIndex={index + 1} />
                {#if item.type === "title"}
                    <h2 class="section-title">{@html formatMathText(item.text)}</h2>
                {:else if item.type === "section_header"}
                    <div class="section-banner">
                        <span class="section-badge">{item.chapter || 'PART'}</span>
                        <h2>{@html formatMathText(item.title)}</h2>
                        {#if item.subtitle}
                            <p>{@html formatMathText(item.subtitle)}</p>
                        {/if}
                    </div>
                {:else if item.type === "image"}
                    <div class="image-wrapper">
                        <img
                            src={import.meta.env.BASE_URL +
                                (item.src.startsWith("/")
                                    ? item.src.slice(1)
                                    : item.src)}
                            alt={`Slide ${index + 1}`}
                        />
                    </div>
                {:else if item.type === "video"}
                    <div class="interactive-wrapper">
                        <h3 class="interactive-title">
                            📺 추천 영상: {item.title || "개념 영상"}
                        </h3>
                        <Video src={item.src} title={item.title} />
                    </div>
                {:else if item.type === "simulation"}
                    <div class="interactive-wrapper">
                        <h3 class="interactive-title">🔬 직접 실험해보기</h3>
                        <p class="interactive-desc">
                            마우스로 요소를 드래그하며 변화를 관찰해보세요.
                        </p>
                        <Simulation
                            src={item.src}
                            title={item.title}
                            height={item.height}
                        />
                    </div>
                {:else if item.type === "quiz"}
                    <div class="quiz-wrapper">
                        <ToggleQuiz
                            question={item.question}
                            answer={item.answer}
                            title={item.title}
                        />
                    </div>
                {:else if item.type === "callout"}
                    <Callout type={item.style || "info"} title={item.title} content={item.content} />
                {/if}
            </div>
        {/each}
    </div>

    <footer class="lecture-footer">
        <div class="footer-content">
            <h3>🎉 {lectureId}강 학습을 완료하셨습니다!</h3>
            <p>다음 강의로 돌아가 물리학의 세계를 계속 탐험해보세요.</p>
            <button class="primary-btn" on:click={() => navigate("home", 1, currentBookId)}>
                목록으로 가기
            </button>
        </div>
    </footer>

    <!-- Premium Scrubber UI -->
    {#if lectureData.length > 0}
        <div class="scrubber-container">
            <div class="scrubber-info">
                <span class="scrub-label">슬라이드 탐색</span>
                <span class="scrub-count"
                    >{currentScrubberSlide}
                    <span class="scrub-total">/ {lectureData.length}</span
                    ></span
                >
            </div>
            <input
                type="range"
                class="scrub-slider"
                min="1"
                max={lectureData.length}
                value={currentScrubberSlide}
                on:input={handleScrubInput}
                on:change={handleScrubChange}
                style="--progress: {((currentScrubberSlide - 1) /
                    Math.max(1, lectureData.length - 1)) *
                    100}%"
            />
        </div>
    {/if}
</main>

<style>
    main {
        min-height: 100vh;
        font-family:
            "Pretendard",
            -apple-system,
            BlinkMacSystemFont,
            "Segoe UI",
            Roboto,
            sans-serif;
        padding-bottom: 8rem; /* Extra padding for scrubber */
    }

    header {
        background: linear-gradient(135deg, #111827 0%, #0b0f19 100%);
        padding: 3rem 2rem 4rem;
        text-align: center;
        border-bottom: 2px solid #1e293b;
        position: relative;
        overflow: hidden;
    }

    header::after {
        content: "";
        position: absolute;
        bottom: -50px;
        left: 50%;
        transform: translateX(-50%);
        width: 300px;
        height: 100px;
        background: rgba(79, 70, 229, 0.4);
        filter: blur(50px);
        pointer-events: none;
    }

    .back-btn {
        position: absolute;
        top: 2rem;
        left: 2rem;
        background: transparent;
        border: 1px solid #334155;
        color: #94a3b8;
        padding: 0.5rem 1rem;
        border-radius: 8px;
        cursor: pointer;
        font-size: 0.9rem;
        transition: all 0.2s ease;
        z-index: 10;
    }

    .back-btn:hover {
        background: #1e293b;
        color: #fff;
        border-color: #4f46e5;
    }

    h1 {
        font-size: 2.5rem;
        font-weight: 800;
        margin: 0 0 0.5rem 0;
        color: #f8fafc;
        position: relative;
        z-index: 1;
    }

    header p {
        color: #94a3b8;
        font-size: 1.1rem;
        margin: 0;
        position: relative;
        z-index: 1;
    }

    .content-stream {
        max-width: 850px;
        margin: -2rem auto 0; /* Pull up into header */
        padding: 0 1.5rem;
        position: relative;
        display: flex;
        flex-direction: column;
        gap: 3rem;
    }

    .stream-item {
        width: 100%;
        animation: fadeIn 0.5s ease-out forwards;
    }

    .section-banner {
        background: linear-gradient(135deg, rgba(79, 70, 229, 0.25) 0%, rgba(168, 85, 247, 0.25) 100%);
        border: 1px solid rgba(129, 140, 248, 0.3);
        border-radius: 16px;
        padding: 2rem;
        margin: 3rem 0 1.5rem;
        position: relative;
        backdrop-filter: blur(10px);
        box-shadow: 0 10px 30px -5px rgba(79, 70, 229, 0.2);
    }

    .section-badge {
        display: inline-block;
        background: #4f46e5;
        color: #fff;
        font-size: 0.75rem;
        font-weight: 800;
        letter-spacing: 1.5px;
        padding: 0.25rem 0.75rem;
        border-radius: 50px;
        margin-bottom: 0.8rem;
    }

    .section-banner h2 {
        margin: 0 0 0.5rem 0;
        font-size: 1.8rem;
        font-weight: 800;
        color: #ffffff;
        letter-spacing: -0.5px;
    }

    .section-banner p {
        margin: 0;
        color: #cbd5e1;
        font-size: 1rem;
        line-height: 1.5;
    }

    .section-title {
        font-size: 1.8rem;
        font-weight: 700;
        color: #f8fafc;
        margin: 2rem 0 1rem;
        padding-bottom: 0.5rem;
        border-bottom: 2px solid #1e293b;
    }

    .image-wrapper {
        position: relative;
        width: 100%;
        border-radius: 16px;
        overflow: hidden;
        box-shadow: 0 12px 30px -5px rgba(0, 0, 0, 0.6);
        border: 1px solid rgba(255, 255, 255, 0.1);
        background: #111827;
        transition: transform 0.3s cubic-bezier(0.2, 0.8, 0.2, 1), border-color 0.3s, box-shadow 0.3s;
    }

    .image-wrapper.zoomable {
        cursor: zoom-in;
    }

    .image-wrapper.zoomable:hover {
        transform: translateY(-4px) scale(1.01);
        border-color: rgba(99, 102, 241, 0.6);
        box-shadow: 0 20px 40px -10px rgba(79, 70, 229, 0.4);
    }

    .image-wrapper img {
        width: 100%;
        height: auto;
        display: block;
    }

    .interactive-wrapper {
        background: #111827;
        border: 1px solid #334155;
        border-radius: 16px;
        padding: 1.5rem;
        box-shadow: 0 0 40px -10px rgba(79, 70, 229, 0.15);
    }

    .interactive-title {
        margin: 0 0 0.5rem 0;
        color: #e2e8f0;
        font-size: 1.25rem;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }

    .interactive-desc {
        color: #94a3b8;
        font-size: 0.95rem;
        margin: 0 0 1.5rem 0;
    }

    .quiz-wrapper {
        margin: 1rem 0;
    }

    .lecture-footer {
        max-width: 600px;
        margin: 4rem auto 0;
        text-align: center;
        padding: 3rem;
        background: #111827;
        border: 1px solid #1e293b;
        border-radius: 20px;
        box-shadow: 0 20px 40px -10px rgba(0, 0, 0, 0.3);
    }

    .lecture-footer h3 {
        font-size: 1.8rem;
        margin: 0 0 1rem 0;
        background: linear-gradient(135deg, #a855f7 0%, #4f46e5 100%);
        -webkit-background-clip: text;
        background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    .lecture-footer p {
        color: #94a3b8;
        margin: 0 0 2rem 0;
    }

    .primary-btn {
        background: linear-gradient(135deg, #4f46e5 0%, #a855f7 100%);
        color: white;
        border: none;
        padding: 1rem 2.5rem;
        font-size: 1.1rem;
        font-weight: 700;
        border-radius: 999px;
        cursor: pointer;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(79, 70, 229, 0.4);
    }

    .primary-btn:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(79, 70, 229, 0.6);
    }

    @keyframes fadeIn {
        from {
            opacity: 0;
            transform: translateY(20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }

    @media (max-width: 768px) {
        header {
            padding: 4rem 1rem 3rem;
        }
        .back-btn {
            top: 1rem;
            left: 1rem;
        }
        h1 {
            font-size: 2rem;
        }
        .content-stream {
            padding: 0 1rem;
            gap: 2rem;
        }
        .scrubber-container {
            padding: 1rem;
        }
    }

    /* Scrubber Styles */
    .scrubber-container {
        position: fixed;
        bottom: 0;
        left: 0;
        right: 0;
        background: rgba(11, 15, 25, 0.85);
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        border-top: 1px solid rgba(255, 255, 255, 0.08);
        padding: 1.2rem 2rem 1.5rem;
        z-index: 100;
        display: flex;
        flex-direction: column;
        gap: 0.8rem;
        box-shadow: 0 -10px 30px rgba(0, 0, 0, 0.5);
    }

    .scrubber-info {
        display: flex;
        justify-content: space-between;
        align-items: center;
        max-width: 850px;
        margin: 0 auto;
        width: 100%;
    }

    .scrub-label {
        color: #94a3b8;
        font-size: 0.95rem;
        font-weight: 500;
        letter-spacing: -0.5px;
    }

    .scrub-count {
        color: #f8fafc;
        font-weight: 800;
        font-size: 1.2rem;
        font-variant-numeric: tabular-nums;
        text-shadow: 0 2px 4px rgba(0, 0, 0, 0.5);
    }

    .scrub-total {
        color: #64748b;
        font-weight: 600;
        font-size: 0.95rem;
    }

    .scrub-slider {
        -webkit-appearance: none;
        appearance: none;
        width: 100%;
        max-width: 850px;
        margin: 0 auto;
        height: 6px;
        border-radius: 6px;
        background: rgba(255, 255, 255, 0.1);
        outline: none;
        cursor: pointer;
        position: relative;
    }

    /* Track fill via CSS variable */
    .scrub-slider::before {
        content: "";
        position: absolute;
        top: 0;
        left: 0;
        height: 100%;
        width: var(--progress, 0%);
        background: linear-gradient(90deg, #4f46e5, #059669);
        border-radius: 6px;
        transition: width 0.1s linear;
        pointer-events: none;
    }

    .scrub-slider::-webkit-slider-thumb {
        -webkit-appearance: none;
        appearance: none;
        width: 22px;
        height: 22px;
        border-radius: 50%;
        background: #fff;
        cursor: pointer;
        transition:
            transform 0.2s cubic-bezier(0.2, 0.8, 0.2, 1),
            box-shadow 0.2s;
        box-shadow:
            0 0 10px rgba(0, 0, 0, 0.3),
            0 0 0 4px rgba(255, 255, 255, 0.1);
        position: relative;
        z-index: 2;
    }

    .scrub-slider::-webkit-slider-thumb:hover,
    .scrub-slider:active::-webkit-slider-thumb {
        transform: scale(1.3);
        box-shadow:
            0 0 15px rgba(168, 85, 247, 0.5),
            0 0 0 6px rgba(255, 255, 255, 0.15);
    }

    .scrub-slider::-moz-range-thumb {
        width: 22px;
        height: 22px;
        border-radius: 50%;
        background: #fff;
        cursor: pointer;
        transition:
            transform 0.2s cubic-bezier(0.2, 0.8, 0.2, 1),
            box-shadow 0.2s;
        box-shadow:
            0 0 10px rgba(0, 0, 0, 0.3),
            0 0 0 4px rgba(255, 255, 255, 0.1);
        border: none;
        position: relative;
        z-index: 2;
    }
</style>
