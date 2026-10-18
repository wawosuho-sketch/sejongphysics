"""구글 슬라이드 PDF를 2배 WebP 슬라이드로 변환합니다.

예시:
  python scripts/convert_pdf_slides.py tmp/presentation_mech04.pdf public/images/slides/mech_04 --thumbnail public/images/thumbnails/mech_04.webp
"""

import argparse
import io
import os
import re
import shutil

import fitz  # PyMuPDF
from PIL import Image


def main():
    parser = argparse.ArgumentParser(description="Render a slide PDF to 2x WebP files.")
    parser.add_argument("pdf", help="내보낸 프레젠테이션 PDF 경로")
    parser.add_argument("output_dir", help="slide_01.webp 를 저장할 폴더")
    parser.add_argument("--scale", type=float, default=2.0, help="렌더 배율 (기본 2.0)")
    parser.add_argument("--quality", type=int, default=82, help="WebP 품질 (기본 82)")
    parser.add_argument("--thumbnail", help="첫 슬라이드를 복사할 썸네일 경로")
    args = parser.parse_args()

    os.makedirs(args.output_dir, exist_ok=True)
    removed = 0
    for name in os.listdir(args.output_dir):
        if re.fullmatch(r"slide_\d+\.webp", name):
            os.remove(os.path.join(args.output_dir, name))
            removed += 1
    if removed:
        print(f"Removed {removed} previous slide_XX.webp file(s). Custom diagrams were kept.")

    doc = fitz.open(args.pdf)
    print(f"Total pages: {len(doc)}")
    matrix = fitz.Matrix(args.scale, args.scale)
    first_path = None

    for i, page in enumerate(doc):
        pix = page.get_pixmap(matrix=matrix, alpha=False)
        img = Image.open(io.BytesIO(pix.tobytes("png")))
        filename = f"slide_{i + 1:02d}.webp"
        save_path = os.path.join(args.output_dir, filename)
        img.save(save_path, "WEBP", quality=args.quality)
        if first_path is None:
            first_path = save_path
        print(f"Rendered {i + 1:02d} -> {filename} ({os.path.getsize(save_path) // 1024} KB)")

    if args.thumbnail and first_path:
        os.makedirs(os.path.dirname(os.path.abspath(args.thumbnail)), exist_ok=True)
        shutil.copyfile(first_path, args.thumbnail)
        print(f"Thumbnail copied to {args.thumbnail}")

    print("Done.")


if __name__ == "__main__":
    main()
