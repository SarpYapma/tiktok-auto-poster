import os

client_key = os.getenv("TIKTOK_CLIENT_KEY")
redirect_uri = os.getenv("TIKTOK_REDIRECT_URI")

url = f"https://www.tiktok.com/v2/auth/authorize/?client_key={client_key}&response_type=code&scope=video.publish&redirect_uri={redirect_uri}"

print("Bu linki aç:")
print(url)