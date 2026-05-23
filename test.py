import requests

def wiki_summary(title, sentences=2):
    url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{title}"
    headers = {
        "User-Agent": "AIAssistant/1.0 (https://github.com/gpmakm/AI-Chatbot-Krishna)"
    }
    r = requests.get(url, headers=headers)
    if r.status_code == 200:
        data = r.json()
        return data.get("extract")
    else:
        print("Error:", r.status_code, r.text)
        return None

print(wiki_summary("Python_(programming_language)"))
