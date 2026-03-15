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
    src: `/images/lecture_12/slide_${num}.webp`
});

/** @type {LectureItem[]} */
export const lectureData = [];

// 12강은 총 74개 슬라이드로 구성
for (let i = 1; i <= 74; i++) {
    // 65번은 구글 드라이브 영상으로 대체
    const hiddenSlides = [41, 65, 74];

    if (!hiddenSlides.includes(i)) {
        lectureData.push(generateSlide(i));
    }

    // 시뮬레이션 및 영상 삽입
    if (i === 41) {
        lectureData.push({
            type: 'simulation',
            src: 'https://javalab.org/ko/photoelectric_effect_2/',
            title: '☀️ 광전 효과 시뮬레이션'
        });
    }

    if (i === 65) {
        lectureData.push({
            type: 'video',
            src: 'https://drive.google.com/file/d/1wcSBjaGH9GrdhlLC2nrsc-aRD3mwhyh_/preview',
            title: '🎥 전자의 이중슬릿'
        });
    }
    if (i === 73) {
        lectureData.push({
            type: 'video',
            src: 'https://drive.google.com/file/d/1EANaJSuCmceixKXaTur88WXw2DhKXGPh/preview',
            title: '☀️ 카메라 사진'
        });
    }
    if (i === 74) {
        lectureData.push({
            type: 'video',
            src: 'https://www.youtube.com/embed/omG_RGU9ymQ',
            title: '🎥 전자현미경'
        });
    }
}
