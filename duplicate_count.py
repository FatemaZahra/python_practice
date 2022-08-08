def duplicate_count(text):
    count = 0
    dict = {}
    lower_text = text.lower()
    for alpha in range(0, len(lower_text)):
        dict[lower_text[alpha]] = 0

    for key in dict:
        for i in range(0, len(lower_text)):
            if (key == lower_text[i]):
                dict[key] = dict[key] + 1

    for key in dict:
        if (dict[key] > 1):
            count = count + 1

    return count