from checker import check_api

print("=" * 50)
print("🌐 API Status Checker")
print("=" * 50)

url = input("\nEnter website/API URL: ")

if not url.startswith(("http://", "https://")):
    url = "https://" + url

check_api(url)
