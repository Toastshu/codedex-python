#Ex 1 Calculate the area of a rectangle
l = float(input("Enter the length of the rectangle: "))
b = float(input("Enter the breadth of the rectangle: "))
area= l*b
print("The area of the rectangle is", area)

Enter the length of the rectangle: 6
Enter the breadth of the rectangle: 7
The area of the rectangle is 42.0

#Ex 2 shopping cart program
item = input("What item would you like to purchase?")
price = float(input("What is the price?: "))
quantity = int(input("How many items would you like to have?:"))
total = price*quantity
print(f"You have bought {quanity} {items}")
print(f"Here is your total: ${total}")

What item would you like to purchase? Burgers
What is the price?: 12
How many items would you like to have?:7
You have bought 7 x  Burgers
Here is your total: $84.0
