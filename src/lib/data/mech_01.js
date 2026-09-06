export const lectureData = [
  {
    type: "title",
    text: "1강. 역학과 에너지 (역학 파트 전체)"
  },
  {
    type: "callout",
    style: "info",
    title: "📖 단원 학습 개요",
    content: "본 강의는 [역학과 에너지] 교과서의 핵심 파트인 벡터와 힘의 평형, 포물선 운동, 등속 원운동, 일-에너지 정리, 역학적 에너지 보존 및 단진자 진동까지 역학의 전 과정을 생생한 시뮬레이션과 수식으로 완벽히 다룹니다."
  },

  // ----------------------------------------------------
  // SECTION 1: 벡터와 힘의 평형
  // ----------------------------------------------------
  {
    type: "title",
    text: "Ⅰ. 벡터와 힘의 평형 (Vector & Force Equilibrium)"
  },
  {
    type: "callout",
    style: "info",
    title: "1. 스칼라(Scalar)와 벡터(Vector)",
    content: "• 스칼라: 크기만을 가지는 물리량 (질량, 시간, 온동, 이동거리, 에너지 등)\n• 벡터: 크기와 방향을 동시에 가지는 물리량 (변위, 속도, 가속도, 힘, 운동량 등)\n• 벡터의 표시: 화살표의 방향은 벡터의 방향을, 화살표의 길이는 벡터의 크기를 나타냅니다."
  },
  {
    type: "callout",
    style: "warning",
    title: "2. 벡터의 합성과 성분 분해",
    content: "• 벡터의 합성: 두 벡터 $\\vec{A}$와 $\\vec{B}$의 합은 평행사변형법 또는 삼각형법으로 구합니다.\n• 벡터 분해: 기준축(x, y축)에 대해 $A_x = A\\cos\\theta$, $A_y = A\\sin\\theta$로 분해합니다.\n• 빗면에서의 중력 분해: 경사각 $\\theta$인 빗면 위 물체의 중력 $mg$는 빗면 내림 방향 성분 $mg\\sin\\theta$와 빗면 수직 방향 성분 $mg\\cos\\theta$로 분해됩니다."
  },
  {
    type: "simulation",
    title: "🕹️ 시뮬레이션 1: 벡터의 합성과 성분 분해 (Vector Addition)",
    src: "https://phet.colorado.edu/sims/html/vector-addition/latest/vector-addition_all.html?locale=ko",
    height: "600"
  },
  {
    type: "callout",
    style: "info",
    title: "3. 힘의 평형 조건",
    content: "물체에 작용하는 모든 힘의 합(알짜힘)이 0일 때 물체는 힘의 평형 상태에 있습니다.\n$$\\sum \\vec{F} = 0 \\quad \\Longrightarrow \\quad \\sum F_x = 0, \\quad \\sum F_y = 0$$\n빗면 위에서 정지한 물체: 빗면 방향 $F_{friction} = mg\\sin\\theta$, 수직 방향 $N = mg\\cos\\theta$"
  },
  {
    type: "quiz",
    title: "💡 개념 확인 퀴즈 1 (빗면에서의 힘)",
    question: "질량 $m=2\\text{kg}$인 물체가 경사각 $\\theta=30^\\circ$인 빗면에 정지해 있을 때, 물체에 작용하는 정지 마찰력의 크기는 얼마인가? ($g=10\\text{m/s}^2$, $\\sin 30^\\circ = 0.5$)",
    answer: "10 N (빗면 내림 방향 성분 $mg\\sin 30^\\circ = 2 \\times 10 \\times 0.5 = 10\\text{N}$ 이므로 정지 마찰력 또한 $10\\text{N}$입니다.)"
  },

  // ----------------------------------------------------
  // SECTION 2: 평면 운동과 포물선 운동
  // ----------------------------------------------------
  {
    type: "title",
    text: "Ⅱ. 평면 운동과 포물선 운동 (2D Motion & Projectile Motion)"
  },
  {
    type: "callout",
    style: "info",
    title: "1. 2차원 평면 운동의 독립성",
    content: "2차원 평면에서의 운동은 서로 직교하는 두 축(x축과 y축)의 독립된 1차원 운동의 합으로 나누어 분석할 수 있습니다.\n• 수평 방향(x축): 공기 저항이 없으면 알짜힘 0 $\\rightarrow$ 등속도 운동 ($v_x = v_0\\cos\\theta$, $x = v_0\\cos\\theta \\cdot t$)\n• 연직 방향(y축): 중력만 작용 $\\rightarrow$ 연직 투상/자유낙하 운동 ($v_y = v_0\\sin\\theta - gt$, $y = v_0\\sin\\theta \\cdot t - \\frac{1}{2}gt^2$)"
  },
  {
    type: "callout",
    style: "warning",
    title: "2. 포물선 운동의 주요 핵심 공식",
    content: "지면과 각도 $\\theta$로 초속도 $v_0$로 던져 올린 포물선 운동:\n1) 최고점 도달 시간: $t_H = \\frac{v_0\\sin\\theta}{g}$\n2) 최고점 높이: $H = \\frac{v_0^2\\sin^2\\theta}{2g}$\n3) 전체 비행 시간: $t_{total} = 2t_H = \\frac{2v_0\\sin\\theta}{g}$\n4) 수평 도달 거리: $R = v_x \\cdot t_{total} = \\frac{v_0^2\\sin 2\\theta}{g} \\quad (\\theta=45^\\circ\\text{일 때 최대})$"
  },
  {
    type: "simulation",
    title: "🕹️ 시뮬레이션 2: 포물선 운동 (Projectile Motion)",
    src: "https://phet.colorado.edu/sims/html/projectile-motion/latest/projectile-motion_all.html?locale=ko",
    height: "600"
  },
  {
    type: "quiz",
    title: "💡 개념 확인 퀴즈 2 (포물선 최고점에서의 속도)",
    question: "지면과 $60^\\circ$의 각도로 $20\\text{m/s}$의 속력으로 던져진 물체가 최고점에 도달했을 때의 속력은 얼마인가? (단, $\\cos 60^\\circ = 0.5$)",
    answer: "10 m/s (최고점에서는 연직 방향 속도 $v_y=0$이고 수평 방향 속도 $v_x = v_0\\cos 60^\\circ = 20 \\times 0.5 = 10\\text{m/s}$ 만 남게 됩니다.)"
  },

  // ----------------------------------------------------
  // SECTION 3: 등속 원운동과 위성의 운동
  // ----------------------------------------------------
  {
    type: "title",
    text: "Ⅲ. 등속 원운동과 위성의 운동 (Uniform Circular Motion)"
  },
  {
    type: "callout",
    style: "info",
    title: "1. 등속 원운동의 물리량",
    content: "• 주기($T$): 원을 한 바퀴 도는 데 걸리는 시간 ($T = \\frac{2\\pi r}{v}$)\n• 각속도($\\omega$): 단위 시간당 회전한 각도 (rad/s, $\\omega = \\frac{\\Delta\\theta}{\\Delta t} = \\frac{2\\pi}{T}$)\n• 선속도($v$): 원주상의 접선 속력 ($v = r\\omega$)"
  },
  {
    type: "callout",
    style: "warning",
    title: "2. 구심가속도와 구심력",
    content: "원운동하는 물체는 속력은 일정하지만 운동 방향이 계속 바뀌므로 원의 중심을 향하는 가속도를 가집니다.\n• 구심가속도: $a_c = \\frac{v^2}{r} = r\\omega^2$\n• 구심력: $F_c = m a_c = m\\frac{v^2}{r} = mr\\omega^2$\n• 구심력의 역할: 실의 장력(돌리기), 지면 마찰력(커브길 자동차), 만유인력(행성과 위성), 전기력(원자핵과 전자)"
  },
  {
    type: "simulation",
    title: "🕹️ 시뮬레이션 3: 중력과 위성 궤도 (Gravity and Orbits)",
    src: "https://phet.colorado.edu/sims/html/gravity-and-orbits/latest/gravity-and-orbits_all.html?locale=ko",
    height: "600"
  },
  {
    type: "video",
    title: "📺 뉴턴의 대포와 인공위성의 궤도 원리",
    src: "https://www.youtube.com/watch?v=IC1Pvr57f6U"
  },
  {
    type: "quiz",
    title: "💡 개념 확인 퀴즈 3 (구심력과 반지름의 관계)",
    question: "동일한 각속도 $\\omega$로 회전하는 원판 위에서 중심으로부터 회전 반지름이 2배가 되면 물체가 받는 구심력의 크기는 몇 배가 되는가?",
    answer: "2배 ($F = mr\\omega^2$에서 각속도 $\\omega$가 일정할 때 구심력은 반지름 $r$에 직비례하므로 2배가 됩니다.)"
  },

  // ----------------------------------------------------
  // SECTION 4: 일과 역학적 에너지 보존
  // ----------------------------------------------------
  {
    type: "title",
    text: "Ⅳ. 일과 역학적 에너지 보존 (Work & Conservation of Energy)"
  },
  {
    type: "callout",
    style: "info",
    title: "1. 일의 정의와 일-에너지 정리",
    content: "• 일($W$): 물체에 힘 $F$를 가하여 힘의 방향으로 거리 $s$만큼 이동시켰을 때 $W = F s \\cos\\theta$\n• 일-에너지 정리: 물체에 작용한 알짜힘이 한 일은 물체의 운동 에너지 변화량과 같습니다.\n$$W_{net} = \\Delta E_k = \\frac{1}{2}mv^2 - \\frac{1}{2}mv_0^2$$"
  },
  {
    type: "callout",
    style: "warning",
    title: "2. 퍼텐셜 에너지와 역학적 에너지 보존",
    content: "• 중력 퍼텐셜 에너지: $E_p = mgh$\n• 탄성 퍼텐셜 에너지: $E_p = \\frac{1}{2}kx^2$\n• 만유인력 퍼텐셜 에너지: $E_p = -G\\frac{Mm}{r}$\n• 역학적 에너지 보존: 보존력(중력, 탄성력 등)만 작용할 때 $E_{total} = E_k + E_p = \\text{일정}$\n• 비보존력(마찰, 공기저항)이 작용할 때: $W_{friction} = E_{final} - E_{initial}$ (역학적 에너지 일부가 열에너지로 전환)"
  },
  {
    type: "simulation",
    title: "🕹️ 시뮬레이션 4: 에너지 스케이트 파크 (Energy Skate Park)",
    src: "https://phet.colorado.edu/sims/html/energy-skate-park-basics/latest/energy-skate-park-basics_all.html?locale=ko",
    height: "600"
  },
  {
    type: "quiz",
    title: "💡 개념 확인 퀴즈 4 (탄성 퍼텐셜 에너지)",
    question: "용수철 상수 $k = 200\\text{N/m}$인 용수철을 원래 길이에서 $0.1\\text{m}$만큼 늘였을 때 용수철에 저장되는 탄성 퍼텐셜 에너지는 얼마인가?",
    answer: "1 J ($E_p = \\frac{1}{2} k x^2 = \\frac{1}{2} \\times 200 \\times (0.1)^2 = 1\\text{J}$ 입니다.)"
  },

  // ----------------------------------------------------
  // SECTION 5: 단진자와 단순조화 진동
  // ----------------------------------------------------
  {
    type: "title",
    text: "Ⅴ. 단진자와 단순조화 진동 (Simple Pendulum & Oscillations)"
  },
  {
    type: "callout",
    style: "info",
    title: "1. 단진자의 복원력과 에너지 전환",
    content: "• 복원력: 진자가 변위 $x$만큼 벗어났을 때 중심으로 돌려놓으려는 힘 $F = -mg\\sin\\theta \\approx -mg\\frac{x}{l}$\n• 에너지 전환: 최고점(운동 에너지 0, 퍼텐셜 에너지 최대) $\\longleftrightarrow$ 평형점(운동 에너지 최대, 퍼텐셜 에너지 0)"
  },
  {
    type: "callout",
    style: "warning",
    title: "2. 단진자 주기 공식과 등시성",
    content: "진폭이 작을 때 단진자의 주기 $T$는 추의 질량이나 진폭에 상관없이 오직 진자의 길이($l$)와 중력 가속도($g$)에 의해서만 결정됩니다 (진자의 등시성).\n$$T = 2\\pi \\sqrt{\\frac{l}{g}}$$\n• 길이를 4배로 늘리면 주기는 2배가 됩니다."
  },
  {
    type: "simulation",
    title: "🕹️ 시뮬레이션 5: 단진자 실험실 (Pendulum Lab)",
    src: "https://phet.colorado.edu/sims/html/pendulum-lab/latest/pendulum-lab_all.html?locale=ko",
    height: "600"
  },
  {
    type: "quiz",
    title: "💡 개념 확인 퀴즈 5 (단진자의 주기)",
    question: "지구에서 주기가 2초인 단진자를 중력 가속도가 지구의 1/4배인 달로 가져가면 주기는 몇 초가 되겠는가?",
    answer: "4초 ($T = 2\\pi\\sqrt{\\frac{l}{g}}$ 에서 $g$가 1/4배가 되면 $\\sqrt{1/g}$에 의해 주기는 $\\sqrt{4} = 2$배 증가하여 $2 \\times 2 = 4\\text{초}$가 됩니다.)"
  },
  {
    type: "callout",
    style: "info",
    title: "🎉 1강 학습 완료!",
    content: "수고하셨습니다! [역학과 에너지] 1강 전체 과정을 완강하셨습니다. 화면 하단의 탐색바나 판서(D키) 기능을 활용하여 자유롭게 복습해보세요."
  }
];
