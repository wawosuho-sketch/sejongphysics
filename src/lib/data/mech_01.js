export const lectureData = [
  {
    type: "title",
    text: "1강. 역학과 에너지 (역학 파트 전체)"
  },
  {
    type: "callout",
    style: "info",
    title: "📖 학습 방법 안내",
    content: "모든 슬라이드 이미지는 클릭하시면 **큰 화면(전체 화면 모달)**으로 선명하게 수식과 그래프를 확대해 보실 수 있습니다. 슬라이드 흐름에 맞춰 배치된 **PhET 시뮬레이션**과 **개념 퀴즈**를 활용해 직접 탐구해보세요!"
  },

  // ====================================================
  // PART 1: 벡터와 힘의 평형 (Slide 01 ~ 14)
  // ====================================================
  {
    type: "section_header",
    chapter: "PART 1",
    title: "Ⅰ. 벡터와 힘의 평형 (Vector & Force Equilibrium)",
    subtitle: "스칼라와 벡터의 차이, 벡터 합성 및 성분 분해, 빗면에서의 힘의 평형"
  },
  { type: "image", src: "/images/slides/mech_01/slide_01.webp" },
  { type: "image", src: "/images/slides/mech_01/slide_02.webp" },
  { type: "image", src: "/images/slides/mech_01/slide_03.webp" },
  { type: "image", src: "/images/slides/mech_01/slide_04.webp" },
  { type: "image", src: "/images/slides/mech_01/slide_05.webp" },

  {
    type: "callout",
    style: "warning",
    title: "📌 핵심 개념 정리: 스칼라 vs 벡터",
    content: "• 스칼라(Scalar): 크기만 갖는 물리량 (질량 $m$, 시간 $t$, 이동거리 $s$, 에너지 $E$)\n• 벡터(Vector): 크기와 방향을 동시에 갖는 물리량 (변위 $\\vec{s}$, 속도 $\\vec{v}$, 가속도 $\\vec{a}$, 힘 $\\vec{F}$, 운동량 $\\vec{p}$)"
  },
  {
    type: "quiz",
    title: "💡 개념 확인 퀴즈 1: 물리량의 분류",
    question: "다음 물리량 중 방향성을 가진 벡터(Vector) 물리량만을 고르시오: [질량, 변위, 온도, 속도, 에너지, 힘]",
    answer: "변위, 속도, 힘 (크기와 방향을 모두 고려해야 하는 물리량이 벡터입니다.)"
  },
  {
    type: "simulation",
    title: "🕹️ 직접 탐구: 벡터의 합성과 성분 분해 (Vector Addition)",
    src: "https://phet.colorado.edu/sims/html/vector-addition/latest/vector-addition_all.html?locale=ko",
    height: "600"
  },

  { type: "image", src: "/images/slides/mech_01/slide_06.webp" },
  { type: "image", src: "/images/slides/mech_01/slide_07.webp" },
  { type: "image", src: "/images/slides/mech_01/slide_08.webp" },
  { type: "image", src: "/images/slides/mech_01/slide_09.webp" },
  { type: "image", src: "/images/slides/mech_01/slide_10.webp" },

  {
    type: "callout",
    style: "info",
    title: "📌 수식 핵심: 빗면에서의 중력 분해",
    content: "경사각 $\\theta$인 빗면 위 물체(질량 $m$)에 작용하는 중력 $mg$의 두 성분:\n1) 빗면 내림 방향 성분: $F_{\\parallel} = mg\\sin\\theta$\n2) 빗면 수직 방향 성분: $F_{\\perp} = mg\\cos\\theta$\n• 정지 상태 시 빗면 정지 마찰력: $f_s = mg\\sin\\theta$\n• 수직 항력: $N = mg\\cos\\theta$"
  },
  {
    type: "simulation",
    title: "🕹️ 직접 탐구: 빗면과 힘의 합성 (Forces on Incline)",
    src: "https://phet.colorado.edu/sims/html/forces-and-motion-basics/latest/forces-and-motion-basics_all.html?locale=ko",
    height: "600"
  },

  { type: "image", src: "/images/slides/mech_01/slide_11.webp" },
  { type: "image", src: "/images/slides/mech_01/slide_12.webp" },
  { type: "image", src: "/images/slides/mech_01/slide_13.webp" },
  { type: "image", src: "/images/slides/mech_01/slide_14.webp" },

  {
    type: "quiz",
    title: "💡 개념 확인 퀴즈 2: 빗면 정지 마찰력",
    question: "경사각 $\\theta=30^\\circ$인 빗면에 질량 $2\\text{kg}$인 물체가 정지해 있을 때 물체에 작용하는 정지 마찰력은? ($g=10\\text{m/s}^2$, $\\sin 30^\\circ=0.5$)",
    answer: "10 N (빗면 내림 방향 성력 $mg\\sin 30^\\circ = 2 \\times 10 \\times 0.5 = 10\\text{N}$ 이므로 정지 마찰력도 10N입니다.)"
  },

  // ====================================================
  // PART 2: 평면 운동과 포물선 운동 (Slide 15 ~ 38)
  // ====================================================
  {
    type: "section_header",
    chapter: "PART 2",
    title: "Ⅱ. 평면 운동과 포물선 운동 (2D Motion & Projectile Motion)",
    subtitle: "2차원 운동의 독립성, 수평/비스듬 투사 포물선 궤적 분석"
  },
  { type: "image", src: "/images/slides/mech_01/slide_15.webp" },
  { type: "image", src: "/images/slides/mech_01/slide_16.webp" },
  { type: "image", src: "/images/slides/mech_01/slide_17.webp" },
  { type: "image", src: "/images/slides/mech_01/slide_18.webp" },
  { type: "image", src: "/images/slides/mech_01/slide_19.webp" },
  { type: "image", src: "/images/slides/mech_01/slide_20.webp" },
  { type: "image", src: "/images/slides/mech_01/slide_21.webp" },
  { type: "image", src: "/images/slides/mech_01/slide_22.webp" },
  { type: "image", src: "/images/slides/mech_01/slide_23.webp" },
  { type: "image", src: "/images/slides/mech_01/slide_24.webp" },
  { type: "image", src: "/images/slides/mech_01/slide_25.webp" },
  { type: "image", src: "/images/slides/mech_01/slide_26.webp" },
  { type: "image", src: "/images/slides/mech_01/slide_27.webp" },

  {
    type: "callout",
    style: "warning",
    title: "📌 수식 핵심: 포물선 운동의 핵심공식 요약",
    content: "각도 $\\theta$, 초속도 $v_0$로 비스듬히 던져 올린 포물선 운동:\n1) 최고점 도달 시간: $t_H = \\frac{v_0\\sin\\theta}{g}$\n2) 최고점 높이: $H = \\frac{v_0^2\\sin^2\\theta}{2g}$\n3) 수평 도달 거리: $R = \\frac{v_0^2\\sin 2\\theta}{g} \\quad (\\theta=45^\\circ\\text{일 때 최대})$"
  },
  {
    type: "simulation",
    title: "🕹️ 직접 탐구: 포물선 운동 각도 및 사거리 실험 (Projectile Motion)",
    src: "https://phet.colorado.edu/sims/html/projectile-motion/latest/projectile-motion_all.html?locale=ko",
    height: "600"
  },

  { type: "image", src: "/images/slides/mech_01/slide_28.webp" },
  { type: "image", src: "/images/slides/mech_01/slide_29.webp" },
  { type: "image", src: "/images/slides/mech_01/slide_30.webp" },
  { type: "image", src: "/images/slides/mech_01/slide_31.webp" },
  { type: "image", src: "/images/slides/mech_01/slide_32.webp" },
  { type: "image", src: "/images/slides/mech_01/slide_33.webp" },
  { type: "image", src: "/images/slides/mech_01/slide_34.webp" },
  { type: "image", src: "/images/slides/mech_01/slide_35.webp" },
  { type: "image", src: "/images/slides/mech_01/slide_36.webp" },
  { type: "image", src: "/images/slides/mech_01/slide_37.webp" },
  { type: "image", src: "/images/slides/mech_01/slide_38.webp" },

  {
    type: "quiz",
    title: "💡 개념 확인 퀴즈 3: 최고점에서의 속력",
    question: "지면과 $60^\\circ$의 각도로 $20\\text{m/s}$의 속력으로 발사된 물체의 최고점에서의 속력은? (단, $\\cos 60^\\circ = 0.5$)",
    answer: "10 m/s (최고점에서는 연직 속도 $v_y=0$이며 수평 속도 $v_x = v_0\\cos 60^\\circ = 20 \\times 0.5 = 10\\text{m/s}$ 만 남게 됩니다.)"
  },

  // ====================================================
  // PART 3: 등속 원운동과 위성의 운동 (Slide 39 ~ 50)
  // ====================================================
  {
    type: "section_header",
    chapter: "PART 3",
    title: "Ⅲ. 등속 원운동과 위성의 운동 (Uniform Circular Motion)",
    subtitle: "각속도, 구심가속도 및 구심력, 뉴턴의 대포와 인공위성 궤도"
  },
  { type: "image", src: "/images/slides/mech_01/slide_39.webp" },
  { type: "image", src: "/images/slides/mech_01/slide_40.webp" },
  { type: "image", src: "/images/slides/mech_01/slide_41.webp" },
  { type: "image", src: "/images/slides/mech_01/slide_42.webp" },
  { type: "image", src: "/images/slides/mech_01/slide_43.webp" },
  { type: "image", src: "/images/slides/mech_01/slide_44.webp" },

  {
    type: "callout",
    style: "info",
    title: "📌 수식 핵심: 구심가속도와 구심력 공식",
    content: "• 각속도: $\\omega = \\frac{\\Delta\\theta}{\\Delta t} = \\frac{2\\pi}{T}$\n• 선속도: $v = r\\omega$\n• 구심가속도: $a_c = \\frac{v^2}{r} = r\\omega^2$\n• 구심력: $F_c = m a_c = m\\frac{v^2}{r} = mr\\omega^2$"
  },
  {
    type: "simulation",
    title: "🕹️ 직접 탐구: 중력과 위성의 궤도 운동 (Gravity and Orbits)",
    src: "https://phet.colorado.edu/sims/html/gravity-and-orbits/latest/gravity-and-orbits_all.html?locale=ko",
    height: "600"
  },

  { type: "image", src: "/images/slides/mech_01/slide_45.webp" },
  { type: "image", src: "/images/slides/mech_01/slide_46.webp" },
  { type: "image", src: "/images/slides/mech_01/slide_47.webp" },
  { type: "image", src: "/images/slides/mech_01/slide_48.webp" },
  { type: "image", src: "/images/slides/mech_01/slide_49.webp" },
  { type: "image", src: "/images/slides/mech_01/slide_50.webp" },

  {
    type: "video",
    title: "📺 추천 영상: 뉴턴의 대포와 인공위성의 궤도 원리",
    src: "https://www.youtube.com/watch?v=MTjPIIIyztE"
  },
  {
    type: "quiz",
    title: "💡 개념 확인 퀴즈 4: 구심력과 반지름",
    question: "동일한 각속도 $\\omega$로 회전하는 원판 위에서 중심으로부터 회전 반지름이 2배가 되면 물체가 받는 구심력의 크기는 몇 배가 되는가?",
    answer: "2배 ($F_c = mr\\omega^2$ 이므로 각속도 $\\omega$가 일정할 때 구심력은 반지름 $r$에 직비례합니다.)"
  },

  // ====================================================
  // PART 4: 일과 역학적 에너지 보존 (Slide 51 ~ 65)
  // ====================================================
  {
    type: "section_header",
    chapter: "PART 4",
    title: "Ⅳ. 일과 역학적 에너지 보존 (Work & Conservation of Energy)",
    subtitle: "일-에너지 정리, 중력/탄성 퍼텐셜 에너지 및 역학적 에너지 보존"
  },
  { type: "image", src: "/images/slides/mech_01/slide_51.webp" },
  { type: "image", src: "/images/slides/mech_01/slide_52.webp" },
  { type: "image", src: "/images/slides/mech_01/slide_53.webp" },
  { type: "image", src: "/images/slides/mech_01/slide_54.webp" },
  { type: "image", src: "/images/slides/mech_01/slide_55.webp" },
  { type: "image", src: "/images/slides/mech_01/slide_56.webp" },
  { type: "image", src: "/images/slides/mech_01/slide_57.webp" },
  { type: "image", src: "/images/slides/mech_01/slide_58.webp" },
  { type: "image", src: "/images/slides/mech_01/slide_59.webp" },
  { type: "image", src: "/images/slides/mech_01/slide_60.webp" },
  { type: "image", src: "/images/slides/mech_01/slide_61.webp" },
  { type: "image", src: "/images/slides/mech_01/slide_62.webp" },

  {
    type: "callout",
    style: "info",
    title: "📌 수식 핵심: 퍼텐셜 에너지와 역학적 에너지",
    content: "• 일-에너지 정리: $W_{net} = \\Delta E_k = \\frac{1}{2}mv^2 - \\frac{1}{2}mv_0^2$\n• 중력 퍼텐셜 에너지: $E_p = mgh$\n• 탄성 퍼텐셜 에너지: $E_p = \\frac{1}{2}kx^2$\n• 역학적 에너지 보존: 보존력만 작용할 때 $E_{total} = E_k + E_p = \\text{일정}$"
  },
  {
    type: "simulation",
    title: "🕹️ 직접 탐구: 역학적 에너지 보존 (Energy Skate Park)",
    src: "https://phet.colorado.edu/sims/html/energy-skate-park-basics/latest/energy-skate-park-basics_all.html?locale=ko",
    height: "600"
  },

  { type: "image", src: "/images/slides/mech_01/slide_63.webp" },
  { type: "image", src: "/images/slides/mech_01/slide_64.webp" },
  { type: "image", src: "/images/slides/mech_01/slide_65.webp" },

  {
    type: "quiz",
    title: "💡 개념 확인 퀴즈 5: 탄성 퍼텐셜 에너지",
    question: "용수철 상수 $k=200\\text{N/m}$ 인 용수철을 원래 길이에서 $0.1\\text{m}$만큼 늘였을 때 저장되는 탄성 퍼텐셜 에너지는?",
    answer: "1 J ($E_p = \\frac{1}{2} k x^2 = \\frac{1}{2} \\times 200 \\times (0.1)^2 = 1\\text{J}$ 입니다.)"
  },

  // ====================================================
  // PART 5: 단진자와 단순조화 진동 (Slide 66 ~ 70)
  // ====================================================
  {
    type: "section_header",
    chapter: "PART 5",
    title: "Ⅴ. 단진자와 단순조화 진동 (Simple Pendulum & Oscillations)",
    subtitle: "복원력, 진자의 에너지 전환, 주기 공식과 진자의 등시성"
  },
  { type: "image", src: "/images/slides/mech_01/slide_66.webp" },
  { type: "image", src: "/images/slides/mech_01/slide_67.webp" },
  { type: "image", src: "/images/slides/mech_01/slide_68.webp" },
  { type: "image", src: "/images/slides/mech_01/slide_69.webp" },
  { type: "image", src: "/images/slides/mech_01/slide_70.webp" },

  {
    type: "callout",
    style: "warning",
    title: "📌 수식 핵심: 단진자의 주기 공식",
    content: "단진자의 복원력 $F = -mg\\sin\\theta \\approx -mg\\frac{x}{l}$ 에 따른 주기 공식:\n$$T = 2\\pi \\sqrt{\\frac{l}{g}}$$\n• 진자의 주기 $T$는 추의 질량이나 진폭과 무관하며 오직 길이 $l$과 중력 가속도 $g$에만 의존합니다 (진자의 등시성)."
  },
  {
    type: "simulation",
    title: "🕹️ 직접 탐구: 단진자 주기와 에너지 실험실 (Pendulum Lab)",
    src: "https://phet.colorado.edu/sims/html/pendulum-lab/latest/pendulum-lab_all.html?locale=ko",
    height: "600"
  },
  {
    type: "quiz",
    title: "💡 개념 확인 퀴즈 6: 단진자의 주기 변화",
    question: "단진자의 길이를 4배로 만들면 진동 주기는 원래의 몇 배가 되겠는가?",
    answer: "2배 ($T = 2\\pi \\sqrt{\\frac{l}{g}}$ 이므로 길이가 4배가 되면 주기는 $\\sqrt{4} = 2$배가 됩니다.)"
  },
  {
    type: "callout",
    style: "info",
    title: "🎉 [역학과 에너지] 1강 전체 학습 완료!",
    content: "축하합니다! 70장의 강의 슬라이드와 5개의 PhET 시뮬레이션을 통해 역학 전체 단원 학습을 마쳤습니다. 필요시 슬라이드를 클릭하여 확대해 보시거나 D키(판서) 기능으로 주요 수식을 직접 필기해 보세요."
  }
];
