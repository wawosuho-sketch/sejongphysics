"""4강 흐름을 잇는 보충 슬라이드. 원본 슬라이드는 건드리지 않습니다."""

import os

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

if os.name == "nt":
    plt.rc("font", family="Malgun Gothic")
else:
    plt.rc("font", family="AppleGothic")
plt.rcParams["axes.unicode_minus"] = False

OUT = r"r:\textbook-svelte\public\images\slides\mech_04"
os.makedirs(OUT, exist_ok=True)

BLUE = "#1d4ed8"
INK = "#0f172a"
MUTED = "#475569"
WARM = "#c2410c"
COLD = "#1d4ed8"
OK = "#047857"
NO = "#b91c1c"


def new_slide():
    fig, ax = plt.subplots(figsize=(16, 9), dpi=100)
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 9)
    ax.axis("off")
    fig.patch.set_facecolor("white")
    ax.set_facecolor("white")
    return fig, ax


def save(fig, name):
    fig.savefig(os.path.join(OUT, name), format="webp", dpi=100)
    preview = os.path.join(r"r:\textbook-svelte\tmp", name.replace(".webp", ".jpg"))
    fig.savefig(preview, format="jpg", dpi=70)
    plt.close(fig)


def title(ax, text):
    ax.text(0.6, 8.35, text, fontsize=32, color=BLUE, fontweight="bold", va="center")


def box(ax, x, y, w, h, fc, ec):
    ax.add_patch(
        FancyBboxPatch(
            (x, y),
            w,
            h,
            boxstyle="round,pad=0.02,rounding_size=0.15",
            facecolor=fc,
            edgecolor=ec,
            linewidth=2,
        )
    )


def slide_sign():
    fig, ax = new_slide()
    title(ax, "이 수업에서 쓰는 부호")
    ax.text(
        0.6,
        7.55,
        "75~78번의 교과서 식과 80번의 ΔU = Q - W 는 같은 약속입니다.",
        fontsize=18,
        color=MUTED,
        va="center",
    )

    box(ax, 0.55, 3.55, 7.3, 3.55, "#f8fafc", "#cbd5e1")
    ax.text(0.9, 6.55, "부호", fontsize=22, color=INK, fontweight="bold")
    rows = [
        ("Q > 0", "기체가 열을 받음"),
        ("Q < 0", "기체가 열을 버림"),
        ("W > 0", "기체가 밖으로 일을 함  (팽창)"),
        ("W < 0", "기체가 일을 받음  (압축)"),
    ]
    y = 5.85
    for symbol, meaning in rows:
        ax.text(0.95, y, symbol, fontsize=20, color=BLUE, fontweight="bold", va="center")
        ax.text(3.15, y, meaning, fontsize=20, color=INK, va="center")
        y -= 0.7

    box(ax, 8.15, 3.55, 7.3, 3.55, "#eff6ff", BLUE)
    ax.text(8.5, 6.55, "같은 식, 두 가지 모양", fontsize=22, color=INK, fontweight="bold")
    ax.text(8.5, 5.55, "ΔU  =  Q  -  W", fontsize=28, color=INK, fontweight="bold")
    ax.text(8.5, 4.7, "Q  =  W  +  ΔU", fontsize=28, color=INK, fontweight="bold")
    ax.text(8.5, 3.9, "위 식을 아래로 옮긴 것입니다.", fontsize=16, color=MUTED)

    box(ax, 0.55, 0.45, 14.9, 2.75, "#fff7ed", WARM)
    ax.text(0.9, 2.7, "82번의 화학 부호와 숫자 예시", fontsize=20, color=WARM, fontweight="bold")
    ax.text(
        0.9,
        1.95,
        "ΔU = Q + W 에서 W가 양수라는 것은 ‘기체가 받은 일’입니다. 부호 정의가 반대일 뿐, 다른 법칙이 아닙니다.",
        fontsize=16,
        color=INK,
    )
    ax.text(
        0.9,
        1.15,
        "단열 압축으로 500 J을 받으면   Q = 0 ,   W = -500 J",
        fontsize=18,
        color=INK,
    )
    ax.text(
        0.9,
        0.65,
        "ΔU = 0 - (-500) = +500 J     내부에너지가 늘어 온도가 올라갑니다.",
        fontsize=18,
        color=OK,
        fontweight="bold",
    )
    save(fig, "supplement_sign.webp")


def slide_carnot():
    fig, ax = new_slide()
    title(ax, "카르노 효율을 숫자로")
    ax.text(
        0.6,
        7.55,
        "120번의 효율 식  1 - Tc / Th  에 온도를 넣습니다.",
        fontsize=18,
        color=MUTED,
    )

    box(ax, 0.55, 5.35, 4.6, 1.7, "#fee2e2", "#dc2626")
    ax.text(2.85, 6.45, "고열원", fontsize=18, color=NO, ha="center", fontweight="bold")
    ax.text(2.85, 5.8, "Th = 600 K", fontsize=26, color=INK, ha="center", fontweight="bold")

    box(ax, 5.7, 5.35, 4.6, 1.7, "#dbeafe", BLUE)
    ax.text(8.0, 6.45, "저열원", fontsize=18, color=COLD, ha="center", fontweight="bold")
    ax.text(8.0, 5.8, "Tc = 300 K", fontsize=26, color=INK, ha="center", fontweight="bold")

    box(ax, 10.85, 5.35, 4.6, 1.7, "#ecfdf5", OK)
    ax.text(13.15, 6.45, "효율", fontsize=18, color=OK, ha="center", fontweight="bold")
    ax.text(13.15, 5.8, "η = 0.50", fontsize=26, color=INK, ha="center", fontweight="bold")

    ax.text(0.7, 4.55, "1 - 300 / 600  =  1 - 0.5  =  0.50     (50%)", fontsize=26, color=INK, fontweight="bold")

    box(ax, 0.55, 1.35, 14.9, 2.7, "#f8fafc", "#cbd5e1")
    ax.text(0.9, 3.5, "고열원에서 1000 J을 받으면", fontsize=20, color=INK, fontweight="bold")
    ax.text(0.9, 2.65, "일로 바뀌는 양    W = 500 J", fontsize=22, color=OK, fontweight="bold")
    ax.text(8.3, 2.65, "저열원으로 버리는 열    500 J", fontsize=22, color=COLD, fontweight="bold")
    ax.text(
        0.9,
        1.75,
        "저열원이 0 K가 아닌 한, 받은 열을 전부 일로 바꿀 수는 없습니다.",
        fontsize=18,
        color=MUTED,
    )
    save(fig, "supplement_carnot.webp")


def slide_entropy():
    fig, ax = new_slide()
    title(ax, "왜 열은 높은 곳에서 낮은 곳으로만 가나")
    ax.text(0.6, 7.55, "115번의  ΔS = Q / T  로 144~145번의 방향을 계산합니다.", fontsize=18, color=MUTED)

    box(ax, 0.5, 4.55, 3.3, 2.45, "#fee2e2", "#dc2626")
    ax.text(2.15, 6.35, "600 K", fontsize=26, color=NO, ha="center", fontweight="bold")
    ax.text(2.15, 5.55, "뜨거운 쪽", fontsize=16, color=INK, ha="center")
    ax.text(2.15, 5.0, "ΔS = -1.0 J/K", fontsize=16, color=INK, ha="center")

    ax.add_patch(
        FancyArrowPatch(
            (4.0, 5.75),
            (6.15, 5.75),
            arrowstyle="-|>",
            mutation_scale=22,
            linewidth=3,
            color=OK,
        )
    )
    ax.text(5.05, 6.35, "Q = 600 J", fontsize=16, color=OK, ha="center", fontweight="bold")

    box(ax, 6.3, 4.55, 3.3, 2.45, "#dbeafe", BLUE)
    ax.text(7.95, 6.35, "300 K", fontsize=26, color=COLD, ha="center", fontweight="bold")
    ax.text(7.95, 5.55, "차가운 쪽", fontsize=16, color=INK, ha="center")
    ax.text(7.95, 5.0, "ΔS = +2.0 J/K", fontsize=16, color=INK, ha="center")

    box(ax, 10.15, 4.55, 5.3, 2.45, "#ecfdf5", OK)
    ax.text(12.8, 6.35, "전체", fontsize=18, color=OK, ha="center", fontweight="bold")
    ax.text(12.8, 5.55, "-1.0 + 2.0", fontsize=22, color=INK, ha="center", fontweight="bold")
    ax.text(12.8, 4.95, "= +1.0 J/K", fontsize=22, color=OK, ha="center", fontweight="bold")

    ax.text(0.6, 3.85, "뜨거운 쪽이 잃은 엔트로피보다, 차가운 쪽이 얻은 엔트로피가 더 큽니다.", fontsize=18, color=INK)

    box(ax, 0.5, 1.55, 7.4, 1.85, "#f8fafc", "#cbd5e1")
    ax.text(0.8, 2.9, "반대로 600 J이 흐르면", fontsize=16, color=MUTED, fontweight="bold")
    ax.text(0.8, 2.15, "ΔS = +1.0 + (-2.0) = -1.0 J/K", fontsize=18, color=NO, fontweight="bold")

    box(ax, 8.15, 1.55, 7.3, 1.85, "#fff7ed", WARM)
    ax.text(8.45, 2.9, "제1법칙과 제2법칙", fontsize=16, color=WARM, fontweight="bold")
    ax.text(8.45, 2.3, "에너지는 양쪽 다 보존됩니다.", fontsize=18, color=INK)
    ax.text(8.45, 1.8, "방향을 정하는 것이 제2법칙입니다.", fontsize=18, color=INK, fontweight="bold")

    ax.text(0.6, 0.85, "고립된 전체의 엔트로피가 줄어드는 방향은 스스로 일어나지 않습니다.", fontsize=18, color=MUTED)
    save(fig, "supplement_entropy.webp")


if __name__ == "__main__":
    slide_sign()
    slide_carnot()
    slide_entropy()
    print("wrote 3 supplements")
