import datetime

def check_coupon(entered_code, correct_code, current_date, expiration_date):
    if entered_code is not correct_code:
        return False
    return False if datetime.datetime.strptime(current_date, "%B %d, %Y") > datetime.datetime.strptime(expiration_date, "%B %d, %Y") else True

print(check_coupon('123','123','September 5, 2014','October 1, 2014'))
print(check_coupon('123a','123','September 5, 2014','October 1, 2014'))

def check_coupon2(entered_code, correct_code, current_date, expiration_date):
    return entered_code is correct_code and datetime.datetime.strptime(current_date, "%B %d, %Y") <= datetime.datetime.strptime(expiration_date, "%B %d, %Y")

print(check_coupon2('123','123','September 5, 2014','October 1, 2014'))
print(check_coupon2('123a','123','September 5, 2014','October 1, 2014'))