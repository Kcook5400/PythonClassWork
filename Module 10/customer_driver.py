
from customer import Customer

Cust1=Customer("Smith", "John", "123 Fake St", "555-123-5555", 12)
print(Cust1.display())

Cust2=Customer("Smith", "Jane", "123 Fake St", "555-123-5555", "NOTanINT")
print(Cust2.display())