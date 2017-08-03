import time
import random
from tkinter import *



#password strength checker and strong password generator app.
#Requisites: Length=8, Symbols=at least 1, Numbers= 2, Capital Letters 2 and small letters: 3+
while True:
	password = input("Enter your password to check strength: ")

	if len(password) < 8:
		print("Short Password. Must be atleast 8 letters.")
	else:



		#Counting presence of numbers in the string with the count method.
		space = password.count(' ')
		numb1 = password.count('1')
		numb2 = password.count('2')
		numb3 = password.count('3')
		numb4 = password.count('4')
		numb5 = password.count('5')
		numb6 = password.count('6')
		numb7 = password.count('7')
		numb8 = password.count('8')
		numb9 = password.count('9')
		numb0 = password.count('0')

		total_numbers = numb1 + numb2 + numb3 + numb4 + numb5 + numb6 + numb7 + numb8 + numb9 + numb0
		# Counting Over

		#Coutnting the symbols present in the string.
		char1 = password.count('~')
		char2 = password.count('`')
		char3 = password.count('!')
		char4 = password.count('@')
		char5 = password.count('#')
		char6 = password.count('$')
		char7 = password.count('%')
		char8 = password.count('^')
		char9 = password.count('&')
		char10 = password.count('*')
		char11= password.count('(')
		char12 = password.count(')')
		char13= password.count('_')
		char14 = password.count('-')
		char15 = password.count('=')
		char16 = password.count('+')
		char17 = password.count('|')
		char18 = password.count('}')
		char19 = password.count('{')
		char20 = password.count(']')
		char21 = password.count('[')
		char22 = password.count('"')
		char23 = password.count("'")
		char24 = password.count(';')
		char25 = password.count(':')
		char26 = password.count('/')
		char27 = password.count('?')
		char28 = password.count('.')
		char29 = password.count('>')
		char30 = password.count('<')
		char31 = password.count(',')

		total_characters = char1 + char2 + char3+ char4+ char5+ char6+ char7+ char8+ char9+ char10+ char11+ char12+ char13
		+ char14+ char15+ char16+ char17+ char18+ char19+ char20+ char21+ char22+ char23+ char24+ char25+ char26+ char27+ char28
		+ char29+ char30+ char31


	    # counting for the charactes ends here.

	    #counting for the presence of a capital letter
		capital_letters = sum(1 for c in password if c.isupper())
		#counting for capital letters ends here



		percentage1 = 0
		#NUMBERS-------------------------------------------------------
		if total_numbers >= 3:
			percentage1 += 25
			#print(percentage1)
		elif total_numbers >= 2:
			percentage1 += 12.5
			#print(percentage1)

		elif total_numbers == 0:
			percentage1 +=0
			#print(percentage1)
		

		#characters--------------------------------------------------------
		percentage2 = 0
		if total_characters >=2:
			percentage2 += 25
			#print(percentage2)
		elif total_characters == 1:
			percentage2 += 12.5
			#print(percentage2)
		elif total_characters == 0:
			percentage2 += 0
			#print(percentage2)

		#CAPIPTAL LETTERS------------------------------------------------------
		percentage3 = 0
		if capital_letters >= 2:
			percentage3 += 25
			#print(percentage3)
		elif capital_letters <= 1:
			percentage3 += 0
			#print(percentage3)

		#length Factor--------------------------------------------------------
		percentage4 = 0
		if len(password) >= 8:
			percentage4 += 25

		total_percentage = percentage1 + percentage2 + percentage3 + percentage4
		if total_percentage == 100:
			print("Very Strong Password.")
		elif total_percentage <= 50:
			print("Weak Password.")
		elif 50 < total_percentage <100:

			print("Decent Password but can be made more strong.")
		print(total_percentage)
		ask = input("Do you want to generate a strong password? (y/n) \n")
		if ask == "y" or ask == "Y":
			root =Tk()
			root.title("Password Generator")
			root.geometry("1920x1080+0+0")	

			heading = Label(root, text = "Welcome to Password Generator.", font=('arial 40 bold'), fg="steelblue").pack()

			#code goes here
			alpha = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
			small = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
			numbers = ['1','2','3','4','5','6','8','7','0','9']
			symbols_lst = ['`','~','!','@','#','$','%','^','&','*','(',')','_','-','=','+','|','}','{',']',
			'[',':',';','"',"'",'/','?','>','<','.',',']

			new1 = random.choice(alpha)
			new2 = random.choice(small)
			new3 = random.choice(numbers)
			new4 = random.choice(numbers)
			new5 = random.choice(small)
			new6 = random.choice(symbols_lst)
			new7 = random.choice(alpha)
			new8 = random.choice(symbols_lst)
			new9 = random.choice(small)
			new10 = random.choice(small)
			new11 = random.choice(numbers)
			new12 = random.choice(small)
			new13 = random.choice(alpha)
			new14 = random.choice(symbols_lst)
			new15 = random.choice(symbols_lst)
			
			total_new = new1 + new2 +new3 +new4 +new5 +new6 +new7 +new8  +new9 +new10 +new11 +new12 +new13 +new14 +new15  

			def calculate():
				label1 = Label(root, text=total_new, font=('arial 40 bold'), fg='green').place(x= 500, y=300)
			def create():
				file = open("password.txt", "w")
				file.write(str(total_new) + " is your new password.")
				file.close()
				lllb = Label(root, text= "Sucessfully created Text File.").place(x=600 , y=570)
			def composition():
				nn = ("Numbers: " + str(total_numbers))
				nn1 = ("Symbols: " + str(total_characters))
				nn2 = ("Capital Letters: " + str(capital_letters))
				nn3 = ("Spaces: " + str(space))
				nn4 = ("Small Letters: " + str(len(password)-(total_numbers+total_characters+capital_letters+space)))

				new_lb = (nn + "   |" + nn1 + "    |" + nn2 + "    |" + nn3 + "    |" + nn4)
				llb = Label(root, text=new_lb, font=('arial 20 bold'), fg="red").place(x =60, y=600)
			def quit():
				root.destroy()
			rule = Label(root, text="Here are the steps: ", font=('arial 20 bold'), fg="black").place(x=60, y=90)
			rule1 = Label(root, text="1. GENERATE will create a very strong password for you only once. ", font=('arial 20 bold'), fg="black").place(x=60, y=130)
			rule2 = Label(root, text="2. CREATE will create a text file with password in it.", font=('arial 20 bold'), fg="black").place(x=60, y=160)
			rule3 = Label(root, text="3. COMPOSITION will show the composition of your previous password.", font=('arial 20 bold'), fg="black").place(x=60, y=190)

			btn1 = Button(root, text="Generate Password", width=30, height=3, bg="lightgreen", command=calculate).place(x=200, y=500)
			btn2 = Button(root, text="Create a Text File", width=30, height=3, bg="red", command=create).place(x=600, y=500)
			btn = Button(root, text="My Password Composition", width=30, height=3, bg="orange", command=composition).place(x=1000, y=500)
			btn_lst = Button(root, text="Exit", width=30, height=3, command=quit).place(x=600, y=800)

			#------------------------------ends--------------------------------

			root.mainloop()
		