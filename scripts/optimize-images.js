import sharp from 'sharp';
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const TARGET_DIR = path.join(__dirname, '../public/images');

async function convertDir(dir) {
    const entries = fs.readdirSync(dir, { withFileTypes: true });

    for (const entry of entries) {
        const fullPath = path.join(dir, entry.name);
        if (entry.isDirectory()) {
            await convertDir(fullPath);
        } else if (entry.isFile() && entry.name.toLowerCase().endsWith('.png')) {
            const webpPath = fullPath.replace(/\.png$/i, '.webp');
            
            console.log(`Converting: ${entry.name} ...`);
            try {
                await sharp(fullPath)
                    .webp({ quality: 80 })
                    .toFile(webpPath);
                
                // Only delete if conversion succeeded
                fs.unlinkSync(fullPath);
                console.log(`  Success! Deleted original PNG.`);
            } catch (err) {
                console.error(`  Error converting ${fullPath}:`, err);
            }
        }
    }
}

console.log('Starting WebP conversion in:', TARGET_DIR);
convertDir(TARGET_DIR)
    .then(() => console.log('All images converted successfully!'))
    .catch(err => console.error('Conversion failed:', err));
