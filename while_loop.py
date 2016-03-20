user_response = input("Enter a number: ")
number = float(user_response)
guess = number/2
accuracy = 0.01
iteration = 0
while abs(number - (guess**2)) > accuracy :
    print("Iteration", iteration, "Guessed square root is", guess)
    guess = (guess + (number/guess)) / 2
    iteration = iteration + 1
print ("The original number is ", number )
print ("The square root of the number is ", guess)
