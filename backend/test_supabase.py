import httpx
from app.core.config import settings

url = f"{settings.SUPABASE_URL}/rest/v1/"

headers = {
    "apikey": settings.SUPABASE_KEY,
    "Authorization": f"Bearer {settings.SUPABASE_KEY}",
}

try:
    response = httpx.get(url, headers=headers, timeout=20)

    print("Status code:", response.status_code)

    if response.status_code == 200:
        print("Successfully connected to Supabase!")
    else:
        print("Supabase responded, but check the response:")
        print(response.text)

except Exception as error:
    print("Connection failed:", error)