import { writable } from 'svelte/store';

const STORAGE_KEY = 'textbookLayoutDrawings';
const STORAGE_FULL_MESSAGE =
    '이 태블릿의 필기 저장 공간이 가득 찼습니다. 💾 버튼으로 필기를 파일로 내보낸 뒤 공간을 비워 주세요.';

const defaultState = {
    isDrawingMode: false,
    activeColor: '#4f46e5',
    activeWidth: 3,
    currentTool: 'pen',
    slideDrawings: {},
    currentLectureId: null,
    currentSlideIndex: null,
    currentDrawingKey: null,
    currentLegacyKey: null,
    storageWarning: ''
};

const storedData = typeof window !== 'undefined' ? localStorage.getItem(STORAGE_KEY) : null;
const initialState = storedData
    ? { ...defaultState, slideDrawings: JSON.parse(storedData) }
    : defaultState;

export const whiteboardStore = writable(initialState);

function persist(drawings) {
    try {
        localStorage.setItem(STORAGE_KEY, JSON.stringify(drawings));
        return '';
    } catch {
        return STORAGE_FULL_MESSAGE;
    }
}

export function readDrawing(drawings, key, legacyKey) {
    if (!drawings) return undefined;
    if (key && drawings[key]) return drawings[key];
    if (legacyKey && drawings[legacyKey]) return drawings[legacyKey];
    return undefined;
}

export function updateCurrentSlide(lectureId, slideIndex, drawingKey = null, legacyKey = null) {
    whiteboardStore.update(s => ({
        ...s,
        currentLectureId: lectureId,
        currentSlideIndex: slideIndex,
        currentDrawingKey: drawingKey,
        currentLegacyKey: legacyKey
    }));
}

/** 예전 순번 키에 있던 필기를 파일명 키로 한 번 옮깁니다. */
export function migrateDrawing(key, legacyKey) {
    if (!key || !legacyKey) return;
    whiteboardStore.update(state => {
        if (!state.slideDrawings[legacyKey] || state.slideDrawings[key]) return state;
        const next = { ...state.slideDrawings, [key]: state.slideDrawings[legacyKey] };
        delete next[legacyKey];
        return { ...state, slideDrawings: next, storageWarning: persist(next) };
    });
}

export function saveDrawing(key, legacyKey, dataUrl) {
    whiteboardStore.update(state => {
        const next = { ...state.slideDrawings, [key]: dataUrl };
        if (legacyKey) delete next[legacyKey];
        return { ...state, slideDrawings: next, storageWarning: persist(next) };
    });
}

export function clearDrawing(key, legacyKey) {
    whiteboardStore.update(state => {
        const next = { ...state.slideDrawings };
        if (key) delete next[key];
        if (legacyKey) delete next[legacyKey];
        return { ...state, slideDrawings: next, storageWarning: persist(next) };
    });
}
