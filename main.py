#This is my first github addition
print ( 'hello world')

#Partners name: Zitlaly
def menu():
	print("Menu")
	print("-------------")
	print("1. Encode")
	print("2. Decode")
	print("3. Quit")

def encode(password):
	new_password = ""
	for  number in password:
		number = int(number) + 3
		new_password += str(number)
	return new_password
def decode(password):
	new_password = ""
	for number in password:
		number = int(number) - 3
		new_password += str(number)
	return new_password

def main():
	while True:
		print()
		menu()
		choice = int(input("Please enter your password to encode: ")
		if choice == 1:
			password = input("Please enter your password to encode: ")
			encode(password)
			print("Your password has been encoded and stored!")
		if choice == 2:
			password = intput("Please enter your password to enocode: ")
			decode(password)
			print("Your password has been encoded and stored!")
		elif choice == 3:
			break

if __name__ == "__main__":
	main()
