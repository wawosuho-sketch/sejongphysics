import matplotlib.pyplot as plt
import matplotlib.patches as patches
import os

# 한글 폰트 설정
plt.style.use('dark_background')
if os.name == 'nt':
    plt.rc('font', family='Malgun Gothic')
else:
    plt.rc('font', family='AppleGothic')
plt.rcParams['axes.unicode_minus'] = False

out_dir = r"r:\textbook-svelte\public\images\slides\mech_02"
os.makedirs(out_dir, exist_ok=True)

def draw_diagram1():
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.set_xlim(-1, 7)
    ax.set_ylim(-1, 2)
    ax.axis('off')
    
    # 별/행성 그리기
    ax.plot(0, 0, 'bo', markersize=20, label='지구')
    ax.plot(3, 0, 'go', markersize=20, label='정중앙 행성')
    ax.plot(6, 0, 'ro', markersize=20, label='B 출발점')
    
    ax.text(0, -0.3, '지구\n(0광년)', ha='center', color='cyan', fontsize=12)
    ax.text(3, -0.3, '행성\n(3광년)', ha='center', color='lime', fontsize=12)
    ax.text(6, -0.3, '우주 공간\n(6광년)', ha='center', color='orange', fontsize=12)
    
    # 텍스트
    ax.text(3, 1.5, "동시성의 현장 관측 (물리적 검증)", ha='center', color='white', fontsize=16, fontweight='bold')
    
    # 빛 신호
    ax.annotate('', xy=(2.8, 0.2), xytext=(0.2, 0.2),
                arrowprops=dict(arrowstyle="->", color="yellow", lw=2, ls="--"))
    ax.annotate('', xy=(3.2, 0.2), xytext=(5.8, 0.2),
                arrowprops=dict(arrowstyle="->", color="yellow", lw=2, ls="--"))
    
    ax.text(1.5, 0.4, '빛 발사', color='yellow', ha='center')
    ax.text(4.5, 0.4, '빛 발사', color='yellow', ha='center')
    ax.text(3, 0.6, '빛 동시 도달\n(동시 출발 증명!)', color='yellow', ha='center', bbox=dict(boxstyle="round,pad=0.3", fc="black", ec="yellow"))

    plt.tight_layout()
    plt.savefig(os.path.join(out_dir, "simultaneity_verification.png"), dpi=150)
    plt.close()

def draw_diagram2():
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.set_xlim(-1, 7)
    ax.set_ylim(-1, 3)
    ax.axis('off')
    
    ax.text(3, 2.5, "지구 관점: 10년짜리 릴레이 비행 (고유 거리 3광년 + 3광년)", ha='center', color='white', fontsize=16, fontweight='bold')
    
    # 위치
    ax.plot(0, 0, 'bo', markersize=15)
    ax.plot(3, 0, 'go', markersize=15)
    ax.plot(6, 0, 'ro', markersize=15)
    ax.text(0, -0.4, '지구\n(0광년)', ha='center', color='cyan')
    ax.text(3, -0.4, '행성\n(3광년)', ha='center', color='lime')
    ax.text(6, -0.4, 'B 출발점\n(6광년)', ha='center', color='orange')
    
    # 거리 표시
    ax.annotate('', xy=(3, -0.9), xytext=(0, -0.9), arrowprops=dict(arrowstyle="<->", color="white"))
    ax.text(1.5, -1.1, '3광년', color='white', ha='center', fontsize=12)
    ax.annotate('', xy=(6, -0.9), xytext=(3, -0.9), arrowprops=dict(arrowstyle="<->", color="white"))
    ax.text(4.5, -1.1, '3광년', color='white', ha='center', fontsize=12)
    
    # 우주선 비행
    ax.annotate('', xy=(2.9, 0.8), xytext=(0.1, 0.8), arrowprops=dict(arrowstyle="->", color="cyan", lw=3))
    ax.annotate('', xy=(0.1, 1.5), xytext=(5.9, 1.5), arrowprops=dict(arrowstyle="->", color="orange", lw=3))
    
    ax.text(1.5, 1.0, '우주선 A (v=0.6c)\n지구 시간 5.0년 소요', color='cyan', ha='center', fontsize=11)
    ax.text(3, 1.7, '우주선 B (v=0.6c)\n지구 시간 10.0년 소요 (최종 도착 시)', color='orange', ha='center', fontsize=11)
    
    ax.plot(3, 0.8, 'w*', markersize=15)
    ax.text(3, 1.1, '교차 (t=5.0년)', color='white', ha='center', bbox=dict(facecolor='black', edgecolor='white'))
    
    plt.tight_layout()
    plt.savefig(os.path.join(out_dir, "earth_perspective_crossing.png"), dpi=150)
    plt.close()

def draw_diagram3():
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.set_xlim(-1, 7)
    ax.set_ylim(-1, 2)
    ax.axis('off')
    
    ax.text(3, 1.5, "우주선 B 관점: 길이 수축과 동시성의 시차 (출발 시점)", ha='center', color='white', fontsize=16, fontweight='bold')
    
    # B 중심 좌표계에서 지구와 행성은 다가옴
    ax.plot(0.8, 0, 'bo', markersize=15)
    ax.plot(3.2, 0, 'go', markersize=15)
    ax.plot(5.6, 0, 'ro', markersize=15)
    
    ax.text(0.8, -0.5, '지구 시계\n[ 3.6년 ]', ha='center', color='magenta', fontweight='bold', fontsize=14, bbox=dict(facecolor='black', edgecolor='magenta'))
    ax.text(3.2, -0.4, '행성\n(다가옴)', ha='center', color='lime')
    ax.text(5.6, -0.4, '우주선 B\n(나)', ha='center', color='orange')
    
    # 수축된 거리 표시
    ax.annotate('', xy=(3.2, 0.5), xytext=(0.8, 0.5), arrowprops=dict(arrowstyle="<->", color="white"))
    ax.text(2.0, 0.6, '수축된 2.4광년', color='white', ha='center', fontsize=12)
    
    ax.annotate('', xy=(5.6, 0.5), xytext=(3.2, 0.5), arrowprops=dict(arrowstyle="<->", color="white"))
    ax.text(4.4, 0.6, '수축된 2.4광년', color='white', ha='center', fontsize=12)
    
    # 속도 화살표 (지구가 B를 향해 다가옴)
    ax.annotate('', xy=(0.3, 0), xytext=(0.7, 0), arrowprops=dict(arrowstyle="->", color="cyan", lw=2))
    ax.annotate('', xy=(2.7, 0), xytext=(3.1, 0), arrowprops=dict(arrowstyle="->", color="lime", lw=2))
    
    # 설명
    ax.text(3, -0.9, "우주선 관점: 지구가 0.6c로 다가옴. 고유거리 3광년 -> 2.4광년으로 수축!\n6광년 떨어진 지구의 시계는 동시성 시차로 인해 이미 3.6년에서 시작합니다.", color='yellow', ha='center', fontsize=12)
    
    plt.tight_layout()
    plt.savefig(os.path.join(out_dir, "spaceship_b_perspective_start.png"), dpi=150)
    plt.close()

def draw_diagram4():
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.set_xlim(-1, 10)
    ax.set_ylim(0, 4)
    ax.axis('off')
    
    ax.text(4.5, 3.5, "우주선 B 관점에서 완성되는 10년의 지구 시계 흐름", ha='center', color='white', fontsize=16, fontweight='bold')
    
    # 3단계 그리기
    steps = [
        (3, "① 출발 (t''=0년)", "지구 시계: 3.6년 (시차)", 3.6),
        (2, "② 행성 교차 (t''=4.0년)", "지구 시계: 3.6 + 3.2 = 6.8년", 6.8),
        (1, "③ 지구 도착 (t''=8.0년)", "지구 시계: 6.8 + 3.2 = 10.0년", 10.0)
    ]
    
    for y, title, desc, val in steps:
        ax.text(0, y, title, color='orange', fontsize=12, fontweight='bold', va='center')
        ax.plot([2.5, 8.5], [y, y], color='gray', lw=2) # bar
        ax.plot([2.5, 2.5 + (val/10)*6], [y, y], color='cyan', lw=6) # progress
        ax.text(8.7, y, desc, color='white', fontsize=12, va='center', fontweight='bold')
        ax.text(2.5 + (val/10)*6, y+0.2, f"{val}년", color='cyan', ha='center', fontweight='bold')
        
    ax.text(4.5, 0.4, "시간 팽창: 내(B) 시계 4년이 흐를 때마다 지구 시계는 3.2년씩 증가!\n(3.6년에서 출발하여 시차 도약 없이 자연스럽게 10.0년 도달)", color='yellow', ha='center', fontsize=13)
    
    plt.tight_layout()
    plt.savefig(os.path.join(out_dir, "spaceship_b_puzzle_completion.png"), dpi=150)
    plt.close()

if __name__ == "__main__":
    draw_diagram1()
    draw_diagram2()
    draw_diagram3()
    draw_diagram4()
    print("All diagrams generated successfully.")
