export const textbooks = [
  {
    id: "physics",
    name: "물리학",
    badge: "PHYSICS COURSE",
    description: "미래를 여는 물리학 교과서",
    school: "세종고등학교",
    homeworkUrl: "https://clipo.ai/students/homeworks/4OA4S9_cTE-y96CD1o3ySQ",
    problems: [
      {
        id: "accel",
        title: "등가속도 운동",
        pdf: "resources/등가속도.pdf",
        solution: "resources/등가속도 해설.pdf"
      },
      {
        id: "force",
        title: "힘과 운동",
        pdf: "resources/힘과운동.pdf",
        solution: "resources/힘과운동 해설.pdf"
      },
      {
        id: "energy",
        title: "에너지 보존",
        pdf: "resources/역학적에너지보존.pdf",
        solution: "resources/일-에너지보존 해설.pdf"
      }
    ],
    lectures: [
      {
        id: "01",
        fullId: "01",
        title: "1강. 물리학이란",
        subtitle: "물리학의 정의와 발전 맛보기",
        tag: "I. 역학 파트",
        image: "/images/thumbnails/lecture_01.webp",
        accent: "#4f46e5"
      },
      {
        id: "02",
        fullId: "02",
        title: "2강. 힘과 에너지 (1차시)",
        subtitle: "돌림힘과 구조물의 평형 조건",
        tag: "I. 역학 파트",
        image: "/images/thumbnails/lecture_02.webp",
        accent: "#6366f1"
      },
      {
        id: "03",
        fullId: "03",
        title: "3강. 힘과 에너지 (2차시)",
        subtitle: "힘과 운동",
        tag: "I. 역학 파트",
        image: "/images/thumbnails/lecture_03.webp",
        accent: "#818cf8"
      },
      {
        id: "04",
        fullId: "04",
        title: "4강. 힘과 에너지 (3차시)",
        subtitle: "일과 에너지",
        tag: "I. 역학 파트",
        image: "/images/thumbnails/lecture_04.webp",
        accent: "#a78bfa"
      },
      {
        id: "05",
        fullId: "05",
        title: "5강. 힘과 에너지 (4차시)",
        subtitle: "충격량과 운동량의 관계",
        tag: "I. 역학 파트",
        image: "/images/thumbnails/lecture_05.webp",
        accent: "#c084fc"
      },
      {
        id: "06",
        fullId: "06",
        title: "6강. 전기와 자기 (1차시)",
        subtitle: "전기력과 마찰전기, 정전기 유도",
        tag: "II. 전자기 파트",
        image: "/images/thumbnails/lecture_06.webp",
        accent: "#e879f9"
      },
      {
        id: "07",
        fullId: "07",
        title: "7강. 전기와 자기 (2차시)",
        subtitle: "축전기",
        tag: "II. 전자기 파트",
        image: "/images/thumbnails/lecture_07.webp",
        accent: "#f43f5e"
      },
      {
        id: "08",
        fullId: "08",
        title: "8강. 전기와 자기 (3차시)",
        subtitle: "자기 현상과 로렌츠 힘",
        tag: "II. 전자기 파트",
        image: "/images/thumbnails/lecture_08.webp",
        accent: "#0ea5e9"
      },
      {
        id: "09",
        fullId: "09",
        title: "9강. 전기와 자기 (4차시)",
        subtitle: "전기자기 유도",
        tag: "II. 전자기 파트",
        image: "/images/thumbnails/lecture_09.webp",
        accent: "#f59e0b"
      },
      {
        id: "10",
        fullId: "10",
        title: "10강. 빛과 물질 (1차시)",
        subtitle: "빛의 파동성 (간섭과 편광)",
        tag: "III. 빛과 물질 파트",
        image: "/images/thumbnails/lecture_10.webp",
        accent: "#10b981"
      },
      {
        id: "11",
        fullId: "11",
        title: "11강. 빛과 물질 (2차시)",
        subtitle: "기하 광학 (렌즈와 거울)",
        tag: "III. 빛과 물질 파트",
        image: "/images/thumbnails/lecture_11.webp",
        accent: "#059669"
      },
      {
        id: "12",
        fullId: "12",
        title: "12강. 빛과 물질 (3차시)",
        subtitle: "빛의 입자성 (광전 효과와 콤프턴 산란)",
        tag: "III. 빛과 물질 파트",
        image: "/images/thumbnails/lecture_12.webp",
        accent: "#047857"
      }
    ]
  },
  {
    id: "mechanics",
    name: "역학과 에너지",
    badge: "MECHANICS & ENERGY",
    description: "물체의 운동과 에너지를 탐구하는 역학과 에너지 교과서",
    school: "세종고등학교",
    homeworkUrl: "https://clipo.ai/students/homeworks/4OA4S9_cTE-y96CD1o3ySQ",
    problems: [
      {
        id: "mech_motion",
        title: "힘과 평형",
        pdf: "resources/mechanics/힘과평형.pdf",
        solution: "resources/mechanics/힘과평형 해설.pdf"
      },
      {
        id: "mech_law",
        title: "운동의 법칙",
        pdf: "resources/mechanics/운동의법칙.pdf",
        solution: "resources/mechanics/운동의법칙 해설.pdf"
      },
      {
        id: "mech_energy",
        title: "역학적 에너지 보존",
        pdf: "resources/mechanics/역학적에너지보존.pdf",
        solution: "resources/mechanics/역학적에너지보존 해설.pdf"
      }
    ],
    lectures: [
      {
        id: "mech_01",
        fullId: "mech_01",
        title: "1강. 역학과 에너지 (역학 파트 전체)",
        subtitle: "벡터, 포물선, 원운동, 에너지 보존, 단진자의 완벽한 통합",
        tag: "I. 역학 파트",
        image: "/images/thumbnails/mech_01.webp",
        accent: "#ef4444"
      },
      {
        id: "mech_02",
        fullId: "mech_02",
        title: "2강. 특수상대성이론",
        subtitle: "상대성 원리, 광속 불변, 시간 지연, 길이 수축 및 질량-에너지 동등성",
        tag: "I. 시공간과 상대성",
        image: "/images/slides/mech_02/slide_01.webp",
        accent: "#f97316"
      },
      {
        id: "mech_03",
        fullId: "mech_03",
        title: "3강. 운동량과 충격량",
        subtitle: "충돌 현상과 운동량 보존 법칙",
        tag: "I. 힘과 운동",
        image: "/images/thumbnails/mech_03.webp",
        accent: "#eab308"
      },
      {
        id: "mech_04",
        fullId: "mech_04",
        title: "4강. 열역학 법칙과 에너지",
        subtitle: "열역학 제1법칙과 열기관의 효율",
        tag: "II. 열과 에너지",
        image: "/images/thumbnails/mech_04.webp",
        accent: "#10b981"
      }
    ]
  }
];

// Helper function to find a lecture's metadata by ID (supports "01", "physics_01", "mech_01", etc.)
export function getLectureMeta(lectureId) {
  for (const book of textbooks) {
    for (const lec of book.lectures) {
      if (lec.id === lectureId || lec.fullId === lectureId) {
        return {
          title: lec.title,
          subtitle: lec.subtitle,
          bookId: book.id,
          bookName: book.name
        };
      }
    }
  }

  // Fallback for legacy 01-12 IDs if not matched above
  const paddedId = String(lectureId).padStart(2, '0');
  const found = textbooks[0].lectures.find(l => l.id === paddedId || l.id === lectureId);
  if (found) {
    return {
      title: found.title,
      subtitle: found.subtitle,
      bookId: textbooks[0].id,
      bookName: textbooks[0].name
    };
  }

  return {
    title: `${lectureId}강`,
    subtitle: "물리학 강의 자료",
    bookId: "physics",
    bookName: "물리학"
  };
}
