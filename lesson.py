code = "Secret123"
while True:
    password = input("Enter the password: ")
    if len(password) != len(code):
        print("Incorrect password length. Try again.")
    elif len(password) == len(code) and password != code:
        print("Password length is correct. But the password is incorrect. Try again.")
    else:
        print("Access granted.")
        break

        


count = 1
while count <= 10:
    if count%3==0 and count%5==0:
        print("FizzBuzz")
    elif count % 3 == 0:
        print("Fizz")
    elif count%5 ==0:
        print("Buzz")
    elif count %3 !=0 and count %5 !=0:
        print(count)
    else:
        print(count)
    count += 1


