<script>
    import { onMount } from "svelte";

    export let src;
    export let title = "관련 영상 보기";

    let online = true;

    onMount(() => {
        online = navigator.onLine;
        const sync = () => {
            online = navigator.onLine;
        };
        window.addEventListener("online", sync);
        window.addEventListener("offline", sync);
        return () => {
            window.removeEventListener("online", sync);
            window.removeEventListener("offline", sync);
        };
    });

    // Automatically convert YouTube watch or youtu.be URLs to embed URLs
    $: embedSrc = (() => {
        if (!src) return "";
        try {
            if (src.includes("youtu.be/")) {
                const videoId = src.split("youtu.be/")[1].split("?")[0];
                return `https://www.youtube.com/embed/${videoId}`;
            }
            if (src.includes("youtube.com/watch")) {
                const url = new URL(src);
                const videoId = url.searchParams.get("v");
                if (videoId) return `https://www.youtube.com/embed/${videoId}`;
            }
        } catch (e) {
            console.error("Failed to parse video URL:", e);
        }
        return src; // Fallback to original src if it fails
    })();
</script>

<div class="video-container">
    <div class="video-header">
        <span class="icon">📺</span>
        <h3>{title}</h3>
    </div>
    {#if !online}
        <div class="offline-note">
            <p>오프라인 상태입니다. 영상은 네트워크에 연결되면 재생할 수 있습니다.</p>
            {#if embedSrc}
                <a href={embedSrc} target="_blank" rel="noopener noreferrer">연결되면 새 창에서 열기</a>
            {/if}
        </div>
    {:else}
        <div class="video-wrapper">
            <iframe
                src={embedSrc}
                frameborder="0"
                allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                allowfullscreen
                loading="lazy"
                {title}
            ></iframe>
        </div>
    {/if}
</div>

<style>
    .video-container {
        margin: 2rem 0;
        border: 2px solid #e2e8f0;
        border-radius: 12px;
        overflow: hidden;
        background: #ffffff;
        box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1);
    }
    .video-header {
        display: flex;
        align-items: center;
        gap: 0.5rem;
        padding: 1rem 1.5rem;
        background: #f8fafc;
        border-bottom: 1px solid #e2e8f0;
    }
    h3 {
        margin: 0;
        font-size: 1.1rem;
        color: #334155;
    }
    .icon {
        font-size: 1.2rem;
    }
    .video-wrapper {
        position: relative;
        padding-bottom: 56.25%; /* 16:9 Aspect Ratio */
        height: 0;
        overflow: hidden;
    }
    .offline-note {
        padding: 2rem 1.5rem;
        text-align: center;
        background: #f1f5f9;
        color: #475569;
    }

    .offline-note a {
        display: inline-block;
        margin-top: 1rem;
        color: #4f46e5;
        font-weight: 600;
    }

    .video-wrapper iframe {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        border: none;
    }
</style>
