import requests
import time


def check_api(url):
    try:
        start = time.time()

        response = requests.get(url, timeout=10)

        end = time.time()

        response_time = round(end - start, 3)

        print("\n📊 Results")
        print("-" * 50)
        print(f"URL           : {url}")
        print(f"Status        : {'✅ UP' if response.ok else '❌ DOWN'}")
        print(f"Status Code   : {response.status_code}")
        print(f"Response Time : {response_time} seconds")

    except requests.exceptions.RequestException as e:
        print("\n❌ Failed to connect.")
        print(e)
