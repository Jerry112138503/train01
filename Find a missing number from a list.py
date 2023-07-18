member = []
number = int(input("Please enter the number of value: "))
for i in range (1,number+1):
    value = int(input(f"Please enter the {i} number: "))
    member.append(value)
for j in range(number):
    if(member[j] != j+1):
        find = j+1
        break
    
print(f"Input: {member} ,Output: {find}")