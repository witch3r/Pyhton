start_number = 2
end_number = 50
current_number = start_number
for current_number in range(start_number, end_number+1) :
    current_divisor = 2
    is_current_number = True
    for current_divisor in range (2,current_number :
        if current_number%current_divisor == 0 :
            is_current_number = False
            break
    if is_current_number :
        print (current_number, "is prime")
print ("All done")
