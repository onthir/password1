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
		if ask == "y":
			root =Tk()
			root.title("Password Generator")
			root.geometry("1200x720+0+0")	

			heading = Label(root, text = "Welcome to Password Generator.", font=('arial 40 bold'), fg="steelblue").pack()

			#code goes here
			alpha = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
			small = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
			numbers = ['1','2','3','4','5','6','8','7','0','9']
			symbols_lst = ['`','~','!','@','#','$','%','^','&','*','(',')','_','-','=','+','|','}','{',']',
			'[',':',';','"',"'",'/','?','>','<','.',',']

			

			#------------------------------ends--------------------------------

			root.mainloop()
		