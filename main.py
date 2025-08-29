fruit_prices = {
    "apple": 2.5,
    "banana": 1.2,
    "orange": 1.8,
    "strawberry": 3.0,
    "mango": 4.5
}
print("==============================")
print(fruit_prices)
print("==============================")
user_input = input("Enter a fruit name: ").lower()

if user_input in fruit_prices:
 
    print(f"The price of {user_input} is {fruit_prices[user_input]} JD")
else:
    print("Sorry, this fruit is not available.")  