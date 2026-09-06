export const lectureData = [
  {
    type: "title",
    text: "2강. 특수상대성이론 (Special Relativity)"
  },
  {
    type: "callout",
    style: "info",
    title: "📖 학습 안내: 특수상대성이론 전체 단원",
    content: "본 강의는 110장의 강의 슬라이드와 **자바실험실 시뮬레이션**, **KaTeX 수식 정리**, **개념 확인 퀴즈**를 결합한 특수상대성이론 통합 강의 자료입니다."
  },

  // ====================================================
  // PART 1: 상대성 원리의 보편성과 갈릴레이 상대성 (Slide 01 ~ 20)
  // ====================================================
  {
    type: "section_header",
    chapter: "PART 1",
    title: "Ⅰ. 상대성 원리의 보편성과 갈릴레이 상대성",
    subtitle: "유소년/청년기 아인슈타인의 사고, 갈릴레이 상대성 원리와 등속 관성계"
  },
  { type: "image", src: "/images/slides/mech_02/slide_01.webp" },
  { type: "image", src: "/images/slides/mech_02/slide_02.webp" },
  { type: "image", src: "/images/slides/mech_02/slide_03.webp" },
  { type: "image", src: "/images/slides/mech_02/slide_04.webp" },
  { type: "image", src: "/images/slides/mech_02/slide_05.webp" },
  { type: "image", src: "/images/slides/mech_02/slide_06.webp" },
  { type: "image", src: "/images/slides/mech_02/slide_07.webp" },
  { type: "image", src: "/images/slides/mech_02/slide_08.webp" },
  { type: "image", src: "/images/slides/mech_02/slide_09.webp" },
  { type: "image", src: "/images/slides/mech_02/slide_10.webp" },
  { type: "image", src: "/images/slides/mech_02/slide_11.webp" },
  { type: "image", src: "/images/slides/mech_02/slide_12.webp" },
  { type: "image", src: "/images/slides/mech_02/slide_13.webp" },
  { type: "image", src: "/images/slides/mech_02/slide_14.webp" },
  { type: "image", src: "/images/slides/mech_02/slide_15.webp" },
  { type: "image", src: "/images/slides/mech_02/slide_16.webp" },
  { type: "image", src: "/images/slides/mech_02/slide_17.webp" },
  { type: "image", src: "/images/slides/mech_02/slide_18.webp" },
  { type: "image", src: "/images/slides/mech_02/slide_19.webp" },
  { type: "image", src: "/images/slides/mech_02/slide_20.webp" },

  {
    type: "callout",
    style: "info",
    title: "📌 수식 핵심: 갈릴레이 상대성 원리",
    content: "• 등속도로 운동하는 모든 관성계에서 역학의 운동 법칙은 동일하게 성립합니다.\n• 갈릴레이 변환: $x' = x - vt, \\quad y' = y, \\quad z' = z, \\quad t' = t$\n• 고전역학에서는 시간 $t$가 모든 관찰자에게 동일한 절대적 시간으로 다루어집니다."
  },
  {
    type: "quiz",
    title: "💡 개념 확인 퀴즈 1: 갈릴레이 상대성 원리",
    question: "일정한 속도 $v$로 달리는 기차 내부에서 공을 위로 똑바로 던져 올렸을 때, 기차 안 관찰자와 지상 정지 관찰자가 보는 공의 운동 궤적은 각각 무엇인가?",
    answer: "기차 안 관찰자는 직선 연직 상하 운동으로 보고, 지상 정지 관찰자는 포물선 운동으로 관측합니다. 그러나 두 관찰자 모두 뉴턴의 운동 법칙($F=ma$)을 동일하게 적용할 수 있습니다."
  },

  // ====================================================
  // PART 2: 마이컬슨-몰리 실험과 특수상대성이론의 가설 (Slide 21 ~ 38)
  // ====================================================
  {
    type: "section_header",
    chapter: "PART 2",
    title: "Ⅱ. 마이컬슨-몰리 실험과 특수상대성이론의 가설",
    subtitle: "빛의 매질(에테르) 검증 실패, 광속 불변의 원리와 2대 가설"
  },
  { type: "image", src: "/images/slides/mech_02/slide_21.webp" },
  { type: "image", src: "/images/slides/mech_02/slide_22.webp" },
  { type: "image", src: "/images/slides/mech_02/slide_23.webp" },
  { type: "image", src: "/images/slides/mech_02/slide_24.webp" },
  { type: "image", src: "/images/slides/mech_02/slide_25.webp" },
  { type: "image", src: "/images/slides/mech_02/slide_26.webp" },
  { type: "image", src: "/images/slides/mech_02/slide_27.webp" },
  { type: "image", src: "/images/slides/mech_02/slide_28.webp" },
  { type: "image", src: "/images/slides/mech_02/slide_29.webp" },
  { type: "image", src: "/images/slides/mech_02/slide_30.webp" },
  { type: "image", src: "/images/slides/mech_02/slide_31.webp" },
  { type: "image", src: "/images/slides/mech_02/slide_32.webp" },
  { type: "image", src: "/images/slides/mech_02/slide_33.webp" },
  { type: "image", src: "/images/slides/mech_02/slide_34.webp" },
  { type: "image", src: "/images/slides/mech_02/slide_35.webp" },
  { type: "image", src: "/images/slides/mech_02/slide_36.webp" },
  { type: "image", src: "/images/slides/mech_02/slide_37.webp" },
  {
    type: "simulation",
    title: "🕹️ 직접 탐구: 동시성의 상대성 시뮬레이션 (자바실험실)",
    src: "https://javalab.org/ko/relativity_of_simultaneity/",
    height: "650"
  },
  { type: "image", src: "/images/slides/mech_02/slide_38.webp" },

  {
    type: "callout",
    style: "warning",
    title: "📌 수식 핵심: 특수상대성이론의 2대 기본 가설",
    content: "1) 상대성 원리: 모든 관성계에서 물리 법칙은 동일한 형태로 적용된다.\n2) 광속 불변 원리: 진공에서의 빛의 속도 $c$는 관찰자나 광원의 운동 상태와 무관하게 항상 일정하다 ($c \\approx 3 \\times 10^8 \\text{m/s}$)."
  },
  {
    type: "quiz",
    title: "💡 개념 확인 퀴즈 2: 광속 불변의 원리",
    question: "속력 $0.8c$로 우주 공간을 날아가는 우주선에서 전방으로 레이저 빛을 발사했습니다. 우주선 안의 조종사와 지구에 있는 정지 관찰자가 측정한 레이저 빛의 속력은 각각 얼마입니까?",
    answer: "두 관찰자 모두 빛의 속력을 $c$ (약 $3 \\times 10^8\\text{m/s}$)로 정밀하게 측정합니다 (광속 불변 원리)."
  },

  // ====================================================
  // PART 3: 동시성의 상대성과 시간 지연, 길이 수축 (Slide 39 ~ 65)
  // ====================================================
  {
    type: "section_header",
    chapter: "PART 3",
    title: "Ⅲ. 동시성의 상대성과 시간 지연, 길이 수축",
    subtitle: "빛시계 모델, 상대론적 시간팽창과 길이수축, 뮤온의 수명 실험"
  },
  { type: "image", src: "/images/slides/mech_02/slide_39.webp" },
  { type: "image", src: "/images/slides/mech_02/slide_40.webp" },
  { type: "image", src: "/images/slides/mech_02/slide_41.webp" },
  { type: "image", src: "/images/slides/mech_02/slide_42.webp" },
  { type: "image", src: "/images/slides/mech_02/slide_43.webp" },
  { type: "image", src: "/images/slides/mech_02/slide_44.webp" },
  {
    type: "simulation",
    title: "🕹️ 직접 탐구: 특수상대성이론 시뮬레이션 (자바실험실)",
    src: "https://javalab.org/ko/special_relativity/",
    height: "650"
  },
  { type: "image", src: "/images/slides/mech_02/slide_45.webp" },
  { type: "image", src: "/images/slides/mech_02/slide_46.webp" },
  { type: "image", src: "/images/slides/mech_02/slide_47.webp" },
  { type: "image", src: "/images/slides/mech_02/slide_48.webp" },
  { type: "image", src: "/images/slides/mech_02/slide_49.webp" },
  { type: "image", src: "/images/slides/mech_02/slide_50.webp" },
  { type: "image", src: "/images/slides/mech_02/slide_51.webp" },
  { type: "image", src: "/images/slides/mech_02/slide_52.webp" },
  { type: "image", src: "/images/slides/mech_02/slide_53.webp" },
  { type: "image", src: "/images/slides/mech_02/slide_54.webp" },
  {
    type: "simulation",
    title: "🕹️ 직접 탐구: 특수상대성이론 2 시뮬레이션 (자바실험실)",
    src: "https://javalab.org/ko/special_relativity_2/",
    height: "650"
  },
  { type: "image", src: "/images/slides/mech_02/slide_55.webp" },
  { type: "image", src: "/images/slides/mech_02/slide_56.webp" },
  { type: "image", src: "/images/slides/mech_02/slide_57.webp" },
  { type: "image", src: "/images/slides/mech_02/slide_58.webp" },
  { type: "image", src: "/images/slides/mech_02/slide_59.webp" },
  { type: "image", src: "/images/slides/mech_02/slide_60.webp" },
  { type: "image", src: "/images/slides/mech_02/slide_61.webp" },
  { type: "image", src: "/images/slides/mech_02/slide_62.webp" },
  { type: "image", src: "/images/slides/mech_02/slide_63.webp" },
  { type: "image", src: "/images/slides/mech_02/slide_64.webp" },
  { type: "image", src: "/images/slides/mech_02/slide_65.webp" },

  {
    type: "callout",
    style: "info",
    title: "📌 수식 핵심: 시간 지연과 길이 수축 공식",
    content: "로런츠 인자 $\\gamma = \\frac{1}{\\sqrt{1 - v^2/c^2}} \\ge 1$ 에 대하여:\n• 시간 지연 (Time Dilation): $t = \\gamma t_0 = \\frac{t_0}{\\sqrt{1 - v^2/c^2}}$ (운동하는 계의 시계가 천천히 흘러감)\n• 길이 수축 (Length Contraction): $L = \\frac{L_0}{\\gamma} = L_0 \\sqrt{1 - v^2/c^2}$ (운동 방향으로 고유 길이 $L_0$가 줄어듦)\n• 고유 시간 $t_0$ 및 고유 길이 $L_0$는 관찰 대상에 대해 정지한 좌표계에서 측정한 값입니다."
  },
  {
    type: "quiz",
    title: "💡 개념 확인 퀴즈 3: 뮤온(Muon)의 지표면 도달 원리",
    question: "대기 상층에서 생성된 뮤온의 고유 수명은 $2.2\\mu\\text{s}$에 불과하여 원래는 지표면에 도달할 수 없습니다. 1) 지상 관찰자 관점과 2) 뮤온 관점 각각에서 지표면 도달 현상을 설명하시오.",
    answer: "1) 지상 관찰자 관점: 고속($v \\approx 0.998c$)으로 이동하는 뮤온의 시간이 지연($t = \\gamma t_0$)되어 수명이 크게 늘어납니다.\n2) 뮤온 관점: 뮤온과 함께 이동하는 좌표계에서는 대기의 두께(지표면까지의 거리)가 길이 수축($L = L_0/\\gamma$)되어 짧은 시간 안에 지표면에 다다릅니다."
  },

  // ====================================================
  // PART 4: 상대론적 역설 - 쌍둥이 역설 & 헛간 역설 (Slide 66 ~ 95)
  // ====================================================
  {
    type: "section_header",
    chapter: "PART 4",
    title: "Ⅳ. 상대론적 역설 - 쌍둥이 역설과 헛간 역설",
    subtitle: "상대론적 도플러 효과, 3관찰자 교대 모델, 동시성의 상대성과 헛간 역설"
  },
  { type: "image", src: "/images/slides/mech_02/slide_66.webp" },
  { type: "image", src: "/images/slides/mech_02/slide_67.webp" },
  { type: "image", src: "/images/slides/mech_02/slide_68.webp" },
  { type: "image", src: "/images/slides/mech_02/slide_69.webp" },
  {
    type: "simulation",
    title: "🕹️ 직접 탐구: 시공간 그래프 시뮬레이션 (자바실험실)",
    src: "https://javalab.org/ko/spacetime/",
    height: "650"
  },
  { type: "image", src: "/images/slides/mech_02/slide_70.webp" },
  { type: "image", src: "/images/slides/mech_02/slide_71.webp" },
  { type: "image", src: "/images/slides/mech_02/slide_72.webp" },
  { type: "image", src: "/images/slides/mech_02/slide_73.webp" },
  { type: "image", src: "/images/slides/mech_02/slide_74.webp" },
  {
    type: "simulation",
    title: "🕹️ 직접 탐구: 쌍둥이 역설 시뮬레이션 (자바실험실)",
    src: "https://javalab.org/ko/twin_paradox/",
    height: "650"
  },
  { type: "image", src: "/images/slides/mech_02/slide_75.webp" },
  { type: "image", src: "/images/slides/mech_02/slide_76.webp" },
  { type: "image", src: "/images/slides/mech_02/slide_77.webp" },
  { type: "image", src: "/images/slides/mech_02/slide_78.webp" },
  { type: "image", src: "/images/slides/mech_02/slide_79.webp" },
  { type: "image", src: "/images/slides/mech_02/slide_80.webp" },
  { type: "image", src: "/images/slides/mech_02/slide_81.webp" },
  { type: "image", src: "/images/slides/mech_02/slide_82.webp" },
  { type: "image", src: "/images/slides/mech_02/slide_83.webp" },
  { type: "image", src: "/images/slides/mech_02/slide_84.webp" },
  { type: "image", src: "/images/slides/mech_02/slide_85.webp" },
  { type: "image", src: "/images/slides/mech_02/slide_86.webp" },
  { type: "image", src: "/images/slides/mech_02/slide_87.webp" },
  { type: "image", src: "/images/slides/mech_02/slide_88.webp" },
  { type: "image", src: "/images/slides/mech_02/slide_89.webp" },
  { type: "image", src: "/images/slides/mech_02/slide_90.webp" },
  { type: "image", src: "/images/slides/mech_02/slide_91.webp" },
  { type: "image", src: "/images/slides/mech_02/slide_92.webp" },
  { type: "image", src: "/images/slides/mech_02/slide_93.webp" },
  { type: "image", src: "/images/slides/mech_02/slide_94.webp" },
  { type: "image", src: "/images/slides/mech_02/slide_95.webp" },

  {
    type: "callout",
    style: "warning",
    title: "📌 수식 핵심: 도플러 효과와 상대론적 비대칭성",
    content: "상대론적 도플러 효과 (Relativistic Doppler Effect):\n• 멀어질 때 진동수/배속: $f_{rec} = f_0 \\sqrt{\\frac{1 - v/c}{1 + v/c}}$ ($v=0.6c$일 때 $0.5$배속)\n• 다가올 때 진동수/배속: $f_{rec} = f_0 \\sqrt{\\frac{1 + v/c}{1 - v/c}}$ ($v=0.6c$일 때 $2.0$배속)\n• 쌍둥이 역설에서 지구 관찰자와 우주선 관찰자는 관성계 변경(프레임 교대) 유무로 인해 영상 시청 총시간 및 비율의 명확한 비대칭성이 발생합니다."
  },
  {
    type: "quiz",
    title: "💡 개념 확인 퀴즈 4: 헛간과 막대의 역설",
    question: "고유 길이가 $10\\text{m}$인 헛간에 고유 길이 $10\\text{m}$인 막대가 고속($0.866c$, 길이 50% 수축)으로 통과합니다. 헛간 기준에서는 막대가 헛간 안으로 완전히 들어와 앞뒤 문을 동시에 닫을 수 있지만, 막대 기준에서는 일어날 수 없는 이유는?",
    answer: "동시성의 상대성 때문입니다. 헛간 관성계에서 '동시에' 일어난 문 닫힘 사건이, 이동하는 막대 관성계에서는 동시에 일어나지 않고 앞문과 뒷문이 시차를 두고 닫히기 때문입니다."
  },

  // ====================================================
  // PART 5: 질량-에너지 동등성 및 핵반응 ($E=mc^2$) (Slide 96 ~ 110)
  // ====================================================
  {
    type: "section_header",
    chapter: "PART 5",
    title: "Ⅴ. 질량-에너지 동등성과 핵반응 ($E=mc^2$)",
    subtitle: "상대론적 운동량, 질량 결손(Mass Defect), 핵분열과 핵융합 에너지"
  },
  { type: "image", src: "/images/slides/mech_02/slide_96.webp" },
  { type: "image", src: "/images/slides/mech_02/slide_97.webp" },
  { type: "image", src: "/images/slides/mech_02/slide_98.webp" },
  { type: "image", src: "/images/slides/mech_02/slide_99.webp" },
  { type: "image", src: "/images/slides/mech_02/slide_100.webp" },
  { type: "image", src: "/images/slides/mech_02/slide_101.webp" },
  { type: "image", src: "/images/slides/mech_02/slide_102.webp" },
  { type: "image", src: "/images/slides/mech_02/slide_103.webp" },
  { type: "image", src: "/images/slides/mech_02/slide_104.webp" },
  { type: "image", src: "/images/slides/mech_02/slide_105.webp" },
  { type: "image", src: "/images/slides/mech_02/slide_106.webp" },
  { type: "image", src: "/images/slides/mech_02/slide_107.webp" },
  { type: "image", src: "/images/slides/mech_02/slide_108.webp" },
  { type: "image", src: "/images/slides/mech_02/slide_109.webp" },
  { type: "image", src: "/images/slides/mech_02/slide_110.webp" },

  {
    type: "callout",
    style: "info",
    title: "📌 수식 핵심: 질량-에너지 동등성과 핵결합 에너지",
    content: "• 질량-에너지 동등성: $E = m c^2$\n• 상대론적 전체 에너지: $E = \\gamma m_0 c^2 = E_k + m_0 c^2$\n• 질량 결손 및 방출 에너지: $\\Delta E = \\Delta m c^2 = (m_{\\text{반응 전}} - m_{\\text{반응 후}}) c^2$\n• 핵반응에서 반응 전후 질량수(핵자 수)는 보존되지만, 핵자당 결합 에너지 차이에 따라 질량이 감소하며($\\Delta m > 0$) 그만큼 막대한 에너지로 변환됩니다."
  },
  {
    type: "quiz",
    title: "💡 개념 확인 퀴즈 5: 질량 결손과 방출 에너지 계산",
    question: "어떤 핵융합 반응에서 발생한 질량 결손이 $\\Delta m = 1\\text{mg} = 10^{-6}\\text{kg}$ 이었습니다. 이 반응으로 생성되는 에너지 $\\Delta E$는 몇 J(줄)입니까? (단, $c = 3 \\times 10^8\\text{m/s}$)",
    answer: "$9 \\times 10^{10} \\text{J} \\quad (\\Delta E = \\Delta m c^2 = 10^{-6} \\times (3 \\times 10^8)^2 = 9 \\times 10^{10} \\text{J}$ 입니다.)"
  },
  {
    type: "callout",
    style: "info",
    title: "🎉 [역학과 에너지] 2강 특수상대성이론 전체 학습 완료!",
    content: "수고하셨습니다! 110장의 슬라이드와 자바실험실 시뮬레이션, KaTeX 수식 정리를 통해 특수상대성이론 단원을 완벽하게 이수하셨습니다."
  }
];
