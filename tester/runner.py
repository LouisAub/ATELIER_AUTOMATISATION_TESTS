from tester.client import get
from tester.tests import (
    test_status_code,
    test_content_type_json,
    test_json_is_dict,
    test_has_ip_field,
    test_latency_reasonable,
    test_response_not_empty
)

from storage import save_run
import time
import statistics

API_URL = "https://api.ipify.org?format=json"


def run_all_tests():

    N = 10
    latencies = []
    errors = 0

    response = None
    data = None

    for _ in range(N):
        response, latency = get(API_URL)
        latencies.append(latency)

        if response is None or response.status_code != 200:
            errors += 1

    if response is not None:
        try:
            data = response.json()
        except:
            data = None

    tests = [
        ("status_code", test_status_code(response)),
        ("content_type_json", test_content_type_json(response)),
        ("json_is_dict", test_json_is_dict(data)),
        ("has_ip_field", test_has_ip_field(data)),
        ("latency_ok", test_latency_reasonable(sum(latencies)/len(latencies))),
        ("response_not_empty", test_response_not_empty(data)),
    ]

    passed = sum(1 for _, ok in tests if ok)
    failed = len(tests) - passed

    status = "PASS" if failed == 0 else "FAIL"

    avg_latency = sum(latencies) / len(latencies)
    p95_latency = statistics.quantiles(latencies, n=100)[94]
    error_rate = errors / N

    save_run(
        timestamp=time.strftime("%Y-%m-%d %H:%M:%S"),
        latency=avg_latency,
        status=status
    )

    return {
        "status": status,
        "passed": passed,
        "failed": failed,
        "tests": tests,
        "qos": {
            "avg_latency": round(avg_latency, 2),
            "p95_latency": round(p95_latency, 2),
            "error_rate": round(error_rate, 2),
            "samples": N
        }
    }