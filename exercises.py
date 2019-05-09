#Exercise11
one_to_hundred = range(1,101)

for num in one_to_hundred:
    if num % 3 == 0 and num % 5 == 0:
        print("BitMaker")
    elif num % 3 == 0:
        print("Bit")
    elif num % 5 == 0:
        print("Maker")
    else:
        print(num)

#Exercise12
print("How many pizzas do you want to order?")
num_pizzas = input()

count = 1 

while count >= 0:
    print("How many toppings for pizza {}?".format(count))
    count+=1
    num_toppings = input()
    print("You have ordered a pizza with {} toppings.".format(num_toppings))

        
