export const lectureData = [
  {
    type: "title",
    text: "3강. 일반상대성이론 (General Relativity)"
  },
  {
    type: "callout",
    style: "info",
    title: "📖 학습 안내: 일반상대성이론 전체 단원",
    content: "본 강의는 125장의 강의 슬라이드와 **자바실험실 중력렌즈 시뮬레이션**, **KaTeX 수식 정리**, **개념 확인 퀴즈**를 결합한 일반상대성이론 통합 강의 자료입니다."
  },

  // ====================================================
  // PART 1: 면적속도 일정의 법칙과 뉴턴 중력 역학 (Slide 01 ~ 30)
  // ====================================================
  {
    type: "section_header",
    chapter: "PART 1",
    title: "Ⅰ. 면적속도 일정의 법칙과 뉴턴 중력 역학",
    subtitle: "케플러 제2법칙 증명, 토크의 소멸과 각운동량 보존 법칙"
  },
  { type: "image", src: "/images/slides/mech_03/slide_01.webp" },
  { type: "image", src: "/images/slides/mech_03/slide_02.webp" },
  { type: "image", src: "/images/slides/mech_03/slide_03.webp" },
  { type: "image", src: "/images/slides/mech_03/slide_04.webp" },
  { type: "image", src: "/images/slides/mech_03/slide_05.webp" },
  { type: "image", src: "/images/slides/mech_03/slide_06.webp" },
  { type: "image", src: "/images/slides/mech_03/slide_07.webp" },
  { type: "image", src: "/images/slides/mech_03/slide_08.webp" },
  { type: "image", src: "/images/slides/mech_03/slide_09.webp" },
  { type: "image", src: "/images/slides/mech_03/slide_10.webp" },
  { type: "image", src: "/images/slides/mech_03/slide_11.webp" },
  { type: "image", src: "/images/slides/mech_03/slide_12.webp" },
  { type: "image", src: "/images/slides/mech_03/slide_13.webp" },
  { type: "image", src: "/images/slides/mech_03/slide_14.webp" },
  { type: "image", src: "/images/slides/mech_03/slide_15.webp" },
  { type: "image", src: "/images/slides/mech_03/slide_16.webp" },
  { type: "image", src: "/images/slides/mech_03/slide_17.webp" },
  { type: "image", src: "/images/slides/mech_03/slide_18.webp" },
  { type: "image", src: "/images/slides/mech_03/slide_19.webp" },
  { type: "image", src: "/images/slides/mech_03/slide_20.webp" },
  { type: "image", src: "/images/slides/mech_03/slide_21.webp" },
  { type: "image", src: "/images/slides/mech_03/slide_22.webp" },
  { type: "image", src: "/images/slides/mech_03/slide_23.webp" },
  { type: "image", src: "/images/slides/mech_03/slide_24.webp" },
  { type: "image", src: "/images/slides/mech_03/slide_25.webp" },
  { type: "image", src: "/images/slides/mech_03/slide_26.webp" },
  { type: "image", src: "/images/slides/mech_03/slide_27.webp" },
  { type: "image", src: "/images/slides/mech_03/slide_28.webp" },
  { type: "image", src: "/images/slides/mech_03/slide_29.webp" },
  { type: "image", src: "/images/slides/mech_03/slide_30.webp" },

  {
    type: "callout",
    style: "info",
    title: "📌 수식 핵심: 면적속도와 각운동량 보존",
    content: "• 중심력(Central Force): 중력 작용선이 항상 중심을 지나므로 외부 토크 $\\vec{\\tau} = \\vec{r} \\times \\vec{F} = 0$\n• 각운동량 보존: $\\vec{L} = m (\\vec{r} \\times \\vec{v}) = \\text{일정}$\n• 면적속도(Areal Velocity): $\\frac{dA}{dt} = \\frac{1}{2} r v \\sin\\theta = \\frac{L}{2m} = \\text{일정}$ (케플러 제2법칙의 물리적 근거)"
  },
  {
    type: "quiz",
    title: "💡 개념 확인 퀴즈 1: 케플러 제2법칙과 공전 속도",
    question: "행성이 타원 궤도를 따라 공전할 때, 태양에 가장 가까운 근일점에서의 거리와 속력을 $r_1, v_1$, 가장 먼 원일점에서의 거리와 속력을 $r_2, v_2$라고 할 때 관계식은?",
    answer: "각운동량 보존 법칙에 의해 $r_1 v_1 = r_2 v_2$ 가 성립합니다. 따라서 태양에 가까울수록 공전 속도가 빨라집니다."
  },

  // ====================================================
  // PART 2: 원뿔곡선과 역학적 에너지 궤도 (Slide 31 ~ 60)
  // ====================================================
  {
    type: "section_header",
    chapter: "PART 2",
    title: "Ⅱ. 원뿔곡선과 역학적 에너지 궤도",
    subtitle: "이심률(e)과 궤도 방정식, 총 역학적 에너지(E)에 따른 궤도의 기하학적 형태"
  },
  { type: "image", src: "/images/slides/mech_03/slide_31.webp" },
  { type: "image", src: "/images/slides/mech_03/slide_32.webp" },
  { type: "image", src: "/images/slides/mech_03/slide_33.webp" },
  { type: "image", src: "/images/slides/mech_03/slide_34.webp" },
  { type: "image", src: "/images/slides/mech_03/slide_35.webp" },
  { type: "image", src: "/images/slides/mech_03/slide_36.webp" },
  { type: "image", src: "/images/slides/mech_03/slide_37.webp" },
  { type: "image", src: "/images/slides/mech_03/slide_38.webp" },
  { type: "image", src: "/images/slides/mech_03/slide_39.webp" },
  { type: "image", src: "/images/slides/mech_03/slide_40.webp" },
  { type: "image", src: "/images/slides/mech_03/slide_41.webp" },
  { type: "image", src: "/images/slides/mech_03/slide_42.webp" },
  { type: "image", src: "/images/slides/mech_03/slide_43.webp" },
  { type: "image", src: "/images/slides/mech_03/slide_44.webp" },
  { type: "image", src: "/images/slides/mech_03/slide_45.webp" },
  { type: "image", src: "/images/slides/mech_03/slide_46.webp" },
  { type: "image", src: "/images/slides/mech_03/slide_47.webp" },
  { type: "image", src: "/images/slides/mech_03/slide_48.webp" },
  { type: "image", src: "/images/slides/mech_03/slide_49.webp" },
  { type: "image", src: "/images/slides/mech_03/slide_50.webp" },
  { type: "image", src: "/images/slides/mech_03/slide_51.webp" },
  { type: "image", src: "/images/slides/mech_03/slide_52.webp" },
  { type: "image", src: "/images/slides/mech_03/slide_53.webp" },
  { type: "image", src: "/images/slides/mech_03/slide_54.webp" },
  { type: "image", src: "/images/slides/mech_03/slide_55.webp" },
  { type: "image", src: "/images/slides/mech_03/slide_56.webp" },
  { type: "image", src: "/images/slides/mech_03/slide_57.webp" },
  { type: "image", src: "/images/slides/mech_03/slide_58.webp" },
  { type: "image", src: "/images/slides/mech_03/slide_59.webp" },
  { type: "image", src: "/images/slides/mech_03/slide_60.webp" },

  {
    type: "callout",
    style: "warning",
    title: "📌 수식 핵심: 이심률과 역학적 에너지 관계",
    content: "원뿔곡선 궤도 방정식 $r(\\theta) = \\frac{p}{1 + e \\cos\\theta}$ 에 대하여:\n• 이심률 $e = \\sqrt{1 + \\frac{2 E L^2}{m k^2}}$\n• $E < 0 \\implies e < 1$: 타원(속박 궤도, 행성 및 위성)\n• $E = 0 \\implies e = 1$: 포물선(탈출 경계 궤도)\n• $E > 0 \\implies e > 1$: 쌍곡선(이탈 궤도, 비주기 혜성)"
  },
  {
    type: "quiz",
    title: "💡 개념 확인 퀴즈 2: 궤도의 종류 결정",
    question: "우주선이 행성 중력장에서 총 역학적 에너지 $E < 0$ 인 상태를 유지하고 있다면, 이 우주선의 궤도는 어떤 모양을 취하게 됩니까?",
    answer: "총 역학적 에너지가 음수($E<0$)이면 중력에 완전히 속박된 상태이므로 타원(또는 원) 궤도를 그리며 주기적으로 공전하게 됩니다."
  },

  // ====================================================
  // PART 3: 비관성계와 등가 원리 (Slide 61 ~ 90)
  // ====================================================
  {
    type: "section_header",
    chapter: "PART 3",
    title: "Ⅲ. 비관성계와 등가 원리",
    subtitle: "가속 관성계, 관성력, 아인슈타인의 등가 원리와 무중력 체감"
  },
  { type: "image", src: "/images/slides/mech_03/slide_61.webp" },
  { type: "image", src: "/images/slides/mech_03/slide_62.webp" },
  { type: "image", src: "/images/slides/mech_03/slide_63.webp" },
  { type: "image", src: "/images/slides/mech_03/slide_64.webp" },
  { type: "image", src: "/images/slides/mech_03/slide_65.webp" },
  { type: "image", src: "/images/slides/mech_03/slide_66.webp" },
  { type: "image", src: "/images/slides/mech_03/slide_67.webp" },
  { type: "image", src: "/images/slides/mech_03/slide_68.webp" },
  { type: "image", src: "/images/slides/mech_03/slide_69.webp" },
  { type: "image", src: "/images/slides/mech_03/slide_70.webp" },
  { type: "image", src: "/images/slides/mech_03/slide_71.webp" },
  { type: "image", src: "/images/slides/mech_03/slide_72.webp" },
  { type: "image", src: "/images/slides/mech_03/slide_73.webp" },
  { type: "image", src: "/images/slides/mech_03/slide_74.webp" },
  { type: "image", src: "/images/slides/mech_03/slide_75.webp" },
  { type: "image", src: "/images/slides/mech_03/slide_76.webp" },
  { type: "image", src: "/images/slides/mech_03/slide_77.webp" },
  { type: "image", src: "/images/slides/mech_03/slide_78.webp" },
  { type: "image", src: "/images/slides/mech_03/slide_79.webp" },
  { type: "image", src: "/images/slides/mech_03/slide_80.webp" },
  { type: "image", src: "/images/slides/mech_03/slide_81.webp" },
  { type: "image", src: "/images/slides/mech_03/slide_82.webp" },
  { type: "image", src: "/images/slides/mech_03/slide_83.webp" },
  { type: "image", src: "/images/slides/mech_03/slide_84.webp" },
  { type: "image", src: "/images/slides/mech_03/slide_85.webp" },
  { type: "image", src: "/images/slides/mech_03/slide_86.webp" },
  { type: "image", src: "/images/slides/mech_03/slide_87.webp" },
  { type: "image", src: "/images/slides/mech_03/slide_88.webp" },
  { type: "image", src: "/images/slides/mech_03/slide_89.webp" },
  { type: "image", src: "/images/slides/mech_03/slide_90.webp" },

  {
    type: "callout",
    style: "info",
    title: "📌 수식 핵심: 아인슈타인의 등가 원리",
    content: "• 관성 질량($m_i$)과 중력 질량($m_g$)은 엄밀히 동일합니다 ($m_i = m_g$).\n• 등가 원리: 균일한 중력장 내의 정지 좌표계에서 느끼는 물리적 효과는, 중력이 없는 우주 공간에서 가속도 $\\vec{a} = -\\vec{g}$ 로 가속되는 계의 효과와 물리적으로 완벽히 구별 불가능합니다."
  },
  {
    type: "quiz",
    title: "💡 개념 확인 퀴즈 3: 자유낙하와 무중력",
    question: "줄이 끊어져 아래로 자유낙하하는 엘리베이터 안의 관찰자가 손에서 사과를 놓았을 때, 관찰자의 눈에는 사과가 어떻게 보입니까?",
    answer: "엘리베이터와 사과가 동일한 중력가속도 $g$로 자유낙하하므로, 내부 관찰자의 눈에는 사과가 공중에 둥둥 떠 있는 무중력 상태로 관측됩니다."
  },

  // ====================================================
  // PART 4: 시공간의 휘어짐과 중력 렌즈 (Slide 91 ~ 115)
  // ====================================================
  {
    type: "section_header",
    chapter: "PART 4",
    title: "Ⅳ. 시공간의 휘어짐과 중력 렌즈",
    subtitle: "질량에 의한 시공간 곡률, 빛의 휘어짐, 수성 세차운동과 중력렌즈 현상"
  },
  { type: "image", src: "/images/slides/mech_03/slide_91.webp" },
  { type: "image", src: "/images/slides/mech_03/slide_92.webp" },
  { type: "image", src: "/images/slides/mech_03/slide_93.webp" },
  { type: "image", src: "/images/slides/mech_03/slide_94.webp" },
  { type: "image", src: "/images/slides/mech_03/slide_95.webp" },
  { type: "image", src: "/images/slides/mech_03/slide_96.webp" },
  { type: "image", src: "/images/slides/mech_03/slide_97.webp" },
  { type: "image", src: "/images/slides/mech_03/slide_98.webp" },
  { type: "image", src: "/images/slides/mech_03/slide_99.webp" },
  { type: "image", src: "/images/slides/mech_03/slide_100.webp" },
  { type: "image", src: "/images/slides/mech_03/slide_101.webp" },
  { type: "image", src: "/images/slides/mech_03/slide_102.webp" },
  { type: "image", src: "/images/slides/mech_03/slide_103.webp" },
  { type: "image", src: "/images/slides/mech_03/slide_104.webp" },
  { type: "image", src: "/images/slides/mech_03/slide_105.webp" },
  { type: "image", src: "/images/slides/mech_03/slide_106.webp" },
  { type: "image", src: "/images/slides/mech_03/slide_107.webp" },
  { type: "image", src: "/images/slides/mech_03/slide_108.webp" },
  { type: "image", src: "/images/slides/mech_03/slide_109.webp" },
  { type: "image", src: "/images/slides/mech_03/slide_110.webp" },
  { type: "image", src: "/images/slides/mech_03/slide_111.webp" },
  { type: "image", src: "/images/slides/mech_03/slide_112.webp" },
  { type: "image", src: "/images/slides/mech_03/slide_113.webp" },
  { type: "image", src: "/images/slides/mech_03/slide_114.webp" },
  {
    type: "simulation",
    title: "🕹️ 직접 탐구: 중력렌즈 현상 시뮬레이션 (자바실험실)",
    src: "https://javalab.org/ko/gravitational_lensing/",
    height: "650"
  },
  { type: "image", src: "/images/slides/mech_03/slide_115.webp" },

  {
    type: "callout",
    style: "warning",
    title: "📌 수식 핵심: 일반상대성이론의 검증 현상",
    content: "• 태양 중력에 의한 빛의 휘어짐 편차: $\\Delta\\theta = \\frac{4GM}{c^2 R} \\approx 1.75''$ (1919년 에딩턴 개기일식 관측 검증)\n• 수성의 근일점 이동(세차 운동): 뉴턴 역학 계산치보다 세기당 $43''$ 더 이동함을 완벽히 설명\n• 중력 적색편이: 강한 중력장 부근에서 방출되는 빛의 파장이 길어짐(시간 지연)"
  },
  {
    type: "quiz",
    title: "💡 개념 확인 퀴즈 4: 중력 렌즈 현상",
    question: "거대한 질량을 가진 은하단 뒤쪽에 위치한 배경 은하의 빛이 왜곡되어 링이나 여러 개의 아치 모양 이미지로 관측되는 현상의 이름은?",
    answer: "중력 렌즈(Gravitational Lensing) 현상입니다. 거대한 질량이 주위의 시공간을 휘게 만들어 빛이 볼록렌즈를 통과하듯 꺾여 보이는 현상입니다."
  },

  // ====================================================
  // PART 5: 블랙홀과 시공간 특이점 (Slide 116 ~ 125)
  // ====================================================
  {
    type: "section_header",
    chapter: "PART 5",
    title: "Ⅴ. 블랙홀과 시공간 특이점",
    subtitle: "슈바르츠실트 반지름, 사건의 지평선, 블랙홀과 현대 우주론"
  },
  { type: "image", src: "/images/slides/mech_03/slide_116.webp" },
  { type: "image", src: "/images/slides/mech_03/slide_117.webp" },
  { type: "image", src: "/images/slides/mech_03/slide_118.webp" },
  { type: "image", src: "/images/slides/mech_03/slide_119.webp" },
  { type: "image", src: "/images/slides/mech_03/slide_120.webp" },
  { type: "image", src: "/images/slides/mech_03/slide_121.webp" },
  { type: "image", src: "/images/slides/mech_03/slide_122.webp" },
  { type: "image", src: "/images/slides/mech_03/slide_123.webp" },
  { type: "image", src: "/images/slides/mech_03/slide_124.webp" },
  { type: "image", src: "/images/slides/mech_03/slide_125.webp" },

  {
    type: "callout",
    style: "info",
    title: "📌 수식 핵심: 슈바르츠실트 반지름과 블랙홀",
    content: "• 탈출 속도가 빛의 속도 $c$가 되는 반경: $v_{escape} = \\sqrt{\\frac{2GM}{r}} = c$\n• 슈바르츠실트 반지름: $$r_s = \\frac{2GM}{c^2}$$\n• 사건의 지평선(Event Horizon): 반경 $r_s$ 내부에서는 빛조차 빠져나올 수 없는 시공간의 한계면입니다."
  },
  {
    type: "quiz",
    title: "💡 개념 확인 퀴즈 5: 블랙홀과 사건의 지평선",
    question: "질량이 커질수록 블랙홀의 사건의 지평선 크기(슈바르츠실트 반지름 $r_s$)는 어떻게 됩니까?",
    answer: "슈바르츠실트 반지름 $r_s = \\frac{2GM}{c^2}$ 이므로 블랙홀의 질량 $M$에 정비례하여 사건의 지평선 반경이 커집니다."
  },
  {
    type: "callout",
    style: "info",
    title: "🎉 [역학과 에너지] 3강 일반상대성이론 전체 학습 완료!",
    content: "축하합니다! 125장의 강의 슬라이드와 중력렌즈 시뮬레이션, KaTeX 수식 정리를 통해 일반상대성이론 단원을 완벽하게 마쳤습니다."
  }
];
