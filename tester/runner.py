from tester.client import get
from tester.tests import test_status_ok, test_has_ip_field, test_latency

API_URL = "https://api.ipify.org?format=json"

def run_all_tests():
    response = get(API_URL)

    tests = [
        ("status_ok", test_status_ok(response)),
        ("has_ip", test_has_ip_field(response)),
        ("fast_response", test_latency(response))
    ]

    passed = sum(1 for _, r in tests if r)
    failed = len(tests) - passed

    return {
        "api": "ipify",
        "passed": passed,
        "failed": failed,
        "tests": tests
    }