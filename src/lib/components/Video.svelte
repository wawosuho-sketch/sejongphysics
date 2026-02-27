<script>
    export let src;
    export let title = "관련 영상 보기";

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
    <div class="video-wrapper">
        <iframe
            src={embedSrc}
            frameborder="0"
            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
            allowfullscreen
            {title}
        ></iframe>
    </div>
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
    .video-wrapper iframe {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        border: none;
    }
</style>
