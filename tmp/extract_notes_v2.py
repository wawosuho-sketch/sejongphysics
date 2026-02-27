import requests
import re
import sys
import json

def extract_links_from_slide(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        html = response.text
        
        youtube_links = re.findall(r'(https?://(?:www\.)?(?:youtube\.com/watch\?v=|youtu\.be/)[a-zA-Z0-9_-]+)', html)
        javalab_links = re.findall(r'(https?://(?:www\.)?javalab\.org/ko/[a-zA-Z0-9_-]+/?)', html)
        phet_links = re.findall(r'(https?://(?:www\.)?phet\.colorado\.edu/[a-zA-Z0-9_/?=-]+)', html)

        print("=== YouTube Links ===")
        for link in set(youtube_links): print(link)
            
        print("\n=== Javalab Links ===")
        for link in set(javalab_links): print(link)
            
        print("\n=== PhET Links ===")
        for link in set(phet_links): print(link)

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Provide the presentation ID")
    else:
        pid = sys.argv[1]
        url = f"https://docs.google.com/presentation/d/{pid}/edit?usp=sharing"
        extract_links_from_slide(url)
