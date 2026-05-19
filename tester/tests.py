# tester/tests.py

# ========= CONTRAT =========

def test_status_code(response):
    return response is not None and response.status_code == 200


def test_content_type_json(response):
    if response is None:
        return False
    return "application/json" in response.headers.get("Content-Type", "")


def test_json_is_dict(data):
    return isinstance(data, dict)


def test_has_ip_field(data):
    return isinstance(data, dict) and "ip" in data


# ========= ROBUSTESSE =========

def test_latency_reasonable(latency_ms):
    # seuil simple attendu dans un contexte API publique
    return latency_ms > 0 and latency_ms < 2000


def test_response_not_empty(data):
    return data is not None and len(data) > 0