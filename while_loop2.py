
#finding prime number using while

current_number = 27
current_divisor = 2
is_x_prime = True

while (current_divisor < current_number) :
    if current_number%current_divisor == 0 :
        is_x_prime = False
        break
    current_divisor = current_divisor + 1
if is_x_prime :
    print (current_number, " is prime " )
print ("Completed! ")
