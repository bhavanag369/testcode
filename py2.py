first = input("Enter 1st String : ")
second =input("Enter 2nd String : ")
count = 0
for i in first:
    if i == second[-1]:
        count +=1

print(count)