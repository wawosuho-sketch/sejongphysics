import { writable } from 'svelte/store';

// Default values
const defaultState = {
    isDrawingMode: false,
    activeColor: '#4f46e5', // Default pen color (Accent Blue)
    activeWidth: 3,         // Default pen width
    currentTool: 'pen',     // 'pen', 'highlighter', 'eraser'
    slideDrawings: {},      // Format: { "lectureId_slideIndex": "data:image/jpeg;base64,..." }
    currentLectureId: null, // Currently visible lecture
    currentSlideIndex: null // Currently visible slide
};

// Try to load saved drawings from localStorage
const storedData = typeof window !== 'undefined' ? localStorage.getItem('textbookLayoutDrawings') : null;
const initialState = storedData ? { ...defaultState, slideDrawings: JSON.parse(storedData) } : defaultState;

export const whiteboardStore = writable(initialState);

// Update which slide is currently in view (called by LecturePage)
export function updateCurrentSlide(lectureId, slideIndex) {
    whiteboardStore.update(s => ({ ...s, currentLectureId: lectureId, currentSlideIndex: slideIndex }));
}

// Helper function to save drawings to localStorage (JPEG compressed)
export function saveDrawing(lectureId, slideIndex, dataUrl) {
    whiteboardStore.update(state => {
        const key = `${lectureId}_${slideIndex}`;
        const newDrawings = { ...state.slideDrawings, [key]: dataUrl };
        localStorage.setItem('textbookLayoutDrawings', JSON.stringify(newDrawings));
        return { ...state, slideDrawings: newDrawings };
    });
}

// Helper function to clear a specific slide's drawing
export function clearDrawing(lectureId, slideIndex) {
    whiteboardStore.update(state => {
        const key = `${lectureId}_${slideIndex}`;
        const newDrawings = { ...state.slideDrawings };
        delete newDrawings[key];
        localStorage.setItem('textbookLayoutDrawings', JSON.stringify(newDrawings));
        return { ...state, slideDrawings: newDrawings };
    });
}
