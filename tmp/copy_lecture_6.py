import os
import shutil

# 강의 번호 설정
lecture_num = 6
original_dir = r"G:\내 드라이브\1. 수업용\고등학교\1. 물리학\2026 물리1\수업\강의 슬라이드 이미지\6강 전기와 자기 1차시.png"
target_dir = fr"G:\내 드라이브\1. 수업용\고등학교\1. 물리학\2026 물리1\수업\textbook-svelte\static\images\lecture_{lecture_num}"

# 대상 디렉토리 보장
if not os.path.exists(target_dir):
    os.makedirs(target_dir)

# 파일 목록 가져오기
files = os.listdir(original_dir)
# '6강 전기와 자기 1차시_N.png' 형식을 찾아서 N 숫자로 정렬
image_files = [f for f in files if f.endswith('.png') and '_' in f]

def get_slide_num(filename):
    try:
        # '6강 전기와 자기 1차시_123.png' -> '123'
        return int(filename.split('_')[-1].split('.')[0])
    except:
        return 9999

image_files.sort(key=get_slide_num)

print(f"총 {len(image_files)}개의 이미지를 복사합니다.")

for i, filename in enumerate(image_files, 1):
    src_path = os.path.join(original_dir, filename)
    # 목표 파일명: slide_N.png
    dest_filename = f"slide_{i}.png"
    dest_path = os.path.join(target_dir, dest_filename)
    
    shutil.copy2(src_path, dest_path)
    if i % 20 == 0:
        print(f"{i}개 복사 완료...")

print("모든 이미지 복사 및 이름 변경 완료!")
