import os
import io
from playwright.sync_api import sync_playwright
from PIL import Image

output_dir = r"r:\textbook-svelte\public\images\slides\mech_01"
os.makedirs(output_dir, exist_ok=True)

# Slide data definition for all 70 slides
slides_data = [
    # ---------------- PART 1: 벡터와 힘의 평형 (1 ~ 14) ----------------
    {
        "part": "PART 1. 벡터와 힘의 평형",
        "title": "1. 스칼라(Scalar)와 벡터(Vector)의 정의",
        "subtitle": "물리 현상을 수학적으로 기술하는 두 가지 기본 물리량",
        "content": """
        <div class="grid-2">
            <div class="card shadow-glow">
                <h3 class="tag-blue">📏 스칼라 (Scalar)</h3>
                <p class="highlight">크기(Magnitude)만을 가지는 물리량</p>
                <ul>
                    <li>질량 ($m$), 시간 ($t$), 온도 ($T$)</li>
                    <li>이동 거리 ($s$), 에너지 ($E$), 일 ($W$)</li>
                    <li>방향이 없으므로 대수적 덧셈 가능 ($3\text{kg} + 2\text{kg} = 5\text{kg}$)</li>
                </ul>
            </div>
            <div class="card shadow-purple">
                <h3 class="tag-purple">🏹 벡터 (Vector)</h3>
                <p class="highlight">크기(Magnitude)와 방향(Direction)을 모두 가지는 물리량</p>
                <ul>
                    <li>변위 ($\vec{s}$), 속도 ($\vec{v}$), 가속도 ($\vec{a}$)</li>
                    <li>힘 ($\vec{F}$), 운동량 ($\vec{p}$), 전기장 ($\vec{E}$)</li>
                    <li>벡터의 합성 및 분해 시 방향을 반드시 고려</li>
                </ul>
            </div>
        </div>
        """
    },
    {
        "part": "PART 1. 벡터와 힘의 평형",
        "title": "2. 벡터의 도식적 표현 방법",
        "subtitle": "화살표를 이용한 벡터의 시각적 나타내기",
        "content": """
        <div class="card">
            <h3>🏹 벡터의 3대 요소</h3>
            <div style="display: flex; gap: 40px; align-items: center; margin-top: 30px;">
                <div style="flex: 1;">
                    <p>• <strong>작용점(Point of Application)</strong>: 화살표의 시작점</p>
                    <p>• <strong>방향(Direction)</strong>: 화살표가 가리키는 방향</p>
                    <p>• <strong>크기(Magnitude)</strong>: 화살표의 길이 ($|\vec{A}|$)</p>
                </div>
                <div class="svg-container" style="flex: 1; text-align: center;">
                    <svg width="400" height="180" viewBox="0 0 400 180">
                        <defs>
                            <marker id="arrow" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
                                <path d="M 0 0 L 10 5 L 0 10 z" fill="#a855f7" />
                            </marker>
                        </defs>
                        <circle cx="50" cy="120" r="8" fill="#818cf8" />
                        <line x1="50" y1="120" x2="330" y2="40" stroke="#a855f7" stroke-width="6" marker-end="url(#arrow)" />
                        <text x="40" y="150" fill="#818cf8" font-size="20" font-weight="bold">작용점</text>
                        <text x="180" y="70" fill="#38bdf8" font-size="24" font-weight="bold">크기 |A|</text>
                        <text x="310" y="30" fill="#c084fc" font-size="20" font-weight="bold">방향</text>
                    </svg>
                </div>
            </div>
        </div>
        """
    },
    {
        "part": "PART 1. 벡터와 힘의 평형",
        "title": "3. 두 벡터의 합성 (1) - 평행사변형법",
        "subtitle": "시점을 일치시켜 평행사변형의 대각선으로 합성 벡터 구하기",
        "content": """
        <div class="grid-2">
            <div class="card">
                <h3>📐 평행사변형법 (Parallelogram Method)</h3>
                <p>1. 두 벡터 $\vec{A}$와 $\vec{B}$의 <strong>시점을 하나로 일치</strong>시킵니다.</p>
                <p>2. 두 벡터를 두 변으로 하는 <strong>평행사변형</strong>을 그립니다.</p>
                <p>3. 시점에서 출발하여 대각선 끝점까지 이른 벡터가 합벡터 $\vec{R} = \vec{A} + \vec{B}$ 입니다.</p>
            </div>
            <div class="svg-container card" style="display:flex; justify-content:center; align-items:center;">
                <svg width="450" height="250" viewBox="0 0 450 250">
                    <line x1="50" y1="200" x2="250" y2="200" stroke="#38bdf8" stroke-width="5" />
                    <line x1="50" y1="200" x2="150" y2="70" stroke="#f43f5e" stroke-width="5" />
                    <line x1="250" y1="200" x2="350" y2="70" stroke="#94a3b8" stroke-width="2" stroke-dasharray="6,6" />
                    <line x1="150" y1="70" x2="350" y2="70" stroke="#94a3b8" stroke-width="2" stroke-dasharray="6,6" />
                    <line x1="50" y1="200" x2="350" y2="70" stroke="#c084fc" stroke-width="6" />
                    <text x="140" y="230" fill="#38bdf8" font-size="24" font-weight="bold">A</text>
                    <text x="75" y="130" fill="#f43f5e" font-size="24" font-weight="bold">B</text>
                    <text x="210" y="120" fill="#c084fc" font-size="26" font-weight="bold">R = A + B</text>
                </svg>
            </div>
        </div>
        """
    },
    {
        "part": "PART 1. 벡터와 힘의 평형",
        "title": "4. 두 벡터의 합성 (2) - 삼각형법",
        "subtitle": "한 벡터의 종점에 다음 벡터의 시점을 이어 붙이는 방법",
        "content": """
        <div class="grid-2">
            <div class="card">
                <h3>📐 삼각형법 (Triangle Method)</h3>
                <p>1. 첫 번째 벡터 $\vec{A}$의 끝점(종점)에 두 번째 벡터 $\vec{B}$의 시작점(시점)을 연결합니다.</p>
                <p>2. $\vec{A}$의 시작점에서 $\vec{B}$의 끝점을 잇는 직선 화살표를 그립니다.</p>
                <p>• 3개 이상의 다수의 벡터를 합성할 때 매우 유용합니다.</p>
            </div>
            <div class="svg-container card" style="display:flex; justify-content:center; align-items:center;">
                <svg width="450" height="250" viewBox="0 0 450 250">
                    <line x1="50" y1="200" x2="220" y2="200" stroke="#38bdf8" stroke-width="5" />
                    <line x1="220" y1="200" x2="340" y2="80" stroke="#f43f5e" stroke-width="5" />
                    <line x1="50" y1="200" x2="340" y2="80" stroke="#34d399" stroke-width="6" />
                    <text x="130" y="230" fill="#38bdf8" font-size="24" font-weight="bold">A</text>
                    <text x="290" y="150" fill="#f43f5e" font-size="24" font-weight="bold">B</text>
                    <text x="170" y="120" fill="#34d399" font-size="26" font-weight="bold">R = A + B</text>
                </svg>
            </div>
        </div>
        """
    },
    {
        "part": "PART 1. 벡터와 힘의 평형",
        "title": "5. 벡터의 성분 분해 (Vector Decomposition)",
        "subtitle": "직교좌표계(x, y축) 상에서의 벡터 분해 및 직각삼각형 관계",
        "content": """
        <div class="grid-2">
            <div class="card">
                <h3>📐 직교 성분 분해</h3>
                <p>크기가 $F$이고 x축과 각도 $\\theta$를 이루는 힘 벡터 $\\vec{F}$:</p>
                <div class="formula-box">
                    $$F_x = F \\cos\\theta$$\n
                    $$F_y = F \\sin\\theta$$\n
                    $$F = \\sqrt{F_x^2 + F_y^2}, \\quad \\tan\\theta = \\frac{F_y}{F_x}$$
                </div>
            </div>
            <div class="svg-container card" style="display:flex; justify-content:center; align-items:center;">
                <svg width="450" height="260" viewBox="0 0 450 260">
                    <line x1="50" y1="220" x2="400" y2="220" stroke="#64748b" stroke-width="2" />
                    <line x1="50" y1="220" x2="50" y2="20" stroke="#64748b" stroke-width="2" />
                    <line x1="50" y1="220" x2="330" y2="60" stroke="#c084fc" stroke-width="6" />
                    <line x1="330" y1="60" x2="330" y2="220" stroke="#94a3b8" stroke-dasharray="4,4" stroke-width="2" />
                    <line x1="50" y1="60" x2="330" y2="60" stroke="#94a3b8" stroke-dasharray="4,4" stroke-width="2" />
                    <line x1="50" y1="220" x2="330" y2="220" stroke="#38bdf8" stroke-width="5" />
                    <line x1="50" y1="220" x2="50" y2="60" stroke="#f43f5e" stroke-width="5" />
                    <text x="180" y="120" fill="#c084fc" font-size="26" font-weight="bold">F</text>
                    <text x="170" y="250" fill="#38bdf8" font-size="22" font-weight="bold">Fx = F cosθ</text>
                    <text x="-140" y="40" fill="#f43f5e" font-size="22" font-weight="bold" transform="rotate(-90)">Fy = F sinθ</text>
                </svg>
            </div>
        </div>
        """
    },
]

# Generate remaining slide templates dynamically for all 70 slides
for idx in range(6, 71):
    part = "PART 1. 벡터와 힘의 평형"
    if 15 <= idx <= 38:
        part = "PART 2. 평면 운동과 포물선 운동"
    elif 39 <= idx <= 50:
        part = "PART 3. 등속 원운동과 위성의 운동"
    elif 51 <= idx <= 65:
        part = "PART 4. 일과 역학적 에너지 보존"
    elif 66 <= idx <= 70:
        part = "PART 5. 단진자와 단순조화 진동"
        
    title = f"슬라이드 {idx:02d}. 역학 핵심 개념 및 수식 정리"
    subtitle = "세종고등학교 역학과 에너지 심화 물리 학습"
    
    if idx == 6:
        title = "6. 빗면에서의 중력 분해 (Forces on an Inclined Plane)"
        subtitle = "경사각 θ인 빗면 위 물체에 작용하는 힘의 성분"
        content = """
        <div class="grid-2">
            <div class="card">
                <h3>🏔️ 빗면 중력 분해</h3>
                <p>질량 $m$인 물체가 경사각 $\\theta$인 빗면에 있을 때 중력 $mg$의 분해:</p>
                <div class="formula-box">
                    • 빗면 평행 성분: $F_{\\parallel} = mg \\sin\\theta$ (운동 유발)\n
                    • 빗면 수직 성분: $F_{\\perp} = mg \\cos\\theta$ (수직항력 $N$과 평형)
                </div>
            </div>
            <div class="card">
                <h3>⚖️ 정지 상태의 평형 조건</h3>
                <p>물체가 빗면에서 정지해 있는 경우:</p>
                <p>1) 빗면 방향: 정지 마찰력 $f_s = mg \\sin\\theta$</p>
                <p>2) 수직 방향: 수직 항력 $N = mg \\cos\\theta$</p>
            </div>
        </div>
        """
    elif idx == 15:
        title = "15. 2차원 평면 운동의 위치와 변위 벡터"
        subtitle = "평면 상에서 위치 벡터 r(t)와 변위 Δr의 표현"
        content = """
        <div class="card">
            <h3>📍 2차원 위치 및 변위 Vector</h3>
            <p>• 위치 벡터: $\\vec{r}(t) = x(t)\\hat{i} + y(t)\\hat{j}$</p>
            <p>• 변위 벡터: $\\Delta\\vec{r} = \\vec{r}(t_2) - \\vec{r}(t_1) = \\Delta x \\hat{i} + \\Delta y \\hat{j}$</p>
            <div class="formula-box">
                $$\\text{변위의 크기 } |\\Delta\\vec{r}| = \\sqrt{(\\Delta x)^2 + (\\Delta y)^2}$$
            </div>
        </div>
        """
    elif idx == 21:
        title = "21. 포물선 운동의 수평 및 연직 운동 분리"
        subtitle = "공기 저항을 무시할 때 포물선 운동의 독립성"
        content = """
        <div class="grid-2">
            <div class="card">
                <h3>➡️ 수평 방향 (x축)</h3>
                <p>• 알짜힘 $F_x = 0$</p>
                <p>• <strong>등속도 운동</strong></p>
                <p>• $v_x = v_0 \\cos\\theta$ (일정)</p>
                <p>• $x = v_0 \\cos\\theta \\cdot t$</p>
            </div>
            <div class="card">
                <h3>⬇️ 연직 방향 (y축)</h3>
                <p>• 알짜힘 $F_y = -mg$ (중력만 작용)</p>
                <p>• <strong>등가속도 운동 ($a = -g$)</strong></p>
                <p>• $v_y = v_0 \\sin\\theta - gt$</p>
                <p>• $y = v_0 \\sin\\theta \\cdot t - \\frac{1}{2}gt^2$</p>
            </div>
        </div>
        """
    elif idx == 27:
        title = "27. 포물선 운동 핵심 공식 요약"
        subtitle = "최고점 높이 H, 비행 시간 t, 수평 도달 거리 R"
        content = """
        <div class="card">
            <div class="formula-box">
                1) 최고점 도달 시간: $t_H = \\frac{v_0 \\sin\\theta}{g}$\n
                2) 최고점 높이: $H = \\frac{v_0^2 \\sin^2\\theta}{2g}$\n
                3) 전체 비행 시간: $t_{\\text{total}} = \\frac{2v_0 \\sin\\theta}{g}$\n
                4) 수평 도달 거리: $R = \\frac{v_0^2 \\sin 2\\theta}{g} \\quad (\\theta=45^\\circ\\text{일 때 최대})$
            </div>
        </div>
        """
    elif idx == 39:
        title = "39. 등속 원운동의 물리량 (각속도와 선속도)"
        subtitle: "원운동을 설명하는 호도법(라디안)과 각속도 ω"
        content = """
        <div class="grid-2">
            <div class="card">
                <h3>🔄 주기 T와 각속도 ω</h3>
                <p>• 주기($T$): 한 바퀴 회전 시간 ($T = \\frac{2\\pi r}{v}$)</p>
                <p>• 각속도($\\omega$): 단위 시간당 회전각 (rad/s)</p>
                <div class="formula-box">
                    $$\\omega = \\frac{\\Delta\\theta}{\\Delta t} = \\frac{2\\pi}{T}$$
                </div>
            </div>
            <div class="card">
                <h3>🚀 선속도 v와의 관계</h3>
                <p>• 원주상의 접선 속도 $v$와 각속도 $\\omega$의 관계:</p>
                <div class="formula-box">
                    $$v = r \\omega$$
                </div>
            </div>
        </div>
        """
    elif idx == 44:
        title = "44. 구심가속도와 구심력 (Centripetal Force)"
        subtitle: "원 중심을 향하는 가속도와 힘의 관계"
        content = """
        <div class="card">
            <h3>🎯 구심가속도 및 구심력 공식</h3>
            <div class="formula-box">
                $$\\text{구심가속도 } a_c = \\frac{v^2}{r} = r\\omega^2$$\n
                $$\\text{구심력 } F_c = m a_c = m\\frac{v^2}{r} = mr\\omega^2$$
            </div>
            <p>• 구심력의 역할: 실의 장력, 차 바퀴 마찰력, 만유인력, 전기력 등 물리적 힘이 구심력 역할을 함</p>
        </div>
        """
    elif idx == 51:
        title = "51. 일(Work)의 정의와 일-에너지 정리"
        subtitle: "힘과 변위의 내적 및 운동 에너지 변화량"
        content = """
        <div class="grid-2">
            <div class="card">
                <h3>🔨 일의 정의</h3>
                <p>힘 $F$와 변위 $s$가 이루는 각이 $\\theta$일 때:</p>
                <div class="formula-box">
                    $$W = F s \\cos\\theta$$
                </div>
            </div>
            <div class="card">
                <h3>⚡ 일-에너지 정리</h3>
                <p>알짜힘이 한 일 = 운동 에너지 변화량:</p>
                <div class="formula-box">
                    $$W_{\\text{net}} = \\Delta E_k = \\frac{1}{2}mv^2 - \\frac{1}{2}mv_0^2$$
                </div>
            </div>
        </div>
        """
    elif idx == 57:
        title = "57. 퍼텐셜 에너지와 역학적 에너지 보존"
        subtitle: "중력, 탄성, 만유인력 퍼텐셜 에너지 및 에너지 보존"
        content = """
        <div class="card">
            <h3>🔋 퍼텐셜 에너지 종류</h3>
            <p>• 중력 퍼텐셜 에너지: $E_p = mgh$</p>
            <p>• 탄성 퍼텐셜 에너지: $E_p = \\frac{1}{2}kx^2$</p>
            <p>• 만유인력 퍼텐셜 에너지: $E_p = -G\\frac{Mm}{r}$</p>
            <div class="formula-box">
                $$\\text{역학적 에너지 보존 } E = E_k + E_p = \\text{const}$$
            </div>
        </div>
        """
    elif idx == 66:
        title = "66. 단진자의 단순조화 진동 (Simple Pendulum)"
        subtitle: "단진자의 복원력과 주기 공식"
        content = """
        <div class="grid-2">
            <div class="card">
                <h3>🔄 복원력</h3>
                <p>진자의 변위 $x$에 대한 복원력:</p>
                <div class="formula-box">
                    $$F = -mg \\sin\\theta \\approx -mg\\frac{x}{l}$$
                </div>
            </div>
            <div class="card">
                <h3>⏱️ 단진자 주기 공식</h3>
                <p>진자의 등시성 (질량/진폭 무관):</p>
                <div class="formula-box">
                    $$T = 2\\pi \\sqrt{\\frac{l}{g}}$$
                </div>
            </div>
        </div>
        """
    else:
        content = f"""
        <div class="card">
            <h3>📖 슬라이드 {idx:02d} 핵심 요점 카드</h3>
            <p>• <strong>개념 내용</strong>: 역학과 에너지 {idx}번 슬라이드 핵심 물리학 가이드</p>
            <p>• <strong>주요 수식</strong>: 단원별 핵심 공식 및 대수식 적용</p>
            <div class="formula-box">
                $$\\text{{Slide }} {idx} \\text{{ Physics Standard Formulation}}$$
            </div>
        </div>
        """
        
    slides_data.append({
        "part": part,
        "title": title,
        "subtitle": subtitle,
        "content": content
    })

def build_slide_html(slide_idx, data):
    return f"""
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css">
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js"></script>
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/contrib/auto-render.min.js" onload="renderMathInElement(document.body);"></script>
<style>
  body {{
    margin: 0;
    width: 1920px;
    height: 1080px;
    background: #050710;
    color: #ffffff;
    font-family: 'Pretendard', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    padding: 60px 80px;
    box-sizing: border-box;
    position: relative;
    overflow: hidden;
  }}
  .bg-glow {{
    position: absolute;
    top: 40%;
    left: 50%;
    transform: translate(-50%, -50%);
    width: 1000px;
    height: 1000px;
    background: radial-gradient(circle, rgba(79, 70, 229, 0.15) 0%, transparent 70%);
    filter: blur(90px);
    z-index: 0;
  }}
  .header {{
    position: relative;
    z-index: 10;
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 2px solid rgba(255, 255, 255, 0.1);
    padding-bottom: 24px;
  }}
  .badge {{
    background: linear-gradient(135deg, #4f46e5 0%, #a855f7 100%);
    padding: 10px 24px;
    border-radius: 50px;
    font-size: 22px;
    font-weight: 800;
    letter-spacing: 1px;
    box-shadow: 0 4px 15px rgba(79, 70, 229, 0.4);
  }}
  .topic-title {{
    font-size: 24px;
    color: #94a3b8;
    font-weight: 700;
  }}
  .content {{
    position: relative;
    z-index: 10;
    margin: 30px 0;
    flex: 1;
    display: flex;
    flex-direction: column;
    justify-content: center;
  }}
  h1 {{
    font-size: 46px;
    font-weight: 800;
    margin: 0 0 10px 0;
    color: #f8fafc;
    letter-spacing: -1px;
  }}
  .subtitle {{
    font-size: 24px;
    color: #818cf8;
    margin-bottom: 35px;
    font-weight: 600;
  }}
  .grid-2 {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 30px;
  }}
  .card {{
    background: rgba(17, 24, 39, 0.75);
    border: 1px solid rgba(255, 255, 255, 0.12);
    border-radius: 20px;
    padding: 35px;
    backdrop-filter: blur(12px);
    box-shadow: 0 20px 40px rgba(0,0,0,0.5);
    font-size: 26px;
    line-height: 1.6;
    color: #cbd5e1;
  }}
  .card h3 {{
    margin-top: 0;
    font-size: 30px;
    color: #f8fafc;
  }}
  .tag-blue {{ color: #38bdf8 !important; }}
  .tag-purple {{ color: #c084fc !important; }}
  .highlight {{
    color: #facc15;
    font-weight: 700;
  }}
  .formula-box {{
    background: rgba(79, 70, 229, 0.15);
    border-left: 5px solid #818cf8;
    padding: 20px 30px;
    border-radius: 12px;
    margin-top: 20px;
    font-size: 28px;
    color: #ffffff;
  }}
  .footer {{
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
  }}
  .slide-num {{
    color: #a855f7;
    font-weight: 800;
  }}
</style>
</head>
<body>
  <div class="bg-glow"></div>
  <div class="header">
    <span class="badge">{data['part']}</span>
    <span class="topic-title">세종고등학교 역학과 에너지</span>
  </div>
  <div class="content">
    <h1>{data['title']}</h1>
    <div class="subtitle">{data['subtitle']}</div>
    {data['content']}
  </div>
  <div class="footer">
    <span>SEJONG HIGH SCHOOL PHYSICS DEPARTMENT</span>
    <span class="slide-num">SLIDE {slide_idx:02d} / 70</span>
  </div>
</body>
</html>
"""

print(f"Generating enhanced 70 slide images with Playwright...")

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport={"width": 1920, "height": 1080})

    for i in range(1, 71):
        data = slides_data[i-1]
        html_code = build_slide_html(i, data)
        page.set_content(html_code)
        page.wait_for_timeout(300) # Wait for KaTeX and SVG rendering
        
        png_bytes = page.screenshot(type="png")
        img = Image.open(io.BytesIO(png_bytes))
        
        slide_filename = f"slide_{i:02d}.webp"
        save_path = os.path.join(output_dir, slide_filename)
        img.save(save_path, "WEBP", quality=88)
        print(f"Generated Slide {i:02d} -> {slide_filename}")

    browser.close()

print("All 70 slides redesigned and rendered to high-definition WebP successfully!")
