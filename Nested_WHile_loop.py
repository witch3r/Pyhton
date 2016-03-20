starting_number = input("Enter a starting number: ")
current_number = int(star_number)
ending_number = input("Enter an ending number: ")
end_number = int(ending_number)

while (current_number <= end_number) :
    current_divisor = 2
    is_current_number_prime = True
    while (current_divisor < current_number) :
        if current_number%current_divisor == 0
            is_current_number_prime = False
            break
        current_divisor = current_divisor + 1
    if is_current_number_is_prime :
        print (current_number, "is prime")
print ("All done!")
