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
    src: `/images/lecture_10/slide_${num}.webp`
});

/** @type {LectureItem[]} */
export const lectureData = [];

// 10강은 총 109개 슬라이드로 구성
for (let i = 1; i <= 109; i++) {
    // 1. 특정 슬라이드 이미지는 생략 (시뮬레이션으로 대체 또는 숨김 처리)
    const hiddenSlides = [6, 32, 80, 87, 89];
    if (!hiddenSlides.includes(i)) {
        lectureData.push(generateSlide(i));
    }

    // 2. 시뮬레이션 및 콜아웃 (슬라이드 대신 또는 뒤에 추가)
    if (i === 6) {
        lectureData.push({
            type: 'simulation',
            src: 'https://phet.colorado.edu/sims/html/waves-intro/latest/waves-intro_all.html?locale=ko',
            title: '🌊 파동 소개 시뮬레이션 (PhET)'
        });
    }
    if (i === 32) {
        lectureData.push({
            type: 'simulation',
            src: 'https://javalab.org/ko/superposition_and_interference/',
            title: '🌊 파동의 중첩과 간섭 시뮬레이션'
        });
    }

    if (i === 80) {
        lectureData.push({
            type: 'simulation',
            src: 'https://javalab.org/ko/double_slit/',
            title: '🔆 영의 이중 슬릿 간섭 시뮬레이션'
        });

        lectureData.push({
            type: 'quiz',
            title: '🤔 중간 점검 퀴즈',
            question: '빛의 간섭 현상이 일어날 때, 두 파동의 위상이 같아 밝게 보이는 간섭을 무엇이라고 할까요?',
            answer: '보강 간섭이라고 합니다. 반대로 위상이 반대여서 어둡게 보이는 경우를 상쇄 간섭이라고 합니다.'
        });
    }

    if (i === 87) {
        lectureData.push({
            type: 'simulation',
            src: 'https://javalab.org/ko/thin_film_interference/',
            title: '🌈 얇은 막에 의한 빛의 간섭 시뮬레이션'
        });
    }

    if (i === 89) {
        lectureData.push({
            type: 'simulation',
            src: 'https://javalab.org/ko/light_interference_on_cd_surface/',
            title: '💿 CD 표면의 빛 간섭 시뮬레이션'
        });
    }

    if (i === 100) {
        lectureData.push({
            type: 'simulation',
            src: 'https://javalab.org/ko/polarization/',
            title: '🕶️ 편광(Polarization)  시뮬레이션'
        });

        lectureData.push({
            type: 'callout',
            style: 'info',
            title: '💡 편광의 핵심 원리',
            content: '편광은 빛이 횡파임을 증명하는 결정적 현상입니다. 특정 방향으로만 진동하는 빛을 걸러내는 원리를 꼭 기억하세요!'
        });
    }

    if (i === 102) {
        lectureData.push({
            type: 'simulation',
            src: 'https://javalab.org/ko/why_is_the_sky_blue/',
            title: '🌈 하늘은 왜 파랗고 노을은 왜 붉을까? (빛의 산란) 시뮬레이션'
        });
    }

    if (i === 109) {
        lectureData.push({
            type: 'callout',
            style: 'success',
            title: '10강 학습 완료!',
            content: '빛의 파동성과 간섭, 편광 현상에 대해 학습했습니다. 다음 시간에는 빛의 입자성에 대해 알아보겠습니다.'
        });
    }
}
