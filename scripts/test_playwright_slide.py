from playwright.sync_api import sync_playwright
from PIL import Image
import io
import os

html_content = """
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css">
<style>
  body {
    margin: 0;
    width: 1920px;
    height: 1080px;
    background: #0b0f19;
    color: #ffffff;
    font-family: 'Pretendard', -apple-system, sans-serif;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    padding: 60px 80px;
    box-sizing: border-box;
    position: relative;
    overflow: hidden;
  }
  .bg-glow {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    width: 800px;
    height: 800px;
    background: radial-gradient(circle, rgba(79, 70, 229, 0.18) 0%, transparent 70%);
    filter: blur(80px);
    z-index: 0;
  }
  .header {
    position: relative;
    z-index: 10;
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 2px solid rgba(255, 255, 255, 0.1);
    padding-bottom: 24px;
  }
  .badge {
    background: linear-gradient(135deg, #4f46e5, #a855f7);
    padding: 8px 20px;
    border-radius: 50px;
    font-size: 20px;
    font-weight: 800;
    letter-spacing: 1px;
  }
  .topic-title {
    font-size: 24px;
    color: #94a3b8;
    font-weight: 600;
  }
  .content {
    position: relative;
    z-index: 10;
    margin: 40px 0;
    flex: 1;
    display: flex;
    flex-direction: column;
    justify-content: center;
  }
  h1 {
    font-size: 52px;
    font-weight: 800;
    margin: 0 0 30px 0;
    color: #f8fafc;
    line-height: 1.2;
  }
  .card {
    background: rgba(17, 24, 39, 0.7);
    border: 1px solid rgba(255, 255, 255, 0.12);
    border-radius: 24px;
    padding: 40px;
    backdrop-filter: blur(12px);
    box-shadow: 0 20px 40px rgba(0,0,0,0.5);
    font-size: 28px;
    line-height: 1.7;
    color: #cbd5e1;
  }
  .footer {
    position: relative;
    z-index: 10;
    display: flex;
    justify-content: space-between;
    align-items: center;
    color: #64748b;
    font-size: 20px;
    font-weight: 600;
    border-top: 1px solid rgba(255, 255, 255, 0.08);
    padding-top: 20px;
  }
</style>
</head>
<body>
  <div class="bg-glow"></div>
  <div class="header">
    <span class="badge">PART 1. 벡터와 힘의 평형</span>
    <span class="topic-title">세종고등학교 역학과 에너지</span>
  </div>
  <div class="content">
    <h1>1. 스칼라(Scalar)와 벡터(Vector)</h1>
    <div class="card">
      <p>• <strong>스칼라(Scalar)</strong>: 크기만 갖는 물리량 (질량, 시간, 온동, 이동거리, 에너지 등)</p>
      <p>• <strong>벡터(Vector)</strong>: 크기와 방향을 동시에 갖는 물리량 (변위, 속도, 가속도, 힘, 운동량 등)</p>
    </div>
  </div>
  <div class="footer">
    <span>SEJONG HIGH SCHOOL PHYSICS</span>
    <span>SLIDE 01 / 70</span>
  </div>
</body>
</html>
"""

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport={"width": 1920, "height": 1080})
    page.set_content(html_content)
    page.wait_for_timeout(500)
    
    png_bytes = page.screenshot(type="png")
    img = Image.open(io.BytesIO(png_bytes))
    
    os.makedirs(r"r:\textbook-svelte\tmp", exist_ok=True)
    img.save(r"r:\textbook-svelte\tmp\test_slide.webp", "WEBP", quality=85)
    browser.close()
    print("Test slide rendered successfully to WebP!")
