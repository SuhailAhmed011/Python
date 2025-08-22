# for i in range(1,11):
#     print( 2  * i)



# def sum ():
#     age = 18
#     if(age<=18):
#         print("you are not adult")
#     else:
#         print("you are adult")
        

# sum()


def factorial(num):
    if(num == 1 or num ==2):
        return 1
    return num * factorial(num-1)


n = int(input("Please enter the number: "))
print(f"The factorial of the number is: {factorial(n)} ")