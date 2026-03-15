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
    src: `/images/lecture_7/slide_${num}.webp`
});

/** @type {LectureItem[]} */
export const lectureData = [];

// 7강은 총 23개 슬라이드로 구성
for (let i = 1; i <= 23; i++) {
    // 1. 기본 슬라이드 이미지 푸시
    lectureData.push(generateSlide(i));

    // 2. 시뮬레이션 및 콜아웃 (슬라이드 뒤에 추가)
    if (i === 3) {
        lectureData.push({
            type: 'video',
            src: 'https://youtu.be/f_MZNsEqyQw', // 대표적인 물리학 축전기 원리 영상
            title: '🎥 [개념 영상] 축전기는 어떻게 전하를 모을까?'
        });
    }

    if (i === 8) {
        lectureData.push({
            type: 'quiz',
            title: '🤔 생각 해보기',
            question: '축전기 두 극판 사이로 전자가 직접 이동하여 전류가 흐를 수 있을까요?',
            answer: '아닙니다. 두 극판 사이에는 절연체(유전체)가 있어서 전자가 직접 건너갈 수 없으며, 대신 양 극판에 (+)전하와 (-)전하가 유도되어 모이게 됩니다.'
        });
    }

    if (i === 11) {
        lectureData.push({
            type: 'simulation',
            src: 'https://javalab.org/ko/capacitor/',
            title: '⚡ 축전기의 원리 시뮬레이션'
        });
        lectureData.push({
            type: 'simulation',
            src: 'https://javalab.org/ko/capacitor_characteristic/',
            title: '📊 축전기의 특성 시뮬레이션'
        });
    }

    if (i === 18) {
        lectureData.push({
            type: 'simulation',
            src: 'https://phet.colorado.edu/sims/html/capacitor-lab-basics/latest/capacitor-lab-basics_all.html?locale=ko',
            title: '🧪 PhET: 축전기 실험실 (기초)'
        });
    }

    if (i === 23) {
        lectureData.push({
            type: 'callout',
            style: 'success',
            title: '단원 마무리 정리',
            content: '축전기의 활용 예, 다양한 종류, 그리고 건전지와의 차이점에 대해 꼼꼼히 복습해 보세요.'
        });
    }
}
