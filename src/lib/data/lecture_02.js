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
 * @property {string} [type_class]
 */

const baseImageName = '2강. 힘과 에너지 1차시(돌림힘과 평형)_';
const generateSlide = (num) => ({
    type: 'image',
    src: `/images/lecture_2/${baseImageName}${num}.png`
});

/** @type {LectureItem[]} */
export const lectureData = [];

for (let i = 1; i <= 60; i++) {
    // === 흐릿한 이미지(동영상/시뮬레이션 캡처본)는 건너뛰고 실제 컴포넌트로 대체 ===

    if (i === 7) {
        lectureData.push({
            type: 'video',
            src: 'https://www.youtube.com/embed/YwOg8CF6BYw',
            title: '📺 무게중심 관련 쇼츠 영상'
        });
        // 퀴즈도 7번 영상 바로 뒤에 이어서 나오게 합니다.
        lectureData.push({
            type: 'quiz',
            question: 'Q. 야구 배트를 휘두를 때, 얇은 손잡이 부분을 잡을 때와 두꺼운 배트 끝부분을 잡을 때 언제가 더 휘두르기 힘들까요?',
            answer: '정답은 두꺼운 부분을 잡을 때입니다! 회전축(손목)에서 무게중심이 멀어질수록 회전시키기 위한 "돌림힘"이 더 많이 필요하기 때문입니다.',
            title: '잠깐 멈추고 생각하기! 💡'
        });
        continue; // 7번 슬라이드 이미지 배제
    }

    if (i === 26) {
        lectureData.push({
            type: 'simulation',
            src: 'https://javalab.org/ko/gear/',
            title: '⚙️ 톱니바퀴 시뮬레이션 (자바실험실)',
            height: '850'
        });
        continue; // 26번 슬라이드 이미지 배제
    }

    if (i === 32) {
        lectureData.push({
            type: 'simulation',
            src: 'https://phet.colorado.edu/sims/html/balancing-act/latest/balancing-act_ko.html',
            title: '직접 해보는 시소 평행(Balancing Act) 실험'
        });
        continue; // 32번 슬라이드 이미지는 화면에 띄우지 않음
    }

    if (i === 43) {
        lectureData.push({
            type: 'video',
            src: 'https://www.youtube.com/embed/989fpCYaP34',
            title: '📺 텐세그리티 구조의 원리 쇼츠'
        });
        continue; // 43번 슬라이드 이미지 배제
    }

    if (i === 44) {
        lectureData.push({
            type: 'video',
            src: 'https://www.youtube.com/embed/RaGUW1d0w8g',
            title: '📺 무게중심과 안정성 원리 영상'
        });
        continue; // 44번 슬라이드 이미지 배제
    }

    // 기본 슬라이드 출력 (60번 텍스트 슬라이드 포함)
    lectureData.push(generateSlide(i));

    // === 분기점마다 퀴즈 추가 (스크롤 중간중간 💡 팝업) ===
    // (7번 퀴즈는 영상 직후에 위에서 바로 삽입)

    if (i === 51) {
        lectureData.push({
            type: 'quiz',
            question: 'Q. 건물이 무너지지 않고, 자동차가 코너를 돌 때 뒤집히지 않으려면 어떻게 설계해야 할까요?',
            answer: '물체의 "무게중심이 낮을수록", 그리고 바닥과 닿는 "밑넓이가 넓을수록" 안정성이 커집니다!',
            title: '잠깐 멈추고 생각하기! 💡'
        });
    }

    // 마지막 정리 Callout 첨부
    if (i === 60) {
        lectureData.push({
            type: 'callout',
            content: '🎉 2강(돌림힘과 평형)을 마무리했습니다! 오늘 배운 알짜힘=0, 알짜돌림힘=0 의 조건은 세상 모든 구조물이 안전하게 서 있는 핵심 원리입니다.',
            style: 'success'
        });
    }
}
