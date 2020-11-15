"""
PEP: 8
Title: customer
Author: Kevin Cook
Status: Active
Type: Process
Created: 11-1-2020
Post: 11-1-2020
History:
"""
import re

from Exceptions import CustIDError, InvalidName, PhoneError


class Customer:

    def __init__(self, last_name, first_name, phone_number, customer_id):
        if customer_id not in range (1000, 9999):
            raise CustIDError
        if not last_name.isalpha():
            raise InvalidName
        if not first_name.isalpha():
            raise InvalidName
        matched = re.match("[0-9][0-9][0-9]-[0-9][0-9][0-9]-[0-9][0-9][0-9][0-9]", phone_number)
        if bool(matched) == False:
            raise PhoneError
        self.last_name = last_name
        self.first_name = first_name
        self.phone_number = phone_number
        self.customer_id = customer_id

    def display(self):
        return str(self)

    def __str__(self):
        return 'Customer Id: ' + str(
            self.customer_id) + ', first name ' + self.first_name + ', last name ' + self.last_name + ', Phone:' + str(
            self.phone_number)