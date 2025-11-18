# # ques 1
# movie1 = input("Enter your 1st fav movie name: ")
# movie2 = input("Enter your 2nd fav movie name: ")
# movie3 = input("Enter your 3rd fav movie name: ")

# storedMovies = [movie1, movie2, movie3]
# print("your movies collection: ", storedMovies)

# #ques 2
# n = int(input("which number table you want: "))
# i =1
# while i <= 10:
#     print(n*i)
#     i+=1

# #ques 3
# foods = ["biryani", "mutton", "eggs", "kabaabs"]
# idx = 0
# while idx < len(foods):
#     print(foods[idx])
#     idx += 1

# #ques 4
# find = int(input("enter number: "))
# numbers = (1,4,6,78,90,3,5,34,58)
# i = 0
# while i < len(numbers):
#     if find == numbers[i]:
#         print(numbers[i])
#         break;
#     else:
#         i +=1
# else:
#         print("not present")


#ques 5
# fruits = ["banana", "apple", "kiwi", "mango", "avacado"]

# for el in fruits:
#      print(el)


#ques 6

# numbers = (1,2,3,4,5,6,7,8)
# x = 5
# for i in numbers:
#     if x == i:
#         print("found", i)
#         break;
# else:
#     print("not found")


# ------------ Loops (Easy) ------------------------------

# ques 1 ----------------------

# i = 1
# while i<=10:
#     print(i)
#     i += 1

# ques 2 ------------------

# num = int(input("Enter a number: "))
# i = 1
# while i <= 10:
#     print(num*i)
#     i += 1

# for i in range(1,11):
#     print(num * i)


# ques 3 ---------------------
# total = 0
# for i in range(1,11):
#     total +=i
 
# print(total)


# ques 4 ---------------------

# num = int(input("enter number: "))

# count = 0
# while num > 0:
#     num = num // 10
#     count += 1


# print(count)



# ques 5 ---------------------

# count = 0

# for i in range(1,41):
#     if i%2 == 0:
#      count += 1
     

# print(count)


# ques 6 ---------------------

number = 12345
reversed_num = 0
while number > 0:
    digit = number % 10 # extract last digit
    reversed_num = reversed_num * 10 + digit # add it to reversed variable
    number = number // 10 # remove last digit from number

print(reversed_num)
