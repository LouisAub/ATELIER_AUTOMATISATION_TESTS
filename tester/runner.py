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

API_URL = "https://api.ipify.org?format=json"


def run_all_tests():
    response, latency = get(API_URL)

    data = None
    if response is not None:
        try:
            data = response.json()
        except Exception:
            data = None

    tests = [
        ("status_code", test_status_code(response)),
        ("content_type_json", test_content_type_json(response)),
        ("json_is_dict", test_json_is_dict(data)),
        ("has_ip_field", test_has_ip_field(data)),
        ("latency_ok", test_latency_reasonable(latency)),
        ("response_not_empty", test_response_not_empty(data)),
    ]

    passed = sum(1 for _, ok in tests if ok)
    failed = len(tests) - passed

    status = "PASS" if failed == 0 else "FAIL"

    save_run(
        timestamp=time.strftime("%Y-%m-%d %H:%M:%S"),
        latency=latency,
        status=status
    )

    return {
        "status": status,
        "latency_ms": round(latency, 2),
        "passed": passed,
        "failed": failed,
        "tests": tests
    }