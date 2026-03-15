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
    src: `/images/lecture_8/slide_${num}.webp`
});

/** @type {LectureItem[]} */
export const lectureData = [];

// 8강은 총 105개 슬라이드로 구성
for (let i = 1; i <= 105; i++) {
    // 1. 기본 슬라이드 이미지 푸시
    lectureData.push(generateSlide(i));

    // 2. 시뮬레이션 및 콜아웃 (슬라이드 뒤에 추가)
    if (i === 16) {
        lectureData.push({
            type: 'simulation',
            src: 'https://javalab.org/ko/magnetic_field_around_a_bar_magnet/',
            title: '🧲 막대자석 주위의 자기장 시뮬레이션'
        });
    }

    if (i === 36) {
        lectureData.push({
            type: 'simulation',
            src: 'https://javalab.org/ko/magnetization/',
            title: '⚡ 자화과정 시뮬레이션'
        });
    }

    if (i === 64) {
        lectureData.push({
            type: 'simulation',
            src: 'https://javalab.org/ko/magnetic_field_around_a_wire/',
            title: '⚡ 직선 도선 주위의 자기장 시뮬레이션'
        });
    }

    if (i === 68) {
        lectureData.push({
            type: 'simulation',
            src: 'https://javalab.org/ko/magnetic_field_around_a_circular_wire/',
            title: '⭕ 원형 전류에 의한 자기장 시뮬레이션'
        });
    }

    if (i === 72) {
        lectureData.push({
            type: 'simulation',
            src: 'https://javalab.org/ko/magnetic_field_around_a_coil/',
            title: '🌀 코일(솔레노이드) 주위의 자기장 시뮬레이션'
        });
    }

    if (i === 86) {
        lectureData.push({
            type: 'simulation',
            src: 'https://javalab.org/ko/lorentzs_force_3d/',
            title: '🧲 전자기력(로렌츠 힘) 시뮬레이션'
        });

        lectureData.push({
            type: 'quiz',
            title: '🤔 확인 퀴즈',
            question: '자기장 속에서 전류가 흐르는 도선이 받는 힘(전자기력)의 방향은 어떻게 찾을 수 있을까요?',
            answer: '오른손을 이용하여 찾을 수 있습니다. 네 손가락을 자기장 방향으로, 엄지손가락을 전류 방향으로 향하게 했을 때 손바닥이 수직으로 향하는 방향이 힘의 방향입니다.'
        });
    }

    if (i === 102) {
        lectureData.push({
            type: 'simulation',
            src: 'https://javalab.org/ko/dc_motor_2/',
            title: '⚙️ 직류 모터 시뮬레이션'
        });

        lectureData.push({
            type: 'simulation',
            src: 'https://javalab.org/ko/homopolar_motor/',
            title: '🔋 호모폴라 전동기 시뮬레이션'
        });
    }

    if (i === 103) {
        lectureData.push({
            type: 'simulation',
            src: 'https://www.labxchange.org/library/pathway/lx-pathway:b0812721-2e01-4d45-bfe0-beec0925dc2e/items/lb:LabXchange:999e0b49:lx_simulation:1/81371?source=%2Flibrary%2Fclusters%2Flx-cluster%3APhysicsResources&fullscreen=true',
            title: '🔬 LabXchange mri 시뮬레이션'
        });
    }

    if (i === 105) {
        lectureData.push({
            type: 'simulation',
            src: 'https://javalab.org/ko/speaker/',
            title: '🔊 스피커의 원리 시뮬레이션'
        });

        lectureData.push({
            type: 'simulation',
            src: 'https://javalab.org/ko/crt_tv/',
            title: '📺 브라운관(CRT) TV 원리 시뮬레이션'
        });

        lectureData.push({
            type: 'callout',
            style: 'success',
            title: '단원 마무리 정리',
            content: '모두 수고하셨습니다. 일상 속 다양한 자기 현상들을 떠올려 보세요.'
        });
    }
}
