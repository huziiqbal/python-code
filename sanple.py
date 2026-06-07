# import random as Rd
#
#
# def options():
#     print("""
#     Player Guidelines:
#     1 FOR STONE
#     2 FOR PAPER
#     3 FOR SCISSORS
#     """)
#
#
# def computers_choice():
#     return Rd.randint(0, 2)
#
#
# def user_choice():
#     a = int(input("Enter Your choice: ")) - 1
#     return a
#
#
# def result(user, computer):
#     grid = [
#         ["DRAW", "LOSE", "WIN"],
#         ["WIN", "DRAW", "LOSE"],
#         ["LOSE", "WIN", "DRAW"]
#     ]
#     return grid[user][computer]
#
#
# if __name__ == "__main__":
#     options()
#     ntimes = int(input("Enter the Number of Rounds you want to Play: "))
#     n = 0
#
#     choices_map = ["STONE", "PAPER", "SCISSORS"]
#
#     while n < ntimes:
#         print(f"\n--- ROUND: {n + 1} ---")
#
#         user_idx = user_choice()
#         comp_idx = computers_choice()
#
#         if user_idx not in [0, 1, 2]:
#             print("Invalid choice! Please pick 1, 2, or 3.")
#             continue
#
#         print(f"You chose: {choices_map[user_idx]}")
#         print(f"Computer chose: {choices_map[comp_idx]}")
#
#         res = result(user_idx, comp_idx)
#
#         if res == "DRAW":
#             print("IT'S A DRAW!")
#         else:
#             print(f"YOU {res}!")
#
#         n += 1






# ////////// FILE HANDLING IN PYTHON ///////////

f = open('C:/Users/ASUS/Desktop/File_Handling.txt','w')
f.write('Huzaifa Iqbal\n')
f.write('Huzi\n')
for i in range (10):
            print(f.write(f"{i}\n"))
f.close()


f = open('C:/Users/ASUS/Desktop/File_Handling.txt','a')
f.write('\nHail NIET\n')
f.close()
print("\n")
f = open('C:/Users/ASUS/Desktop/File_Handling.txt','r')
print(f.read())
# print(f.read(7))

# f = open ('File_Handling.txt','w')
# f.write('Hail CS-B')
# f.close()
# f = open('File_Handling.txt', 'r')
# print(f.read())
# f.close()

try:
  f = open ('File_Handlin','r')
  print(f.read())
except:
  print("some error occured")

