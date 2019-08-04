# Given a range of numbers. Iterate from o^th number to the end
# number and print the sum of the current number and previous number
#
# for i in range(10):
#  if i == 0:
#    i_sum = i
# else:
#  i_sum = (i + i - 1)
# print(i_sum)
#
#
# Accept string from the user and display only those characters which are present at an even index
#
# i_input = input("Enter string: ")
# length = len(i_input)
# for i in range(0, len(i_input)-1, 2):
#  print( i_input[i])
#
# Given a string and an int n, remove characters from string
# starting from zero up to n and return a new string
#
# i_input = input("enter string : ")
# i_number = int(input("enter number:  "))
# new_string = i_input[i_number:]
# print(new_string)
#
# Given a list of ints, return True if first and last number of a list is same
# List = [1, 2, 3, 4, 5, 6]
# firstnumber = List[0]
# lastnumber = List[-1]
# if firstnumber == lastnumber:
#  print("True")
# else:
#  print("false")
#
#
# Given a list of numbers, Iterate it and print only those numbers which are divisible of 5
# List = [10, 23, 45, 87, 75, 100]
# for i in List:
#     if i % 5 == 0:
#         print("Divisible by 5")
#     else:
#         print("not divisible")

# Return the number of times that the string “Emma” appears anywhere in the given string
# string = "Emma is a good developer. Emma is also a writer"
# print(string.count("Emma"))
# print(string.count("writer"))

# Print the following pattern
# for num in range(6):
#     for i in range(num):
#         print(num,  end=" " )
#     print("\n")

# Reverse a given number and return true if it is the same as the original number

# def reverseCheck(number):
#     originalNum = number
#     reverseNum = 0
#     while (number > 0):
#         reminder = number % 10
#         reverseNum = (reverseNum * 10) + reminder
#         number = number // 10
#     if originalNum == reverseNum:
#         return True
#     else:
#         return False
#
#
# print("orignal and revers number is equal")
# print(reverseCheck(121))

# Given a two list of ints create a third list such that should contain only
# odd numbers from the first list and even numbers from the second list Expected Output:

# listOne = [10, 20, 23, 11, 17]
# listTwo = [13, 43, 24, 36, 12]
# listThree = listOne + listTwo
# listEven = []
# listOdd = []
# for i in listThree:
#     if i % 2 == 0:
#         listEven.append(i)
#     else:
#         listOdd.append(i)
#
# print(listOdd, '\n', listEven)

