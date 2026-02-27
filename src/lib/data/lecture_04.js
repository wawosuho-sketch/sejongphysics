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
    src: `/images/lecture_4/slide_${num}.png`
});

/** @type {LectureItem[]} */
export const lectureData = [];

// 4강은 총 55개 슬라이드로 구성
for (let i = 1; i <= 55; i++) {
    // 특정 슬라이드를 영상이나 시뮬레이션으로 대체
    if (i === 8) {
        lectureData.push({
            type: 'video',
            src: 'https://www.youtube.com/watch?v=B2Owjwh1pgQ',
            title: '🎥 상대 속도와 운동량 (관련 영상)'
        });
        continue;
    }

    if (i === 11) {
        lectureData.push({
            type: 'simulation',
            src: 'https://javalab.org/ko/collision/',
            title: '💥 충돌과 운동량 보존 시뮬레이션 (자바실험실)'
        });
        continue;
    }

    if (i === 24) {
        lectureData.push({
            type: 'simulation',
            src: 'https://phet.colorado.edu/sims/html/collision-lab/latest/collision-lab_all.html?locale=ko',
            title: '🎯 충돌 실험실 (PhET)'
        });
        continue;
    }

    if (i === 30) {
        lectureData.push({
            type: 'simulation',
            src: 'https://javalab.org/ko/work/',
            title: '⚙️ 일과 에너지 시뮬레이션 (자바실험실)'
        });
        continue;
    }

    if (i === 40) {
        lectureData.push({
            type: 'simulation',
            src: 'https://javalab.org/ko/elastic_energy/',
            title: '🏹 탄성 퍼텐셜 에너지 (자바실험실)'
        });
        continue;
    }

    if (i === 48) {
        lectureData.push({
            type: 'simulation',
            src: 'https://phet.colorado.edu/sims/html/energy-skate-park/latest/energy-skate-park_all.html?locale=ko',
            title: '🛹 에너지 스케이트 파크 (PhET)'
        });
        continue;
    }

    // 1. 기본 슬라이드 이미지 푸시
    lectureData.push(generateSlide(i));
}
