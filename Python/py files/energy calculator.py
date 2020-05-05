price = input('Enter Unit Price:')
hours = input('Enter Hours used in a day:')
watts = input('Enter wattage of appliance:')

DailyEM = int(watts) * int(hours) / 1000
print(f'Daily Enery consumption = {DailyEM}kwh')
MonthlyEM = int(DailyEM) * 30
print (f'Yearly Energy Consumption = {MonthlyEM}kwh')
price = int(DailyEM) * int(price)
print(f'\nthis is how much it costs to run per day:{price}')
