/**
 * 원본 PPT 번호는 스트림 순번과 다릅니다.
 * 파일명의 slide_84 / _84 가 교사가 말하는 슬라이드 번호입니다.
 */
export function sourceSlideFromItem(item) {
    if (!item?.src || /^https?:/i.test(item.src)) return null;
    if (Number.isInteger(item.sourceSlide)) return item.sourceSlide;
    const file = item.src.split("/").pop() || "";
    const match = file.match(/(?:^|slide_|_)(\d+)\.(?:webp|png|jpe?g)$/i);
    return match ? Number(match[1]) : null;
}

/**
 * 필기 저장 키. 이미지는 파일명에 고정해서, 퀴즈를 끼워 넣어도
 * 학생 필기가 다음 슬라이드로 밀리지 않게 합니다.
 * legacy 는 예전 스트림 순번 키입니다.
 */
export function drawingKeys(lectureId, item, streamIndex) {
    const legacy = `${lectureId}_${streamIndex}`;
    const src = item?.src || "";
    let id;

    if (src && !/^https?:/i.test(src)) {
        id = `file:${src.split("/").pop()}`;
    } else if (src) {
        id = `${item?.type || "embed"}:${src}`;
    } else if (item?.type === "quiz") {
        id = `quiz:${item.question || streamIndex}`;
    } else if (item?.type === "callout") {
        id = `callout:${item.title || ""}:${item.content || ""}`;
    } else if (item?.type === "section_header") {
        id = `section:${item.chapter || ""}:${item.title || ""}`;
    } else if (item?.type === "title") {
        id = `title:${item.text || streamIndex}`;
    } else {
        id = `${item?.type || "item"}:${streamIndex}`;
    }

    return { key: `${lectureId}::${id}`, legacy };
}
