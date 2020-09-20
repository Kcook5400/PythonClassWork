


platinum_cost = 60
gold_cost = platinum_cost-10
silver_cost = platinum_cost-20
bronze_cost = platinum_cost-30

signup = str(input("Would you like to sign up for the Programmers Monthly Toolkit Subscription Box?"))
if signup == "Yes":
    membership_level = str((input("Great! Please select your level of membership: \nPlatinum\nGold\nSilver\nBronze\nFree trial")))
    if membership_level == "Platinum":
        print("Great choice! You have chosen " + membership_level + ", our highest tier! \nEach month, you will recieve: a t-shirt, stickers, figurine and programming books!")
        print("Your cost is:$" + str(platinum_cost))
    elif membership_level == "Gold":
        print("Great choice! You have chosen " + membership_level + ", one of our top tiers! \nEach month, you will recieve: stickers, figurine and programming books!")
        print("Your cost is:$" + str(gold_cost))
    elif membership_level == "Silver":
        print("Great choice! You have chosen " + membership_level + ", a good tier! \nEach month, you will recieve: a figurine and programming books!")
        print("Your cost is:$" + str(silver_cost))
    elif membership_level == "Bronze":
        print("Great choice! You have chosen " + membership_level + ", an entry level tier. \nEach month, you will recieve: programming books!")
        print("Your cost is:$" + str(bronze_cost))
    elif membership_level == "Free trial":
        print("Great choice! You have chosen " + membership_level + ". Let's get you started! \nEach month, you will receive: our newsletter!!")
else:
    print("Okay, have a  great day!")
