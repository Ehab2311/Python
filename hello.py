# num=int( input("ENter number"))
# if num >0:
#     print (" The number is positive")
# elif num<0:
#     print("The number is negative")
# else:
#     print("number is zero")       
# name = input("Enter your name")
# print ("hello {}, how are you today ??!".format(name))
# friends=["mahmoud", "ehab","osama","ali","shms","homam","kaser","ritta","reham"]
# friends.sort()
# friends.append("bilal")
# friends.sort()

# print(friends)
# friends={"key01","bilal"}
# for i in range(5):print(i)
# for i in friends:
#     print(i)
weigh= int(input("ENter weigh"))
height= int(input("ENTER YOUR HIEGH"))
bmi= (weigh/(height*height))
convert = bmi*10000
print(round(convert,2))