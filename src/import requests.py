import requests

url = "https://vidcache.net:8161/a20250111FnkHnkTsDcg/video.mp4"
headers = {
    "User -Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    with open("video.mp4", "wb") as f:
        f.write(response.content)
else:
    print(f"Error: {response.status_code}")