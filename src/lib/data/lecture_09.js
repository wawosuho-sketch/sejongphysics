/**
 * @typedef {Object} LectureItem
 * @property {'image'|'youtube_shorts'|'video'|'quiz'|'callout'|'simulation'} type
 * @property {string} [src]
 * @property {string} [title]
 * @property {string} [question]
 * @property {string} [answer]
 * @property {string} [content]
 * @property {string} [calloutType]
 * @property {string} [height]
 * @property {string} [style]
 */

/** @returns {LectureItem} */
const generateSlide = (num) => ({
    type: 'image',
    src: `/images/lecture_9/slide_${num}.png`
});

/** @type {LectureItem[]} */
export const lectureData = [];

// 9강은 총 48개 슬라이드로 구성
for (let i = 1; i <= 48; i++) {
    // 1. 기본 슬라이드 이미지 푸시
    lectureData.push(generateSlide(i));

    // 2. 시뮬레이션 및 콜아웃 (슬라이드 뒤에 추가)
    if (i === 15) {
        lectureData.push({
            type: 'simulation',
            src: 'https://javalab.org/ko/faradays_law_2/',
            title: '🧲 패러데이 전자기 유도 법칙 시뮬레이션'
        });
    }


    if (i === 47) {
        lectureData.push({
            type: 'simulation',
            src: 'https://javalab.org/ko/ac_generator/',
            title: '⚡ 교류 발전기 시뮬레이션'
        });
    }

    if (i === 48) {
        lectureData.push({
            type: 'callout',
            style: 'info',
            title: '다양한 전자기 유도 활용 사례',
            content: '마이크, 금속 탐지기, 교통 카드, 스마트폰 무선 충전기 등 우리 주변에는 전자기 유도를 활용한 사례가 매우 많습니다. 주변에 또 어떤 것들이 있는지 찾아보세요!'
        });

        lectureData.push({
            type: 'callout',
            style: 'success',
            title: '단원 마무리 정리',
            content: '패러데이의 전자기 유도 법칙을 통해 자기장 변화가 어떻게 전기 에너지를 만들어내는지 학습했습니다. 발전소에서 각 가정으로 전기가 오는 과정을 떠올려 보세요.'
        });
    }
}
