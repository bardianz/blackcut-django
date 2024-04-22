from datetime import datetime,timedelta
from utils.persian_weekday import convert_to_persian_weekday


def date_generator(days_number:int):
    current_datetime = datetime.now()
    dates_list = []
    for i in range(days_number):
        future_date = current_datetime + timedelta(days=i)
        dates_list.append(future_date)
    print(dates_list)
    return dates_list




def generate_date_list_with_persian_weekday(dates_list):
    dates_weekday_list = []
    for date in dates_list:
        formatted_date = convert_to_persian_weekday(date)
        dates_weekday_list.append(formatted_date)
    return dates_weekday_list


# def persian_weekday_generator(dates_list:list):
#     persian_weekdays = {
#         "Monday": "دوشنبه",
#         "Tuesday": "سه‌شنبه",
#         "Wednesday": "چهارشنبه",
#         "Thursday": "پنج‌شنبه",
#         "Friday": "جمعه",
#         "Saturday": "شنبه",
#         "Sunday": "یک‌شنبه"
#     }
#     dates_weekday_list = []
#     for i in dates_list:
#         formatted_date = persian_weekdays[i.strftime("%A")]
#         dates_weekday_list.append(formatted_date)
#     return dates_weekday_list



def date_dict_with_persian_weekday(days_number):
    dates_list = date_generator(days_number)
    dates_weekday_list = generate_date_list_with_persian_weekday(dates_list)
    result = []
    for weekday, date in zip(dates_weekday_list, dates_list):
        formatted_date = date.strftime('%Y-%m-%d')
        result.append({'weekday':weekday, "date":date , "formatted_date":formatted_date,})
    return result



def is_future_date(date):
    return True
    """
    Checks if the given date is in the future compared to the current date.
    
    Args:
        date (str): The date to be checked in the format "YYYY-MM-DD".
        
    Returns:
        bool: True if the given date is in the future, False otherwise.
    """

    today_date = datetime.now().strftime("%Y-%m-%d")
    selected_date = datetime.strptime(str(date), "%Y-%m-%d").date()
    today_date = datetime.strptime(today_date, '%Y-%m-%d').date()

    if selected_date >= today_date:
        return True
    
    else : return False