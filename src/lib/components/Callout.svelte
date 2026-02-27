<script>
    export let content = "";
    export let type = "info"; // 'info', 'success', 'warning'
    export let title = "";
</script>

<div class="callout {type}">
    <div class="icon-container">
        <span class="icon">
            {#if type === "info"}💡
            {:else if type === "success"}✅
            {:else}⚠️{/if}
        </span>
    </div>
    <div class="content-container">
        {#if title}
            <h4>{title}</h4>
        {/if}
        <p>
            {#if content}
                {content}
            {:else}
                <slot />
            {/if}
        </p>
    </div>
</div>

<style>
    .callout {
        display: flex;
        align-items: flex-start;
        gap: 1rem;
        margin: 2rem 0;
        padding: 1.5rem;
        border-radius: 12px;
        box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1);
    }

    /* Type variants */
    .info {
        background-color: #f0fdf4;
        border-left: 6px solid #22c55e;
    }
    .success {
        background-color: #eff6ff;
        border-left: 6px solid #3b82f6;
    }
    .warning {
        background-color: #fffbeb;
        border-left: 6px solid #f59e0b;
    }

    .icon-container {
        flex-shrink: 0;
        margin-top: 2px;
    }
    .icon {
        font-size: 1.5rem;
    }
    .content-container h4 {
        margin: 0 0 0.5rem 0;
        color: #1e293b;
        font-size: 1.2rem;
    }
    .content-container p {
        margin: 0;
        color: #334155;
        font-size: 1.1rem;
        line-height: 1.6;
        font-weight: 500;
    }
</style>
