# member = []
# value = 1
# while(value != '-1'):
#     value = input("Please enter the string (Exit:-1): ")
#     if(value != '-1'):
#         member.append(value)
# print(f"Sample String: {member}")
# reverse_string = member[::-1]
# print(f"Expected Output: {reverse_string}")

list1 = input("Please enter the string:" )
print(f"Sample String: {list1}")
words = list1.split()
rev_list = words[::-1]
print(f"Expected Output: {' '.join(rev_list)}")