user  = input("enter the number : ")
print(user[::3])
user = user[::3] + user + user[::]
print(user)
