print("welcomee to python pizza deliveries:")
size = input("Enter thee size of pizza. S,M or L ")
pepperoni =  input("Do you want pepperoni ? Y OR N ")
extra_cheese = input("Do you want extra cheese or not  ? Y OR N ")
small  = 15
medium = 20
large = 25
price = 0
if size == "S":
    price = small
elif size == "M":
    price = medium
elif size == "L":
    price = large
else:
    print("Enter valid input")

if pepperoni == "Y":
    price = price + 3
if extra_cheese == "Y":
    price = price + 1

print(f"your total price is {price}")


import random
res = random.randint(1,2)
print(res)
if res == 1:
    print("Heads")
else:
    print("Tails")

fruits = ["apple","banana","orange"]
for i in fruits:
    print(i + " pie")

for i in range (1,31):
    print(i,"huzi")
    print(f"{i} huzi")


marks = [12,25,3,6,56,88,90]
total = 0
for i in marks:
    total += i

print(total)


marks = [12,25,3,6,56,88,90]
print(min(marks))
print(max(marks))


marks = [12,25,3,6,56,88,90]
maximum = 0
for i in marks:
    if i >= maximum :
        maximum = i
print(maximum)


for i in range ( 1, 11 , 3 ):
    print(i)
    # 1 4 7 10 skips 3 form 1 till 11


for i in range(1, 101):
    if i % 3 == i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")

    else:
        print(i)



alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
symbols_list = ['!', '@', '#', '$', '%','&', '*']
numbers = [0,1,2,3,4,5,6,7,8,9]

total = (int(input("Enter the size of your password ")))
alp = (int(input("Enter the number of alphabets in that ")))
num = (int(input("Enter the number of numbers in that ")))
sym = (int(input("Enter the number of spl symbols in that ")))

password = []
import random
for i in range(alp):
    password.append(alphabets[random.randint(0,len(alphabets)-1)])

for j in range(sym):
    password.append(symbols_list[random.randint(0,len(symbols_list)-1)])

for k in range(num):
    password.append(numbers[random.randint(0,len(numbers)-1)])

print("Your password is: " + "".join(map(str,password)))



import random

alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
symbols_list = ['!', '@', '#', '$', '%','&', '*']
numbers = [0,1,2,3,4,5,6,7,8,9]

total = (int(input("Enter the size of your password ")))
alp = (int(input("Enter the number of alphabets in that ")))
num = (int(input("Enter the number of numbers in that ")))
sym = (int(input("Enter the number of spl symbols in that ")))
password = []

for i in range(alp):
    password.append(alphabets[random.randint(0,len(alphabets)-1)])

for k in range(num):
    password.append(numbers[random.randint(0,len(numbers)-1)])

for j in range(sym):
    password.append(symbols_list[random.randint(0,len(symbols_list)-1)])


random.shuffle(password)
for u in range(len(password)):
    j = random.randint(0,len(password)-1)
    temp = password[u]
    password[u] = password[j]
    password[j] = temp


print("Your password is: " + "".join(map(str,password)))


import random
words = ["apple","boy","laptop","pen","kite","cat","bottle"]
word = random.choice(words)
length = len(word)
guess = []
life = length + 3
attempt = life
print(f"you have {life} life")
for u in range (0,length):
    guess.append("_")
while life > 0 and attempt > 0:
        found = 0
        first = input("Guess a letter ")
        for i in range ( 0 , length ):
            if word[i] == first:
                guess[i] = word[i]
                found = 1

        if found == 0 :
            print("Wrong guess")
            life = life - 1
            print(f"Now you have {life} life")
            print(" ".join(map(str, guess)))
        if found == 1 :
            print("Correct")
            attempt = attempt - 1
            print(" ".join(map(str, guess)))
        if "_" not in guess:
            print("You win!")
            break

if life == 0:
    print(f"Game over. Word was: {word}")
