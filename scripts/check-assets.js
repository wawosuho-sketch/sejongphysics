import { existsSync, readdirSync } from "fs";
import path from "path";
import { fileURLToPath, pathToFileURL } from "url";

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const publicDir = path.join(root, "public");
const dataDir = path.join(root, "src", "lib", "data");

function publicFile(urlPath) {
    const rel = urlPath.replace(/^\//, "").split("/").join(path.sep);
    return path.join(publicDir, rel);
}

const missing = [];

function expect(urlPath, label) {
    if (!urlPath || /^https?:/i.test(urlPath)) return;
    const normalized = urlPath.startsWith("/") ? urlPath : `/${urlPath}`;
    if (!existsSync(publicFile(normalized))) {
        missing.push(`${label}: ${normalized}`);
    }
}

const dataFiles = readdirSync(dataDir).filter((name) => name.endsWith(".js"));

for (const name of dataFiles) {
    const mod = await import(pathToFileURL(path.join(dataDir, name)).href);
    if (name === "textbooks.js") {
        for (const book of mod.textbooks) {
            for (const lecture of book.lectures) {
                if (lecture.image) {
                    expect(lecture.image, `${book.id}/${lecture.id} thumbnail`);
                }
            }
            for (const problem of book.problems || []) {
                expect(problem.pdf, `${book.id}/${problem.id} pdf`);
                if (problem.solution) {
                    expect(problem.solution, `${book.id}/${problem.id} solution`);
                }
            }
            for (const guide of book.guides || []) {
                expect(guide.pdf, `${book.id}/${guide.id} guide`);
            }
        }
        continue;
    }

    for (const item of mod.lectureData || []) {
        if (item?.src) expect(item.src, `${name} ${item.type || "item"}`);
    }
}

if (missing.length) {
    console.error(`Missing ${missing.length} public file(s):`);
    for (const line of missing) console.error(` - ${line}`);
    process.exit(1);
}

console.log(`Asset check passed (${dataFiles.length} data files).`);
