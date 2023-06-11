#Travel Expenses
#06-10-23
#CTI-110 P1HW2 - Travel Expense
#Taylor Rockefeller
#
#Display('This program calculates and displays travel expenses')
print('This program calculates and displays travel expenses')
#Display('Please enter your budget:') Input and set budget
budget = int(input('Please enter your budget:'))
#Display('Please enter your travel destination:') input and set location
location = input('Please enter your travel destination:')
#Display('Please enter estimated cost of gas:') input and set gas
gas = int(input('Please enter estimated cost of gas:'))
#Display('Please enter how much accomidations(Hotel) will cost:') input and set hotel
hotel = int(input('Please enter how much accomidations/Hotel will cost:'))
#Display('Please enter how much you will spend on food:') input and set food
food = int(input('Please enter how much you will spend on food:'))
#set total_expenses = gas + hotel + food
total_expenses = gas+hotel+food
#set remaining_balance = budget - total_expenses
remaining_balance = budget-total_expenses
#Display(Travel Expenses)
print('Travel Expenses')
#Display('Location:', location)
print('Location:',location)
#Display('Budget:', budget)
print('Budget:', budget)
#Display('Expenses')
print('Expenses')
#Display('Hotel:', hotel)
print('Hotel:', hotel)
#Display('Gas:', gas)
print('Gas:', gas)
#Display('Food:', food)
print('Food:', food)
#Display('Remaining Balance:', remaining_balance)
print('Remaining Balance:', remaining_balance)
