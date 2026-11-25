"""4강에서 강의로 풀어서 설명할 보충 슬라이드. 원본 슬라이드는 유지합니다."""

import os

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch, FancyBboxPatch, Rectangle, Wedge

if os.name == "nt":
    plt.rc("font", family="Malgun Gothic")
else:
    plt.rc("font", family="AppleGothic")
plt.rcParams["axes.unicode_minus"] = False

OUT = r"r:\textbook-svelte\public\images\slides\mech_04"
PREVIEW = r"r:\textbook-svelte\tmp"
os.makedirs(OUT, exist_ok=True)

BLUE = "#1d4ed8"
INK = "#0f172a"
MUTED = "#475569"
WARM = "#c2410c"
OK = "#047857"
NO = "#b91c1c"
LINE = "#334155"


def new_slide():
    fig, ax = plt.subplots(figsize=(16, 9), dpi=100)
    fig.subplots_adjust(0, 0, 1, 1)
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 9)
    ax.axis("off")
    fig.patch.set_facecolor("white")
    ax.set_facecolor("white")
    return fig, ax


def save(fig, name):
    fig.savefig(os.path.join(OUT, name), format="webp", dpi=100)
    fig.savefig(os.path.join(PREVIEW, name.replace(".webp", ".jpg")), format="jpg", dpi=60)
    plt.close(fig)


def title(ax, text):
    ax.text(0.55, 8.45, text, fontsize=28, color=BLUE, fontweight="bold", va="center")


def box(ax, x, y, w, h, fc, ec):
    ax.add_patch(
        FancyBboxPatch(
            (x, y), w, h,
            boxstyle="round,pad=0.02,rounding_size=0.12",
            facecolor=fc, edgecolor=ec, linewidth=2,
        )
    )


def note(ax, text, y=0.45):
    ax.text(0.55, y, text, fontsize=16, color=MUTED, va="center")


def slide_pressure_question():
    fig, ax = new_slide()
    title(ax, "압력은 분자가 벽을 미는 힘이다")
    ax.text(0.55, 7.75, "70번의 열운동을, 압력의 뜻으로 바꿉니다.", fontsize=18, color=MUTED)

    ax.add_patch(Rectangle((1.0, 2.3), 4.6, 4.4, fill=False, edgecolor=LINE, linewidth=2.5))
    ax.add_patch(Circle((2.3, 4.6), 0.22, facecolor="#38bdf8", edgecolor=BLUE, lw=1.5))
    ax.add_patch(Circle((3.4, 3.4), 0.22, facecolor="#38bdf8", edgecolor=BLUE, lw=1.5))
    ax.add_patch(Circle((4.2, 5.4), 0.22, facecolor="#38bdf8", edgecolor=BLUE, lw=1.5))
    ax.add_patch(FancyArrowPatch((4.5, 5.4), (5.45, 5.4), arrowstyle="-|>", mutation_scale=16, lw=2, color=WARM))
    ax.text(3.3, 2.05, "기체 통", fontsize=16, color=MUTED, ha="center")

    rows = [
        "분자는 멈추지 않고 벽과 부딪힙니다.",
        "부딪힐 때마다 벽은 힘을 받습니다.",
        "그 평균 힘을 벽의 넓이로 나눈 값이 압력입니다.",
        "P  =  F  /  A",
    ]
    y = 6.5
    for i, row in enumerate(rows):
        weight = "bold" if i == 3 else "regular"
        size = 26 if i == 3 else 20
        color = INK if i == 3 else INK
        ax.text(6.6, y, row, fontsize=size, color=color, fontweight=weight, va="center")
        y -= 1.15
    note(ax, "빠르고, 무겁고, 많은 분자가 좁은 벽을 자주 치면 압력이 큽니다.")
    save(fig, "lesson_pressure_question.webp")


def slide_collision():
    fig, ax = new_slide()
    title(ax, "입자 하나가 벽을 치고 되돌아갈 때")
    ax.text(0.55, 7.75, "정육면체의 한 변을 L이라 하고, 탄성 충돌로 봅니다.", fontsize=18, color=MUTED)

    ax.add_patch(Rectangle((0.8, 3.3), 5.2, 3.3, fill=False, edgecolor=LINE, lw=2.5))
    ax.add_patch(Rectangle((6.0, 3.3), 0.18, 3.3, facecolor="#cbd5e1", edgecolor=LINE))
    ax.add_patch(Circle((4.3, 4.95), 0.28, facecolor="#f59e0b", edgecolor=WARM, lw=1.5))
    ax.add_patch(FancyArrowPatch((2.2, 4.95), (3.7, 4.95), arrowstyle="-|>", mutation_scale=18, lw=2.4, color=BLUE))
    ax.text(2.9, 5.45, "들어올 때  vx", fontsize=16, color=BLUE, ha="center")
    ax.add_patch(FancyArrowPatch((3.85, 4.15), (2.55, 4.15), arrowstyle="-|>", mutation_scale=18, lw=2.4, color=OK))
    ax.text(0.95, 4.15, "나갈 때", fontsize=15, color=OK, va="center")
    ax.text(0.9, 2.85, "길이 L     초록 화살은 반사된 속도 -vx", fontsize=16, color=MUTED)

    steps = [
        "1   벽이 받은 충격의 크기   2 m vx",
        "2   같은 벽에 다시 오기까지   2L / vx",
        "3   평균 힘   =   m vx² / L",
        "4   벽 넓이 L² 로 나누면   m vx² / V",
    ]
    y = 6.7
    for step in steps:
        ax.text(7.0, y, step, fontsize=20, color=INK, va="center")
        y -= 1.05
    note(ax, "V = L³ 입니다. 입자 하나의 x방향 몫만 먼저 구한 단계입니다.")
    save(fig, "lesson_collision.webp")


def slide_pressure_result():
    fig, ax = new_slide()
    title(ax, "세 방향을 모으면 압력 공식이 됩니다")
    ax.text(0.55, 7.75, "분자는 x, y, z로 고르게 움직입니다.", fontsize=18, color=MUTED)

    labels = [("vx²", 1.1), ("vy²", 4.5), ("vz²", 7.9)]
    for text, x in labels:
        box(ax, x, 5.55, 2.8, 1.45, "#eff6ff", BLUE)
        ax.text(x + 1.4, 6.28, text, fontsize=22, color=INK, ha="center", fontweight="bold")
    ax.text(0.7, 5.15, "속력의 제곱은 세 성분의 합입니다.  평균도 같습니다.", fontsize=18, color=INK)
    ax.text(0.7, 4.45, "<vx²>  =  <v²>  /  3", fontsize=24, color=BLUE, fontweight="bold")

    box(ax, 0.55, 1.35, 15.0, 2.55, "#ecfdf5", OK)
    ax.text(0.9, 3.25, "N개를 더하고 부피 V로 나누면", fontsize=18, color=MUTED)
    ax.text(0.9, 2.4, "P   =   (1/3)  (N / V)  m <v²>", fontsize=28, color=INK, fontweight="bold")
    ax.text(0.9, 1.65, "빠르거나, 무겁거나, 많으면 압력이 크고, 통이 넓으면 압력이 작습니다.", fontsize=18, color=OK)
    save(fig, "lesson_pressure.webp")


def slide_temperature():
    fig, ax = new_slide()
    title(ax, "압력 공식과 상태방정식이 만나 온도의 정체가 드러난다")
    ax.text(0.55, 7.7, "71번의 내부에너지 정의(분자 운동에너지의 총합)를 방금 구한 압력 식과 합칩니다.", fontsize=18, color=MUTED)

    box(ax, 0.5, 4.25, 7.4, 3.0, "#f8fafc", "#cbd5e1")
    ax.text(0.85, 6.65, "1. 기체분자운동론 (미시)", fontsize=19, color=BLUE, fontweight="bold")
    ax.text(0.85, 5.9, "P V  =  (1/3) N m <v²>  =  (2/3) N (1/2 m <v²>)", fontsize=17.5, color=INK, fontweight="bold")
    ax.text(0.85, 5.1, "내부에너지   U  =  N × (1/2 m <v²>)", fontsize=18, color=INK)
    ax.text(0.85, 4.5, "따라서   P V  =  (2/3) U     →     U  =  (3/2) P V", fontsize=18, color=OK, fontweight="bold")

    box(ax, 8.15, 4.25, 7.35, 3.0, "#eff6ff", BLUE)
    ax.text(8.5, 6.65, "2. 이상기체 법칙 (거시) 와 비교", fontsize=19, color=BLUE, fontweight="bold")
    ax.text(8.5, 5.9, "P V  =  N k T  =  n R T", fontsize=20, color=INK, fontweight="bold")
    ax.text(8.5, 5.1, "(2/3) N (1/2 m <v²>)  =  N k T   양변의 N 을 나누면", fontsize=16.5, color=MUTED)
    ax.text(8.5, 4.5, "분자 1개 평균 운동에너지   (1/2) m <v²>  =  (3/2) k T", fontsize=18, color=WARM, fontweight="bold")

    box(ax, 0.5, 0.9, 15.0, 2.95, "#fff7ed", WARM)
    ax.text(0.85, 3.25, "3. 분자 1개(k)에서 기체 전체(R)로 이어지는 내부에너지", fontsize=19, color=WARM, fontweight="bold")
    ax.text(0.85, 2.35, "U  =  N × (3/2 k T)  =  (3/2) N k T  =  (3/2) n R T", fontsize=25, color=INK, fontweight="bold")
    ax.text(0.85, 1.4, "볼츠만 상수 k 는 '분자 1개의 에너지를 온도 T 로 바꿔 주는 환율'이고,  기체 상수 R 은 '1몰 전체의 환율'입니다.", fontsize=17.5, color=INK)
    save(fig, "lesson_temperature.webp")


def slide_rms_speed():
    fig, ax = new_slide()
    title(ax, "분자의 평균 속력(v_rms)과 상수 k · R 의 짝 맞춤")
    ax.text(0.55, 7.75, "(1/2) m <v²> = (3/2) k T 에서 분자가 실제로 얼마나 빠르게 날아다니는지 구합니다.", fontsize=18, color=MUTED)

    box(ax, 0.5, 4.25, 7.35, 3.0, "#eff6ff", BLUE)
    ax.text(0.85, 6.65, "분자 1개 기준 (질량 m, 상수 k)", fontsize=20, color=BLUE, fontweight="bold")
    ax.text(0.85, 5.75, "<v²>  =  3 k T / m", fontsize=22, color=INK, fontweight="bold")
    ax.text(0.85, 4.85, "v_rms  =  √<v²>  =  √(3 k T / m)", fontsize=22, color=OK, fontweight="bold")

    box(ax, 8.15, 4.25, 7.35, 3.0, "#ecfdf5", OK)
    ax.text(8.5, 6.65, "1몰 묶음 기준 (몰질량 M, 상수 R)", fontsize=20, color=OK, fontweight="bold")
    ax.text(8.5, 5.75, "분자 1몰 질량  M = NA m,   기체 상수  R = NA k", fontsize=17.5, color=INK)
    ax.text(8.5, 4.85, "v_rms  =  √(3 R T / M)", fontsize=22, color=OK, fontweight="bold")

    box(ax, 0.5, 1.0, 15.0, 2.8, "#f8fafc", "#cbd5e1")
    ax.text(0.85, 3.2, "핵심 정리 (이어지는 72번 슬라이드와 연결)", fontsize=19, color=WARM, fontweight="bold")
    ax.text(0.85, 2.4, "• 같은 온도 T 이면 기체 종류와 상관없이 분자 1개의 평균 운동에너지 (3/2) k T 는 같습니다.", fontsize=18, color=INK)
    ax.text(0.85, 1.6, "• 온도가 높을수록(√T), 분자가 가벼울수록(1/√m) 분자는 더 빠르게 움직입니다.", fontsize=18, color=INK)
    save(fig, "lesson_rms_speed.webp")


def slide_monatomic():
    fig, ax = new_slide()
    title(ax, "단원자는 세 방향으로 에너지를 나눈다")
    ax.text(0.55, 7.75, "에너지 등분배: 제곱으로 된 에너지 항마다 분자 1개에 평균 (1/2) k T 씩 배당됩니다.", fontsize=18, color=MUTED)

    ax.add_patch(Circle((2.4, 5.3), 0.55, facecolor="#fde68a", edgecolor=WARM, lw=2))
    ax.text(2.4, 5.3, "He", fontsize=18, color=INK, ha="center", va="center", fontweight="bold")
    for ang, label, dx, dy in (
        (0, "vx", 1.5, 0.15),
        (90, "vy", 0.15, 1.45),
        (40, "vz", 1.15, 1.05),
    ):
        ax.annotate(
            "",
            xy=(2.4 + dx, 5.3 + dy),
            xytext=(2.4, 5.3),
            arrowprops=dict(arrowstyle="-|>", color=BLUE, lw=2),
        )
        ax.text(2.4 + dx + 0.15, 5.3 + dy + 0.05, label, fontsize=16, color=BLUE)

    box(ax, 6.3, 3.7, 9.1, 3.35, "#f8fafc", "#cbd5e1")
    ax.text(6.65, 6.4, "병진 운동  vx, vy, vz  세 항 (자유도 f = 3)", fontsize=20, color=INK, fontweight="bold")
    ax.text(6.65, 5.55, "각 방향마다   (1/2) k T", fontsize=22, color=BLUE, fontweight="bold")
    ax.text(6.65, 4.65, "분자 1개   (3/2) k T", fontsize=22, color=INK, fontweight="bold")
    ax.text(6.65, 3.9, "기체 전체   U = (3/2) N k T = (3/2) n R T", fontsize=20, color=OK, fontweight="bold")

    note(ax, "헬륨(He)·네온(Ne)·아르곤(Ar)처럼 원자 하나로 돌아다니는 기체입니다.", y=2.3)
    ax.text(0.55, 1.35, "자유도(f)는 '분자가 에너지를 나눠 가질 독립된 운동 방향의 수'입니다.", fontsize=18, color=MUTED)
    save(fig, "lesson_monatomic.webp")


def slide_diatomic():
    fig, ax = new_slide()
    title(ax, "이원자는 회전이 두 방향 더 있다")
    ax.text(0.55, 7.75, "산소(O2)·질소(N2)·수소(H2)처럼 원자 둘이 아령처럼 붙은 기체입니다.", fontsize=18, color=MUTED)

    ax.add_patch(Circle((1.7, 5.5), 0.48, facecolor="#bfdbfe", edgecolor=BLUE, lw=2))
    ax.add_patch(Circle((3.5, 5.5), 0.48, facecolor="#bfdbfe", edgecolor=BLUE, lw=2))
    ax.plot([2.15, 3.05], [5.5, 5.5], color=LINE, lw=4)
    ax.text(2.6, 4.55, "결합축", fontsize=15, color=MUTED, ha="center")
    ax.text(2.6, 6.55, "결합축 둘레 회전은 관성모멘트가 무시되어 빠짐", fontsize=14, color=WARM, ha="center")

    rows = [
        ("병진", "vx, vy, vz", "3", "(3/2) k T"),
        ("회전", "결합축에 수직인 두 축", "2", "(2/2) k T"),
        ("합", "보통 온도의 이원자", "5", "(5/2) k T"),
    ]
    y = 6.55
    for name, how, f, energy in rows:
        ax.text(5.3, y, name, fontsize=20, color=BLUE, fontweight="bold", va="center")
        ax.text(7.2, y, how, fontsize=18, color=INK, va="center")
        ax.text(12.0, y, "f = " + f, fontsize=18, color=INK, va="center")
        ax.text(13.5, y, energy, fontsize=18, color=OK, fontweight="bold", va="center")
        y -= 1.15

    box(ax, 0.5, 0.45, 15.0, 1.7, "#fff7ed", WARM)
    ax.text(0.85, 1.5, "기체 전체   U  =  (5/2) N k T  =  (5/2) n R T     (일반식 : U = (f/2) N k T = (f/2) n R T)", fontsize=21, color=INK, fontweight="bold")
    ax.text(0.85, 0.8, "진동(f = 2 추가)은 아주 높은 온도에서만 켜지므로, 상온에서는 병진 3 + 회전 2 = 5 만 씁니다.", fontsize=17.5, color=MUTED)
    save(fig, "lesson_diatomic.webp")


def slide_isobaric_split():
    fig, ax = new_slide()
    title(ax, "등압에서 열은 두 갈래로 쓰인다")
    ax.text(0.55, 7.75, "90번의  Q = PΔV + ΔU  를 단원자·이원자로 나눕니다.", fontsize=18, color=MUTED)

    box(ax, 0.7, 4.5, 4.2, 2.4, "#fee2e2", NO)
    ax.text(2.8, 5.7, "넣은 열  Q", fontsize=22, color=NO, ha="center", fontweight="bold")
    ax.add_patch(FancyArrowPatch((5.1, 5.7), (6.3, 6.5), arrowstyle="-|>", mutation_scale=16, lw=2, color=OK))
    ax.add_patch(FancyArrowPatch((5.1, 5.7), (6.3, 4.9), arrowstyle="-|>", mutation_scale=16, lw=2, color=BLUE))

    box(ax, 6.5, 5.85, 8.8, 1.7, "#ecfdf5", OK)
    ax.text(6.85, 6.95, "밖으로 한 일", fontsize=18, color=OK, fontweight="bold")
    ax.text(6.85, 6.25, "W  =  P ΔV  =  n R ΔT", fontsize=20, color=INK, fontweight="bold")

    box(ax, 6.5, 3.7, 8.8, 1.7, "#eff6ff", BLUE)
    ax.text(6.85, 4.8, "온도를 올리는 몫", fontsize=18, color=BLUE, fontweight="bold")
    ax.text(6.85, 4.1, "ΔU  =  (f/2) n R ΔT", fontsize=20, color=INK, fontweight="bold")

    note(ax, "등압 팽창은 부피가 늘어 일을 합니다. 넣은 열이 전부 온도 상승에 쓰이지 않습니다.", y=2.4)
    ax.text(0.55, 1.5, "f는 자유도입니다. 단원자는 3, 보통 온도의 이원자는 5입니다.", fontsize=18, color=INK)
    save(fig, "lesson_isobaric_split.webp")


def slide_isobaric_heat():
    fig, ax = new_slide()
    title(ax, "등압에서 필요한 열")
    ax.text(0.55, 7.75, "Q = W + ΔU 에 자유도를 넣습니다.", fontsize=18, color=MUTED)

    box(ax, 0.5, 3.5, 7.3, 3.6, "#f8fafc", "#cbd5e1")
    ax.text(0.85, 6.45, "단원자", fontsize=22, color=BLUE, fontweight="bold")
    ax.text(0.85, 5.6, "ΔU = (3/2) n R ΔT", fontsize=20, color=INK)
    ax.text(0.85, 4.85, "W = n R ΔT", fontsize=20, color=INK)
    ax.text(0.85, 3.9, "Q = (5/2) n R ΔT", fontsize=24, color=OK, fontweight="bold")

    box(ax, 8.15, 3.5, 7.3, 3.6, "#fff7ed", WARM)
    ax.text(8.5, 6.45, "이원자", fontsize=22, color=WARM, fontweight="bold")
    ax.text(8.5, 5.6, "ΔU = (5/2) n R ΔT", fontsize=20, color=INK)
    ax.text(8.5, 4.85, "W = n R ΔT", fontsize=20, color=INK)
    ax.text(8.5, 3.9, "Q = (7/2) n R ΔT", fontsize=24, color=OK, fontweight="bold")

    note(ax, "5/2와 7/2는 외울 암호가 아닙니다. 일을 위한 1과, 자유도의 절반을 더한 수입니다.", y=2.2)
    ax.text(0.55, 1.3, "등압 압축이면 ΔT가 음수라 열을 버립니다. 식의 모양은 같습니다.", fontsize=18, color=INK)
    save(fig, "lesson_isobaric_heat.webp")


def slide_molar_heat():
    fig, ax = new_slide()
    title(ax, "등압 몰비열이 등적보다 R만큼 크다")
    ax.text(0.55, 7.75, "92번의 등적 과정과 90번의 등압 과정을 나란히 봅니다.", fontsize=18, color=MUTED)

    box(ax, 0.45, 4.15, 7.4, 3.15, "#eff6ff", BLUE)
    ax.text(0.8, 6.7, "등적", fontsize=22, color=BLUE, fontweight="bold")
    ax.text(0.8, 5.9, "부피가 고정되어 일이 0입니다.", fontsize=18, color=INK)
    ax.text(0.8, 5.15, "넣은 열은 전부 ΔU가 됩니다.", fontsize=18, color=INK)
    ax.text(0.8, 4.45, "몰비열의 이름   Cv", fontsize=20, color=INK, fontweight="bold")

    box(ax, 8.15, 4.15, 7.4, 3.15, "#ecfdf5", OK)
    ax.text(8.5, 6.7, "등압", fontsize=22, color=OK, fontweight="bold")
    ax.text(8.5, 5.9, "온도를 올릴 뿐 아니라 일도 합니다.", fontsize=18, color=INK)
    ax.text(8.5, 5.15, "일이 n R ΔT만큼 더 듭니다.", fontsize=18, color=INK)
    ax.text(8.5, 4.45, "Cp  =  Cv  +  R", fontsize=22, color=INK, fontweight="bold")

    ax.text(0.55, 3.35, "단원자   Cv = 3/2 R    Cp = 5/2 R    γ = Cp/Cv = 5/3", fontsize=20, color=INK)
    ax.text(0.55, 2.55, "이원자   Cv = 5/2 R    Cp = 7/2 R    γ = 7/5", fontsize=20, color=INK)
    note(ax, "같은 온도를 올리려면 등압이 등적보다 열이 더 필요합니다. γ는 비열비입니다.", y=1.4)
    save(fig, "lesson_molar_heat.webp")


def slide_stirling_cycle():
    fig, ax = new_slide()
    title(ax, "스털링 기관은 등온과 등적이 번갈아 온다")
    ax.text(0.55, 7.75, "106번 다음에, 한 바퀴의 네 과정을 말로 고정합니다.", fontsize=18, color=MUTED)

    steps = [
        ("1 → 2", "고온 등온 팽창", "열을 받으며 일을 합니다.  ΔU = 0", "#fee2e2", NO),
        ("2 → 3", "등적 냉각", "부피는 그대로, 온도만 TH에서 TC로.  일 = 0", "#f8fafc", LINE),
        ("3 → 4", "저온 등온 압축", "열을 버리며 일을 받습니다.  ΔU = 0", "#dbeafe", BLUE),
        ("4 → 1", "등적 가열", "부피는 그대로, 온도만 TC에서 TH로.  일 = 0", "#ecfdf5", OK),
    ]
    y = 6.85
    for tag, name, desc, fc, ec in steps:
        box(ax, 0.5, y - 0.55, 15.0, 1.25, fc, ec)
        ax.text(0.8, y, tag, fontsize=18, color=ec, fontweight="bold", va="center")
        ax.text(2.7, y, name, fontsize=20, color=INK, fontweight="bold", va="center")
        ax.text(6.5, y, desc, fontsize=18, color=INK, va="center")
        y -= 1.5
    note(ax, "등온에서는 온도가 안 변해 내부에너지가 그대로입니다. 등적에서는 부피가 안 변해 일이 없습니다.")
    save(fig, "lesson_stirling_cycle.webp")


def slide_stirling_efficiency():
    fig, ax = new_slide()
    title(ax, "등적에서 받은 열은 효율의 분모에 남는다")
    ax.text(0.55, 7.7, "등적 가열과 등적 냉각의 열은 크기가 같습니다.  n Cv (TH - TC)", fontsize=17, color=MUTED)

    box(ax, 0.45, 4.4, 15.1, 2.85, "#f8fafc", "#cbd5e1")
    ax.text(0.8, 6.65, "일", fontsize=18, color=OK, fontweight="bold")
    ax.text(0.8, 5.95, "등적 열은 들어왔다가 같은 양으로 나가므로, 일에는 등온의 차이만 남습니다.", fontsize=17, color=INK)
    ax.text(0.8, 5.25, "받은 열", fontsize=18, color=NO, fontweight="bold")
    ax.text(0.8, 4.7, "분모에는 고온 등온의 열과 등적 가열의 열이 모두 들어갑니다.", fontsize=17, color=INK)

    box(ax, 0.45, 1.35, 7.3, 2.85, "#ecfdf5", OK)
    ax.text(0.8, 3.6, "카르노", fontsize=20, color=OK, fontweight="bold")
    ax.text(0.8, 2.8, "등적 가열이 없습니다.", fontsize=18, color=INK)
    ax.text(0.8, 2.05, "TH = 400 K, TC = 300 K", fontsize=18, color=INK)
    ax.text(0.8, 1.45, "η = 1 - 300/400 = 0.25", fontsize=20, color=INK, fontweight="bold")

    box(ax, 8.05, 1.35, 7.5, 2.85, "#fff7ed", WARM)
    ax.text(8.4, 3.6, "이 계산의 스털링", fontsize=20, color=WARM, fontweight="bold")
    ax.text(8.4, 2.8, "단원자, 부피비 e", fontsize=18, color=INK)
    ax.text(8.4, 2.05, "η = 100 / 550", fontsize=20, color=INK, fontweight="bold")
    ax.text(8.4, 1.45, "약 0.18", fontsize=20, color=NO, fontweight="bold")

    note(ax, "등적 열을 저장했다가 다시 쓰는 재생기가 있으면 그 열은 분모에서 빠지고, 효율은 카르노와 같아집니다.")
    save(fig, "lesson_stirling_efficiency.webp")


def slide_coins():
    fig, ax = new_slide()
    title(ax, "동전 네 개로 거시상태와 미시상태를 센다")
    ax.text(0.55, 7.75, "130~134번의 주사위와 같은 생각입니다. 앞면의 개수만 거시상태입니다.", fontsize=18, color=MUTED)

    headers = ["앞면 수", "0", "1", "2", "3", "4"]
    values = ["경우의 수 Ω", "1", "4", "6", "4", "1"]
    xs = [0.7, 3.3, 5.5, 7.7, 9.9, 12.1]
    for x, h in zip(xs, headers):
        ax.text(x, 6.35, h, fontsize=20, color=BLUE, fontweight="bold")
    for x, v in zip(xs, values):
        weight = "bold" if v == "6" else "regular"
        color = OK if v == "6" else INK
        ax.text(x, 5.45, v, fontsize=26, color=color, fontweight=weight)

    ax.plot([0.55, 14.5], [5.95, 5.95], color="#cbd5e1", lw=1.5)
    ax.text(0.55, 4.2, "전부 16가지입니다.  1 + 4 + 6 + 4 + 1 = 16", fontsize=20, color=INK)
    ax.text(0.55, 3.3, "앞면이 정확히 2개인 거시상태가 가장 많습니다.", fontsize=20, color=INK)
    ax.text(0.55, 2.4, "어느 동전이 앞면인지는 미시상태입니다. 거시상태는 그 개수만 봅니다.", fontsize=20, color=INK)
    note(ax, "전부 앞면인 경우는 1가지, 반반인 경우는 6가지입니다. 섞인 쪽이 흔합니다.")
    save(fig, "lesson_coins.webp")


def slide_coin_entropy():
    fig, ax = new_slide()
    title(ax, "경우의 수가 많을수록 엔트로피가 크다")
    ax.text(0.55, 7.75, "볼츠만의 식은 그 경우의 수에 로그를 씌웁니다.", fontsize=18, color=MUTED)

    box(ax, 0.5, 4.7, 15.0, 2.3, "#eff6ff", BLUE)
    ax.text(0.9, 6.15, "S  =  k ln Ω", fontsize=32, color=INK, fontweight="bold")
    ax.text(0.9, 5.15, "k는 볼츠만 상수입니다. Ω가 1이면 ln 1 = 0이라 엔트로피가 가장 작습니다.", fontsize=18, color=INK)

    box(ax, 0.5, 1.7, 7.3, 2.55, "#f8fafc", "#cbd5e1")
    ax.text(0.85, 3.6, "전부 앞면", fontsize=20, color=BLUE, fontweight="bold")
    ax.text(0.85, 2.75, "Ω = 1", fontsize=22, color=INK, fontweight="bold")
    ax.text(0.85, 2.05, "가장 질서 있고, 가장 드뭅니다.", fontsize=18, color=INK)

    box(ax, 8.15, 1.7, 7.35, 2.55, "#ecfdf5", OK)
    ax.text(8.5, 3.6, "앞면 2개", fontsize=20, color=OK, fontweight="bold")
    ax.text(8.5, 2.75, "Ω = 6", fontsize=22, color=INK, fontweight="bold")
    ax.text(8.5, 2.05, "가장 흔하고, 엔트로피가 가장 큽니다.", fontsize=18, color=INK)

    note(ax, "저절로 동전 네 개가 모두 앞면으로 모이는 일은, 경우의 수가 너무 적어 거의 일어나지 않습니다.")
    save(fig, "lesson_coin_entropy.webp")


def slide_free_expansion():
    fig, ax = new_slide()
    title(ax, "칸막이를 없애면 기체가 빈 방으로 퍼진다")
    ax.text(0.55, 7.75, "바깥벽은 단열이고, 오른쪽 방은 진공입니다.", fontsize=18, color=MUTED)

    ax.add_patch(Rectangle((0.8, 3.6), 3.3, 3.0, facecolor="#dbeafe", edgecolor=BLUE, lw=2))
    ax.add_patch(Rectangle((4.1, 3.6), 3.3, 3.0, facecolor="#f8fafc", edgecolor=LINE, lw=2))
    ax.plot([4.1, 4.1], [3.6, 6.6], color=WARM, lw=3, linestyle="--")
    for xy in ((1.5, 5.5), (2.2, 4.5), (2.8, 5.8), (3.3, 4.2)):
        ax.add_patch(Circle(xy, 0.16, facecolor="#38bdf8", edgecolor=BLUE))
    ax.text(2.45, 3.2, "기체", fontsize=16, color=BLUE, ha="center")
    ax.text(5.75, 5.1, "진공", fontsize=18, color=MUTED, ha="center")
    ax.text(4.1, 2.7, "칸막이", fontsize=14, color=WARM, ha="center")

    box(ax, 8.0, 3.4, 7.4, 3.3, "#fff7ed", WARM)
    ax.text(8.35, 6.05, "이 과정의 세 가지", fontsize=18, color=WARM, fontweight="bold")
    ax.text(8.35, 5.25, "Q = 0     열이 드나들지 않습니다.", fontsize=18, color=INK)
    ax.text(8.35, 4.55, "W = 0     밀어 낸 피스톤이 없습니다.", fontsize=18, color=INK)
    ax.text(8.35, 3.8, "ΔU = 0    그래서 온도도 그대로입니다.", fontsize=18, color=INK, fontweight="bold")

    note(ax, "Q = W + ΔU 에서 열도 일도 없으면 내부에너지가 변하지 않습니다. 이상기체의 온도는 그대로입니다.")
    save(fig, "lesson_free_expansion.webp")


def slide_free_count():
    fig, ax = new_slide()
    title(ax, "온도는 그대로인데 엔트로피는 늘어난다")
    ax.text(0.55, 7.75, "부피가 두 배가 되면, 분자 하나가 있을 자리가 두 배가 됩니다.", fontsize=18, color=MUTED)

    box(ax, 0.45, 4.35, 15.1, 2.9, "#f8fafc", "#cbd5e1")
    ax.text(0.8, 6.6, "N개의 분자가 서로 독립이면", fontsize=18, color=BLUE, fontweight="bold")
    ax.text(0.8, 5.75, "미시상태의 비   Ω뒤 / Ω처음  =  2^N", fontsize=22, color=INK, fontweight="bold")
    ax.text(0.8, 4.85, "ΔS  =  k ln(2^N)  =  N k ln 2  =  n R ln 2", fontsize=22, color=OK, fontweight="bold")

    box(ax, 0.45, 1.45, 15.1, 2.5, "#eff6ff", BLUE)
    ax.text(0.8, 3.3, "같은 답을 등온 경로로도 확인할 수 있습니다.", fontsize=18, color=BLUE, fontweight="bold")
    ax.text(0.8, 2.5, "엔트로피는 상태함수입니다. 처음과 끝이 같으면 경로는 달라도 ΔS가 같습니다.", fontsize=18, color=INK)
    ax.text(0.8, 1.75, "가역 등온 팽창으로 바꾸면  Q = n R T ln 2,   ΔS = Q / T = n R ln 2", fontsize=18, color=INK)

    note(ax, "열도 없고 일도 없었지만, 퍼진 상태는 경우의 수가 많아 저절로 한쪽으로 돌아가지 않습니다.")
    save(fig, "lesson_free_count.webp")


def slide_thermal_resistance():
    fig, ax = new_slide()
    title(ax, "열전도는 전기 저항처럼 읽는다")
    ax.text(0.55, 7.75, "13~14번의 전도 식을 열저항으로 바꾸면, 겹벽과 단열재가 한눈에 보입니다.", fontsize=18, color=MUTED)

    ax.add_patch(Rectangle((0.8, 4.1), 1.3, 2.5, facecolor="#fee2e2", edgecolor=NO, lw=2))
    ax.add_patch(Rectangle((2.1, 4.1), 1.9, 2.5, facecolor="#e2e8f0", edgecolor=LINE, lw=2))
    ax.add_patch(Rectangle((4.0, 4.1), 1.9, 2.5, facecolor="#fef3c7", edgecolor=WARM, lw=2))
    ax.add_patch(Rectangle((5.9, 4.1), 1.3, 2.5, facecolor="#dbeafe", edgecolor=BLUE, lw=2))
    ax.text(1.45, 5.35, "고온", fontsize=17, color=NO, ha="center", fontweight="bold")
    ax.text(3.05, 5.35, "벽 1\nR1", fontsize=17, color=INK, ha="center", va="center", fontweight="bold")
    ax.text(4.95, 5.35, "단열재\nR2", fontsize=17, color=WARM, ha="center", va="center", fontweight="bold")
    ax.text(6.55, 5.35, "저온", fontsize=17, color=BLUE, ha="center", fontweight="bold")
    ax.text(4.0, 3.55, "같은 열전류 H 가 두 층을 차례로 지나갑니다.", fontsize=16, color=MUTED, ha="center")

    box(ax, 7.9, 3.8, 7.6, 3.1, "#eff6ff", BLUE)
    ax.text(8.25, 6.3, "시간당 흐르는 열   H = Q / t", fontsize=18, color=BLUE, fontweight="bold")
    ax.text(8.25, 5.5, "H  =  k A ΔT / L  =  ΔT / R", fontsize=22, color=INK, fontweight="bold")
    ax.text(8.25, 4.65, "열저항   R  =  L / (k A)", fontsize=22, color=OK, fontweight="bold")
    ax.text(8.25, 4.05, "두께 L 이 두껍고, k 와 A 가 작을수록 열이 잘 안 통합니다.", fontsize=15, color=INK)

    box(ax, 0.5, 1.15, 15.0, 1.95, "#fff7ed", WARM)
    ax.text(0.85, 2.55, "전기 회로와의 짝     전류 I = ΔV / R     ↔     열전류 H = ΔT / R", fontsize=20, color=INK, fontweight="bold")
    ax.text(0.85, 1.65, "벽을 겹치면 직렬 연결입니다.   R전체 = R1 + R2     단열재는 k 가 작아 R 이 매우 큰 층입니다.", fontsize=18, color=INK)
    note(ax, "이어지는 열전도도 표(15번)와 단열재(16번)는 모두 이 R = L/(kA) 를 키우는 이야기입니다.")
    save(fig, "lesson_thermal_resistance.webp")


def slide_volume_expansion():
    fig, ax = new_slide()
    title(ax, "부피팽창 계수는 왜 선팽창의 세 배인가")
    ax.text(0.55, 7.75, "31~32번의 선팽창 α 로 가로·세로·높이가 함께 늘어나는 정육면체를 봅니다.", fontsize=18, color=MUTED)

    ax.add_patch(Rectangle((0.9, 3.55), 2.5, 2.5, facecolor="#dbeafe", edgecolor=BLUE, lw=2.2))
    ax.add_patch(Rectangle((3.4, 3.55), 0.45, 2.5, facecolor="#fde68a", edgecolor=WARM, lw=1.8))
    ax.add_patch(Rectangle((0.9, 6.05), 2.5, 0.45, facecolor="#fde68a", edgecolor=WARM, lw=1.8))
    ax.add_patch(Rectangle((3.4, 6.05), 0.45, 0.45, facecolor="#fecaca", edgecolor=NO, lw=1.5))
    ax.text(2.15, 4.8, "L", fontsize=22, color=BLUE, ha="center", va="center", fontweight="bold")
    ax.text(3.62, 4.8, "ΔL", fontsize=14, color=WARM, ha="center", va="center", fontweight="bold")
    ax.text(2.15, 6.27, "ΔL", fontsize=14, color=WARM, ha="center", va="center", fontweight="bold")
    ax.text(2.35, 3.05, "모서리의 작은 칸 (ΔL)² 은 매우 작습니다.", fontsize=15, color=MUTED, ha="center")

    box(ax, 5.1, 3.45, 10.4, 3.55, "#f8fafc", "#cbd5e1")
    ax.text(5.45, 6.4, "한 변   L'  =  L (1 + α ΔT)", fontsize=20, color=INK, fontweight="bold")
    ax.text(5.45, 5.55, "부피   V'  =  L³ (1 + α ΔT)³  =  V (1 + 3α ΔT + 3α² ΔT² + α³ ΔT³)", fontsize=18, color=INK)
    ax.text(5.45, 4.65, "α 가 10^-5 정도로 매우 작으므로, α² 과 α³ 항은 버립니다.", fontsize=18, color=MUTED)
    ax.text(5.45, 3.85, "ΔV  =  3α V ΔT  =  β V ΔT       따라서   β  =  3α", fontsize=22, color=OK, fontweight="bold")

    box(ax, 0.5, 1.15, 15.0, 1.65, "#ecfdf5", OK)
    ax.text(0.85, 2.2, "세 방향(가로·세로·높이)으로 각각 α 만큼 늘어나니, 부피 비율은 그 합인 3α 가 됩니다.", fontsize=19, color=INK, fontweight="bold")
    ax.text(0.85, 1.45, "면적팽창이라면 가로·세로 두 방향이므로 2α 입니다.", fontsize=17, color=MUTED)
    save(fig, "lesson_volume_expansion.webp")


def slide_boltzmann_constant():
    fig, ax = new_slide()
    title(ax, "왜 비례상수가 두 개일까 : PV = nRT 와 PV = NkT")
    ax.text(0.55, 7.75, "66번의 PV / T = 일정 에서, 일정한 값은 기체의 양에 비례합니다. 양을 세는 단위만 다릅니다.", fontsize=18, color=MUTED)

    box(ax, 0.5, 4.05, 7.3, 3.2, "#ecfdf5", OK)
    ax.text(0.85, 6.65, "거시 세계 : 몰(묶음) 단위로 세기", fontsize=20, color=OK, fontweight="bold")
    ax.text(0.85, 5.75, "P V  =  n R T", fontsize=28, color=INK, fontweight="bold")
    ax.text(0.85, 4.95, "n : 몰수  (1몰 = NA = 6.02 × 10^23 개 묶음)", fontsize=17.5, color=INK)
    ax.text(0.85, 4.35, "R : 기체 상수  (1몰 묶음당 비례상수,  8.31 J/mol·K)", fontsize=16.5, color=MUTED)

    box(ax, 8.2, 4.05, 7.3, 3.2, "#eff6ff", BLUE)
    ax.text(8.55, 6.65, "미시 세계 : 분자 낱개로 세기 (67번)", fontsize=20, color=BLUE, fontweight="bold")
    ax.text(8.55, 5.75, "P V  =  N k T", fontsize=28, color=INK, fontweight="bold")
    ax.text(8.55, 4.95, "N = n × NA : 기체 분자의 총개수", fontsize=17.5, color=INK)
    ax.text(8.55, 4.35, "k = R / NA : 볼츠만 상수  (분자 1개당 상수,  1.38 × 10^-23 J/K)", fontsize=16, color=MUTED)

    box(ax, 0.5, 1.15, 15.0, 2.45, "#fff7ed", WARM)
    ax.text(0.85, 3.0, "두 식을 잇는 핵심 등식     n R  =  n × (NA k)  =  (n NA) × k  =  N k", fontsize=21, color=INK, fontweight="bold")
    ax.text(0.85, 2.1, "• 기체 전체(몇 몰)를 다룰 때는  n 과 R 을 쓰고,   분자 1개의 운동을 다룰 때는  N 과 k 를 씁니다.", fontsize=18, color=INK)
    ax.text(0.85, 1.4, "• 볼츠만 상수 k 는 기체 상수 R 을 아보가드로수 NA 로 잘게 나눈 '분자 1개 몫의 상수'입니다.", fontsize=17.5, color=WARM, fontweight="bold")
    save(fig, "lesson_boltzmann_constant.webp")


def slide_isothermal_work():
    fig, ax = new_slide()
    title(ax, "등온 과정의 일은 왜 로그가 되는가")
    ax.text(0.55, 7.75, "86번처럼 온도가 일정하면, 팽창할수록 압력이 P = nRT / V 로 내려갑니다.", fontsize=18, color=MUTED)

    ax.plot([1.0, 1.0, 6.2], [6.8, 2.3, 2.3], color=LINE, lw=2.2)
    xs = [1.5 + i * 0.08 for i in range(46)]
    ys = [2.3 + 4.8 / x for x in xs]
    ax.plot(xs, ys, color=BLUE, lw=3)
    fill_x = [1.9 + i * 0.06 for i in range(42)]
    fill_y = [2.3 + 4.8 / x for x in fill_x]
    ax.fill_between(fill_x, 2.3, fill_y, color="#dbeafe", alpha=0.85)
    ax.text(0.65, 6.65, "P", fontsize=18, color=INK, fontweight="bold")
    ax.text(6.35, 2.2, "V", fontsize=18, color=INK, fontweight="bold")
    ax.text(1.9, 1.85, "V1", fontsize=16, color=INK, ha="center")
    ax.text(4.35, 1.85, "V2", fontsize=16, color=INK, ha="center")
    ax.text(3.15, 3.1, "넓이 = W", fontsize=17, color=BLUE, ha="center", fontweight="bold")

    box(ax, 6.9, 2.2, 8.6, 4.9, "#f8fafc", "#cbd5e1")
    ax.text(7.25, 6.45, "압력이 바뀌므로 P ΔV 를 바로 쓸 수 없습니다.", fontsize=18, color=INK, fontweight="bold")
    ax.text(7.25, 5.6, "작은 구간 dV 마다 한 일을 모두 더합니다.", fontsize=18, color=MUTED)
    ax.text(7.25, 4.7, "W  =  ∫ P dV  =  n R T ∫ (1 / V) dV", fontsize=21, color=INK, fontweight="bold")
    ax.text(7.25, 3.7, "W  =  n R T ln (V2 / V1)", fontsize=25, color=OK, fontweight="bold")
    ax.text(7.25, 2.7, "등온이므로 ΔU = 0     →     Q = W = n R T ln (V2 / V1)", fontsize=18, color=BLUE, fontweight="bold")

    note(ax, "뒤에 나오는 카르노 효율, 스털링 기관, 자유팽창의 ln(V2/V1) 이 모두 이 넓이에서 나옵니다.", y=0.95)
    save(fig, "lesson_isothermal_work.webp")


def slide_adiabatic_curve():
    fig, ax = new_slide()
    title(ax, "왜 단열 곡선은 등온선을 가로지르며 더 가파른가")
    ax.text(0.55, 7.75, "88번 그래프의 빨간 두 곡선(T1 > T2)은 등온선입니다. 원점에서 멀수록 PV = nRT 가 커서 고온입니다.", fontsize=17.5, color=MUTED)

    ax.plot([0.9, 0.9, 6.3], [6.9, 2.0, 2.0], color=LINE, lw=2.2)
    xs = [1.45 + i * 0.08 for i in range(52)]
    iso_high = [2.0 + 5.2 / x for x in xs]
    iso_low = [2.0 + 3.1 / x for x in xs]
    adi = [2.0 + 5.2 * (1.45 ** 0.67) / (x ** 1.67) for x in xs]
    ax.plot(xs, iso_high, color=BLUE, lw=2.5, linestyle="--")
    ax.plot(xs, iso_low, color="#94a3b8", lw=2, linestyle="--")
    ax.plot(xs[:36], adi[:36], color=NO, lw=3.2)
    ax.fill_between(xs[:36], 2.0, adi[:36], color="#fee2e2", alpha=0.7)
    ax.text(5.2, 3.18, "고온 등온선 T1", fontsize=14, color=BLUE, fontweight="bold")
    ax.text(5.2, 2.38, "저온 등온선 T2", fontsize=14, color=MUTED)
    ax.text(2.95, 3.9, "단열 팽창", fontsize=16, color=NO, fontweight="bold")
    ax.text(2.85, 2.55, "W단열 < W등온", fontsize=14, color=NO, ha="center", fontweight="bold")
    ax.text(0.6, 6.7, "P", fontsize=18, color=INK, fontweight="bold")
    ax.text(6.45, 1.9, "V", fontsize=18, color=INK, fontweight="bold")
    ax.text(1.45, 1.55, "V1", fontsize=15, color=INK, ha="center")
    ax.text(4.25, 1.55, "V2", fontsize=15, color=INK, ha="center")

    box(ax, 6.85, 4.4, 8.65, 2.75, "#fee2e2", NO)
    ax.text(7.2, 6.55, "1. 단열 팽창 (V1 → V2) : 압력이 두 번 깎인다", fontsize=19, color=NO, fontweight="bold")
    ax.text(7.2, 5.8, "• 등온 팽창 : 열 Q 를 계속 보충받아 온도 T1 유지  →  부피 증가만 작용", fontsize=16.5, color=INK)
    ax.text(7.2, 5.15, "• 단열 팽창 : Q = 0 이라 내부에너지를 써서 일을 함 (W = -ΔU > 0)", fontsize=16.5, color=INK)
    ax.text(7.2, 4.6, "   →  부피 증가 + 온도 하강(T1 → T2)이 겹쳐 아래 등온선으로 가파르게 낙하!", fontsize=16.5, color=NO, fontweight="bold")

    box(ax, 6.85, 1.5, 8.65, 2.55, "#eff6ff", BLUE)
    ax.text(7.2, 3.45, "2. 단열 압축 (V2 → V1) 과 한 일(넓이) 비교", fontsize=19, color=BLUE, fontweight="bold")
    ax.text(7.2, 2.7, "• 단열 압축 : 외부에서 받은 일이 ΔU > 0 로 쌓여 온도 상승(T2 → T1)  →  더 가파르게 상승", fontsize=16, color=INK)
    ax.text(7.2, 1.95, "• 같은 부피(V1 → V2)로 팽창할 때 단열선이 더 아래에 놓이므로  W단열 < W등온", fontsize=16.5, color=OK, fontweight="bold")

    note(ax, "88번 표의 단열 팽창(하강)과 단열 압축(상승) 화살표가 빨간 등온선 두 개를 가로지르는 이유입니다.", y=0.75)
    save(fig, "lesson_adiabatic_curve.webp")


def slide_why_molar_heat_in_adiabatic():
    fig, ax = new_slide()
    title(ax, "단열(Q = 0)인데 왜 몰비열 Cv, Cp 가 나오고 γ 배 가파를까?")
    ax.text(0.55, 7.75, "핵심은 두 식(제1법칙 + 상태방정식)에서 온도 변화 dT 를 소거할 때 Cv + R = Cp 가 만들어지는 것입니다.", fontsize=17.5, color=MUTED)

    box(ax, 0.5, 4.35, 7.35, 2.95, "#eff6ff", BLUE)
    ax.text(0.85, 6.75, "1단계 : 왜 단열에서도 ΔU = n Cv ΔT 인가?", fontsize=19, color=BLUE, fontweight="bold")
    ax.text(0.85, 6.0, "• 등적(W = 0) :  Qv = ΔU = (f/2) n R ΔT = n Cv ΔT   →   Cv = (f/2) R", fontsize=16, color=INK)
    ax.text(0.85, 5.3, "• 등압(W = nRΔT) :  Qp = n Cv ΔT + n R ΔT   →   Cp = Cv + R", fontsize=16, color=INK)
    ax.text(0.85, 4.65, "• 내부에너지 U 는 온도만의 함수이므로, 단열에서도  dU = n Cv dT  입니다.", fontsize=16, color=BLUE, fontweight="bold")

    box(ax, 8.15, 4.35, 7.35, 2.95, "#fff7ed", WARM)
    ax.text(8.5, 6.75, "2단계 : 제1법칙과 상태방정식에서 dT 소거하기", fontsize=19, color=WARM, fontweight="bold")
    ax.text(8.5, 6.0, "① 단열 제1법칙 (dQ = 0) :   n Cv dT + P dV = 0   →   n dT = -(P/Cv) dV", fontsize=15.8, color=INK)
    ax.text(8.5, 5.3, "② 상태방정식 미분 (PV = nRT) :   P dV + V dP = n R dT", fontsize=15.8, color=INK)
    ax.text(8.5, 4.65, "①을 ②에 대입 :   V dP + (1 + R / Cv) P dV = 0     ← 여기서 (Cv+R)/Cv = γ 등장!", fontsize=15.8, color=NO, fontweight="bold")

    box(ax, 0.5, 0.9, 15.0, 3.05, "#ecfdf5", OK)
    ax.text(0.85, 3.35, "3단계 : 정리된 식   V dP + γ P dV = 0   에서 기울기와 곡선 식 한 번에 읽기", fontsize=19, color=OK, fontweight="bold")
    ax.text(0.85, 2.5, "• P-V 접선 기울기 비교 :   등온(dT = 0)은  dP/dV = -(P/V),     단열(dQ = 0)은  dP/dV = -γ (P/V)", fontsize=18, color=INK, fontweight="bold")
    ax.text(0.85, 1.8, "   →  같은 점 (P, V) 에서 단열 곡선의 기울기가 등온 곡선보다 정확히  γ = Cp / Cv 배 (단원자 5/3배, 이원자 7/5배) 더 가파릅니다!", fontsize=17, color=NO, fontweight="bold")
    ax.text(0.85, 1.15, "• 양변을 PV 로 나누어 적분 :   (dP / P) + γ (dV / V) = 0   →   ln P + γ ln V = 일정   →   P V^γ = 일정", fontsize=17, color=BLUE, fontweight="bold")
    save(fig, "lesson_why_molar_heat_in_adiabatic.webp")


def slide_adiabatic_equation():
    fig, ax = new_slide()
    title(ax, "수식으로 보는 단열 곡선(PV^γ = 일정)과 단열 과정의 일")
    ax.text(0.55, 7.75, "온도가 함께 변하는 단열 과정의 관계식과, 그래프 아래 넓이(적분)가 -ΔU 가 되는 이유입니다.", fontsize=17.5, color=MUTED)

    box(ax, 0.5, 4.25, 7.35, 3.0, "#eff6ff", BLUE)
    ax.text(0.85, 6.65, "등온 곡선 vs 단열 곡선 식", fontsize=20, color=BLUE, fontweight="bold")
    ax.text(0.85, 5.8, "등온 (T 일정) :   P V  =  일정     →   P ∝ 1 / V", fontsize=18, color=INK)
    ax.text(0.85, 5.05, "단열 (Q = 0)  :   P V^γ  =  일정   →   P ∝ 1 / V^γ", fontsize=18, color=NO, fontweight="bold")
    ax.text(0.85, 4.45, "단원자 γ = 5/3 (약 1.67),  이원자 γ = 7/5 (1.4)  →  항상 γ > 1", fontsize=16, color=MUTED)

    box(ax, 8.15, 4.25, 7.35, 3.0, "#fff7ed", WARM)
    ax.text(8.5, 6.65, "온도와 부피의 관계 (P = nRT / V 대입)", fontsize=20, color=WARM, fontweight="bold")
    ax.text(8.5, 5.75, "T V^(γ-1)  =  일정", fontsize=24, color=INK, fontweight="bold")
    ax.text(8.5, 4.95, "γ - 1 > 0 이므로,  팽창(V 증가)하면 온도 T 는 반드시 하락하고", fontsize=16.5, color=INK)
    ax.text(8.5, 4.45, "압축(V 감소)하면 온도 T 는 반드시 상승합니다.", fontsize=16.5, color=INK)

    box(ax, 0.5, 1.0, 15.0, 2.8, "#ecfdf5", OK)
    ax.text(0.85, 3.2, "단열 곡선 아래 넓이(적분)와 제1법칙(W = -ΔU)의 일치", fontsize=19, color=OK, fontweight="bold")
    ax.text(0.85, 2.35, "W  =  ∫ P dV  =  (P1 V1 - P2 V2) / (γ - 1)  =  n R (T1 - T2) / (γ - 1)  =  (f/2) n R (T1 - T2)  =  -ΔU", fontsize=18.5, color=INK, fontweight="bold")
    ax.text(0.85, 1.45, "즉, 복잡한 곡선 적분을 하지 않아도 처음·나중 온도 차이(T1 - T2)만 알면 단열 과정의 일을 바로 구할 수 있습니다.", fontsize=17.5, color=INK)
    save(fig, "lesson_adiabatic_equation.webp")


def slide_four_processes_compare():
    fig, ax = new_slide()
    title(ax, "한 점에서 출발하는 네 가지 열역학 과정 한눈에 비교")
    ax.text(0.55, 7.75, "93번 정리표의 네 과정을 한 점 (P0, V0) 에서 함께 팽창시켜 기울기와 일(넓이)을 비교합니다.", fontsize=17.5, color=MUTED)

    ax.plot([0.9, 0.9, 6.3], [6.9, 2.0, 2.0], color=LINE, lw=2.2)
    ax.plot([1.6, 5.4], [5.8, 5.8], color=WARM, lw=3.2)
    xs = [1.6 + i * 0.08 for i in range(48)]
    iso = [2.0 + 3.8 * 1.6 / x for x in xs]
    adi = [2.0 + 3.8 * (1.6 ** 1.67) / (x ** 1.67) for x in xs]
    ax.plot(xs, iso, color=BLUE, lw=3.0)
    ax.plot(xs, adi, color=NO, lw=3.0)
    ax.plot([1.6, 1.6], [5.8, 2.4], color=OK, lw=3.2)
    ax.add_patch(Circle((1.6, 5.8), 0.1, facecolor=INK, edgecolor=INK))
    ax.text(5.5, 5.75, "① 등압 (ΔP = 0)", fontsize=15, color=WARM, fontweight="bold")
    ax.text(5.45, 3.1, "② 등온 (PV = 일정)", fontsize=15, color=BLUE, fontweight="bold")
    ax.text(5.45, 2.35, "③ 단열 (PV^γ = 일정)", fontsize=15, color=NO, fontweight="bold")
    ax.text(1.75, 2.55, "④ 등적 (ΔV = 0)", fontsize=15, color=OK, fontweight="bold")
    ax.text(0.6, 6.7, "P", fontsize=18, color=INK, fontweight="bold")
    ax.text(6.45, 1.9, "V", fontsize=18, color=INK, fontweight="bold")

    box(ax, 7.1, 3.7, 8.4, 3.45, "#f8fafc", "#cbd5e1")
    ax.text(7.45, 6.55, "같은 부피까지 팽창할 때 비교", fontsize=20, color=INK, fontweight="bold")
    ax.text(7.45, 5.75, "• 가파른 순서 :  등압(수평)  <  등온  <  단열  <  등적(수직)", fontsize=17.5, color=INK, fontweight="bold")
    ax.text(7.45, 5.0, "• 기체가 한 일(넓이) :  W등압  >  W등온  >  W단열  >  W등적(= 0)", fontsize=17.5, color=BLUE, fontweight="bold")
    ax.text(7.45, 4.2, "• 나중 온도 :  T등압(상승)  >  T등온(일정)  >  T단열(하강)", fontsize=17.5, color=WARM, fontweight="bold")

    box(ax, 7.1, 1.4, 8.4, 1.9, "#fff7ed", WARM)
    ax.text(7.45, 2.75, "93번 슬라이드 오탈자 바로잡기", fontsize=18, color=NO, fontweight="bold")
    ax.text(7.45, 2.0, "93번 오른쪽 위 '단열 과정' 그래프는 부피가 늘어나는 단열 팽창(V1 → V2)", fontsize=16, color=INK)
    ax.text(7.45, 1.55, "이므로, 초록색 넓이 안의  W < 0 은  W > 0 (88번과 동일)으로 읽습니다.", fontsize=16, color=INK, fontweight="bold")
    save(fig, "lesson_four_processes_compare.webp")


def slide_omega_two_faces():
    fig, ax = new_slide()
    title(ax, "혼동 주의: 경우의 수(Ω, W)의 두 가지 얼굴")
    ax.text(0.55, 7.75, "앞의 동전·주사위(131~136번)와 방금 본 자유팽창은 Ω 를 부르는 맥락이 다릅니다.", fontsize=18, color=MUTED)

    box(ax, 0.45, 3.35, 7.35, 3.85, "#eff6ff", BLUE)
    ax.text(0.8, 6.6, "맥락 A : 특정 거시상태가 품은 수", fontsize=20, color=BLUE, fontweight="bold")
    ax.text(0.8, 5.85, "조건 : 전체 부피(판의 크기)가 이미 고정됨", fontsize=17, color=INK)
    ax.text(0.8, 5.1, "의미 : 한쪽 쏠림 vs 반반 퍼짐 중", fontsize=17, color=INK)
    ax.text(0.8, 4.55, "         그 거시상태에 속한 미시상태의 개수", fontsize=17, color=INK)
    ax.text(0.8, 3.75, "예 : 입자 4개 중 반반(2:2)  →  Ω반반 = 6", fontsize=18, color=BLUE, fontweight="bold")

    box(ax, 8.15, 3.35, 7.4, 3.85, "#ecfdf5", OK)
    ax.text(8.5, 6.6, "맥락 B : 허용된 전체 미시상태의 총합", fontsize=20, color=OK, fontweight="bold")
    ax.text(8.5, 5.85, "조건 : 칸막이를 치워 부피가 V → 2V 로 커짐", fontsize=17, color=INK)
    ax.text(8.5, 5.1, "의미 : 시스템에 새로 열린 전체 자리의 총합", fontsize=17, color=INK)
    ax.text(8.5, 4.55, "         (3면 주사위 판이 6면 주사위 판으로 커짐)", fontsize=17, color=INK)
    ax.text(8.5, 3.75, "예 : 입자 4개의 전체 자리  →  Ω전체 = 2^4 = 16", fontsize=18, color=OK, fontweight="bold")

    box(ax, 0.45, 1.15, 15.1, 1.75, "#fff7ed", WARM)
    ax.text(0.8, 2.3, "학생들이 묻는 핵심 질문", fontsize=18, color=WARM, fontweight="bold")
    ax.text(0.8, 1.55, "입자 4개일 때 반반 퍼진 경우는 6가지인데, 왜 자유팽창 공식은 전체인 16(2^N)을 넣을까요?", fontsize=18, color=INK, fontweight="bold")
    save(fig, "lesson_omega_two_faces.webp")


def slide_omega_two_steps():
    fig, ax = new_slide()
    title(ax, "칸막이를 치울 때 일어나는 2단계와 큰 수의 마법")
    ax.text(0.55, 7.75, "시간 순서로 1단계와 2단계를 나누어 보면, 두 설명이 하나로 합쳐집니다.", fontsize=18, color=MUTED)

    box(ax, 0.45, 5.2, 7.35, 2.05, "#eff6ff", BLUE)
    ax.text(0.8, 6.65, "1단계 : 판 자체가 커진다 (V → 2V)", fontsize=19, color=BLUE, fontweight="bold")
    ax.text(0.8, 5.95, "칸막이를 빼는 순간 허용된 전체 미시상태가", fontsize=17, color=INK)
    ax.text(0.8, 5.45, "1배에서 2^N 배로 확 열립니다.", fontsize=17, color=INK)

    box(ax, 8.15, 5.2, 7.4, 2.05, "#ecfdf5", OK)
    ax.text(8.5, 6.65, "2단계 : 가장 큰 무리로 이동한다", fontsize=19, color=OK, fontweight="bold")
    ax.text(8.5, 5.95, "왼쪽에만 모여 있던 기체가, 새로 열린 전체 판 중", fontsize=17, color=INK)
    ax.text(8.5, 5.45, "지분이 가장 큰 '골고루 퍼진 상태'로 이동합니다.", fontsize=17, color=INK)

    box(ax, 0.45, 1.35, 15.1, 3.4, "#f8fafc", "#cbd5e1")
    ax.text(0.8, 4.15, "왜 물리학 책은 1단계와 2단계를 구별하지 않고 2^N 으로 바로 쓸까?", fontsize=19, color=WARM, fontweight="bold")
    ax.text(0.8, 3.35, "입자가 2개·4개일 때는 '반반 상태(2가지·6가지)'와 '전체(4가지·16가지)'의 차이가 눈에 보입니다. (136번)", fontsize=17, color=INK)
    ax.text(0.8, 2.55, "하지만 기체 분자처럼 N = 10^23 개가 되면, 141번의 뾰족한 그래프처럼 골고루 퍼진 평형 상태가", fontsize=17, color=INK)
    ax.text(0.8, 1.8, "전체 2^N 가지의 99.9999...% 를 독차지하여   ln(Ω평형) = ln(Ω전체) = N ln 2   가 됩니다.", fontsize=18, color=OK, fontweight="bold")
    save(fig, "lesson_omega_two_steps.webp")


def slide_omega_stirling():
    fig, ax = new_slide()
    title(ax, "왜 반반의 수와 전체 2^(2n)을 같다고 놓을까")
    ax.text(
        0.55, 7.72,
        "앞 장의 입자 수 N을 2n이라 두면, 반반의 수는 C(2n, n)이고 전체는 2^(2n)입니다. 두 수는 다릅니다.",
        fontsize=17, color=MUTED,
    )

    box(ax, 0.4, 1.55, 7.5, 5.5, "#eff6ff", BLUE)
    ax.text(0.75, 6.5, "첫째. 확률이 정중앙에 몰립니다", fontsize=20, color=BLUE, fontweight="bold")
    ax.text(0.75, 5.7, "전체 경우의 수 2^(2n)을 펼치면", fontsize=17, color=INK)
    ax.text(0.75, 5.05, "C(2n, 0) + ... + C(2n, n) + ... + C(2n, 2n)", fontsize=16, color=INK, fontweight="bold")
    ax.text(0.75, 4.2, "입자 수가 10^23개쯤 되면", fontsize=17, color=INK)
    ax.text(0.75, 3.55, "한쪽으로 쏠리는 경우는 사실상 0이고,", fontsize=17, color=INK)
    ax.text(0.75, 2.9, "반반인 C(2n, n)과 그 근처에", fontsize=17, color=INK)
    ax.text(0.75, 2.2, "경우의 수가 바늘처럼 몰립니다.", fontsize=18, color=BLUE, fontweight="bold")

    box(ax, 8.15, 1.55, 7.45, 5.5, "#ecfdf5", OK)
    ax.text(8.5, 6.5, "둘째. 엔트로피는 로그를 씌웁니다", fontsize=20, color=OK, fontweight="bold")
    ax.text(8.5, 5.75, "S  =  k ln Ω", fontsize=22, color=INK, fontweight="bold")
    ax.text(8.5, 5.0, "스털링 근사     ln x!  ~  x ln x - x", fontsize=17, color=INK)
    ax.text(8.5, 4.15, "조합에 로그를 씌우면", fontsize=16, color=MUTED)
    ax.text(8.5, 3.55, "ln C(2n, n) = ln(2n)! - 2 ln n!", fontsize=16, color=INK)
    ax.text(8.5, 2.9, "~  2n ln 2", fontsize=22, color=OK, fontweight="bold")
    ax.text(8.5, 2.15, "전체에 로그를 씌우면    ln 2^(2n) = 2n ln 2", fontsize=16, color=INK, fontweight="bold")

    box(ax, 0.4, 0.32, 15.2, 1.0, "#f0fdf4", OK)
    ax.text(
        0.75, 0.82,
        "확률이 반반 근처에 몰리고, 로그를 씌우면 두 값이 같습니다.  그래서 조합 대신 2^(2n)을 씁니다.",
        fontsize=17, color=OK, fontweight="bold", va="center",
    )
    save(fig, "lesson_omega_stirling.webp")


def slide_bit_erase():
    fig, ax = new_slide()
    title(ax, "1비트를 지우면 경우의 수가 반으로 줄어듭니다")
    ax.text(
        0.55, 7.72,
        "0인지 1인지 모르는 비트를 0으로 덮어쓰면, 가능한 상태가 하나로 줄어듭니다.",
        fontsize=17, color=MUTED,
    )

    box(ax, 0.4, 2.05, 7.35, 5.0, "#eff6ff", BLUE)
    ax.text(0.8, 6.4, "지우기 전", fontsize=22, color=BLUE, fontweight="bold")
    ax.text(0.8, 5.45, "W  =  2", fontsize=32, color=INK, fontweight="bold")
    ax.text(0.8, 4.55, "0일 수도 있고, 1일 수도 있습니다.", fontsize=18, color=INK)
    ax.text(0.8, 3.85, "비트가 있을 수 있는 상태가 두 가지입니다.", fontsize=18, color=INK)
    box(ax, 0.9, 2.4, 2.5, 0.95, "white", BLUE)
    ax.text(2.15, 2.88, "0", fontsize=24, color=BLUE, ha="center", va="center", fontweight="bold")
    box(ax, 3.85, 2.4, 2.5, 0.95, "white", BLUE)
    ax.text(5.1, 2.88, "1", fontsize=24, color=BLUE, ha="center", va="center", fontweight="bold")

    box(ax, 8.15, 2.05, 7.45, 5.0, "#ecfdf5", OK)
    ax.text(8.55, 6.4, "0으로 지운 뒤", fontsize=22, color=OK, fontweight="bold")
    ax.text(8.55, 5.45, "W  =  1", fontsize=32, color=INK, fontweight="bold")
    ax.text(8.55, 4.55, "상태는 0 하나만 남습니다.", fontsize=18, color=INK)
    ax.text(8.55, 3.85, "1일 가능성은 더 이상 없습니다.", fontsize=18, color=INK)
    box(ax, 10.15, 2.4, 3.4, 0.95, "white", OK)
    ax.text(11.85, 2.88, "0", fontsize=24, color=OK, ha="center", va="center", fontweight="bold")

    box(ax, 0.4, 0.35, 15.2, 1.4, "#f8fafc", "#cbd5e1")
    ax.text(0.75, 1.15, "경우의 수가 2에서 1로 줄어듭니다.", fontsize=18, color=INK, fontweight="bold")
    ax.text(0.75, 0.6, "분자 하나를 한쪽 방에만 남기는 압축과 같은 과정입니다.", fontsize=17, color=MUTED)
    save(fig, "lesson_bit_erase.webp")


def slide_bit_piston():
    fig, ax = new_slide()
    title(ax, "한쪽 방으로 압축하면 열이 방출됩니다")
    ax.text(0.55, 7.72, "비트의 0과 1을, 분자 하나가 있을 수 있는 두 방으로 생각합니다.", fontsize=17, color=MUTED)

    ax.text(0.6, 6.85, "지우기 전    W = 2", fontsize=16, color=BLUE, fontweight="bold")
    ax.add_patch(Rectangle((0.6, 4.9), 6.7, 1.7, facecolor="#dbeafe", edgecolor=BLUE, lw=2))
    ax.text(2.3, 6.2, "0", fontsize=18, color=BLUE, ha="center", fontweight="bold")
    ax.text(5.6, 6.2, "1", fontsize=18, color=BLUE, ha="center", fontweight="bold")
    ax.add_patch(Circle((3.95, 5.75), 0.18, facecolor="#f59e0b", edgecolor=WARM, lw=1.5))
    ax.add_patch(FancyArrowPatch((2.15, 5.25), (5.75, 5.25), arrowstyle="<->", mutation_scale=14, lw=1.8, color=INK))

    ax.text(0.6, 4.4, "압축한 뒤    W = 1", fontsize=16, color=OK, fontweight="bold")
    ax.add_patch(Rectangle((0.6, 2.15), 3.35, 1.85, facecolor="#d1fae5", edgecolor=OK, lw=2))
    ax.add_patch(Rectangle((3.95, 2.15), 3.35, 1.85, facecolor="#f8fafc", edgecolor="#cbd5e1", lw=1.5))
    ax.add_patch(Rectangle((3.78, 2.15), 0.24, 1.85, facecolor="#334155", edgecolor=LINE))
    ax.add_patch(Circle((2.15, 3.05), 0.18, facecolor="#f59e0b", edgecolor=WARM, lw=1.5))
    ax.text(2.15, 3.6, "0", fontsize=18, color=OK, ha="center", fontweight="bold")
    ax.add_patch(FancyArrowPatch((6.7, 3.15), (4.35, 3.15), arrowstyle="-|>", mutation_scale=16, lw=2.2, color=WARM))
    ax.text(5.6, 3.6, "피스톤", fontsize=15, color=WARM, ha="center", fontweight="bold")

    box(ax, 8.15, 1.35, 7.45, 5.7, "#fff7ed", WARM)
    ax.text(8.5, 6.4, "세 단계로 보면", fontsize=20, color=WARM, fontweight="bold")
    ax.text(8.5, 5.5, "1   칸막이가 없으면 양쪽을 오갈 수 있습니다.", fontsize=17, color=INK)
    ax.text(8.5, 4.75, "2   피스톤으로 왼쪽 방에만 둡니다.", fontsize=17, color=INK)
    ax.text(8.5, 4.0, "3   압축에 쓴 일은 열로 방출됩니다.", fontsize=17, color=INK)
    ax.text(8.5, 2.9, "온도를 일정하게 유지하면", fontsize=18, color=INK)
    ax.text(8.5, 2.2, "방출되는 열은 최소  k T ln 2  입니다.", fontsize=18, color=WARM, fontweight="bold")
    save(fig, "lesson_bit_piston.webp")


def slide_bit_heat():
    """k_B * 300 * ln 2 = 2.870978e-21 J."""
    fig, ax = new_slide()
    title(ax, "줄어든 엔트로피만큼 외부로 열이 방출됩니다")
    ax.text(0.55, 7.72, "볼츠만의 식과 열역학 제2법칙을 비트 하나에 적용합니다.", fontsize=18, color=MUTED)

    box(ax, 0.4, 5.35, 15.2, 1.85, "#eff6ff", BLUE)
    ax.text(0.75, 6.7, "비트의 엔트로피 변화", fontsize=18, color=BLUE, fontweight="bold")
    ax.text(0.75, 5.9, "ΔS  =  k ln 1  -  k ln 2  =  - k ln 2", fontsize=26, color=INK, fontweight="bold")

    box(ax, 0.4, 3.2, 15.2, 1.9, "#fff7ed", WARM)
    ax.text(0.75, 4.6, "제2법칙    고립계의 엔트로피는 감소하지 않습니다.", fontsize=18, color=WARM, fontweight="bold")
    ax.text(0.75, 3.75, "비트가  k ln 2  만큼 줄면, 외부는 최소한  k ln 2  만큼 증가해야 합니다.", fontsize=19, color=INK, fontweight="bold")

    box(ax, 0.4, 0.4, 15.2, 2.55, "#ecfdf5", OK)
    ax.text(0.75, 2.4, "외부로 방출되는 최소 열량     ΔS = Q / T 에서", fontsize=18, color=OK, fontweight="bold")
    ax.text(0.75, 1.6, "Q  =  T ΔS  =  k T ln 2", fontsize=26, color=INK, fontweight="bold")
    ax.text(0.75, 0.85, "ΔS는 외부의 증가량입니다.   상온 300 K에서는 비트 하나당 약  2.87 x 10^-21 J", fontsize=18, color=OK, fontweight="bold")
    save(fig, "lesson_bit_heat.webp")


def slide_bit_landauer():
    fig, ax = new_slide()
    title(ax, "정보는 지울 때 열이 발생합니다")
    ax.text(0.55, 7.72, "경우의 수가 줄지 않으면, 이론상 이 열은 발생하지 않을 수 있습니다.", fontsize=18, color=MUTED)

    box(ax, 0.4, 1.7, 7.4, 5.35, "#eff6ff", BLUE)
    ax.text(0.75, 6.4, "읽거나 복사할 때", fontsize=22, color=BLUE, fontweight="bold")
    ax.text(0.75, 5.4, "원래의 0과 1이 그대로 남습니다.", fontsize=18, color=INK)
    ax.text(0.75, 4.6, "경우의 수 W는 변하지 않습니다.", fontsize=18, color=INK)
    ax.text(0.75, 3.55, "이론상 열 방출이 필요 없습니다.", fontsize=18, color=BLUE, fontweight="bold")
    ax.text(0.75, 2.35, "저장된 정보가 유지되기 때문입니다.", fontsize=17, color=MUTED)

    box(ax, 8.15, 1.7, 7.45, 5.35, "#fff7ed", WARM)
    ax.text(8.5, 6.4, "지우거나 덮어쓸 때", fontsize=22, color=WARM, fontweight="bold")
    ax.text(8.5, 5.4, "두 상태가 하나의 상태로 줄어듭니다.", fontsize=18, color=INK)
    ax.text(8.5, 4.6, "W :  2  →  1    되돌릴 수 없습니다.", fontsize=18, color=INK)
    ax.text(8.5, 3.55, "최소 열량   k T ln 2", fontsize=22, color=WARM, fontweight="bold")
    ax.text(8.5, 2.35, "경우의 수가 감소하기 때문입니다.", fontsize=17, color=MUTED)

    box(ax, 0.4, 0.32, 15.2, 1.15, "#f0fdf4", OK)
    ax.text(0.7, 0.95, "이 최소 열량을 란다우어의 원리라고 합니다.", fontsize=17, color=OK, fontweight="bold")
    ax.text(0.7, 0.52, "현재 컴퓨터가 뜨거워지는 주된 원인은 전기 저항입니다.  저항이 없어도 비트를 지울 때의 이 열은 남습니다.", fontsize=15, color=INK)
    save(fig, "lesson_bit_landauer.webp")


if __name__ == "__main__":
    slide_pressure_question()
    slide_collision()
    slide_pressure_result()
    slide_temperature()
    slide_rms_speed()
    slide_monatomic()
    slide_diatomic()
    slide_isobaric_split()
    slide_isobaric_heat()
    slide_molar_heat()
    slide_stirling_cycle()
    slide_stirling_efficiency()
    slide_coins()
    slide_coin_entropy()
    slide_free_expansion()
    slide_free_count()
    slide_thermal_resistance()
    slide_volume_expansion()
    slide_boltzmann_constant()
    slide_isothermal_work()
    slide_adiabatic_curve()
    slide_why_molar_heat_in_adiabatic()
    slide_adiabatic_equation()
    slide_four_processes_compare()
    slide_omega_two_faces()
    slide_omega_two_steps()
    slide_omega_stirling()
    slide_bit_erase()
    slide_bit_piston()
    slide_bit_heat()
    slide_bit_landauer()
    print("31 lesson slides")
