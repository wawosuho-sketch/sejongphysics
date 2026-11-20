export const lectureData = [
  {
    type: "title",
    text: "5강. 탄성력과 단진동"
  },
  {
    type: "callout",
    style: "info",
    title: "학습 안내",
    content: "용수철에 매단 물체의 왕복 운동으로 단진동을 봅니다. 가속도는 변위에 비례하고 방향은 평형점 쪽이며, 주기는 $T=2\\pi\\sqrt{m/k}$ 입니다. 진폭을 바꿔도 주기는 변하지 않습니다.\n고체가 늘어나는 정도에서 용수철 상수가 어떻게 나오는지도 보고, 에너지와 작은 각의 단진자까지 같은 식으로 묶습니다."
  },
  { type: "image", src: "/images/slides/mech_05/lesson_course_map.webp" },

  {
    type: "section_header",
    chapter: "PART 1",
    title: "Ⅰ. 힘과 고체의 변형",
    subtitle: "힘을 받아도 안 움직일 수 있다. 대신 모양이 변한다"
  },
  { type: "image", src: "/images/slides/mech_05/slide_03.webp" },
  { type: "image", src: "/images/slides/mech_05/slide_04.webp" },
  {
    type: "callout",
    style: "info",
    title: "모양이 변한 다음",
    content: "물체가 통째로 움직이지 않아도 힘은 모양을 바꿉니다. 그 변형이 물체를 제자리로 되돌릴 때 단진동이 됩니다."
  },
  { type: "image", src: "/images/slides/mech_05/slide_05.webp" },
  { type: "image", src: "/images/slides/mech_05/slide_06.webp" },
  { type: "image", src: "/images/slides/mech_05/slide_07.webp" },
  { type: "image", src: "/images/slides/mech_05/slide_08.webp" },
  { type: "image", src: "/images/slides/mech_05/slide_09.webp" },
  { type: "image", src: "/images/slides/mech_05/slide_10.webp" },

  {
    type: "section_header",
    chapter: "PART 2",
    title: "Ⅱ. 세 가지 변형과 탄성률",
    subtitle: "늘어남, 비틀림, 부피 변화. 식의 꼴은 같고, 단진동은 길이 방향만 쓴다"
  },
  { type: "image", src: "/images/slides/mech_05/slide_14.webp" },
  { type: "image", src: "/images/slides/mech_05/slide_15.webp" },
  { type: "image", src: "/images/slides/mech_05/slide_16.webp" },
  { type: "image", src: "/images/slides/mech_05/slide_18.webp" },
  { type: "image", src: "/images/slides/mech_05/lesson_three_moduli.webp" },
  { type: "image", src: "/images/slides/mech_05/slide_19.webp" },
  { type: "image", src: "/images/slides/mech_05/slide_20.webp" },
  { type: "image", src: "/images/slides/mech_05/slide_21.webp" },
  { type: "image", src: "/images/slides/mech_05/slide_22.webp" },
  {
    type: "callout",
    style: "tip",
    title: "세 문제의 공통점",
    content: "철선, 알루미늄 막대, 구리 공은 같은 비례식에 숫자를 넣습니다. 이 다음부터 단진동에 쓰는 상수는 영률 $Y$에서 나온 용수철 상수 $k$ 하나입니다."
  },

  {
    type: "section_header",
    chapter: "PART 3",
    title: "Ⅲ. 후크 법칙과 용수철 상수",
    subtitle: "물질의 영률이 이 용수철의 k가 된다. 직렬은 길어지고 병렬은 굵어진다"
  },
  { type: "image", src: "/images/slides/mech_05/slide_25.webp" },
  { type: "image", src: "/images/slides/mech_05/slide_26.webp" },
  {
    type: "callout",
    style: "info",
    title: "작은 힘에도 늘어난다",
    content: "늘어난 길이는 작은 힘에서도 힘의 크기에 비례합니다. 어느 한계를 넘어야만 모양이 변한다는 생각과 다릅니다."
  },
  {
    type: "simulation",
    title: "힘과 늘인 길이가 비례하는지, 직렬과 병렬에서 상수가 어떻게 바뀌는지 보기",
    src: "https://phet.colorado.edu/sims/html/hookes-law/latest/hookes-law_all.html?locale=ko",
    height: "620"
  },
  { type: "image", src: "/images/slides/mech_05/slide_28.webp" },
  { type: "image", src: "/images/slides/mech_05/lesson_rod_as_spring.webp" },
  { type: "image", src: "/images/slides/mech_05/slide_30.webp" },
  { type: "image", src: "/images/slides/mech_05/slide_31.webp" },
  { type: "image", src: "/images/slides/mech_05/slide_32.webp" },
  { type: "image", src: "/images/slides/mech_05/slide_33.webp" },
  { type: "image", src: "/images/slides/mech_05/lesson_series_parallel.webp" },
  {
    type: "quiz",
    title: "개념 확인: 반으로 자른 용수철",
    question: "용수철 상수가 $k$인 용수철을 반으로 자르면 조각 하나의 용수철 상수는 얼마인가?",
    answer: "$2k$입니다. $k = YS/L$ 이므로 길이만 절반이 되면 상수는 2배가 됩니다. 두 조각을 다시 직렬로 잇면 원래의 $k$로 돌아옵니다."
  },

  {
    type: "section_header",
    chapter: "PART 4",
    title: "Ⅳ. 탄성력과 단진동",
    subtitle: "되돌리는 힘, 진폭과 주기, 사인으로 보이는 운동"
  },
  { type: "image", src: "/images/slides/mech_05/slide_36.webp" },
  { type: "image", src: "/images/slides/mech_05/slide_37.webp" },
  {
    type: "callout",
    style: "warning",
    title: "단진동이 성립하는 범위",
    content: "탄성 한계를 넘으면 후크 법칙이 성립하지 않고, 힘을 빼도 원래 길이로 돌아오지 않습니다. 단진동은 그 한계 안에서만 다룹니다."
  },
  { type: "image", src: "/images/slides/mech_05/slide_38.webp" },
  { type: "image", src: "/images/slides/mech_05/slide_39.webp" },
  { type: "image", src: "/images/slides/mech_05/lesson_vertical_spring.webp" },
  {
    type: "simulation",
    title: "연직 용수철에서 질량과 용수철 상수를 바꿔 주기가 어떻게 변하는지 보기",
    src: "https://javalab.org/ko/spring_pendulum/",
    height: "680"
  },
  {
    type: "quiz",
    title: "개념 확인: 중력이 바뀌면",
    question: "연직 용수철 진자를 중력이 더 큰 행성으로 가져가면 주기는 어떻게 되는가? 용수철 상수와 질량은 그대로이다.",
    answer: "주기는 그대로입니다. 중력은 평형에서 늘어난 길이 $x_0 = mg/k$만 바꿉니다. 새 평형점에서의 알짜힘은 여전히 $F=-kx$이고, $T=2\\pi\\sqrt{m/k}$에는 $g$가 없습니다."
  },
  { type: "image", src: "/images/slides/mech_05/slide_40.webp" },
  { type: "image", src: "/images/slides/mech_05/slide_41.webp" },
  { type: "image", src: "/images/slides/mech_05/slide_43.webp" },
  { type: "image", src: "/images/slides/mech_05/lesson_shm_terms.webp" },
  { type: "image", src: "/images/slides/mech_05/slide_44.webp" },

  {
    type: "section_header",
    chapter: "PART 5",
    title: "Ⅴ. 주기를 구하는 두 길",
    subtitle: "원운동의 그림자로 주기를 구하고, 미분으로 같은 식을 확인한다"
  },
  { type: "image", src: "/images/slides/mech_05/slide_48.webp" },
  { type: "image", src: "/images/slides/mech_05/slide_49.webp" },
  { type: "image", src: "/images/slides/mech_05/slide_50.webp" },
  { type: "image", src: "/images/slides/mech_05/slide_51.webp" },
  { type: "image", src: "/images/slides/mech_05/lesson_projection.webp" },
  { type: "image", src: "/images/slides/mech_05/slide_52.webp" },
  { type: "image", src: "/images/slides/mech_05/lesson_xva.webp" },
  { type: "image", src: "/images/slides/mech_05/lesson_period.webp" },
  {
    type: "quiz",
    title: "개념 확인: 최대인 곳과 주기",
    question: "단진동에서 속력이 최대인 위치와 가속도의 크기가 최대인 위치를 쓰시오. 이어서, 질량을 4배, 진폭을 2배로 하면 주기는 몇 배가 되는가?",
    answer: "속력은 평형점에서 최대이고 크기는 $A\\omega$입니다. 가속도의 크기는 양쪽 끝에서 최대이고, 방향은 평형점 쪽입니다. 주기는 2배입니다. $T=2\\pi\\sqrt{m/k}$에서 질량 4배는 주기 2배이고, 진폭은 식에 없습니다."
  },
  {
    type: "simulation",
    title: "질량, 용수철 상수, 진폭을 바꿔 주기와 에너지 막대를 함께 보기",
    src: "https://phet.colorado.edu/sims/html/masses-and-springs/latest/masses-and-springs_all.html?locale=ko",
    height: "620"
  },
  {
    type: "callout",
    style: "warning",
    title: "왜 사인이 되는가",
    content: "이어지는 계산은 운동방정식의 해가 사인과 코사인이 되는 과정입니다. 주기와 위치별 속도, 가속도는 바로 앞에서 이미 구했습니다."
  },
  { type: "image", src: "/images/slides/mech_05/lesson_ode_bridge.webp" },
  { type: "image", src: "/images/slides/mech_05/slide_53.webp" },
  { type: "image", src: "/images/slides/mech_05/slide_54.webp" },
  { type: "image", src: "/images/slides/mech_05/slide_55.webp" },
  { type: "image", src: "/images/slides/mech_05/slide_56.webp" },
  { type: "image", src: "/images/slides/mech_05/slide_57.webp" },
  { type: "image", src: "/images/slides/mech_05/slide_58.webp" },

  {
    type: "section_header",
    chapter: "PART 6",
    title: "Ⅵ. 단진동의 에너지",
    subtitle: "진폭이 에너지를 정하고, 에너지가 임의 위치의 속력을 정한다"
  },
  { type: "image", src: "/images/slides/mech_05/lesson_energy.webp" },
  { type: "image", src: "/images/slides/mech_05/lesson_speed.webp" },
  {
    type: "simulation",
    title: "용수철을 늘이며 탄성 에너지가 변위의 제곱에 비례하는지 보기",
    src: "https://javalab.org/ko/elastic_energy/",
    height: "680"
  },
  {
    type: "quiz",
    title: "개념 확인: 에너지와 속력",
    question: "용수철 상수 $100\\,\\mathrm{N/m}$, 진폭 $0.2\\,\\mathrm{m}$인 단진동의 전체 역학적 에너지는 몇 J인가? 변위가 $0.1\\,\\mathrm{m}$인 순간의 운동 에너지도 구하시오.",
    answer: "전체 에너지는 $\\frac{1}{2}kA^2 = \\frac{1}{2}\\times 100\\times 0.04 = 2\\,\\mathrm{J}$입니다. 변위 $0.1\\,\\mathrm{m}$에서 탄성 에너지는 $0.5\\,\\mathrm{J}$이므로 운동 에너지는 $1.5\\,\\mathrm{J}$입니다. 이때 속력은 최대 속력의 $\\sqrt{3}/2$배입니다."
  },

  {
    type: "section_header",
    chapter: "PART 7",
    title: "Ⅶ. 같은 방정식이 되는 운동",
    subtitle: "평형 근처에서 되돌리는 힘이 변위에 비례하면 모두 단진동이다"
  },
  { type: "image", src: "/images/slides/mech_05/slide_61.webp" },
  { type: "image", src: "/images/slides/mech_05/slide_62.webp" },
  { type: "image", src: "/images/slides/mech_05/slide_63.webp" },
  { type: "image", src: "/images/slides/mech_05/lesson_pendulum.webp" },
  { type: "image", src: "/images/slides/mech_05/lesson_pendulum_bottom.webp" },
  {
    type: "simulation",
    title: "길이, 질량, 중력, 각도를 바꿔 단진자 주기가 무엇에 따라 변하는지 보기",
    src: "https://phet.colorado.edu/sims/html/pendulum-lab/latest/pendulum-lab_all.html?locale=ko",
    height: "620"
  },
  {
    type: "quiz",
    title: "개념 확인: 단진자의 주기",
    question: "작은 각으로 진동하는 단진자의 길이를 4배, 추의 질량을 2배로 하면 주기는 몇 배가 되는가?",
    answer: "2배입니다. $T=2\\pi\\sqrt{l/g}$에서 길이가 4배이면 주기는 2배이고, 질량은 힘과 가속도에서 함께 사라져 주기에 남지 않습니다."
  },
  {
    type: "callout",
    style: "info",
    title: "원형 골짜기",
    content: "원형 궤도의 바닥 근처는 작은 각의 단진자와 같은 복원력입니다. 반지름 $r$이 진자의 길이 역할을 하므로 주기는 $T=2\\pi\\sqrt{r/g}$입니다."
  },
  { type: "image", src: "/images/slides/mech_05/slide_64.webp" },
  { type: "image", src: "/images/slides/mech_05/slide_65.webp" },
  {
    type: "callout",
    style: "info",
    title: "물에 뜬 통",
    content: "더 잠기면 부력이 커져 위로 밉니다. 늘어난 부력은 더 잠긴 깊이 $x$에 비례하므로 $F=-(\\rho_0 S g)x$인 용수철과 같습니다. 질량은 통 전체의 질량 $\\rho S l$입니다."
  },
  { type: "image", src: "/images/slides/mech_05/slide_66.webp" },
  { type: "image", src: "/images/slides/mech_05/slide_67.webp" },
  {
    type: "callout",
    style: "info",
    title: "양쪽에 연결된 용수철",
    content: "한쪽이 늘어나면 다른 쪽은 줄어듭니다. 두 힘이 물체를 같은 방향으로 밀고 당기므로 알짜힘은 $F=-(k_1+k_2)x$이고, 병렬 연결과 같은 상수가 됩니다."
  },
  { type: "image", src: "/images/slides/mech_05/slide_68.webp" },
  { type: "image", src: "/images/slides/mech_05/lesson_tunnel.webp" },
  { type: "image", src: "/images/slides/mech_05/slide_69.webp" },
  { type: "image", src: "/images/slides/mech_05/slide_70.webp" },
  { type: "image", src: "/images/slides/mech_05/lesson_family.webp" }
];
