import { writable } from 'svelte/store';

// Default values
const defaultState = {
    isDrawingMode: false,
    activeColor: '#4f46e5', // Default pen color (Accent Blue)
    activeWidth: 3,         // Default pen width
    currentTool: 'pen',     // 'pen', 'highlighter', 'eraser'
    slideDrawings: {}       // Format: { "lectureId_slideIndex": "data:image/png;base64,..." }
};

// Try to load saved drawings from localStorage
const storedData = typeof window !== 'undefined' ? localStorage.getItem('textbookLayoutDrawings') : null;
const initialState = storedData ? { ...defaultState, slideDrawings: JSON.parse(storedData) } : defaultState;

export const whiteboardStore = writable(initialState);

// Helper function to save drawings to localStorage
export function saveDrawing(lectureId, slideIndex, dataUrl) {
    whiteboardStore.update(state => {
        const key = `${lectureId}_${slideIndex}`;
        const newDrawings = { ...state.slideDrawings, [key]: dataUrl };
        localStorage.setItem('textbookLayoutDrawings', JSON.stringify(newDrawings));
        return { ...state, slideDrawings: newDrawings };
    });
}

// Helper function to clear a drawing
export function clearDrawing(lectureId, slideIndex) {
    whiteboardStore.update(state => {
        const key = `${lectureId}_${slideIndex}`;
        const newDrawings = { ...state.slideDrawings };
        delete newDrawings[key];
        localStorage.setItem('textbookLayoutDrawings', JSON.stringify(newDrawings));
        return { ...state, slideDrawings: newDrawings };
    });
}
