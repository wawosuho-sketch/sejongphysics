/**
 * @typedef {Object} LectureItem
 * @property {string} type
 * @property {string} [src]
 * @property {string} [title]
 * @property {string} [question]
 * @property {string} [answer]
 * @property {string} [content]
 * @property {string} [type_class]
 */

/** @type {LectureItem[]} */
export const lectureData = [
  // 1. 물리학이란 (도입부)
  { type: 'image', src: '/images/lecture_1/1강 물리학이란._1.png' },
  { type: 'image', src: '/images/lecture_1/1강 물리학이란._2.png' },
  { type: 'image', src: '/images/lecture_1/1강 물리학이란._3.png' },
  { type: 'image', src: '/images/lecture_1/1강 물리학이란._4.png' },
  { type: 'image', src: '/images/lecture_1/1강 물리학이란._5.png' },
  { type: 'image', src: '/images/lecture_1/1강 물리학이란._6.png' },
  { type: 'image', src: '/images/lecture_1/1강 물리학이란._7.png' },

  // [AI 보조자료 자동 삽입] 중간 개념 확인 퀴즈 1
  {
    type: 'quiz',
    question: 'Q. 방금 전까지 여러 물리학 분야를 보았는데요, 물체의 움직임과 힘을 주로 다루는 분야는 무엇일까요?',
    answer: '정답은 바로 역학 (Mechanics) 입니다!',
    title: '잠깐 멈추고 생각하기! 💡'
  },

  // 8. 갈릴레이 사고 실험 (역학)
  { type: 'image', src: '/images/lecture_1/1강 물리학이란._8.png' },

  // [AI 보조자료 자동 삽입] 8번 슬라이드 갈릴레이 빗면 사고 실험 관련 시뮬레이션
  {
    type: 'simulation',
    src: 'https://phet.colorado.edu/sims/html/energy-skate-park-basics/latest/energy-skate-park-basics_ko.html',
    title: '직접 해보는 갈릴레이의 역학적 에너지 보존 실험'
  },

  { type: 'image', src: '/images/lecture_1/1강 물리학이란._9.png' },
  { type: 'image', src: '/images/lecture_1/1강 물리학이란._10.png' },
  { type: 'image', src: '/images/lecture_1/1강 물리학이란._11.png' },

  // 12. 외르스테드와 패러데이
  { type: 'image', src: '/images/lecture_1/1강 물리학이란._12.png' },

  // [AI 보조자료 자동 삽입] 12번 슬라이드 전자기 유도 시뮬레이션
  {
    type: 'simulation',
    src: 'https://phet.colorado.edu/sims/html/faradays-law/latest/faradays-law_ko.html',
    title: '패러데이의 전자기 유도 법칙 시뮬레이션'
  },

  { type: 'image', src: '/images/lecture_1/1강 물리학이란._13.png' },

  // [AI 보조자료 자동 삽입] 중간 개념 확인 퀴즈 2
  {
    type: 'quiz',
    question: 'Q. 패러데이가 실험한 것처럼, 코일 근처에서 자석을 움직이면 무엇이 발생할까요?',
    answer: '유도 전류가 발생합니다! 이 현상을 전자기 유도라고 부릅니다.',
    title: '잠깐 멈추고 생각하기! 💡'
  },

  // 14. 무선 충전, 자이로드롭 원리
  { type: 'image', src: '/images/lecture_1/1강 물리학이란._14.png' },

  // [AI 보조자료 자동 삽입] 무선 충전 원리 유튜브 영상
  {
    type: 'video',
    src: 'https://www.youtube.com/embed/zPqEEZa2Gis',
    title: '자이로드롭 제동 / 무선 충전의 전자기 유도 원리 영상'
  },

  { type: 'image', src: '/images/lecture_1/1강 물리학이란._15.png' },
  { type: 'image', src: '/images/lecture_1/1강 물리학이란._16.png' },
  { type: 'image', src: '/images/lecture_1/1강 물리학이란._17.png' },
  { type: 'image', src: '/images/lecture_1/1강 물리학이란._18.png' },
  { type: 'image', src: '/images/lecture_1/1강 물리학이란._19.png' },

  // 20. 왜 역학부터 배우는가
  { type: 'image', src: '/images/lecture_1/1강 물리학이란._20.png' },

  // [AI 보조자료 자동 삽입] 마무리 퀴즈
  {
    type: 'quiz',
    question: 'Q. 갈릴레이의 사고 실험에서, 빗면을 굴러 내려간 공은 마찰이 없다면 어떻게 될까요?',
    answer: '원래 공이 출발했던 높이와 동일한 높이까지 올라가게 됩니다! (역학적 에너지 보존)',
    title: '1강 핵심 개념 점검'
  },
  {
    type: 'callout',
    content: '1강을 마무리했습니다! 물리학은 자연에 대한 호기심에서 출발하여, 힘과 에너지, 전자기, 빛에 이르기까지 세상을 근본적으로 이해하는 학문입니다.',
    type_class: 'success'
  }
];
