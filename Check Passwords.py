import hashlib
import requests
import time

def checkPassword(pwd):
    sha1pwd = hashlib.sha1(pwd.encode('ascii')).hexdigest().upper()
    head, tail = sha1pwd[:5], sha1pwd[5:]
    url = 'https://api.pwnedpasswords.com/range/' + head
    res = requests.get(url)
    if res.status_code != 200:
        print("Connection error")
    hashes = (line.split(':') for line in res.text.splitlines())
    count = next((int(count) for t, count in hashes if t == tail), 0)
    return count


def takePasswords(pwdList):
    for i in range(0,len(pwdList)):
        count = checkPassword(pwdList[i])
        if count:
            print('"',pwdList[i],'" %d times occurrences'%(count))
        else:
            print(pwdList[i], "was not found")
        time.sleep(0.1)


print("Select how you want to proceed\n1. Get my passwords from text file\n2. I want to type my passwords\n3. Exit")
print("\nEnter your choice : ",end="")
choice = int(input())
pwdList = []
if choice == 1:
    print("\nEnter file name : ",end="")
    filename = str(input())
    fp = open(filename)
    pwdList= fp.read().splitlines()
    takePasswords(pwdList)
elif choice == 2:
    print("Enter passwords (write exit to stop) ; ")
    pwd=str(input())
    while pwd != "exit":
        pwdList.append(pwd)
        pwd=str(input())
    takePasswords(pwdList)
