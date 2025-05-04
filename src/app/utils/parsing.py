def get_text_from_attribute_list(data: list) -> list:
    for i in range(len(data)):
        data[i] = data[i].text
    return data
