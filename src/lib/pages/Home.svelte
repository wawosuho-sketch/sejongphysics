<script>
    import { fade, fly } from "svelte/transition";
    import { onMount } from "svelte";
    import { textbooks } from "../data/textbooks.js";

    export let navigate;
    export let initialBookId = "physics";

    let selectedBookId = initialBookId || "physics";

    // 해설지 공개 기간 (3주 뒤인 2026-05-01 00:00:00 까지)
    const isSolutionVisible = new Date() < new Date("2026-05-01T00:00:00+09:00");

    $: activeBook = textbooks.find(b => b.id === selectedBookId) || textbooks[0];
    $: lectures = activeBook.lectures;
    $: problems = activeBook.problems;

    $: if (initialBookId && textbooks.some(b => b.id === initialBookId)) {
        selectedBookId = initialBookId;
    }

    onMount(() => {
        const params = new URLSearchParams(window.location.search);
        const bookParam = params.get("book");
        const savedBook = localStorage.getItem("selectedBookId");
        if (bookParam && textbooks.some(b => b.id === bookParam)) {
            selectedBookId = bookParam;
        } else if (savedBook && textbooks.some(b => b.id === savedBook)) {
            selectedBookId = savedBook;
        }
    });

    function selectBook(id) {
        selectedBookId = id;
        localStorage.setItem("selectedBookId", id);
        const url = new URL(window.location.href);
        url.searchParams.set("book", id);
        window.history.replaceState({}, "", url);
    }
</script>

<div class="home-container">
    <!-- Textbook Selector Navigation Bar -->
    <nav class="textbook-nav">
        <div class="nav-content">
            <span class="nav-label">교과서 선택:</span>
            <div class="tab-group">
                {#each textbooks as book}
                    <button
                        class="tab-btn"
                        class:active={selectedBookId === book.id}
                        on:click={() => selectBook(book.id)}
                    >
                        <span class="tab-name">{book.name}</span>
                        <span class="tab-badge">{book.lectures.length}강</span>
                    </button>
                {/each}
            </div>
        </div>
    </nav>

    <!-- Hero Section -->
    <section class="hero hero-animate">
        <div class="hero-content">
            <span class="badge">{activeBook.badge}</span>
            <h1>
                미래를 여는<br /><span class="gradient-text">{activeBook.name} 교과서</span
                >
            </h1>
            <p class="school-name">{activeBook.school} — {activeBook.description}</p>
            <div class="hero-decoration"></div>
        </div>
    </section>

    <!-- Action Center (Hidden per user request: 교과서 변경에 따른 숨김 처리) -->
    {#if false}
    <section class="action-center action-animate">
        <div class="action-grid">
            <!-- Homework Submission -->
            <a href={activeBook.homeworkUrl} target="_blank" rel="noopener noreferrer" class="action-card primary-action">
                <div class="action-icon">📝</div>
                <div class="action-content">
                    <h3>과제 제출하기</h3>
                    <p>Clipo AI 플랫폼으로 이동하여 부여받은 과제를 제출합니다.</p>
                </div>
                <div class="action-arrow">
                    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14"></path><path d="m12 5 7 7-7 7"></path></svg>
                </div>
            </a>

            <!-- Physics Problems -->
            <div class="action-card secondary-action">
                <div class="action-header">
                    <div class="action-icon">📚</div>
                    <div class="action-content">
                        <h3>{activeBook.name} 문제 모음</h3>
                        <p>주요 단원별 기출 및 연습 문제를 새 창에서 열어 풀어보세요.</p>
                    </div>
                </div>
                <div class="download-buttons">
                    {#each problems as prob}
                        <div class="problem-group">
                            <a href="{import.meta.env.BASE_URL}{prob.pdf}" target="_blank" rel="noopener noreferrer" class="dl-btn">{prob.title}</a>
                            {#if isSolutionVisible && prob.solution}
                                <a href="{import.meta.env.BASE_URL}{prob.solution}" target="_blank" rel="noopener noreferrer" class="dl-btn solution-btn">해설</a>
                            {/if}
                        </div>
                    {/each}
                </div>
            </div>
        </div>
    </section>
    {/if}

    <!-- Lecture Grid -->
    <section class="lecture-section">
        <div class="section-header">
            <h2>{activeBook.name} 강의 커리큘럼</h2>
            <div class="header-line"></div>
        </div>

        <div class="lecture-grid">
            {#each lectures as lecture, i (lecture.fullId || lecture.id)}
                <button
                    class="lecture-card card-animate"
                    style="--accent-color: {lecture.accent}; animation-delay: {i *
                        100}ms;"
                    on:click={() => navigate(`lecture_${lecture.fullId || lecture.id}`, 1, activeBook.id)}
                >
                    {#if lecture.image}
                        <img
                            src={import.meta.env.BASE_URL +
                                (lecture.image.startsWith("/")
                                    ? lecture.image.slice(1)
                                    : lecture.image)}
                            alt={lecture.title}
                            class="card-bg-image"
                        />
                    {/if}
                    <div class="card-overlay"></div>

                    <div class="card-content">
                        <div class="card-top">
                            <span class="tag">{lecture.tag}</span>
                            <span class="chapter-badge">{lecture.id.replace(/^(physics_|mech_)/, '')}</span>
                        </div>

                        <div class="card-bottom">
                            <h3>{lecture.title}</h3>
                            <p>{lecture.subtitle}</p>

                            <div class="card-footer">
                                <span class="explore-btn">
                                    <span>학습 시작</span>
                                    <svg
                                        width="16"
                                        height="16"
                                        viewBox="0 0 24 24"
                                        fill="none"
                                        stroke="currentColor"
                                        stroke-width="2.5"
                                        stroke-linecap="round"
                                        stroke-linejoin="round"
                                    >
                                        <line x1="5" y1="12" x2="19" y2="12"
                                        ></line>
                                        <polyline points="12 5 19 12 12 19"
                                        ></polyline>
                                    </svg>
                                </span>
                            </div>
                        </div>
                    </div>
                </button>
            {/each}
        </div>
    </section>

    <!-- Copyright & Usage Notice -->
    <section class="notice-section notice-animate">
        <div class="notice-box">
            <div class="notice-icon">🚨</div>
            <div class="notice-content">
                <h3>저작권 및 이용 안내</h3>
                <p>
                    본 수업 자료는 <strong>천재교과서 교사용 지도서</strong>
                    및
                    <strong>각종 블로그, 유튜브 등 외부 과학 지식 미디어</strong
                    >의 시각 자료를 바탕으로 공교육 수업을 위해
                    재구성되었습니다.
                </p>
                <p class="warning-text">
                    오직 <strong>교내 수업 목적</strong>으로만 사용되어야 하며,
                    화면 캡쳐 및 링크 공유 등을 통한
                    <strong
                        >본 사이트의 무단 배포 및 외부 유출을 엄히 금지</strong
                    >합니다.
                </p>
                <p class="info-text">
                    본 자료에는 <strong>오류나 오타</strong>가 포함되어 있을 수
                    있으므로,
                    <strong
                        >정기 고사 전 반드시 지도교사에게 내용의 이상 유무를
                        확인</strong
                    >하시기 바랍니다.
                </p>
            </div>
        </div>
    </section>

    <footer class="home-footer">
        <p>© 2026 Sejong High School Physics Department</p>
    </footer>
</div>

<style>
    :global(body) {
        margin: 0;
        padding: 0;
        overflow-x: hidden;
    }

    .home-container {
        min-height: 100vh;
        background-color: #05070a;
        color: #ffffff;
        font-family:
            "Pretendard",
            -apple-system,
            sans-serif;
    }

    /* Textbook Nav Bar */
    .textbook-nav {
        position: sticky;
        top: 0;
        z-index: 100;
        background: rgba(5, 7, 10, 0.85);
        backdrop-filter: blur(16px);
        -webkit-backdrop-filter: blur(16px);
        border-bottom: 1px solid rgba(255, 255, 255, 0.08);
        padding: 0.8rem 2rem;
    }

    .nav-content {
        max-width: 1400px;
        margin: 0 auto;
        display: flex;
        align-items: center;
        gap: 1rem;
    }

    .nav-label {
        font-size: 0.85rem;
        font-weight: 700;
        color: #94a3b8;
        letter-spacing: -0.3px;
        white-space: nowrap;
    }

    .tab-group {
        display: flex;
        gap: 0.5rem;
        flex-wrap: wrap;
    }

    .tab-btn {
        display: inline-flex;
        align-items: center;
        gap: 0.6rem;
        background: rgba(255, 255, 255, 0.04);
        border: 1px solid rgba(255, 255, 255, 0.1);
        color: #cbd5e1;
        padding: 0.55rem 1.2rem;
        border-radius: 12px;
        font-size: 0.95rem;
        font-weight: 700;
        font-family: inherit;
        cursor: pointer;
        transition: all 0.25s cubic-bezier(0.2, 0.8, 0.2, 1);
    }

    .tab-btn:hover {
        background: rgba(255, 255, 255, 0.08);
        color: #ffffff;
        border-color: rgba(255, 255, 255, 0.2);
        transform: translateY(-1px);
    }

    .tab-btn.active {
        background: linear-gradient(135deg, rgba(79, 70, 229, 0.4) 0%, rgba(168, 85, 247, 0.4) 100%);
        border-color: rgba(129, 140, 248, 0.6);
        color: #ffffff;
        box-shadow: 0 4px 20px -2px rgba(79, 70, 229, 0.4);
    }

    .tab-name {
        letter-spacing: -0.3px;
    }

    .tab-badge {
        font-size: 0.72rem;
        font-weight: 800;
        background: rgba(0, 0, 0, 0.3);
        padding: 0.15rem 0.45rem;
        border-radius: 20px;
        color: #a5b4fc;
        border: 1px solid rgba(255, 255, 255, 0.1);
    }

    .tab-btn.active .tab-badge {
        background: rgba(255, 255, 255, 0.2);
        color: #ffffff;
    }

    /* Hero */
    .hero {
        padding: 6rem 2rem 3rem;
        text-align: center;
        position: relative;
    }

    .hero-content {
        position: relative;
        z-index: 10;
        max-width: 900px;
        margin: 0 auto;
    }

    .badge {
        display: inline-block;
        padding: 0.4rem 1rem;
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 50px;
        font-size: 0.75rem;
        font-weight: 800;
        letter-spacing: 2px;
        color: #a5b4fc;
        margin-bottom: 1.5rem;
        backdrop-filter: blur(5px);
    }

    .hero h1 {
        font-size: 3.5rem;
        font-weight: 900;
        line-height: 1.1;
        margin-bottom: 1.5rem;
        letter-spacing: -2px;
    }

    .gradient-text {
        background: linear-gradient(to right, #ffffff, #818cf8, #c084fc);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }

    .school-name {
        font-size: 1.2rem;
        color: #94a3b8;
        font-weight: 500;
        opacity: 0.8;
    }

    .hero-decoration {
        position: absolute;
        top: 40%;
        left: 50%;
        transform: translate(-50%, -50%);
        width: 80vw;
        height: 60vh;
        background: radial-gradient(
            circle,
            rgba(79, 70, 229, 0.15) 0%,
            transparent 70%
        );
        filter: blur(80px);
        z-index: -1;
    }

    /* CSS Animations to replace JS transitions */
    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(30px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }

    @keyframes flyInUp {
        from {
            opacity: 0;
            transform: translateY(50px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }

    .hero-animate {
        animation: fadeInUp 1s cubic-bezier(0.2, 0.8, 0.2, 1) forwards;
    }

    .card-animate {
        opacity: 0; /* Starts hidden */
        animation: flyInUp 0.8s cubic-bezier(0.2, 0.8, 0.2, 1) forwards;
    }

    .notice-animate {
        opacity: 0;
        animation: fadeInUp 0.8s cubic-bezier(0.2, 0.8, 0.2, 1) forwards;
        animation-delay: 600ms;
    }

    /* Action Center */
    .action-center {
        max-width: 900px;
        margin: -0.5rem auto 3rem;
        padding: 0 2rem;
        position: relative;
        z-index: 20;
    }

    .action-grid {
        display: grid;
        grid-template-columns: 1fr 1.5fr;
        gap: 1rem;
    }

    .action-card {
        background: rgba(17, 24, 39, 0.7);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 16px;
        padding: 1rem;
        display: flex;
        align-items: flex-start;
        gap: 0.8rem;
        text-decoration: none;
        color: #fff;
        backdrop-filter: blur(10px);
        transition: all 0.3s cubic-bezier(0.2, 0.8, 0.2, 1);
        box-shadow: 0 10px 30px -10px rgba(0,0,0,0.5);
    }
    
    .primary-action:hover {
        transform: translateY(-5px);
        background: rgba(79, 70, 229, 0.15);
        border-color: rgba(99, 102, 241, 0.5);
        box-shadow: 0 15px 35px -10px rgba(79, 70, 229, 0.3);
    }

    .secondary-action {
        flex-direction: column;
        gap: 0.6rem;
    }

    .secondary-action .action-header {
        display: flex;
        align-items: flex-start;
        gap: 0.8rem;
    }

    .action-icon {
        font-size: 1.2rem;
        background: rgba(255, 255, 255, 0.05);
        width: 36px;
        height: 36px;
        display: flex;
        align-items: center;
        justify-content: center;
        border-radius: 8px;
        flex-shrink: 0;
    }

    .action-content h3 {
        margin: 0 0 0.2rem 0;
        font-size: 1rem;
        font-weight: 700;
        color: #fff;
    }

    .action-content p {
        margin: 0;
        font-size: 0.8rem;
        color: #94a3b8;
        line-height: 1.4;
    }

    .action-arrow {
        margin-left: auto;
        color: #6366f1;
        transition: transform 0.3s;
        align-self: center;
        display: flex;
        align-items: center;
    }

    .action-arrow svg {
        width: 18px;
        height: 18px;
    }

    .primary-action:hover .action-arrow {
        transform: translateX(5px);
    }

    .download-buttons {
        display: flex;
        gap: 0.6rem;
        flex-wrap: wrap;
        width: 100%;
        margin-top: 0.2rem;
    }

    .problem-group {
        display: inline-flex;
        gap: 0.2rem;
        background: rgba(0, 0, 0, 0.2);
        padding: 0.2rem;
        border-radius: 8px;
        border: 1px solid rgba(255, 255, 255, 0.05);
    }

    .dl-btn {
        background: rgba(255, 255, 255, 0.05);
        color: #e2e8f0;
        text-decoration: none;
        padding: 0.35rem 0.7rem;
        border-radius: 6px;
        font-size: 0.75rem;
        font-weight: 600;
        border: 1px solid rgba(255, 255, 255, 0.1);
        transition: all 0.2s;
        display: inline-flex;
        align-items: center;
        gap: 4px;
    }

    .dl-btn::before {
        content: '↗';
        color: #818cf8;
        font-weight: 800;
    }

    .dl-btn:hover {
        background: rgba(99, 102, 241, 0.2);
        border-color: rgba(99, 102, 241, 0.5);
        color: #fff;
        transform: translateY(-2px);
    }

    .solution-btn {
        background: rgba(16, 185, 129, 0.1);
        color: #34d399; /* Emerald-400 */
        border-color: rgba(16, 185, 129, 0.3);
    }

    .solution-btn::before {
        content: '💡';
        color: inherit;
    }

    .solution-btn:hover {
        background: rgba(16, 185, 129, 0.25);
        border-color: rgba(16, 185, 129, 0.6);
        color: #fff;
    }

    .action-animate {
        opacity: 0;
        animation: fadeInUp 0.8s cubic-bezier(0.2, 0.8, 0.2, 1) forwards;
        animation-delay: 300ms;
    }

    @media (max-width: 768px) {
        .action-grid {
            grid-template-columns: 1fr;
        }
        .action-center {
            margin-top: 0;
        }
    }

    /* Grid */
    .lecture-section {
        max-width: 1400px;
        margin: 0 auto;
        padding: 0 2rem 8rem;
    }

    .section-header {
        margin-bottom: 3rem;
        display: flex;
        align-items: center;
        gap: 1.5rem;
    }

    .section-header h2 {
        font-size: 1.8rem;
        font-weight: 800;
        margin: 0;
        white-space: nowrap;
    }

    .header-line {
        height: 1px;
        background: linear-gradient(to right, #1e293b, transparent);
        flex-grow: 1;
    }

    .lecture-grid {
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
        gap: 1.5rem;
    }

    /* Card */
    .lecture-card {
        position: relative;
        background-color: #111827;
        border: 1px solid rgba(255, 255, 255, 0.05);
        border-radius: 20px;
        overflow: hidden;
        text-align: left;
        cursor: pointer;
        transition: all 0.4s cubic-bezier(0.2, 0.8, 0.2, 1);
        display: flex;
        flex-direction: column;
        height: 240px; /* Reduced height by half */
        color: #fff;
        font-family: inherit;
        padding: 0;
    }

    .card-bg-image {
        position: absolute;
        inset: 0;
        width: 100%;
        height: 100%;
        object-fit: cover;
        z-index: 0;
        transition: transform 0.4s cubic-bezier(0.2, 0.8, 0.2, 1);
    }

    .lecture-card:hover .card-bg-image {
        transform: scale(1.05);
    }

    .lecture-card::after {
        content: "";
        position: absolute;
        inset: 0;
        border-radius: 20px;
        padding: 1px;
        background: linear-gradient(
            135deg,
            rgba(255, 255, 255, 0.2),
            transparent,
            rgba(255, 255, 255, 0.1)
        );
        -webkit-mask:
            linear-gradient(#fff 0 0) content-box,
            linear-gradient(#fff 0 0);
        mask:
            linear-gradient(#fff 0 0) content-box,
            linear-gradient(#fff 0 0);
        -webkit-mask-composite: xor;
        mask-composite: exclude;
        opacity: 0.5;
        transition: opacity 0.3s;
        z-index: 20;
    }

    .card-overlay {
        position: absolute;
        inset: 0;
        background: linear-gradient(
            to top,
            rgba(5, 7, 10, 0.95) 0%,
            fill,
            rgba(5, 7, 10, 0.7) 40%,
            rgba(5, 7, 10, 0.4) 100%
        );
        transition: background 0.4s ease;
        z-index: 1;
    }

    .lecture-card:hover {
        transform: translateY(-8px) scale(1.02);
        border-color: var(--accent-color);
        box-shadow:
            0 20px 40px -10px rgba(0, 0, 0, 0.7),
            0 10px 20px -10px var(--accent-color);
    }

    .lecture-card:hover .card-overlay {
        background: linear-gradient(
            to top,
            rgba(5, 7, 10, 0.9) 0%,
            rgba(5, 7, 10, 0.5) 50%,
            rgba(5, 7, 10, 0.2) 100%
        );
    }

    .lecture-card:hover::after {
        opacity: 1;
        background: linear-gradient(135deg, var(--accent-color), transparent);
    }

    .card-content {
        position: relative;
        z-index: 10;
        padding: 1.5rem;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        height: 100%;
        box-sizing: border-box;
    }

    .card-top {
        display: flex;
        justify-content: space-between;
        align-items: flex-start;
    }

    .chapter-badge {
        width: 36px;
        height: 36px;
        background: rgba(0, 0, 0, 0.5);
        backdrop-filter: blur(5px);
        border: 1px solid rgba(255, 255, 255, 0.2);
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: 800;
        font-size: 0.9rem;
        color: #fff;
    }

    .tag {
        font-size: 0.8rem;
        color: var(--accent-color);
        font-weight: 800;
        letter-spacing: 1px;
        opacity: 0.9;
        text-shadow: 0 2px 4px rgba(0, 0, 0, 0.8);
    }

    .card-bottom h3 {
        margin: 0 0 0.5rem 0;
        font-size: 1.4rem;
        font-weight: 800;
        line-height: 1.3;
        letter-spacing: -0.5px;
        text-shadow: 0 2px 4px rgba(0, 0, 0, 0.8);
    }

    .card-bottom p {
        margin: 0;
        color: #ffffff;
        font-weight: 500;
        font-size: 0.95rem;
        line-height: 1.4;
        text-shadow:
            0 2px 4px rgba(0, 0, 0, 0.9),
            0 0 10px rgba(0, 0, 0, 0.6);
    }

    .card-footer {
        margin-top: 1rem;
    }

    .explore-btn {
        display: inline-flex;
        align-items: center;
        gap: 0.5rem;
        font-size: 0.9rem;
        font-weight: 700;
        color: #fff;
        transition: all 0.3s;
        background: rgba(255, 255, 255, 0.1);
        padding: 0.4rem 0.8rem;
        border-radius: 50px;
        backdrop-filter: blur(5px);
        border: 1px solid rgba(255, 255, 255, 0.05);
    }

    .lecture-card:hover .explore-btn {
        background: var(--accent-color);
        color: #fff;
        transform: translateX(4px);
    }

    /* Notice Section */
    .notice-section {
        max-width: 900px;
        margin: 0 auto;
        padding: 0 2rem 4rem;
    }

    .notice-box {
        display: flex;
        gap: 1.5rem;
        background: rgba(239, 68, 68, 0.05); /* Very dark red/transparent */
        border: 1px solid rgba(239, 68, 68, 0.2);
        border-radius: 16px;
        padding: 2rem;
        align-items: flex-start;
        backdrop-filter: blur(10px);
        box-shadow: 0 15px 35px -5px rgba(239, 68, 68, 0.1);
        transition:
            transform 0.3s ease,
            box-shadow 0.3s ease;
    }

    .notice-box:hover {
        transform: translateY(-5px);
        box-shadow: 0 20px 40px -5px rgba(239, 68, 68, 0.15);
        border-color: rgba(239, 68, 68, 0.4);
    }

    .notice-icon {
        font-size: 2.5rem;
        flex-shrink: 0;
        animation: pulseAlert 2s infinite;
    }

    @keyframes pulseAlert {
        0% {
            transform: scale(1);
            opacity: 1;
        }
        50% {
            transform: scale(1.1);
            opacity: 0.8;
        }
        100% {
            transform: scale(1);
            opacity: 1;
        }
    }

    .notice-content h3 {
        margin: 0 0 0.8rem 0;
        font-size: 1.3rem;
        font-weight: 800;
        color: #f87171; /* Red-400 */
        letter-spacing: -0.5px;
    }

    .notice-content p {
        margin: 0 0 0.5rem 0;
        color: #cbd5e1; /* Slate-300 */
        font-size: 0.95rem;
        line-height: 1.6;
    }

    .notice-content .warning-text {
        margin-top: 1rem;
        color: #fecaca; /* Red-200 */
        font-weight: 600;
        border-left: 3px solid #ef4444;
        padding-left: 1rem;
    }

    .notice-content .info-text {
        margin-top: 0.8rem;
        color: #fde68a; /* Amber-200 */
        font-weight: 600;
        border-left: 3px solid #f59e0b; /* Amber-500 */
        padding-left: 1rem;
    }

    .notice-content strong {
        color: #fff;
    }

    .home-footer {
        padding: 4rem 2rem;
        text-align: center;
        border-top: 1px solid rgba(255, 255, 255, 0.05);
        opacity: 0.5;
    }

    /* Mobile */
    @media (max-width: 640px) {
        .hero h1 {
            font-size: 2.5rem;
        }
        .lecture-grid {
            grid-template-columns: 1fr;
        }
    }
</style>
