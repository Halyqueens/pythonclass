# # def add(*args):
# #     addition = 0
# #     for num in args:
# #         addition += num
# #     return addition
# #     
# # print(sum)
# # print(add(1,2,3,4))
# # print(add(1,2,3,4,5,6,7,8,9,10))
#         
#         #create a function that can multiply any quantity of numbers using this operator: *=
# 
# def multi(*args):
#     multi = 1
#     for num in args:
#         multi *= num
#     return multi
#     
# xvbc print(multi(5,2,6,4,1))
# print(multi(2,0,9,3,1,8,3,4,9))
#

# Don't change the code
# print("welcome to python Pizza Deliveries!")
# size = input("what size of pizza do you want? S, M, or L ")
# add_pepperoni = input("Do yo want pepperoni? Y or N")
# extra_cheese = input("Do you want extra cheese? Y or N")

print("Welcome to Python Pizza Deliveries!")

# Get pizza size from the user
print("Prices: S - $10, M - $12, L - $14")
size = input("What size of pizza do you want? S, M, or L: ").upper()

# Get user's choice for pepperoni
add_pepperoni = input("Do you want pepperoni? Y or N: ").upper()

# Get user's choice for extra cheese
extra_cheese = input("Do you want extra cheese? Y or N: ").upper()

# Initialize the base price of the pizza
base_price = 0

# Calculate the price based on the size
if size == "S":
    base_price = 10
elif size == "M":
    base_price = 12
elif size == "L":
    base_price = 14
else:
    print("Invalid pizza size selected. Please choose S, M, or L.")

# Add pepperoni cost if requested
if add_pepperoni == "Y":
    if size == "S" or size == "M":
        base_price += 2
    else:
        base_price += 3

# Add extra cheese cost if requested
if extra_cheese == "Y":
    base_price += 1

# Calculate the total cost and display it to the user
print(f"Your total bill is ${base_price}. Enjoy your pizza!")
