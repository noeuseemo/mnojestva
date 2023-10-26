list = [1,5,1,2,4,6,6]

numbers = set()
for number in list:
    if number in numbers:
        print ("nice")
    else:
        print ("no nice")
        numbers.add(number)
    
