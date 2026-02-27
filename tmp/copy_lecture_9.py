import os
import re
import shutil

src_dir = r"g:\내 드라이브\1. 수업용\고등학교\1. 물리학\2026 물리1\수업\강의 슬라이드 이미지\9강 전기와 자기 4차시.png"
dst_dir = r"g:\내 드라이브\1. 수업용\고등학교\1. 물리학\2026 물리1\수업\textbook-svelte\public\images\lecture_9"

# Create destination directory if it doesn't exist
os.makedirs(dst_dir, exist_ok=True)

for filename in os.listdir(src_dir):
    match = re.search(r'_(\d+)\.png$', filename)
    if match:
        slide_num = match.group(1)
        new_filename = f"slide_{slide_num}.png"
        src_path = os.path.join(src_dir, filename)
        dst_path = os.path.join(dst_dir, new_filename)
        shutil.copy2(src_path, dst_path)
        print(f"Copied {filename} -> {new_filename}")
