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
    src: `/images/lecture_11/slide_${num}.png`
});

/** @type {LectureItem[]} */
export const lectureData = [];

// 11강은 총 49개 슬라이드로 구성
for (let i = 1; i <= 49; i++) {
    // 1. 특정 슬라이드 이미지는 생략 (시뮬레이션으로 대체 또는 숨김 처리)
    // 32번: 기하 광학 시뮬레이션
    // 41번: 카메라 및 눈의 구조 비교 시뮬레이션
    // 46번: 유튜브 영상 대체
    // 47~49번: 공백 슬라이드 숨김
    const hiddenSlides = [32, 41, 46, 47, 48, 49];

    if (!hiddenSlides.includes(i)) {
        lectureData.push(generateSlide(i));
    }

    // 2. 시뮬레이션 및 추가 요소 삽입
    if (i === 23) {
        lectureData.push({
            type: 'simulation',
            src: 'https://phet.colorado.edu/sims/html/bending-light/latest/bending-light_all.html?locale=ko',
            title: '🌈 빛의 굴절과 반사 시뮬레이션 (PhET)'
        });
    }

    if (i === 25) {
        lectureData.push({
            type: 'simulation',
            src: 'https://javalab.org/ko/total_internal_reflection/',
            title: '💎 빛의 전반사와 임계각 시뮬레이션'
        });
    }

    if (i === 32) {
        lectureData.push({
            type: 'simulation',
            src: 'https://phet.colorado.edu/sims/html/geometric-optics/latest/geometric-optics_all.html',
            title: '🔍 기하 광학 시뮬레이션 (PhET)'
        });
    }

    if (i === 41) {
        lectureData.push({
            type: 'simulation',
            src: 'https://javalab.org/ko/camera/',
            title: '📷 카메라의 원리 시뮬레이션'
        });

        lectureData.push({
            type: 'simulation',
            src: 'https://javalab.org/ko/correction_of_near_sightedness/',
            title: '👀 근시 교정 원리 시뮬레이션'
        });

        lectureData.push({
            type: 'simulation',
            src: 'https://javalab.org/ko/camera_2/',
            title: '👁️ 카메라의 노출과 초점 조절'
        });
    }

    if (i === 46) {
        lectureData.push({
            type: 'video',
            src: 'https://www.youtube.com/embed/qxdLZ7JHrng',
            title: '🎥 거울과 렌즈의 특징 요약 영상'
        });
    }

    if (i === 49) {
        lectureData.push({
            type: 'callout',
            style: 'success',
            title: '11강 기하 광학 요약',
            content: '렌즈와 거울을 통과하는 빛의 굴절과 상의 작도를 배웠습니다. 다음 시간에는 전자기파의 종류와 활용에 대해 알아봅시다.'
        });
    }
}
