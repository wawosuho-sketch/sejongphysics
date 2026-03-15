/**
 * @typedef {Object} LectureItem
 * @property {string} type
 * @property {string} [src]
 * @property {string} [title]
 * @property {string} [question]
 * @property {string} [answer]
 * @property {string} [content]
 * @property {string} [style]
 * @property {string} [height]
 */

const generateSlide = (num) => ({
    type: 'image',
    src: `/images/lecture_3/slide_${num}.webp`
});

/** @type {LectureItem[]} */
export const lectureData = [];

for (let i = 1; i <= 98; i++) {
    if (i === 5) {
        lectureData.push({
            type: 'simulation',
            src: 'https://javalab.org/ko/average_velocity/',
            title: '🏃 평균 속도 시뮬레이션 (자바실험실)',
            height: '800'
        });
    }

    if (i === 68) {
        // 68번 슬라이드는 텍스트 대신 시뮬레이션으로 대체
        lectureData.push({
            type: 'simulation',
            src: 'https://phet.colorado.edu/sims/html/hookes-law/latest/hookes-law_all.html?locale=ko',
            title: '🔬 훅의 법칙 시뮬레이션'
        });
        continue;
    }

    // 기본 슬라이드 출력 (42번, 50번 포함 모두 정상 출력)
    lectureData.push(generateSlide(i));

    // === 분기점마다 퀴즈 및 추가 시뮬레이션 자연스럽게 삽입 ===


    if (i === 75) {
        // 도르래 시뮬레이션으로 교체 (선생님 요청)
        lectureData.push({
            type: 'simulation',
            src: 'https://javalab.org/ko/pulley_3/',
            title: '⚙️ 도르래 시뮬레이션 (자바실험실)',
            height: '850'
        });
    }

    // 마지막 정리 Callout
    if (i === 98) {
        lectureData.push({
            type: 'callout',
            content: '🎉 3강(힘과 에너지 2차시) 학습을 완료했습니다! 일과 에너지의 관계, 그리고 역학적 에너지 보존 법칙을 완벽히 이해했습니다.',
            style: 'success'
        });
    }
}
