import jsonpath


def extract(resp, attr_name, exp):
    try:
        resp.json = resp.json()

    except Exception:
        resp.json = {}

    attr = getattr(resp, attr_name)
    res = jsonpath.jsonpath(attr, exp)

    return res[0]


