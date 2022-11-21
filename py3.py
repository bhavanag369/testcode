def func(number, invalid_numbers):
    while(number!=0):
        if str(number%10) in invalid_numbers:
            return False
        number = number//10
    return True

num = int(input())
valid_numbers = "0125689"
invalid_numbers = "347"

count = 0
run = 0

while(count != num):
    if func(run, invalid_numbers):
        count+=1
    run +=1
print(run)