def ignore_dict_element(dct: dict, k: str) -> dict:
    del dct[k]
    return dct


def delete_nones_from_dict(dct: dict) -> dict:
    return {k: v for k, v in dct.items() if v is not None}
