"""5강 단진동에서 강의로 풀어서 설명할 보충 슬라이드. 원본 슬라이드는 유지합니다."""

import os

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle, FancyArrowPatch, FancyBboxPatch, Polygon, Rectangle, Wedge

if os.name == "nt":
    plt.rc("font", family="Malgun Gothic")
else:
    plt.rc("font", family="AppleGothic")
plt.rcParams["axes.unicode_minus"] = False
plt.rcParams["mathtext.fontset"] = "dejavusans"

OUT = r"r:\textbook-svelte\public\images\slides\mech_05"
PREVIEW = r"r:\textbook-svelte\tmp\shm_lesson_preview"
os.makedirs(OUT, exist_ok=True)
os.makedirs(PREVIEW, exist_ok=True)

BLUE = "#1d4ed8"
INK = "#0f172a"
MUTED = "#475569"
WARM = "#c2410c"
OK = "#047857"
LINE = "#334155"
PALE = "#eff6ff"
CREAM = "#fff7ed"
MINT = "#ecfdf5"


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
    fig.savefig(os.path.join(PREVIEW, name.replace(".webp", ".jpg")), format="jpg", dpi=70)
    plt.close(fig)


def title(ax, text):
    ax.text(0.5, 8.48, text, fontsize=28, color=BLUE, fontweight="bold", va="center")


def note(ax, text, y=0.42):
    ax.text(0.5, y, text, fontsize=15, color=MUTED, va="center")


def box(ax, x, y, w, h, fc, ec):
    ax.add_patch(
        FancyBboxPatch(
            (x, y),
            w,
            h,
            boxstyle="round,pad=0.02,rounding_size=0.12",
            facecolor=fc,
            edgecolor=ec,
            linewidth=1.8,
        )
    )


def wall(ax, x, y0, y1, color=LINE):
    ax.plot([x, x], [y0, y1], color=color, lw=4, solid_capstyle="butt")
    for i in range(6):
        yy = y0 + (y1 - y0) * i / 5
        ax.plot([x - 0.22, x], [yy - 0.12, yy], color=color, lw=1.4)


def spring_h(ax, x0, x1, y, coils=7, amp=0.22, color=LINE, lw=2.2):
    xs = [x0]
    ys = [y]
    n = coils * 2
    for i in range(1, n):
        xs.append(x0 + (x1 - x0) * i / n)
        ys.append(y + (amp if i % 2 else -amp))
    xs.append(x1)
    ys.append(y)
    ax.plot(xs, ys, color=color, lw=lw, solid_capstyle="round")


def spring_v(ax, x, y0, y1, coils=7, amp=0.2, color=LINE, lw=2.2):
    ys = [y0]
    xs = [x]
    n = coils * 2
    for i in range(1, n):
        ys.append(y0 + (y1 - y0) * i / n)
        xs.append(x + (amp if i % 2 else -amp))
    ys.append(y1)
    xs.append(x)
    ax.plot(xs, ys, color=color, lw=lw, solid_capstyle="round")


def arrow(ax, p0, p1, color=WARM, lw=2.2):
    ax.add_patch(
        FancyArrowPatch(p0, p1, arrowstyle="-|>", mutation_scale=14, lw=lw, color=color)
    )


def slide_course_map():
    fig, ax = new_slide()
    title(ax, "이번 단원에서 보는 것")
    ax.text(
        0.5,
        7.88,
        "용수철의 왕복 운동으로 주기와 에너지를 구합니다.",
        fontsize=16,
        color=MUTED,
    )

    cols = [
        (0.4, PALE, BLUE, "꼭 가져갈 것", [
            "용수철이 물체를 되돌린다.",
            "가속도는 변위에 비례한다.",
            "방향은 항상 평형점 쪽이다.",
            r"$a = -\frac{k}{m}x$",
            r"주기  $T = 2\pi\sqrt{m/k}$",
            "진폭을 바꿔도 주기는 같다.",
            "평형점에서 속력이 가장 크다.",
        ]),
        (5.55, MINT, OK, "이어서 계산하는 것", [
            "어디서 속력이 최대인지",
            "어디서 힘이 가장 센지",
            r"에너지  $\frac{1}{2}kA^{2}$",
            "임의의 위치에서의 속력",
            "연직 용수철의 새 평형점",
            "작게 흔들리는 단진자",
            "주기에 들어가는 것과 아닌 것",
        ]),
        (10.7, CREAM, WARM, "조금 더 보는 것", [
            "고체가 늘어나는 정도와 영률",
            "영률이 용수철 상수가 되는 과정",
            "직렬은 길어지고 병렬은 굵어진다",
            "진자, 떠 있는 통, 지구 터널",
            "되돌리는 힘이 변위에 비례하면",
            "주기는 모두 같은 꼴이다.",
            "왜 사인인지는 미분으로 확인한다.",
        ]),
    ]
    for x, fc, ec, head, rows in cols:
        box(ax, x, 1.15, 4.9, 6.35, fc, ec)
        ax.text(x + 0.28, 6.95, head, fontsize=18, color=ec, fontweight="bold", va="center")
        y = 6.35
        for row in rows:
            ax.text(x + 0.28, y, row, fontsize=16, color=INK, va="center")
            y -= 0.68
    note(ax, "가운데의 용수철 진자가 이 단원의 중심입니다.")
    save(fig, "lesson_course_map.webp")


def slide_three_moduli():
    fig, ax = new_slide()
    title(ax, "세 변형은 방향만 다르고 식의 꼴은 같다")
    ax.text(0.5, 7.85, "고등학교 단진동은 이 중 길이 방향, 영률만 사용합니다.", fontsize=16, color=MUTED)

    cards = [
        (0.45, "인장", "길이 방향", r"$\frac{F}{S} = Y\frac{\Delta L}{L}$", "Y  영률", "용수철, 철선이 늘어날 때"),
        (5.55, "층밀림", "면을 비틀 때", r"$\frac{F}{S} = G\frac{\Delta x}{L}$", "G  층밀림 탄성률", "책 옆면을 밀 때"),
        (10.65, "부피", "사방에서 누를 때", r"$P = -B\frac{\Delta V}{V}$", "B  부피 탄성률", "깊은 바다의 금속 공"),
    ]
    for x, name, how, formula, symbol, example in cards:
        box(ax, x, 1.55, 4.9, 5.85, PALE, "#bfdbfe")
        ax.text(x + 2.45, 6.75, name, fontsize=24, color=BLUE, fontweight="bold", ha="center")
        ax.text(x + 2.45, 6.15, how, fontsize=16, color=MUTED, ha="center")
        ax.text(x + 2.45, 4.85, formula, fontsize=22, color=INK, ha="center", va="center")
        ax.text(x + 2.45, 3.45, symbol, fontsize=18, color=OK, ha="center", fontweight="bold")
        ax.text(x + 2.45, 2.55, example, fontsize=15, color=INK, ha="center")
    note(ax, "뒤의 세 문제는 같은 비례식에 숫자를 넣습니다. 단진동으로 이어지는 것은 첫 칸, 영률입니다.")
    save(fig, "lesson_three_moduli.webp")


def slide_rod_as_spring():
    fig, ax = new_slide()
    title(ax, "쇠막대도 아주 단단한 용수철이다")
    ax.text(0.5, 7.85, "영률은 물질의 성질이고, 용수철 상수는 그 물체의 성질입니다.", fontsize=16, color=MUTED)

    wall(ax, 0.8, 3.15, 6.55)
    ax.add_patch(FancyBboxPatch((0.8, 4.35), 4.3, 0.85, boxstyle="round,pad=0.01,rounding_size=0.04", fc="#94a3b8", ec=LINE, lw=1.5))
    ax.plot([0.8, 5.1], [4.35, 4.35], color=LINE, lw=1)
    ax.text(2.9, 4.78, "S", fontsize=16, color="white", ha="center", fontweight="bold")
    arrow(ax, (5.15, 4.78), (6.55, 4.78), WARM, 2.4)
    ax.text(5.85, 5.25, "F", fontsize=18, color=WARM, ha="center")
    ax.annotate("", xy=(5.1, 3.55), xytext=(0.8, 3.55), arrowprops=dict(arrowstyle="<->", color=BLUE, lw=1.6))
    ax.text(2.95, 3.15, "원래 길이  L", fontsize=15, color=BLUE, ha="center")
    ax.text(5.35, 3.85, "x", fontsize=16, color=WARM)

    box(ax, 7.3, 4.55, 8.2, 2.85, PALE, "#bfdbfe")
    ax.text(7.55, 6.85, "후크 법칙으로 읽으면", fontsize=16, color=BLUE, fontweight="bold")
    ax.text(7.55, 6.1, r"$F = \left(Y\frac{S}{L}\right) x = kx$", fontsize=22, color=INK, va="center")
    ax.text(7.55, 5.15, r"용수철 상수   $k = Y\frac{S}{L}$", fontsize=20, color=OK, va="center")

    box(ax, 7.3, 1.35, 8.2, 2.9, CREAM, "#fdba74")
    ax.text(7.55, 3.75, "숫자로 보면", fontsize=16, color=WARM, fontweight="bold")
    ax.text(7.55, 3.1, "철, 길이 1 m, 반지름 0.5 cm", fontsize=16, color=INK)
    ax.text(7.55, 2.5, r"$k \approx 1.6\times 10^{7}\ \mathrm{N/m}$", fontsize=20, color=INK, va="center")
    ax.text(7.55, 1.75, "1000 N을 걸어도 0.06 mm 정도", fontsize=16, color=INK)
    note(ax, "굵고 짧으면 k가 크고, 가늘고 길면 k가 작습니다. 평소에 강체처럼 보이는 이유는 k가 매우 크기 때문입니다.")
    save(fig, "lesson_rod_as_spring.webp")


def slide_series_parallel():
    fig, ax = new_slide()
    title(ax, "직렬은 길어지고, 병렬은 굵어진다")
    ax.text(0.5, 7.88, r"같은 관계 $k = YS/L$ 로 읽으면 합성 공식이 자연스럽습니다.", fontsize=16, color=MUTED)

    box(ax, 0.4, 4.15, 7.55, 3.4, PALE, "#bfdbfe")
    ax.text(0.65, 7.15, "직렬", fontsize=20, color=BLUE, fontweight="bold")
    wall(ax, 0.85, 5.35, 6.85)
    spring_h(ax, 0.85, 2.55, 6.15, coils=5, amp=0.16)
    spring_h(ax, 2.55, 4.35, 6.15, coils=5, amp=0.16)
    ax.add_patch(Rectangle((4.35, 5.8), 0.7, 0.7, fc="#fdba74", ec=WARM, lw=1.4))
    ax.text(1.7, 6.7, "k1", fontsize=13, color=MUTED, ha="center")
    ax.text(3.45, 6.7, "k2", fontsize=13, color=MUTED, ha="center")
    ax.text(0.7, 4.55, r"$1/k = 1/k_1 + 1/k_2$", fontsize=18, color=INK)

    box(ax, 8.15, 4.15, 7.4, 3.4, MINT, "#6ee7b7")
    ax.text(8.4, 7.15, "병렬", fontsize=20, color=OK, fontweight="bold")
    wall(ax, 8.55, 5.35, 6.9)
    spring_h(ax, 8.55, 11.3, 6.45, coils=6, amp=0.14)
    spring_h(ax, 8.55, 11.3, 5.7, coils=6, amp=0.14)
    ax.plot([11.3, 11.3], [5.45, 6.75], color=LINE, lw=3)
    ax.add_patch(Rectangle((11.3, 5.7), 0.65, 0.7, fc="#fdba74", ec=WARM, lw=1.4))
    ax.text(8.45, 4.55, r"$k = k_1 + k_2$", fontsize=20, color=INK)

    box(ax, 0.4, 1.15, 15.15, 2.7, CREAM, "#fdba74")
    ax.text(0.7, 3.3, "길이만 바뀌면", fontsize=18, color=WARM, fontweight="bold")
    ax.text(0.7, 2.55, "같은 용수철을 반으로 자르면 길이만 절반이 되므로 용수철 상수는 2배가 됩니다.", fontsize=17, color=INK)
    ax.text(0.7, 1.75, "그 두 조각을 다시 직렬로 잇면 원래의 k로 돌아옵니다. 병렬로 잇으면 4k가 됩니다.", fontsize=17, color=INK)
    save(fig, "lesson_series_parallel.webp")


def slide_vertical_spring():
    fig, ax = new_slide()
    title(ax, "연직 용수철도 알짜힘은 -kx")
    ax.text(0.5, 7.85, "중력은 평형점만 내리고, 진동의 주기에는 들어가지 않습니다.", fontsize=16, color=MUTED)

    ax.plot([1.5, 4.3], [7.35, 7.35], color=LINE, lw=4)
    ax.plot([1.35, 2.15], [5.7, 5.7], color="#94a3b8", lw=2)
    ax.text(3.45, 5.7, "자연 길이", fontsize=13, color=MUTED, va="center")
    spring_v(ax, 2.85, 7.35, 2.85, coils=9, amp=0.18)
    ax.add_patch(Rectangle((2.4, 2.05), 0.9, 0.8, fc="#fb923c", ec=WARM, lw=1.5))
    ax.plot([1.35, 5.15], [4.55, 4.55], color=OK, lw=1.4, ls="--")
    ax.text(5.25, 4.55, "새 평형  O'", fontsize=14, color=OK, va="center")
    ax.annotate("", xy=(1.15, 4.55), xytext=(1.15, 5.7), arrowprops=dict(arrowstyle="<->", color=BLUE, lw=1.4))
    ax.text(0.7, 5.15, "x0", fontsize=15, color=BLUE, ha="center")
    ax.annotate("", xy=(3.85, 2.45), xytext=(3.85, 4.55), arrowprops=dict(arrowstyle="<->", color=WARM, lw=1.4))
    ax.text(4.05, 3.45, "x", fontsize=16, color=WARM)

    box(ax, 6.3, 4.35, 9.2, 3.05, PALE, "#bfdbfe")
    ax.text(6.55, 6.9, "아래 방향을 + 로 두고", fontsize=16, color=BLUE, fontweight="bold")
    ax.text(6.55, 6.15, r"평형에서   $kx_0 = mg$", fontsize=20, color=INK, va="center")
    ax.text(6.55, 5.35, r"더 내린 곳에서  $F = mg - k(x_0+x)$", fontsize=18, color=INK, va="center")
    ax.text(6.55, 4.7, r"$F = -kx$", fontsize=26, color=OK, va="center")

    box(ax, 6.3, 1.2, 9.2, 2.8, MINT, "#6ee7b7")
    ax.text(6.55, 3.5, "그래서 주기도 수평 용수철과 같다", fontsize=16, color=OK, fontweight="bold")
    ax.text(6.55, 2.7, r"$T = 2\pi\sqrt{m/k}$", fontsize=24, color=INK, va="center")
    ax.text(6.55, 1.75, "중력 mg는 x0를 정할 뿐, 알짜 복원력에서 사라집니다.", fontsize=15, color=INK)
    save(fig, "lesson_vertical_spring.webp")


def slide_shm_terms():
    fig, ax = new_slide()
    title(ax, "단진동 그래프에서 읽는 것")
    ax.text(0.5, 7.88, r"앞에서 본 $x = A\sin\omega t$ 를 한 주기 그림으로 보면 이렇습니다.", fontsize=16, color=MUTED)

    t = np.linspace(0, 2 * np.pi, 400)
    xs = 0.7 + t / (2 * np.pi) * 8.6
    ys = 4.55 + 1.55 * np.sin(t)
    ax.plot(xs, ys, color=BLUE, lw=2.6)
    ax.plot([0.7, 9.3], [4.55, 4.55], color="#94a3b8", lw=1.2, ls="--")
    ax.text(9.45, 4.55, "평형", fontsize=13, color=MUTED, va="center")
    ax.annotate("", xy=(0.55, 4.55), xytext=(0.55, 6.1), arrowprops=dict(arrowstyle="<->", color=WARM, lw=1.5))
    ax.text(0.85, 6.45, "A", fontsize=16, color=WARM, ha="center")
    ax.annotate("", xy=(0.7, 2.15), xytext=(9.3, 2.15), arrowprops=dict(arrowstyle="<->", color=OK, lw=1.6))
    ax.text(5.0, 1.65, "한 주기  T    ·    이 동안 실제 이동 거리는 4A", fontsize=15, color=OK, ha="center")

    items = [
        (OK, "평형점", "복원력이 0인 위치. 그래프의 가운데 선"),
        (WARM, "진폭 A", "평형점에서 가장 멀리 간 거리. 전체가 아니라 한쪽"),
        (BLUE, "주기 T", "같은 운동이 다시 시작되기까지 걸린 시간"),
        (BLUE, "진동수 f", "1초 동안의 왕복 횟수.  f = 1/T , 단위 Hz"),
        (INK, "각진동수", "ω = 2πf = 2π/T . 곧 원운동의 각속도와 같은 양"),
    ]
    y = 7.15
    for color, head, body in items:
        ax.text(10.15, y, head, fontsize=16, color=color, fontweight="bold", va="center")
        ax.text(10.15, y - 0.38, body, fontsize=13, color=INK, va="center")
        y -= 1.05
    save(fig, "lesson_shm_terms.webp")


def slide_projection():
    fig, ax = new_slide()
    title(ax, "등속 원운동의 그림자가 단진동이다")
    ax.text(0.5, 7.85, "미분 없이 위치, 속도, 가속도를 읽는 고등학교 그림입니다. 반지름이 진폭 A입니다.", fontsize=16, color=MUTED)

    c = (3.15, 4.15)
    R = 1.85
    ang = np.deg2rad(52)
    px = c[0] + R * np.cos(ang)
    py = c[1] + R * np.sin(ang)
    ax.add_patch(Circle(c, R, fill=False, ec=LINE, lw=2))
    ax.plot([c[0] - R - 0.2, c[0] + R + 0.35], [c[1], c[1]], color="#94a3b8", lw=1.2)
    ax.plot([c[0], px], [c[1], py], color="#93c5fd", lw=1.4)
    ax.add_patch(Circle((px, py), 0.12, fc=WARM, ec=WARM))
    ax.plot([px, px], [c[1], py], color=WARM, lw=1.2, ls="--")
    ax.add_patch(Circle((px, c[1]), 0.1, fc=BLUE, ec=BLUE))
    ax.text(px + 0.15, c[1] - 0.35, "그림자", fontsize=13, color=BLUE)
    arc = np.linspace(0, ang, 30)
    ax.plot(c[0] + 0.55 * np.cos(arc), c[1] + 0.55 * np.sin(arc), color=OK, lw=1.5)
    ax.text(c[0] + 0.75, c[1] + 0.28, "ωt", fontsize=14, color=OK)
    # tangent velocity, CCW: direction (-sin, cos)
    tx = -np.sin(ang)
    ty = np.cos(ang)
    arrow(ax, (px, py), (px + 1.15 * tx, py + 1.15 * ty), OK, 2)
    ax.text(px + 1.15 * tx - 0.15, py + 1.15 * ty + 0.25, "Aω", fontsize=13, color=OK)
    arrow(ax, (px, py), (c[0], c[1]), "#7c3aed", 1.8)
    ax.text((px + c[0]) / 2 - 0.55, (py + c[1]) / 2, r"$A\omega^{2}$", fontsize=13, color="#7c3aed")

    cards = [
        (PALE, BLUE, "위치", r"$x = A\cos\omega t$"),
        (MINT, OK, "속도", r"$v = -A\omega\sin\omega t$"),
        (CREAM, WARM, "가속도", r"$a = -\omega^{2} x$"),
    ]
    y = 6.85
    for fc, ec, head, formula in cards:
        box(ax, 7.55, y - 1.35, 7.95, 1.5, fc, ec)
        ax.text(7.8, y - 0.35, head, fontsize=16, color=ec, fontweight="bold", va="center")
        ax.text(10.3, y - 0.35, formula, fontsize=22, color=INK, va="center")
        y -= 1.7
    ax.text(7.8, 1.55, r"최대 속력 $A\omega$,   최대 가속도 $A\omega^{2}$", fontsize=16, color=INK)
    note(ax, "이어지는 계산은 이 그림자의 속도를 미분으로 구한 것입니다. 원의 반지름이 진폭 A입니다.")
    save(fig, "lesson_projection.webp")


def slide_xva():
    fig, ax = new_slide()
    title(ax, "어디서 가장 빠르고, 어디서 힘이 센가")
    ax.text(0.5, 7.88, "성취기준의 핵심은 가속도와 변위가 반대 방향이며 크기가 비례한다는 점입니다.", fontsize=16, color=MUTED)

    headers = ["", "왼쪽 끝", "평형점", "오른쪽 끝"]
    rows = [
        ["변위 x", "-A", "0", "+A"],
        ["속력", "0", "최대  Aω", "0"],
        ["가속도", "오른쪽  ω²A", "0", "왼쪽  ω²A"],
        ["복원력", "오른쪽  kA", "0", "왼쪽  kA"],
    ]
    x0, y0 = 0.45, 6.95
    col_w = [2.15, 2.45, 2.55, 2.45]
    row_h = 0.78
    cx = x0
    for i, h in enumerate(headers):
        ax.add_patch(Rectangle((cx, y0 - row_h), col_w[i], row_h, fc="#dbeafe", ec="#bfdbfe", lw=1))
        ax.text(cx + col_w[i] / 2, y0 - row_h / 2, h, ha="center", va="center", fontsize=15, color=BLUE, fontweight="bold")
        cx += col_w[i]
    for r, row in enumerate(rows):
        cx = x0
        yy = y0 - (r + 1) * row_h
        bg = "#f8fafc" if r % 2 == 0 else "white"
        for i, cell in enumerate(row):
            ax.add_patch(Rectangle((cx, yy - row_h), col_w[i], row_h, fc=bg, ec="#e2e8f0", lw=1))
            weight = "bold" if i == 0 else "regular"
            ax.text(cx + col_w[i] / 2, yy - row_h / 2, cell, ha="center", va="center", fontsize=15, color=INK, fontweight=weight)
            cx += col_w[i]

    t = np.linspace(0, 2 * np.pi, 300)
    waves = [
        (r"$x$", np.cos(t), BLUE),
        (r"$v$", -np.sin(t), OK),
        (r"$a$", -np.cos(t), WARM),
    ]
    for i, (lab, wave, color) in enumerate(waves):
        axp = fig.add_axes([0.655, 0.30 + (2 - i) * 0.155, 0.30, 0.12])
        axp.plot(t, wave, color=color, lw=2)
        axp.axhline(0, color="#cbd5e1", lw=0.8)
        axp.set_xlim(0, 2 * np.pi)
        axp.set_ylim(-1.4, 1.4)
        axp.set_xticks([])
        axp.set_yticks([])
        axp.set_ylabel(lab, fontsize=12, rotation=0, labelpad=14, color=color)
        for s in axp.spines.values():
            s.set_color("#e2e8f0")

    box(ax, 0.45, 0.95, 9.55, 1.15, MINT, "#6ee7b7")
    ax.text(0.7, 1.52, r"$a = -\omega^{2} x = -\frac{k}{m}x$", fontsize=20, color=OK, va="center")
    note(ax, "변위가 최대일 때 가속도도 최대이고, 평형점에서는 가속도가 0이며 속력이 최대입니다.")
    save(fig, "lesson_xva.webp")


def slide_period():
    fig, ax = new_slide()
    title(ax, "그림으로 주기를 구하면")
    ax.text(0.5, 7.85, "원운동 그림자의 가속도와 후크 법칙을 같은 힘으로 보면 됩니다.", fontsize=16, color=MUTED)

    steps = [
        (r"1", r"그림자에서  $a = -\omega^{2} x$"),
        (r"2", r"뉴턴 법칙  $F = ma = -m\omega^{2} x$"),
        (r"3", r"후크 법칙  $F = -kx$"),
        (r"4", r"비교하면  $m\omega^{2} = k$"),
    ]
    for i, (n, text) in enumerate(steps):
        y = 6.85 - i * 1.15
        circle = Circle((1.05, y), 0.32, fc=BLUE, ec=BLUE)
        ax.add_patch(circle)
        ax.text(1.05, y, n, fontsize=16, color="white", ha="center", va="center", fontweight="bold")
        ax.text(1.7, y, text, fontsize=22, color=INK, va="center")

    box(ax, 9.3, 3.55, 6.2, 3.85, PALE, "#bfdbfe")
    ax.text(12.4, 6.85, "주기", fontsize=16, color=BLUE, ha="center", fontweight="bold")
    ax.text(12.4, 5.85, r"$\omega = \sqrt{k/m}$", fontsize=24, color=INK, ha="center", va="center")
    ax.text(12.4, 4.7, r"$T = 2\pi\sqrt{m/k}$", fontsize=26, color=OK, ha="center", va="center")
    ax.text(12.4, 3.9, "진폭 A는 식에 없습니다.", fontsize=15, color=MUTED, ha="center")

    box(ax, 0.45, 0.95, 15.1, 1.85, CREAM, "#fdba74")
    ax.text(0.75, 2.25, "바뀌는 것", fontsize=16, color=WARM, fontweight="bold")
    ax.text(0.75, 1.5, "질량 4배이면 주기 2배.   용수철 상수가 4배이면 주기 1/2.", fontsize=17, color=INK)
    ax.text(8.7, 2.25, "안 바뀌는 것", fontsize=16, color=OK, fontweight="bold")
    ax.text(8.7, 1.5, "진폭. 용수철을 세우거나 눕혀도 주기는 같다.", fontsize=16, color=INK)
    save(fig, "lesson_period.webp")


def slide_ode_bridge():
    fig, ax = new_slide()
    title(ax, "같은 답을 미분으로 확인하면")
    ax.text(0.5, 7.85, "주기와 위치 식은 이미 구했습니다. 이어지는 계산은 그 식이 운동방정식을 만족하는지 봅니다.", fontsize=16, color=MUTED)

    box(ax, 0.45, 1.45, 7.3, 5.9, MINT, "#6ee7b7")
    ax.text(0.75, 6.75, "이미 구한 답", fontsize=20, color=OK, fontweight="bold")
    lines = [
        r"$x = A\cos\omega t$",
        r"또는   $x = A\sin\omega t$",
        r"$\omega = \sqrt{k/m}$",
        r"$T = 2\pi\sqrt{m/k}$",
        r"$v_{\max} = A\omega$",
        r"$a = -\omega^{2} x$",
    ]
    y = 5.9
    for line in lines:
        ax.text(0.9, y, line, fontsize=22, color=INK, va="center")
        y -= 0.72

    box(ax, 8.05, 1.45, 7.5, 5.9, CREAM, "#fdba74")
    ax.text(8.35, 6.75, "이어지는 계산", fontsize=20, color=WARM, fontweight="bold")
    rights = [
        r"방정식  $\frac{d^{2}x}{dt^{2}}+\omega^{2}x=0$",
        "해를 지수함수로 가정한다.",
        "지수가 허수가 된다.",
        "오일러 공식으로",
        "사인과 코사인을 얻는다.",
        "처음 위치와 속도로 상수를 정한다.",
    ]
    y = 5.9
    for line in rights:
        ax.text(8.4, y, line, fontsize=18, color=INK, va="center")
        y -= 0.72
    note(ax, "주기와 위치별 비교는 앞 슬라이드가 답입니다. 여기는 왜 사인과 코사인인지를 확인합니다.")
    save(fig, "lesson_ode_bridge.webp")


def slide_energy():
    fig, ax = new_slide()
    title(ax, "에너지는 진폭이 정한다")
    ax.text(0.5, 7.85, "용수철을 늘이는 평균 힘으로 탄성 에너지를 읽습니다.", fontsize=16, color=MUTED)

    box(ax, 0.4, 3.55, 7.5, 3.85, PALE, "#bfdbfe")
    ax.text(0.7, 6.85, "늘어난 길이 x까지", fontsize=18, color=BLUE, fontweight="bold")
    ax.text(0.7, 6.05, "힘은 0에서 kx까지 커집니다.", fontsize=17, color=INK)
    ax.text(0.7, 5.35, r"평균 힘  $= \frac{1}{2}kx$", fontsize=20, color=INK, va="center")
    ax.text(0.7, 4.5, r"저장 에너지  $= \frac{1}{2}kx^{2}$", fontsize=22, color=OK, va="center")

    axp = fig.add_axes([0.05, 0.07, 0.40, 0.28])
    xs = np.linspace(-1, 1, 200)
    axp.plot(xs, xs ** 2, color=BLUE, lw=2.4)
    axp.axhline(1, color=WARM, lw=1.6, ls="--")
    axp.set_xlim(-1.25, 1.25)
    axp.set_ylim(-0.05, 1.35)
    axp.set_xticks([-1, 0, 1])
    axp.set_xticklabels(["-A", "0", "+A"], fontsize=11)
    axp.set_yticks([])
    axp.text(0.08, 1.08, "전체 에너지", color=WARM, fontsize=11)
    axp.text(0.12, 0.28, "탄성 에너지", color=BLUE, fontsize=11)

    box(ax, 8.35, 1.35, 7.2, 6.05, MINT, "#6ee7b7")
    ax.text(8.65, 6.8, "보존되면", fontsize=18, color=OK, fontweight="bold")
    ax.text(8.65, 5.9, r"$\frac{1}{2}mv^{2} + \frac{1}{2}kx^{2}$", fontsize=22, color=INK, va="center")
    ax.text(8.65, 5.05, r"$= \frac{1}{2}kA^{2}$", fontsize=24, color=OK, va="center")
    ax.text(8.65, 4.1, r"평형점:  속력 최대  $A\omega$", fontsize=18, color=INK, va="center")
    ax.text(8.65, 3.3, "양 끝:  속력 0, 에너지 전부 탄성", fontsize=18, color=INK, va="center")
    ax.text(8.65, 2.2, "진폭이 2배이면 에너지는 4배.", fontsize=18, color=WARM, va="center")
    ax.text(8.65, 1.45, "주기는 그대로입니다.", fontsize=18, color=INK, va="center")
    save(fig, "lesson_energy.webp")


def slide_speed():
    fig, ax = new_slide()
    title(ax, "임의의 위치에서 속력")
    ax.text(0.5, 7.85, "에너지 식은 원운동 그림자의 직각삼각형과 같습니다.", fontsize=16, color=MUTED)

    ax.text(0.6, 6.7, r"$\frac{1}{2}mv^{2} + \frac{1}{2}kx^{2} = \frac{1}{2}kA^{2}$", fontsize=22, color=INK)
    ax.text(0.6, 5.7, r"$v = \pm\, \omega\sqrt{A^{2} - x^{2}}$", fontsize=26, color=OK)
    ax.text(0.6, 4.75, r"$\omega = \sqrt{k/m}$,    $v_{\max} = A\omega$", fontsize=18, color=INK)

    box(ax, 0.5, 1.2, 7.3, 2.9, CREAM, "#fdba74")
    ax.text(0.8, 3.55, "확인 숫자", fontsize=16, color=WARM, fontweight="bold")
    ax.text(0.8, 2.75, r"위치가 $x = A/2$ 이면", fontsize=18, color=INK)
    ax.text(0.8, 1.9, r"$v = \frac{\sqrt{3}}{2}\, v_{\max}$", fontsize=22, color=INK, va="center")

    c = (12.15, 4.35)
    R = 2.05
    ang = np.deg2rad(58)
    px = c[0] + R * np.cos(ang)
    py = c[1] + R * np.sin(ang)
    ax.add_patch(Circle(c, R, fill=False, ec=LINE, lw=2))
    ax.plot([c[0], px], [c[1], c[1]], color=BLUE, lw=2.4)
    ax.plot([px, px], [c[1], py], color=OK, lw=2.4)
    ax.plot([c[0], px], [c[1], py], color="#94a3b8", lw=1.4, ls="--")
    ax.text((c[0] + px) / 2, c[1] - 0.35, "x", fontsize=16, color=BLUE, ha="center")
    ax.text(px + 0.2, (c[1] + py) / 2, r"$v/\omega$", fontsize=16, color=OK)
    ax.text((c[0] + px) / 2 - 0.35, (c[1] + py) / 2 + 0.25, "A", fontsize=16, color=MUTED)
    ax.text(10.15, 1.55, r"$x^{2} + (v/\omega)^{2} = A^{2}$", fontsize=18, color=INK)
    save(fig, "lesson_speed.webp")


def slide_pendulum():
    fig, ax = new_slide()
    title(ax, "단진자는 작은 각에서만 단진동")
    ax.text(0.5, 7.85, "접선 방향의 힘으로 풀면 됩니다. 이어지는 토크 계산과 같은 결과가 나옵니다.", fontsize=16, color=MUTED)

    pivot = (2.5, 6.9)
    L = 3.5
    ang = np.deg2rad(28)
    bob = (pivot[0] + L * np.sin(ang), pivot[1] - L * np.cos(ang))
    ax.plot([pivot[0] - 0.8, pivot[0] + 0.8], [pivot[1], pivot[1]], color=LINE, lw=4)
    ax.plot([pivot[0], pivot[0]], [pivot[1], pivot[1] - L], color="#cbd5e1", lw=1.4, ls="--")
    ax.plot([pivot[0], bob[0]], [pivot[1], bob[1]], color=LINE, lw=2)
    ax.add_patch(Circle(bob, 0.16, fc=WARM, ec=WARM))
    arrow(ax, bob, (bob[0], bob[1] - 1.15), "#64748b", 1.8)
    ax.text(bob[0] + 0.2, bob[1] - 0.7, "mg", fontsize=14, color="#64748b")
    # tangent direction for increasing angle is roughly (cos, sin) in this geometry
    tx, ty = np.cos(ang), np.sin(ang)
    arrow(ax, bob, (bob[0] - 1.25 * tx, bob[1] - 1.25 * ty), BLUE, 2.2)
    ax.text(bob[0] - 1.45 * tx, bob[1] - 1.15 * ty - 0.25, r"$mg\sin\theta$", fontsize=15, color=BLUE)
    ax.text(pivot[0] + 0.85 * np.sin(ang / 2) + 0.12, pivot[1] - 0.85 * np.cos(ang / 2), "θ", fontsize=15, color=OK)

    box(ax, 6.4, 4.55, 9.15, 2.85, PALE, "#bfdbfe")
    ax.text(6.65, 6.9, "작은 각이면", fontsize=16, color=BLUE, fontweight="bold")
    ax.text(6.65, 6.15, r"$\sin\theta \approx \theta$   (각은 라디안)", fontsize=18, color=INK, va="center")
    ax.text(6.65, 5.4, r"$a = -(g/l)\, x$", fontsize=22, color=OK, va="center")
    ax.text(6.65, 4.75, r"$T = 2\pi\sqrt{l/g}$", fontsize=22, color=INK, va="center")

    headers = ["각도", "라디안", "sin", "차이"]
    data = [("5도", "0.087", "0.087", "0.1%"), ("10도", "0.175", "0.174", "0.5%"), ("20도", "0.349", "0.342", "2%"), ("30도", "0.524", "0.500", "4.5%")]
    x0, y0 = 6.4, 4.15
    widths = [1.7, 2.0, 2.0, 1.8]
    rh = 0.48
    cx = x0
    for i, h in enumerate(headers):
        ax.add_patch(Rectangle((cx, y0 - rh), widths[i], rh, fc="#dbeafe", ec="#bfdbfe"))
        ax.text(cx + widths[i] / 2, y0 - rh / 2, h, ha="center", va="center", fontsize=13, color=BLUE, fontweight="bold")
        cx += widths[i]
    for r, row in enumerate(data):
        cx = x0
        yy = y0 - (r + 1) * rh
        for i, cell in enumerate(row):
            ax.add_patch(Rectangle((cx, yy - rh), widths[i], rh, fc="white", ec="#e2e8f0"))
            ax.text(cx + widths[i] / 2, yy - rh / 2, cell, ha="center", va="center", fontsize=13, color=INK)
            cx += widths[i]
    note(ax, "10도 안쪽이면 차이가 1%보다 작습니다. 질량은 식에서 사라지고, 주기를 바꾸는 것은 길이와 중력입니다.")
    save(fig, "lesson_pendulum.webp")


def slide_pendulum_bottom():
    fig, ax = new_slide()
    title(ax, "에너지와 장력은 각이 커도 성립한다")
    ax.text(0.5, 7.85, "단진동 근사는 주기에만 필요합니다. 높이와 장력은 각이 커도 같은 식으로 계산합니다.", fontsize=16, color=MUTED)

    box(ax, 0.4, 1.25, 7.45, 6.15, PALE, "#bfdbfe")
    ax.text(0.7, 6.85, "놓은 높이", fontsize=18, color=BLUE, fontweight="bold")
    ax.text(0.7, 6.05, r"$h = l(1 - \cos\theta)$", fontsize=24, color=INK, va="center")
    ax.text(0.7, 5.15, r"$mgh = \frac{1}{2}mv^{2}$", fontsize=22, color=INK, va="center")
    ax.text(0.7, 4.2, "예: 길이 1 m, 60도에서 가만히 놓으면", fontsize=16, color=INK)
    ax.text(0.7, 3.45, r"$h = 0.5\,\mathrm{m}$,   최저 속력 약 3.1 m/s", fontsize=18, color=INK, va="center")
    ax.text(0.7, 2.45, "60도는 단진동 근사 밖입니다.", fontsize=16, color=WARM)
    ax.text(0.7, 1.75, "그래도 에너지 계산은 맞습니다.", fontsize=16, color=INK)

    box(ax, 8.1, 1.25, 7.45, 6.15, CREAM, "#fdba74")
    ax.text(8.4, 6.85, "최저점의 실", fontsize=18, color=WARM, fontweight="bold")
    ax.plot([11.8, 11.8], [6.2, 4.15], color=LINE, lw=2)
    ax.add_patch(Circle((11.8, 3.95), 0.16, fc=WARM, ec=WARM))
    arrow(ax, (11.8, 3.95), (11.8, 5.15), BLUE, 2)
    ax.text(12.05, 4.7, "장력", fontsize=14, color=BLUE)
    arrow(ax, (11.8, 3.95), (11.8, 2.85), "#64748b", 2)
    ax.text(12.05, 3.2, "mg", fontsize=14, color="#64748b")
    ax.text(8.4, 2.55, r"$F_T - mg = m\frac{v^{2}}{l}$", fontsize=22, color=INK, va="center")
    ax.text(8.4, 1.7, "위 예에서는 장력 = 2mg", fontsize=18, color=OK)
    save(fig, "lesson_pendulum_bottom.webp")


def slide_tunnel():
    fig, ax = new_slide()
    title(ax, "지구 중심 터널도 용수철이다")
    ax.text(0.5, 7.85, "다음 계산 슬라이드 앞에서, 왜 복원력이 거리에 비례하는지만 봅니다.", fontsize=16, color=MUTED)

    c = (3.3, 4.15)
    ax.add_patch(Circle(c, 2.35, fc="#dbeafe", ec=BLUE, lw=2))
    ax.plot([c[0] - 2.35, c[0] + 2.35], [c[1], c[1]], color=LINE, lw=2)
    ax.add_patch(Circle(c, 1.15, fill=False, ec=OK, lw=1.6, ls="--"))
    ax.add_patch(Circle((c[0] + 1.15, c[1]), 0.12, fc=WARM, ec=WARM))
    ax.annotate("", xy=(c[0], c[1]), xytext=(c[0] + 1.15, c[1]), arrowprops=dict(arrowstyle="<->", color=WARM, lw=1.4))
    ax.text(c[0] + 0.55, c[1] + 0.25, "x", fontsize=16, color=WARM, ha="center")
    ax.text(c[0], c[1] - 2.7, "균일한 지구라고 가정", fontsize=14, color=MUTED, ha="center")

    points = [
        "바깥 껍질의 중력은 안에서 상쇄됩니다.",
        "실제로 끌어당기는 질량은 반지름 x 안의 공입니다.",
        r"그 질량은 전체의 $(x/R)^{3}$ 배입니다.",
        r"힘의 $x^{2}$ 과 부피의 $x^{3}$ 이 만나",
        r"$F = -\left(\frac{GMm}{R^{3}}\right) x$",
        "거리가 멀수록 힘이 커지는 용수철과 같습니다.",
    ]
    y = 6.9
    for i, row in enumerate(points):
        ax.text(6.5, y, row, fontsize=17, color=INK if i != 4 else OK, va="center")
        y -= 0.85
    note(ax, "균일한 지구라면 주기는 약 84분입니다. 지표면을 스치는 원궤도 위성의 주기와 같은 식입니다.")
    save(fig, "lesson_tunnel.webp")


def slide_family():
    fig, ax = new_slide()
    title(ax, "되돌리는 힘이 변위에 비례하면 주기는 하나")
    ax.text(0.5, 7.9, r"유효 용수철 상수를 $F = -k_{\mathrm{eff}} x$ 에서 읽습니다.", fontsize=16, color=MUTED)

    headers = ["계", "읽는 힘", "주기"]
    rows = [
        ["수평, 연직 용수철", r"$F=-kx$", r"$2\pi\sqrt{m/k}$"],
        ["직렬", r"$k=k_1 k_2/(k_1+k_2)$", "더 느리다"],
        ["병렬, 양쪽 용수철", r"$k=k_1+k_2$", "더 빠르다"],
        ["단진자, 작은 각", r"$a=-(g/l)x$", r"$2\pi\sqrt{l/g}$"],
        ["원형 골짜기", "단진자와 같은 꼴", r"$2\pi\sqrt{r/g}$"],
        ["물에 더 잠긴 통", r"$F=-\rho_0 S g\, x$", r"$2\pi\sqrt{\rho l/(\rho_0 g)}$"],
        ["지구 관통 터널", r"$F=-(GMm/R^{3})x$", r"$2\pi\sqrt{R^{3}/(GM)}$"],
    ]
    x0, y_top = 0.4, 7.35
    col_w = [3.5, 6.3, 5.4]
    row_h = 0.72
    cx = x0
    for i, h in enumerate(headers):
        ax.add_patch(Rectangle((cx, y_top - row_h), col_w[i], row_h, fc="#dbeafe", ec="#bfdbfe"))
        ax.text(cx + col_w[i] / 2, y_top - row_h / 2, h, ha="center", va="center", fontsize=15, color=BLUE, fontweight="bold")
        cx += col_w[i]
    for r, row in enumerate(rows):
        cx = x0
        yy = y_top - (r + 1) * row_h
        bg = "#f8fafc" if r % 2 == 0 else "white"
        for i, cell in enumerate(row):
            ax.add_patch(Rectangle((cx, yy - row_h), col_w[i], row_h, fc=bg, ec="#e2e8f0"))
            ax.text(cx + 0.15, yy - row_h / 2, cell, ha="left", va="center", fontsize=15, color=INK)
            cx += col_w[i]
    note(ax, "주기를 묻는 문제는 먼저 평형점을 정하고, 그곳에서 힘을 -kx 꼴로 고치면 됩니다.", y=0.38)
    save(fig, "lesson_family.webp")


if __name__ == "__main__":
    slide_course_map()
    slide_three_moduli()
    slide_rod_as_spring()
    slide_series_parallel()
    slide_vertical_spring()
    slide_shm_terms()
    slide_projection()
    slide_xva()
    slide_period()
    slide_ode_bridge()
    slide_energy()
    slide_speed()
    slide_pendulum()
    slide_pendulum_bottom()
    slide_tunnel()
    slide_family()
    print("16 lesson slides written")
