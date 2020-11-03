"""
PEP: 8
Title: invoice
Author: Kevin Cook
Status: Active
Type: Process
Created: 11-1-2020
Post: 11-1-2020
History:
"""

from numpy import double

class Invoice:

    def __init__(self, last_name, first_name, address, phone_number, invoice_id, customer_id, items_with_price=''):
        self.last_name = last_name
        self.first_name = first_name
        self.address = address
        self.phone_number = phone_number
        self.customer_id = customer_id
        self.invoice_id = invoice_id
        self.items_with_price = {}


    def add_item(self,data):
        self.items_with_price.update(data)

    def __str__(self):
        return "last name:" + "first name" + "address: " + "phone: " + "customer id: " +"invoice id:"
    def create_invoice(self):
        print(self.items_with_price)
        total = sum(self.items_with_price.values())*1.06
        print("{:.2f}".format(total))