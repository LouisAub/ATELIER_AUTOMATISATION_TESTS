from tester.client import get_ip

# 1. HTTP status OK
def test_status_code():
    r, _ = get_ip()
    return r is not None and r.status_code == 200


# 2. réponse JSON valide
def test_is_json():
    r, _ = get_ip()
    try:
        r.json()
        return True
    except:
        return False


# 3. champ obligatoire présent
def test_has_ip_field():
    r, _ = get_ip()
    data = r.json()
    return "ip" in data


# 4. type du champ IP
def test_ip_type():
    r, _ = get_ip()
    data = r.json()
    return isinstance(data.get("ip"), str)


# 5. latence raisonnable (< 1000ms)
def test_latency():
    r, latency = get_ip()
    return latency < 1000


# 6. réponse stable (non vide)
def test_not_empty():
    r, _ = get_ip()
    return bool(r.json())