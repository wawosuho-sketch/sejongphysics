export const lectureData = [
  {
    type: "title",
    text: "1강. 역학과 에너지 (역학 파트 전체)"
  },
  {
    type: "callout",
    style: "info",
    title: "📖 단원 학습 안내",
    content: "본 강의는 [역학과 에너지] 교과서 1강 전체 강의 슬라이드 70장과 핵심 시뮬레이션, 수식 정리, 개념 확인 퀴즈로 구성되어 있습니다."
  },

  // ====================================================
  // SECTION 1: 벡터와 힘의 평형 (Slides 1 ~ 14)
  // ====================================================
  { type: "title", text: "Ⅰ. 벡터와 힘의 평형" },
  { type: "image", src: "/images/slides/mech_01/slide_01.webp" },
  { type: "image", src: "/images/slides/mech_01/slide_02.webp" },
  { type: "image", src: "/images/slides/mech_01/slide_03.webp" },
  { type: "image", src: "/images/slides/mech_01/slide_04.webp" },
  { type: "image", src: "/images/slides/mech_01/slide_05.webp" },
  {
    type: "quiz",
    title: "💡 개념 확인 퀴즈: 스칼라 vs 벡터",
    question: "다음 중 벡터(Vector) 물리량에 해당하는 것만을 고르시오: [질량, 변위, 온도, 속도, 에너지, 힘]",
    answer: "변위, 속도, 힘 (크기와 방향을 함께 가지는 물리량이 벡터입니다.)"
  },
  {
    type: "simulation",
    title: "🕹️ 직접 해보기: 벡터의 합성과 성분 분해 (Vector Addition)",
    src: "https://phet.colorado.edu/sims/html/vector-addition/latest/vector-addition_all.html?locale=ko",
    height: "600"
  },
  { type: "image", src: "/images/slides/mech_01/slide_06.webp" },
  { type: "image", src: "/images/slides/mech_01/slide_07.webp" },
  { type: "image", src: "/images/slides/mech_01/slide_08.webp" },
  { type: "image", src: "/images/slides/mech_01/slide_09.webp" },
  { type: "image", src: "/images/slides/mech_01/slide_10.webp" },
  {
    type: "simulation",
    title: "🕹️ 직접 해보기: 빗면에서의 힘과 운동 (Forces on Incline)",
    src: "https://phet.colorado.edu/sims/html/forces-and-motion-basics/latest/forces-and-motion-basics_all.html?locale=ko",
    height: "600"
  },
  { type: "image", src: "/images/slides/mech_01/slide_11.webp" },
  { type: "image", src: "/images/slides/mech_01/slide_12.webp" },
  { type: "image", src: "/images/slides/mech_01/slide_13.webp" },
  { type: "image", src: "/images/slides/mech_01/slide_14.webp" },
  {
    type: "quiz",
    title: "💡 개념 확인 퀴즈: 빗면에서의 정지 마찰력",
    question: "경사각 $\\theta=30^\\circ$인 빗면에 질량 $2\\text{kg}$인 물체가 정지해 있을 때 정지 마찰력의 크기는? ($g=10\\text{m/s}^2$, $\\sin 30^\\circ=0.5$)",
    answer: "10 N (빗면 내림 방향 성력 $mg\\sin 30^\\circ = 2 \\times 10 \\times 0.5 = 10\\text{N}$ 이므로 정지 마찰력도 10N입니다.)"
  },

  // ====================================================
  // SECTION 2: 평면 운동과 포물선 운동 (Slides 15 ~ 38)
  // ====================================================
  { type: "title", text: "Ⅱ. 평면 운동과 포물선 운동" },
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
    type: "simulation",
    title: "🕹️ 직접 해보기: 포물선 운동 각도 및 발사 실험 (Projectile Motion)",
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
    title: "💡 개념 확인 퀴즈: 포물선 최고점에서의 속력",
    question: "지면과 $60^\\circ$의 각도로 $20\\text{m/s}$로 발사된 물체의 최고점에서의 속력은?",
    answer: "10 m/s (최고점에서는 연직 속도 $v_y=0$이며 수평 속도 $v_x = 20\\cos 60^\\circ = 10\\text{m/s}$ 만 남습니다.)"
  },

  // ====================================================
  // SECTION 3: 등속 원운동과 위성의 운동 (Slides 39 ~ 50)
  // ====================================================
  { type: "title", text: "Ⅲ. 등속 원운동과 위성의 운동" },
  { type: "image", src: "/images/slides/mech_01/slide_39.webp" },
  { type: "image", src: "/images/slides/mech_01/slide_40.webp" },
  { type: "image", src: "/images/slides/mech_01/slide_41.webp" },
  { type: "image", src: "/images/slides/mech_01/slide_42.webp" },
  { type: "image", src: "/images/slides/mech_01/slide_43.webp" },
  { type: "image", src: "/images/slides/mech_01/slide_44.webp" },
  {
    type: "simulation",
    title: "🕹️ 직접 해보기: 중력과 위성 궤도 시뮬레이션 (Gravity & Orbits)",
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
    title: "💡 개념 확인 퀴즈: 구심력과 회전 반지름",
    question: "동일한 각속도 $\\omega$로 회전할 때 회전 반지름이 2배가 되면 구심력의 크기는 몇 배가 되는가?",
    answer: "2배 ($F_c = mr\\omega^2$ 이므로 각속도가 일정할 때 구심력은 반지름에 비례합니다.)"
  },

  // ====================================================
  // SECTION 4: 일과 역학적 에너지 보존 (Slides 51 ~ 65)
  // ====================================================
  { type: "title", text: "Ⅳ. 일과 역학적 에너지 보존" },
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
    type: "simulation",
    title: "🕹️ 직접 해보기: 역학적 에너지 보존 (Energy Skate Park)",
    src: "https://phet.colorado.edu/sims/html/energy-skate-park-basics/latest/energy-skate-park-basics_all.html?locale=ko",
    height: "600"
  },
  { type: "image", src: "/images/slides/mech_01/slide_63.webp" },
  { type: "image", src: "/images/slides/mech_01/slide_64.webp" },
  { type: "image", src: "/images/slides/mech_01/slide_65.webp" },
  {
    type: "quiz",
    title: "💡 개념 확인 퀴즈: 탄성 퍼텐셜 에너지",
    question: "용수철 상수 $k=200\\text{N/m}$ 인 용수철을 $0.1\\text{m}$ 변형시켰을 때 탄성 퍼텐셜 에너지는?",
    answer: "1 J ($E_p = \\frac{1}{2} k x^2 = \\frac{1}{2} \\times 200 \\times (0.1)^2 = 1\\text{J}$)"
  },

  // ====================================================
  // SECTION 5: 단진자와 단순조화 진동 (Slides 66 ~ 70)
  // ====================================================
  { type: "title", text: "Ⅴ. 단진자와 단순조화 진동" },
  { type: "image", src: "/images/slides/mech_01/slide_66.webp" },
  { type: "image", src: "/images/slides/mech_01/slide_67.webp" },
  { type: "image", src: "/images/slides/mech_01/slide_68.webp" },
  { type: "image", src: "/images/slides/mech_01/slide_69.webp" },
  { type: "image", src: "/images/slides/mech_01/slide_70.webp" },
  {
    type: "simulation",
    title: "🕹️ 직접 해보기: 단진자 주기와 에너지 시뮬레이션 (Pendulum Lab)",
    src: "https://phet.colorado.edu/sims/html/pendulum-lab/latest/pendulum-lab_all.html?locale=ko",
    height: "600"
  },
  {
    type: "quiz",
    title: "💡 개념 확인 퀴즈: 단진자의 주기 공식",
    question: "단진자의 길이를 4배로 만들면 진동 주기는 몇 배가 되는가?",
    answer: "2배 ($T = 2\\pi \\sqrt{\\frac{l}{g}}$ 이므로 길이 $l$이 4배가 되면 주기는 $\\sqrt{4}=2$배가 됩니다.)"
  },
  {
    type: "callout",
    style: "info",
    title: "🎉 1강 전체 과정 완강!",
    content: "수고하셨습니다! [역학과 에너지] 1강 슬라이드 70장과 핵심 시뮬레이션을 모두 학습하셨습니다. 화면 하단의 탐색바나 판서(D키)를 사용하여 복습해보세요."
  }
];
