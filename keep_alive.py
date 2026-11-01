import requests
import os

COOKIE_VALUE = os.environ.get("WISP_COOKIE") # Берем из секретов

def keep_alive():
    url = "https://wispbyte.com/client"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Cookie": f"session={COOKIE_VALUE}" # Имя cookie может отличаться, проверь в браузере
    }
    try:
        response = requests.get(url, headers=headers, timeout=15)
        if response.status_code == 200 and "login" not in response.url.lower():
            print("✅ Успешно зашёл, сервер активен.")
        else:
            print(f"❌ Не удалось войти. Код: {response.status_code}. Cookie мог истечь.")
    except Exception as e:
        print(f"⚠️ Ошибка сети: {e}")

if __name__ == "__main__":
    keep_alive()
