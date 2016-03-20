#Eating all the cookies
user_response = input("How many cookies do you want to eat?")
number_of_cookies = int(user_response)
cookies_eaten = 0
while number_of_cookies > 0:
    number_of_cookies = number_of_cookies - 1
    cookies_eaten = cookies_eaten + 1
    print("Eat a cookie", cookies_eaten)
print("I ate all the cookies")


