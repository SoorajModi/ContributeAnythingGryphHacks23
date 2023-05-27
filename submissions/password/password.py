import sys
import time
def slowprint(s):
  for c in s + '\n':
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(2./10)
if __name__ == "__main__":
 print("what do you what your username to be?")
username = (input())
print("enter password")
password1 = (input())
while username == password1:
    print("password can not be the same as the user name. Please try again.")
    password1 = (input())
print("remember this password when you log on again!")
time.sleep(2)
print("please insert hint for assistance for remembering the password")
hint = (input())
while password1 == hint or username == hint:
    print("hint can not be the same as the password or username. Please try again.")
    hint = (input())
time.sleep(1)
print("testing logging on. Please be patient")
time.sleep(1)
slowprint("logging off")
time.sleep(0.5)
slowprint(". . .")
time.sleep(0.5)
slowprint("logging on")
time.sleep(0.5)
print("insert password")
password = (input())
count = 0
while password1 != password:
    print("try again")
    password = (input())
    count += 1
    if count >= 3:
        print("hint: " + str(hint))
print("Loading")
time.sleep(1)
slowprint(". . .")
slowprint(". . .")
time.sleep(0.5)
print("Welcome Back " + str(username))
