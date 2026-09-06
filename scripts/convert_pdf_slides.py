import fitz # PyMuPDF
from PIL import Image
import os
import io

pdf_path = r"r:\textbook-svelte\tmp\presentation.pdf"
output_dir = r"r:\textbook-svelte\public\images\slides\mech_01"

os.makedirs(output_dir, exist_ok=True)

doc = fitz.open(pdf_path)
print(f"Total pages in presentation PDF: {len(doc)}")

# Render each slide at 2x resolution (crisp text & math) and save as WebP
matrix = fitz.Matrix(2.0, 2.0)

for i, page in enumerate(doc):
    pix = page.get_pixmap(matrix=matrix, alpha=False)
    img_data = pix.tobytes("png")
    
    # Convert PNG bytes to Pillow Image and save as optimized WebP
    img = Image.open(io.BytesIO(img_data))
    slide_filename = f"slide_{i+1:02d}.webp"
    save_path = os.path.join(output_dir, slide_filename)
    
    img.save(save_path, "WEBP", quality=82)
    print(f"Rendered Slide {i+1:02d} -> {slide_filename} ({os.path.getsize(save_path)//1024} KB)")

print("All presentation slides converted to WebP successfully!")
