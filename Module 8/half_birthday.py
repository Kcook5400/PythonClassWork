
from datetime import datetime, timedelta
from time import strftime


def half_birthday(birthday):
    six_months = datetime.strptime(str(birthday), '%m/%d/%Y')
    half_birthday = six_months + timedelta(6*30)

    return half_birthday.strftime('%m/%d/%Y')

