from . import jalali
from .per_num import persian_number_convertor

def jalali_convertor(time, lang_format="fa", time_status="off"):
    lang_format_x = lang_format
    if lang_format_x == "fa":
        j_months = ["۱", "۲", "۳", "۴", "۵",
                    "۶", "۷", "۸", "۹", "۱۰", "۱۱", "۱۲"]
    elif lang_format_x == "en":
        j_months = ["1", "2", "3", "4", "5",
                    "6", "7", "8", "9", "10", "11", "12"]

    timeToStr = "{},{},{}".format(time.year, time.month, time.day)
    timeToTuple = jalali.Gregorian(timeToStr).persian_tuple()
    timeToList = list(timeToTuple)

    for index, month in enumerate(j_months):
        if timeToList[1] == index + 1:
            timeToList[1] = month
            break
        if time_status == "off":
            output = "{}/{}/{}".format(
                timeToList[0],
                timeToList[1],
                timeToList[2],
                time.hour,
                time.minute,
            )
        elif time_status == "on":
            output = "{}/{}/{} - {}:{}".format(
                timeToList[0],
                timeToList[1],
                timeToList[2],
                time.hour,
                time.minute,
            )

    return persian_number_convertor(output, lang_format=lang_format_x)
