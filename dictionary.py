
# my_dict = {}


# my_dict['name'] = 'John'
# my_dict['age'] = 25
# my_dict['city'] = 'New York'

# # Access values using keys
# print(my_dict['name'])  # Output: John
# print(my_dict['age'])   # Output: 25
# print(my_dict['city'])  # Output: New York

# # Update the value of a key
# my_dict['age'] = 26

# # Remove a key-value pair from the dictionary
# del my_dict['city']

# # Check if a key exists in the dictionary
# if 'name' in my_dict:
#     print('Name:', my_dict['name'])

# # Iterate over the keys and values in the dictionary
# for key, value in my_dict.items()
#     print(key, ':', value)

s = 's2x1'
result = ''
for i in range(len(s)):
    if s[i].isalpha():
        result += s[i]
    else:
        result += s[i-1] * (int(s[i]) - 1)
print(result)

