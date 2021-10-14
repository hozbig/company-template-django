def persian_number_convertor(my_str, lang_format):
    if lang_format == "fa":
        numbers = {
            "0": "۰",
            "1": "۱",
            "2": "۲",
            "3": "۳",
            "4": "۴",
            "5": "۵",
            "6": "۶",
            "7": "۷",
            "8": "۸",
            "9": "۹",
        }
    elif lang_format == "en":
        numbers = {
            "0": "0",
            "1": "1",
            "2": "2",
            "3": "3",
            "4": "4",
            "5": "5",
            "6": "6",
            "7": "7",
            "8": "8",
            "9": "9",
        }

    for e, p in numbers.items():
        my_str = my_str.replace(e, p)

    return my_str