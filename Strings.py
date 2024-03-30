# my_string = 'Hello!, world'
# print(my_string[::-1])#string reverse

# print(my_string[-1::7])

# print(my_string[:5:-1])


# print(len(my_string))


# accept a string from user and count the vowels and consonants from it
# user_string = input("Enter a string: ")

# vowels = 0
# consonants = 0

# for char in user_string:
#     if char.isalpha():
#         if char.islower() in 'aeiou':
#             vowels += 1
#         else:
#             consonants += 1

# print("Number of vowels:", vowels)

# print("Number of consonants:", consonants)


# take 2 randomized strings, and then find common characters between them
list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))

common = []

for i in list1:
    if i in list2:
        common.append(i)
        
print(common) 

print(list1.list2count(common)) #using set

    



