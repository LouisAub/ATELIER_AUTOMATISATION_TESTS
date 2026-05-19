def test_status_ok(response):
    return response["status_code"] == 200


def test_has_ip_field(response):
    return response["json"] is not None and "ip" in response["json"]


def test_latency(response):
    return response["latency"] < 1000