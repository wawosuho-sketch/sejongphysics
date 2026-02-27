<script>
  export let src;
  export let title = "물리 시뮬레이션";
  export let height = "600";

  // Check if the site is known to block iframes (like LabXchange)
  $: isNonEmbeddable = src && src.includes("labxchange.org");
</script>

<div class="simulation-container">
  <div class="sim-header">
    <span class="icon">🕹️</span>
    <h3>{title}</h3>
  </div>

  {#if isNonEmbeddable}
    <div class="fallback-container">
      <div class="fallback-content">
        <p>이 시뮬레이션은 보안 정책으로 인해 직접 임베드할 수 없습니다.</p>
        <p>아래 버튼을 눌러 새 창에서 실험을 진행해 주세요. 😊</p>
        <a
          href={src}
          target="_blank"
          rel="noopener noreferrer"
          class="link-btn"
        >
          📍 시뮬레이션 새 창에서 열기
        </a>
      </div>
    </div>
  {:else}
    <iframe {src} width="100%" {height} scrolling="auto" allowfullscreen {title}
    ></iframe>
  {/if}
</div>

<style>
  .simulation-container {
    margin: 2rem 0;
    border: 2px solid #e2e8f0;
    border-radius: 12px;
    overflow: hidden;
    background: #ffffff;
    box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1);
  }
  .sim-header {
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
  iframe {
    border: none;
    display: block;
    background: white;
  }

  .fallback-container {
    padding: 3rem 1.5rem;
    background: #f1f5f9;
    display: flex;
    justify-content: center;
    align-items: center;
    text-align: center;
  }

  .fallback-content p {
    margin: 0.5rem 0;
    color: #475569;
    font-size: 1rem;
  }

  .link-btn {
    display: inline-block;
    margin-top: 1.5rem;
    padding: 0.8rem 1.5rem;
    background: #4f46e5;
    color: white;
    text-decoration: none;
    border-radius: 8px;
    font-weight: 600;
    transition: all 0.2s ease;
    box-shadow: 0 4px 6px -1px rgba(79, 70, 229, 0.4);
  }

  .link-btn:hover {
    background: #4338ca;
    transform: translateY(-2px);
    box-shadow: 0 10px 15px -3px rgba(79, 70, 229, 0.5);
  }
</style>
