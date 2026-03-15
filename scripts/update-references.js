import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const FILES_TO_UPDATE = [
    'src/lib/pages/Home.svelte',
    ...Array.from({ length: 12 }, (_, i) => `src/lib/data/lecture_${String(i + 1).padStart(2, '0')}.js`)
].map(f => path.join(__dirname, '../', f));

FILES_TO_UPDATE.forEach(filePath => {
    if (fs.existsSync(filePath)) {
        console.log(`Updating references in: ${filePath}`);
        const content = fs.readFileSync(filePath, 'utf8');
        const updatedContent = content.replace(/\.png/g, '.webp');
        fs.writeFileSync(filePath, updatedContent);
        console.log(`  Done.`);
    } else {
        console.log(`File not found, skipping: ${filePath}`);
    }
});
