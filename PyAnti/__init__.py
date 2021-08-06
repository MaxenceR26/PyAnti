
"""
By Katsu'hi
Version 1.0

My github : https://www.github.com/Kijusu-Dev

Love U
"""

import time
class pyanti:
	def Countdown(start:int = None,end_sentence:str = None):
		try:
			if not start:
				number = 10
				for cdown in range(number):
					print(f"{number - cdown} Secondes")
					time.sleep(1)
				if not end_sentence:
					print("\nFinished times!")
				else:
					end = print(end_sentence)
					return f"{end}"
			else:
				number = start
				for cdown in range(number):
					print(f"{number - cdown} Secondes")
					time.sleep(1)
				if not end_sentence:
					print("\nFinished times!")
				else:
					end = print(end_sentence)
					return f"{end}"
		except TypeError as e:
			print(f"Countdown Error -> Invalid Syntax")

	def Counter(start:int = None,end_sentence:str = None):
		try:
			if not start:
				number = 10
				for cdown in range(number):
					print(f"{cdown+1} Secondes")
					time.sleep(1)
				if not end_sentence:
					print("\nFinished times!")
				else:
					end = print(end_sentence)
					return f"{end}"
			else:
				number = start
				for cdown in range(number):
					print(f"{cdown+1} Secondes")
					time.sleep(1)
				if not end_sentence:
					print("\nFinished times!")
				else:
					end = print(end_sentence)
					return f"{end}"
		except TypeError as e:
			print(f"Counter Error -> Invalid Syntax")


