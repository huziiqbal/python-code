# print("welcomee to python pizza deliveries:")
# size = input("Enter thee size of pizza. S,M or L ")
# pepperoni =  input("Do you want pepperoni ? Y OR N ")
# extra_cheese = input("Do you want extra cheese or not  ? Y OR N ")
# small  = 15
# medium = 20
# large = 25
# price = 0
# if size == "S":
#     price = small
# elif size == "M":
#     price = medium
# elif size == "L":
#     price = large
# else:
#     print("Enter valid input")
#
# if pepperoni == "Y":
#     price = price + 3
# if extra_cheese == "Y":
#     price = price + 1
#
# print(f"your total price is {price}")
#
#
# import random
# res = random.randint(1,2)
# print(res)
# if res == 1:
#     print("Heads")
# else:
#     print("Tails")
#
# fruits = ["apple","banana","orange"]
# for i in fruits:
#     print(i + " pie")
#
# for i in range (1,31):
#     print(i,"huzi")
#     print(f"{i} huzi")
#
#
# marks = [12,25,3,6,56,88,90]
# total = 0
# for i in marks:
#     total += i
#
# print(total)
#
#
# marks = [12,25,3,6,56,88,90]
# print(min(marks))
# print(max(marks))
#
#
# marks = [12,25,3,6,56,88,90]
# maximum = 0
# for i in marks:
#     if i >= maximum :
#         maximum = i
# print(maximum)
#
#
# for i in range ( 1, 11 , 3 ):
#     print(i)
#     # 1 4 7 10 skips 3 form 1 till 11
#
#
# for i in range(1, 101):
#     if i % 3 == i % 5 == 0:
#         print("FizzBuzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#
#     else:
#         print(i)
#
#
#
# alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# symbols_list = ['!', '@', '#', '$', '%','&', '*']
# numbers = [0,1,2,3,4,5,6,7,8,9]
#
# total = (int(input("Enter the size of your password ")))
# alp = (int(input("Enter the number of alphabets in that ")))
# num = (int(input("Enter the number of numbers in that ")))
# sym = (int(input("Enter the number of spl symbols in that ")))
#
# password = []
# import random
# for i in range(alp):
#     password.append(alphabets[random.randint(0,len(alphabets)-1)])
#
# for j in range(sym):
#     password.append(symbols_list[random.randint(0,len(symbols_list)-1)])
#
# for k in range(num):
#     password.append(numbers[random.randint(0,len(numbers)-1)])
#
# print("Your password is: " + "".join(map(str,password)))
#
#
#

# import random
#
# alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# symbols_list = ['!', '@', '#', '$', '%','&', '*']
# numbers = [0,1,2,3,4,5,6,7,8,9]
#
# total = (int(input("Enter the size of your password ")))
# alp = (int(input("Enter the number of alphabets in that ")))
# num = (int(input("Enter the number of numbers in that ")))
# sym = (int(input("Enter the number of spl symbols in that ")))
# password = []
#
# for i in range(alp):
#     password.append(alphabets[random.randint(0,len(alphabets)-1)])
#
# for k in range(num):
#     password.append(numbers[random.randint(0,len(numbers)-1)])
#
# for j in range(sym):
#     password.append(symbols_list[random.randint(0,len(symbols_list)-1)])
#
#
# random.shuffle(password)
# for u in range(len(password)):
#     j = random.randint(0,len(password)-1)
#     temp = password[u]
#     password[u] = password[j]
#     password[j] = temp
#
#
# print("Your password is: " + "".join(map(str,password)))

#


# import random
# words = ["apple","boy","laptop","pen","kite","cat","bottle"]
# word = random.choice(words)
# length = len(word)
# guess = []
# life = length + 3
# attempt = life
# print(f"you have {life} life")
# for u in range (0,length):
#     guess.append("_")
# while life > 0 and attempt > 0:
#         found = 0
#         first = input("Guess a letter ")
#         for i in range ( 0 , length ):
#             if word[i] == first:
#                 guess[i] = word[i]
#                 found = 1
#
#         if found == 0 :
#             print("Wrong guess")
#             life = life - 1
#             print(f"Now you have {life} life")
#             print(" ".join(map(str, guess)))
#         if found == 1 :
#             print("Correct")
#             attempt = attempt - 1
#             print(" ".join(map(str, guess)))
#         if "_" not in guess:
#             print("*************You win!*************")
#             break
#
# if life == 0:
#     print(f"Game over. Word was: {word}")
#
#




# alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# operation = (input("Type e for encryption and d for decryption ? "))
# shift =int(input ("Enter the number of shift "))
# msg = input("Type your message: ")
# new_msg = []
# if operation == 'e':
#     for ch in msg:
#         if ch == " ":
#             new_msg.append("@")
#         else:
#             new_msg.append(alphabets[(alphabets.index(ch) + shift)%26])
# elif operation == 'd':
#     for ch in msg:
#         if ch == "@":
#             new_msg.append(" ")
#         else:
#             new_msg.append(alphabets[(alphabets.index(ch) - shift)%26])
# else:
#     print("Invalid input")
#
# print("".join(map(str,new_msg)))




# DICTIONARY NOTES:

# # 1. accessing element(value) of dictionary
# dict = {"huzi" : "student"}
# print(dict["huzi"])
#
# # 2. edit in dictionary
# dict["huzi"] = "first year student"
# print(dict["huzi"])
#
# # 3. adding in  dictionary
# dict["huzaifa"] = " 1st year B.Tech student"
# print(dict)
#
# # 4 . looping in a dictionary
# for i in dict:
#     print(i , ":" , dict[i])
# #      (i) will give the key and dict[i] will give the value associated with key





 # imp ques
# student_scores = {
#     'Harry': 88,
#     'Ron': 78,
#     'Hermione': 95,
#     'Draco': 75,
#     'Neville': 60
# }
# student_grades = {}
#
# for i in student_scores:
#     if 90 < student_scores[i] <= 100:
#         student_grades[i] = "Outstanding"
#         # IMP: here the i is automatically
#         # becoming the key for (student_grade dictionary)
#         # and outstanding is becoming the value
#         # in a single argument
#         # so no need to give the keys value in the dict again
#
#     elif 80 < student_scores[i] <= 90:
#         student_grades[i] = "Exceeds"
#     elif 70 < student_scores[i] <= 80:
#         student_grades[i] = "Acceptable"
#     else:
#         student_grades[i] = "Fail"
#

# print(student_grades)



# NESTED DICTIONARY
# travel_log = {
#     "France": {
#         "cities_visited": ["Paris", "Lille", "Dijon"],
#         "total_visits": 12
#         },
#
#     "Germany": {
#         "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
#         "total_visits": 5
#     },
# }
#
# print(travel_log["Germany"]["cities_visited"][2])



# BLIND BIDDING PROGRAM
# bid = {}
# for i in range(3):
#     print("\n" * 100)
#     bid[input("Enter your name ")] = int(input("Enter your bid ₹"))
#     # the above is same as ,
#     # bid[name] = amount1
#     print("\n" * 100)
#
# print("The highest bidder is " + max(bid),
#       "with the bid of ₹" + str(bid[max(bid)]))


# bid = {}
# for i in range (3):
#     print("\n" * 100)
#     name = input("Enter your name ")
#     amount = int(input("Enter your bid ₹"))
#     bid[name] = amount
#     print("\n" * 100)


# print("The highest bidder is " + max(bid),
#       "with the bid of ₹" + str(bid[max(bid)]))


# NUMBER GUESSING GAME
#
# import random
# number = random.randint(1,100)
# level = input("Easy or Hard? ").lower()
# life = 10 if level == "hard" else 20
# space = " "*50
# while life > 0:
#     user_num = int(input("Guess the number"))
#     if user_num == number:
#         print("You won!")
#         break
#     elif user_num > number:
#         print("too high")
#         life -=1
#     else:
#         print("too low")
#         life -= 1
#     print(f"{space}Lives left: {life} ❤️")
# if life == 0:
#     print("Game Over")
#

# def add(num1 , num2):
#     return num1 + num2
#
# def sub(num1 , num2):
#     return num1 - num2
#
# def mul(num1 , num2):
#     return num1 * num2
#
# def div(num1 , num2):
#     return num1 / num2
#
# num1 = int(input("Enter the first number: "))
# inn = 1
# while (inn != 0 ):
#     num2 = int(input("Enter the second number: "))
#     operation = input("Enter the operation: ")
#     if operation == "+":
#             result = add(num1, num2)
#             print(result)
#     elif operation == "-":
#         result = sub(num1, num2)
#         print(result)
#     elif operation == "*":
#         result = mul(num1, num2)
#         print(result)
#     elif operation == "/":
#         result = div(num1, num2)
#         print(result)
#     inn = int (input(f"type 1 to continue calculating with {result} or\n"
#                      f"type 0 to start with a new value"))
#     if inn == 1 :
#         num1 = result
#     if inn == 0 :
#         print("\ncalculation finished")


# BLACKJACK GAME

# import random
# cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
# total = 0
# comp_total = 0
# decision = 'y'
# card1 = cards.pop(random.randint(0,len(cards)-1))
# comp_card1 = cards.pop(random.randint(0,len(cards)-1))
# card2 = cards.pop(random.randint(0,len(cards)-1))
# comp_card2 = cards.pop(random.randint(0,len(cards)-1))
# comp_total = comp_total + comp_card1 + comp_card2
# while decision != 'n':
#     decision = input("Do you want to play the game? y or n ")
#     if decision == 'y':
#         print(f"your cards are : {card1} {card2}")
#         total = total + card1 + card2
#         print(f"Total is {total}")
#         inp = "h"
#
#         if inp == 'h':
#             while inp != 's':
#                 inp = input("h for HIT\ns for STAND : ")
#                 new_card = cards.pop(random.randint(0,len(cards)-1))
#                 total = total + new_card
#                 print(f"New card = {new_card}")
#                 print(f"Total is {total}")
#                 if total > 21:
#                     print("You lost")
#                     total = 0
#                     break
#                 if inp == 's':
#                     player_score = total
#                     while (comp_total < 17):
#                         new_comp_card = cards.pop(random.randint(0,len(cards)-1))
#                         comp_total = comp_total + new_comp_card
#                         if comp_total >= 17:
#                             dealer_score = comp_total
#                             if player_score > dealer_score:
#                                 print("You won")
#                             elif player_score < dealer_score:
#                                 print("You lost")
#                             else:
#                                 print("Draw")




# basic program of increment in python

# method 1 by returning the incremented value

# number = 0
# def increment (num):
#     return num + 1
#
# number = increment(number)
# print(number)
# number = increment(number)
# print(number)
# number = increment(number)
# print(number)

# method 2 using global key word

# number = 0
# def increment (num):
#     global number
#     number += 1
#     print(number)
#
# increment (number)
# increment (number)
# increment (number)

# //////////////////////////////////////
# //////////HIGHER LOWER GAME//////////
# ////////////////////////////////////
import random
data = [
    {"name": "Spain", "info": "Located in Europe", "value": 48},
    {"name": "Argentina", "info": "Located in South America", "value": 46},
    {"name": "South Africa", "info": "Located in Africa", "value": 60},
    {"name": "Canada", "info": "Located in North America", "value": 40},
    {"name": "Australia", "info": "Located in Oceania", "value": 26},
    {"name": "Saudi Arabia", "info": "Located in Middle East", "value": 36},
    {"name": "South Korea", "info": "Located in East Asia", "value": 52},
    {"name": "Colombia", "info": "Located in South America", "value": 52},
    {"name": "Ukraine", "info": "Located in Europe", "value": 37},
    {"name": "Kenya", "info": "Located in Africa", "value": 55},
    {"name": "Poland", "info": "Located in Europe", "value": 38},
    {"name": "Morocco", "info": "Located in Africa", "value": 37},
    {"name": "Peru", "info": "Located in South America", "value": 34},
    {"name": "Malaysia", "info": "Located in Southeast Asia", "value": 34},
    {"name": "Uzbekistan", "info": "Located in Central Asia", "value": 36},
    {"name": "Ghana", "info": "Located in Africa", "value": 34},
    {"name": "Algeria", "info": "Located in Africa", "value": 45},
    {"name": "Iraq", "info": "Located in Middle East", "value": 44},
    {"name": "Afghanistan", "info": "Located in South Asia", "value": 41},
    {"name": "Nepal", "info": "Located in South Asia", "value": 30}
]
result = " "
score = 0
while result != "incorrect":
        first = data[random.randint(0,len(data)-1)]
        second = data[random.randint(0,len(data)-1)]
        # print(first)
        option1 = print(f"Option 1: {first['name']} : {first['info']}")
        option2 = print(f"Option 2: {second['name']} : {second['info']}\n")

        comparison1 = first['value']
        comparison2 = second['value']
        larger = comparison1 if comparison1 > comparison2 else comparison2
        choice = int(input("Enter your choice\n"
                       "Which one is greater\n"
                       "1 for first option\n"
                       "2 for second option\n"))
        if choice == 1 and larger == comparison1 or choice == 2 and larger == comparison2:
            result = "correct"
            print(result)
            score = score + 1
            print(f"Your score is {score}")
        elif choice ==2 and larger == comparison1 or choice == 1 and larger == comparison2:
            result = "incorrect"
            print(result)
            print(f"Your score is {score}")
            break




COFFEE MACHINE GAME