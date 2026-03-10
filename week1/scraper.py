import typing as _t
import requests
import time


def fetch_website_contents(url: str, *, timeout: int = 10, retries: int = 3) -> str:
    """
    Fetch the raw text contents of a web page with retry logic.
    """

    if not isinstance(url, str) or not url.strip():
        raise ValueError("url must be a non-empty string")

    headers: _t.Dict[str, str] = {
        "User-Agent": (
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/123.0 Safari/537.36"
        )
    }

    for attempt in range(retries):
        try:
            response = requests.get(url, headers=headers, timeout=timeout)

            # Handle rate limiting
            if response.status_code == 429:
                print("Rate limited. Waiting before retry...")
                time.sleep(5)
                continue

            response.raise_for_status()
            return response.text

        except requests.RequestException as e:
            if attempt == retries - 1:
                raise e
            print(f"Request failed. Retrying ({attempt+1}/{retries})...")
            time.sleep(3)

    raise RuntimeError("Failed to fetch website after retries")