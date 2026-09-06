export const lectureData = [
  {
    type: "title",
    text: "3강. 운동량과 충격량"
  },
  {
    type: "callout",
    style: "info",
    title: "학습 목표",
    content: "운동량과 충격량의 관계를 파악하고, 충돌 안전 설계에서의 충격력 완화 원리를 분석할 수 있다."
  },
  {
    type: "simulation",
    title: "충돌 실험 및 운동량 보존",
    src: "https://phet.colorado.edu/sims/html/collision-lab/latest/collision-lab_all.html?locale=ko",
    height: "600"
  },
  {
    type: "quiz",
    title: "개념 확인 퀴즈",
    question: "동일한 충격량을 받을 때 작용 시간이 길어지면 물체가 받는 평균 힘(충격력)의 크기는 작아진다. (O / X)",
    answer: "O ($I = F \\cdot \\Delta t$ 이므로 충격량 $I$가 일정할 때 시간 $\\Delta t$가 증가하면 힘 $F$는 감소합니다.)"
  }
];
