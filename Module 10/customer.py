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



class Customer:

    def __init__(self, last_name, first_name, address, phone_number, customer_id):
        self.last_name = last_name
        self.first_name = first_name
        self.address = address
        self.phone_number = phone_number

        check = isinstance(self.customer_id, int)
        if check:
            self.customer_id = customer_id
        else:
            raise(AttributeError)
            print("Customer object has no attribute 'Customer ID'")
    def display(self):
       return str(self)

    def __str__(self):
        return 'Customer Id: ' + str(self.customer_id) + ', first name ' + self.first_name + ', last name ' + self.last_name + ', address ' + self.address+ ', Phone:' + str(self.phone_number)