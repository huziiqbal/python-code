# /////////////////COFFEE MACHINE///////////////////////
Menu = {
        "Espresso":{
            "ingredients" : {
                "water":50 ,
                "coffee" : 18 ,
                "milk" : 0
            },
            "cost": 1.50
        },
        "Latte":{
            "ingredients" : {
                "water":200 ,
                "coffee" : 24 ,
                "milk" : 150
            },
            "cost": 2.50
        },
        "Cappuccino":{
            "ingredients" : {
                "water":250 ,
                "coffee" : 24 ,
                "milk" : 100
            },
            "cost": 3.00
        }
}
Resources = { "water" : 300 ,
              "Milk" : 200 ,
              "Coffee" : 100
              }
Coins = { "penny": 0.01,
          "Dime" : 0.10 ,
          "Nickel" : 0.05,
          "Quarter": 0.25
          }

order = "ON"
while order != "OFF":
    order = input("What would you like to order?( Espresso/Latte/Cappuccino/)")
    if order == "Espresso" or order == "Latte" or order == "Cappuccino":
        order_cost = Menu[order]["cost"]
        if (Resources["water"] < Menu[order]["ingredients"]["water"]
            or Resources["Milk"] < Menu[order]["ingredients"]["milk"]
            or Resources["Coffee"] < Menu[order]["ingredients"]["coffee"]) :
            print("Sorry Out of Stock")

        else :
            print("please insert coins.")
            quarters = int(input("How many quarters? "))
            dime = int(input("How many dimes? "))
            nickel = int(input("How many nickels? "))
            penny = int(input("How many pennies? "))
            customer_money = quarters * 0.25 + dime * 0.10 + nickel * 0.05 + penny * 0.01
            if customer_money < order_cost:
                print("Sorry, you don't have enough money.")
            else:
                money_left = customer_money - order_cost
                Resources["water"] -= Menu[order]["ingredients"]["water"]
                Resources["Milk"] -= Menu[order]["ingredients"]["milk"]
                Resources["Coffee"] -= Menu[order]["ingredients"]["coffee"]

                print(f"Here is ${money_left:.2f} in change")
                print(f"Here is your {order}☕ Enjoy!")

    if order == "Report":
        for key, value in Resources.items():
            print(f"{key}: {value}")


