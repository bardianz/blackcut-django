
def get_shamsi_month(month_number):
    shamsi_months = {
        '01': 'فروردین',
        '02': 'اردیبهشت',
        '03': 'خرداد',
        '04': 'تیر',
        '05': 'مرداد',
        '06': 'شهریور',
        '07': 'مهر',
        '08': 'آبان',
        '09': 'آذر',
        '10': 'دی',
        '11': 'بهمن',
        '12': 'اسفند'
    }
    if month_number in shamsi_months:
        return shamsi_months[month_number]
    else:
        return "ماه نامعتبر"
    
