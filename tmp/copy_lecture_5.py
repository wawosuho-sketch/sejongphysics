import os
import re
import shutil

dir_source = r"G:\내 드라이브\1. 수업용\고등학교\1. 물리학\2026 물리1\수업\강의 슬라이드 이미지\5강 힘과 에너지 4차시.png"
dir_dest = r"G:\내 드라이브\1. 수업용\고등학교\1. 물리학\2026 물리1\수업\textbook-svelte\public\images\lecture_5"

if not os.path.exists(dir_dest):
    os.makedirs(dir_dest)

if not os.path.exists(dir_source):
    print(f"Source directory {dir_source} does not exist.")
else:
    for filename in os.listdir(dir_source):
        if filename.endswith(".png"):
            # Look for underscore followed by one or more digits at the end before extension
            match = re.search(r'_(\d+)\.png$', filename)
            if match:
                num = match.group(1)
                new_filename = f"slide_{num}.png"
                old_path = os.path.join(dir_source, filename)
                new_path = os.path.join(dir_dest, new_filename)
                try:
                    shutil.copy2(old_path, new_path)
                    print(f"Copied {filename} to {new_filename}")
                except Exception as e:
                    print(f"Error copying {filename}: {e}")
