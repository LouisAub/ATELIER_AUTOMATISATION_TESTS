import requests
import time

def get(url, timeout=3):
    start = time.time()

    try:
        r = requests.get(url, timeout=timeout)
        latency = (time.time() - start) * 1000

        return {
            "status_code": r.status_code,
            "json": r.json() if "application/json" in r.headers.get("Content-Type", "") else None,
            "latency": latency
        }

    except Exception as e:
        return {
            "status_code": None,
            "json": None,
            "latency": 0,
            "error": str(e)
        }