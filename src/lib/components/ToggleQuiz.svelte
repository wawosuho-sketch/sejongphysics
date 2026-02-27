<script>
    export let question;
    export let answer;
    export let title = "개념 다지기 퀴즈";
    let showAnswer = false;
</script>

<div class="quiz-container">
    <button class="quiz-header" on:click={() => (showAnswer = !showAnswer)}>
        <div class="title-wrap">
            <span class="icon">🤔</span>
            <h3>{title}</h3>
        </div>
        <span class="chevron" class:open={showAnswer}>▼</span>
    </button>

    <div class="quiz-body">
        <p class="question">Q. {question}</p>

        {#if showAnswer}
            <div class="answer-box">
                <span class="answer-label">A.</span>
                <p class="answer-text">{answer}</p>
            </div>
        {/if}
    </div>
</div>

<style>
    .quiz-container {
        margin: 2rem 0;
        border: 2px solid #cbd5e1;
        border-radius: 12px;
        background: #ffffff;
        box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1);
        overflow: hidden;
    }
    .quiz-header {
        width: 100%;
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 1rem 1.5rem;
        background: #f1f5f9;
        border: none;
        border-bottom: 1px solid #cbd5e1;
        cursor: pointer;
        font-family: inherit;
        text-align: left;
        transition: background 0.2s;
    }
    .quiz-header:hover {
        background: #e2e8f0;
    }
    .title-wrap {
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }
    h3 {
        margin: 0;
        font-size: 1.1rem;
        color: #1e293b;
        font-weight: 600;
    }
    .icon {
        font-size: 1.2rem;
    }
    .chevron {
        transition: transform 0.3s;
        color: #64748b;
    }
    .chevron.open {
        transform: rotate(180deg);
    }
    .quiz-body {
        padding: 1.5rem;
    }
    .question {
        font-size: 1.1rem;
        font-weight: bold;
        color: #0f172a;
        margin: 0 0 1rem 0;
        line-height: 1.5;
    }
    .answer-box {
        margin-top: 1rem;
        padding: 1rem;
        background: #eff6ff;
        border-left: 4px solid #3b82f6;
        border-radius: 0 8px 8px 0;
        display: flex;
        gap: 0.8rem;
        animation: fadeIn 0.3s ease-out;
    }
    .answer-label {
        font-weight: bold;
        color: #2563eb;
        font-size: 1.1rem;
    }
    .answer-text {
        margin: 0;
        color: #1e3a8a;
        line-height: 1.6;
    }

    @keyframes fadeIn {
        from {
            opacity: 0;
            transform: translateY(-10px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
</style>
