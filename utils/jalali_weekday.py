from . import jalali

jalali_month = [
    "فروردین",
    "اردیبهشت",
    "خرداد",
    "تیر",
    "مهر",
    "آبان",
    "آذر",
    "دی",
    "بهمن",
    "اسفند",
]


def jalali_weekday_convertor(date):
    time_to_str = "{},{},{}".format(date.year, date.month, date.day)
    time_to_tuple = jalali.Gregorian(time_to_str).persian_tuple()
    time_to_list = list(time_to_tuple)
    time_to_list[1] = jalali_month[time_to_list[1] - 1] 

    output = "{} {} {}".format(time_to_list[2], time_to_list[1], time_to_list[0])
    return output

def jalali_numerical_convertor(date):
    time_to_tuple = jalali.Gregorian(date).persian_tuple()
    time_to_list = list(time_to_tuple)
    output = "{}-{}-{}".format(time_to_list[0], time_to_list[1], time_to_list[2])
    return output

def jalali_to_georgian(date):
    time_to_tuple = jalali.Persian(date).gregorian_tuple
    time_to_list = list(time_to_tuple)
    output = "{}-{}-{}".format(time_to_list[0], time_to_list[1], time_to_list[2])
    return output