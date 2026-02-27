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
    src: `/images/lecture_6/slide_${num}.png`
});

/** @type {LectureItem[]} */
export const lectureData = [];

// 6강은 총 115개 슬라이드로 구성
for (let i = 1; i <= 115; i++) {
    // 1. 영상 (슬라이드 대체형)
    if (i === 2) {
        lectureData.push({
            type: 'video',
            src: 'https://www.youtube.com/watch?v=3Ptu07enIsY',
            title: '🎥 마찰 전기'
        });
        continue;
    }

    if (i === 107) {
        lectureData.push({
            type: 'video',
            src: 'https://youtu.be/O8VQFHfDqg4',
            title: '🎥 올바른 전기 사용법'
        });
        continue;
    }

    // 1.5. 시뮬레이션 (슬라이드 대체형)
    if (i === 17) {
        lectureData.push({
            type: 'simulation',
            src: 'https://phet.colorado.edu/sims/html/charges-and-fields/latest/charges-and-fields_all.html?locale=ko',
            title: '📏 전기력선 시뮬레이션'
        });
        continue;
    }

    if (i === 18) {
        lectureData.push({
            type: 'simulation',
            src: 'https://javalab.org/ko/electric_field_line/',
            title: '🧲 전기력선 관찰 시뮬레이션'
        });
        continue;
    }

    if (i === 55) {
        lectureData.push({
            type: 'simulation',
            src: 'https://javalab.org/ko/same_circuit/',
            title: '💡 동일한 회로 찾기'
        });
        lectureData.push({
            type: 'simulation',
            src: 'https://javalab.org/ko/parallel_circuit/',
            title: '💡 병렬회로 분석'
        });
        lectureData.push({
            type: 'simulation',
            src: 'https://javalab.org/ko/incandescence/',
            title: '💡 백열등 원리'
        });
        continue;
    }

    if (i === 56) {
        lectureData.push({
            type: 'simulation',
            src: 'https://phet.colorado.edu/sims/html/circuit-construction-kit-dc/latest/circuit-construction-kit-dc_all.html?locale=ko',
            title: '🛠️ 직류 회로 제작 키트'
        });
        continue;
    }

    if (i === 110) {
        lectureData.push({
            type: 'simulation',
            src: 'https://javalab.org/ko/home_wiring/',
            title: '🏠 가정용 배선 시뮬레이션'
        });
        continue;
    }

    // 2. 기본 슬라이드 이미지 푸시
    lectureData.push(generateSlide(i));

    // 3. 시뮬레이션 및 콜아웃 (슬라이드 유지 + 뒤에 추가)
    if (i === 12) {
        lectureData.push({
            type: 'simulation',
            src: 'https://javalab.org/ko/triboelectricity/',
            title: '⚡ 마찰 전기의 원리 체험'
        });
    }

    if (i === 20) {
        lectureData.push({
            type: 'callout',
            style: 'info',
            title: '핵심 개념: 전하량 보존 법칙',
            content: '두 물체를 마찰시킬 때 한 물체에서 다른 물체로 이동하는 것은 전자뿐이며, 전체 전하의 양은 변용되지 않습니다.'
        });
    }

    if (i === 35) {
        lectureData.push({
            type: 'callout',
            style: 'warning',
            title: '필수 공식: 쿨롱의 법칙 (Coulomb\'s Law)',
            content: 'F = k * (q1 * q2) / r² <br> 두 전하 사이의 전기력은 거리의 제곱에 반비례하고 전하량의 곱에 비례합니다.'
        });
    }

    if (i === 47) {
        lectureData.push({
            type: 'video',
            src: 'https://youtu.be/m4jzgqZu-4s',
            title: '📏 회로안내'
        });
    }

    if (i === 58) {
        lectureData.push({
            type: 'simulation',
            src: 'https://javalab.org/ko/electrostatic_induction/',
            title: '🧲 정전기 유도 현상 관찰'
        });
    }

    if (i === 114 || i === 115) {
        lectureData.push({
            type: 'callout',
            style: 'success',
            title: '단원 마무리 정리',
            content: '전기에 관한 용어를 다시 한번 복습해 보세요.'
        });
    }
}
