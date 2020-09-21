"""
PEP: 8
Title: CouponDealsCook
Author: Kevin Cook
Status: Active
Type: Process
Created: 20-September-2020
Post: 20-September-2020
History:
"""
def calculate_price(price, cash_coupon, percent_coupon):

    tax = .06


    if price < 10:
        shipping = 5.95
    elif 10 <= price < 30:
        shipping = 7.95
    elif 30 <= price < 50:
        shipping = 11.95
    elif 50 <= price:
        shipping = 0

    price_minus_coupons = price-cash_coupon
    price_after_discount = price_minus_coupons - (price_minus_coupons*(percent_coupon/100))
    price_after_tax = price_after_discount-(price_after_discount*tax)
    order_total = price_after_tax+shipping
    order_total_formatted = round(order_total,2)

    return order_total_formatted

if __name__ == '__main__':

    prices = [9, 11, 31, 51]
    cash_coupons = [5,10]
    discounts = [10,15,20]
    for  x in prices:
      for y in cash_coupons:
          for z in discounts:
              print(calculate_price(x,y,z))