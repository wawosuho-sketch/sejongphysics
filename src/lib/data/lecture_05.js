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
    src: `/images/lecture_5/slide_${num}.png`
});

/** @type {LectureItem[]} */
export const lectureData = [];

// 5강은 총 50개 슬라이드로 구성
for (let i = 1; i <= 50; i++) {
    if (i === 8) {
        lectureData.push({
            type: 'video',
            src: 'https://www.youtube.com/watch?v=NBoMTYZAyJc',
            title: '🎥 역학적 에너지의 전환 (Car Crash)'
        });
        continue; // 슬라이드 이미지 제외
    }

    if (i === 28) {
        lectureData.push({
            type: 'video',
            src: 'https://www.youtube.com/watch?v=3FyhNpHeHMM',
            title: " Hero's Engine (기체가 하는 일)"
        });
        continue; // 슬라이드 이미지 제외
    }

    // 2. 기본 슬라이드 이미지 푸시 (시뮬레이션/콜아웃은 슬라이드 다음에 나옴)
    lectureData.push(generateSlide(i));

    // 3. 시뮬레이션 및 콜아웃 (슬라이드 유지 + 뒤에 추가)
    if (i === 11) {
        lectureData.push({
            type: 'simulation',
            src: 'https://javalab.org/ko/gas_model/',
            title: '🌡️ 온도와 내부 에너지 (기체 분자 운동)'
        });
    }

    if (i === 20) {
        lectureData.push({
            type: 'callout',
            style: 'info',
            title: '핵심 정리: 열의 전달 방식',
            content: '전도(고체), 대류(액체/기체), 복사(매질 없음)의 차이를 이해하는 것이 중요합니다.'
        });
    }

    if (i === 24) {
        lectureData.push({
            type: 'simulation',
            src: 'https://javalab.org/ko/status_change_of_water/',
            title: '💧 물질의 상태 변화 시뮬레이션'
        });
    }

    if (i === 33) {
        lectureData.push({
            type: 'simulation',
            src: 'https://javalab.org/ko/pressure_volume_diagram/',
            title: '📊 압력-부피 그래프 (기체가 하는 일)'
        });
    }

    if (i === 40) {
        lectureData.push({
            type: 'simulation',
            src: 'https://javalab.org/ko/4_stroke_engine/',
            title: '🏎️ 4행정 기관의 원리 (열기관)'
        });
    }

}
