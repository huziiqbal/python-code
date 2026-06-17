# # import random as Rd
# #
# #
# # def options():
# #     print("""
# #     Player Guidelines:
# #     1 FOR STONE
# #     2 FOR PAPER
# #     3 FOR SCISSORS
# #     """)
# #
# #
# # def computers_choice():
# #     return Rd.randint(0, 2)
# #
# #
# # def user_choice():
# #     a = int(input("Enter Your choice: ")) - 1
# #     return a
# #
# #
# # def result(user, computer):
# #     grid = [
# #         ["DRAW", "LOSE", "WIN"],
# #         ["WIN", "DRAW", "LOSE"],
# #         ["LOSE", "WIN", "DRAW"]
# #     ]
# #     return grid[user][computer]
# #
# #
# # if __name__ == "__main__":
# #     options()
# #     ntimes = int(input("Enter the Number of Rounds you want to Play: "))
# #     n = 0
# #
# #     choices_map = ["STONE", "PAPER", "SCISSORS"]
# #
# #     while n < ntimes:
# #         print(f"\n--- ROUND: {n + 1} ---")
# #
# #         user_idx = user_choice()
# #         comp_idx = computers_choice()
# #
# #         if user_idx not in [0, 1, 2]:
# #             print("Invalid choice! Please pick 1, 2, or 3.")
# #             continue
# #
# #         print(f"You chose: {choices_map[user_idx]}")
# #         print(f"Computer chose: {choices_map[comp_idx]}")
# #
# #         res = result(user_idx, comp_idx)
# #
# #         if res == "DRAW":
# #             print("IT'S A DRAW!")
# #         else:
# #             print(f"YOU {res}!")
# #
# #         n += 1
#
#
#
#
#
#
# # ////////// FILE HANDLING IN PYTHON ///////////
#
# f = open('C:/Users/ASUS/Desktop/File_Handling.txt','w')
# f.write('Huzaifa Iqbal\n')
# f.write('Huzi\n')
# for i in range (10):
#             print(f.write(f"{i}\n"))
# f.close()
#
#
# f = open('C:/Users/ASUS/Desktop/File_Handling.txt','a')
# f.write('\nHail NIET\n')
# f.close()
# print("\n")
# f = open('C:/Users/ASUS/Desktop/File_Handling.txt','r')
# print(f.read())
# # print(f.read(7))
#
# # f = open ('File_Handling.txt','w')
# # f.write('Hail CS-B')
# # f.close()
# # f = open('File_Handling.txt', 'r')
# # print(f.read())
# # f.close()
#
# try:
#   f = open ('File_Handling
#   ','r')
#   print(f.read())
# except:
#   print("some error occurred")
#
#
#

from tkinter import *

window = Tk()
window.title("hello, NIET")
window.geometry('500x300')

def button_click():
    label = Label(window, text="Respect++", font=('Arial Bold', 30))
    label.config(bg='pink', fg='Brown')

    label.pack()

button = Button(window,text = "AMIT Sir Respect Button", command = button_click)
button.pack()

# label = Label(window, text="Hello", font=('Arial Bold', 30))
# label.config(bg='pink' ,fg='Brown')
#
# label.pack()
# spinbox , checkbox , radiobutton ,

#
#
#
# radio_var = tkinter.StringVar()
# radiobutton1 =tkinter.Radiobutton(window,text = "Pass", variable = radio_var, value = "1")
# radiobutton2 =tkinter.Radiobutton(window,text = "Fail", variable = radio_var, value = "2")
# radiobutton1.pack()
# radiobutton2.pack()
#
#
#
# window.mainloop()


# from tkinter import *
#
# window = Tk()
# window.title("Login example")
#
# def submit_clicked():
#     result_label.config(text="Good Job")
#
# # Username label and entry
# username_label = Label(window, text="Username:")
# username_label.grid(row=0, column=0, padx=10, pady=5)
#
# username_entry = Entry(window)
# username_entry.grid(row=0, column=1)
#
# # Password label and entry
# password_label = Label(window, text="Password:")
# password_label.grid(row=1, column=0, padx=10, pady=5)
#
# password_entry = Entry(window, show="*")
# password_entry.grid(row=1, column=1)
#
# # Submit button
# submit_btn = Button(window, text="Submit", command=submit_clicked)
# submit_btn.grid(row=2, column=1, pady=10)
#
# # Result label
# result_label = Label(window, text="")
# result_label.grid(row=3, column=1)
#
# window.mainloop()
#

from tkinter import *
def calculate():
    try:
        num1=float(entry1.get())
        num2=float(entry2.get())
        op=operation.get()

        if op=="+":
            result=num1+num2
        elif op=="+":
            result=num1-num2
        elif op=="*":
            result=num1*num2
        else:
            result=num1/num2
    except ValueError:
        print("Error","Please enter valid number")
from tkinter import messagebox
root = Tk()
root.title("Arithmetic Calculator")
root.geometry("350x250")

Label(root,text="First Number").grid(row=0,column=0,padx=10,pady=10)
entry1= Entry(root)
entry1.grid(row=0,coloumn=1)

Label(root,text="Second Number").grid(row=1,column=0,padx=10,pady=10)
entry2= Entry(root)
entry2.grid(row=1,coloumn=1)

Label(root,text="Operation").grid(row=2,column=0,padx=10,pady=10)

operation=StringVar()
operation.set("+")

operation_menu= OptionMenu(root,operation,"+","-","*","/")
operation_menu.grid(row=2,coloumn=1)
Button(root,text="Calculate",command=calculate).grid(
    row=3,column=0,columnspan=2,pady=15
)
result_label=Label(root,text="Result= ")
result_label.grid(row=4,column=0,columnspan=2)

root.mainloop()
