from utils.persian_month import get_shamsi_month


def persian_date_string_convertor(date_str: str):
    try:
        date_str = str(date_str)
        year = date_str[:4]
        month = date_str[5:7]
        day = date_str[8:].lstrip('0')  
        persian_month = get_shamsi_month(month)
        return f"{day} {persian_month} {year}"

    except Exception as e:
        return f"مشکل در تبدیل تاریخ: {e}"
