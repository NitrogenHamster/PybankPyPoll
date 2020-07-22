import csv

# Files to load and output (Remember to change these)
file = "Resources/budget_data.csv"

MonthsTotal = 0
FullAmount = 0

previous = 0
monthly_change = []
Increase = 0
Decrease = 0

# Read the csv and use the information
with open(file) as revenue_data:
    reader = csv.DictReader(revenue_data)
    
    for row in reader:
        # Tracking  the values
        MonthsTotal = MonthsTotal + 1
        FullAmount = FullAmount + int(row['Profit/Losses'])

        if MonthsTotal > 1 :
            change=int(row['Profit/Losses'])-previous
            monthly_change.append(change)
        
            if change > Increase :
                Increase = change
                IncreaseMonth = row['Date']
                
            if change < Decrease :
                Decrease = change
                DecreaseMonth = row['Date']                
            
        previous= int(row['Profit/Losses'])
        
Amount_average = round(sum(monthly_change)/(len(monthly_change)+0.0),2)

print('Total months ' + str(MonthsTotal))
print('Total net amount pf profit/loses = ' + str(FullAmount))
print('Average change in profit/losses between months = ' + str(Amount_average))
print('The greatest increase in profits (date and amount) = ' + IncreaseMonth + ' $'+str(Increase))
print('The greatest decrease in losses (date and amount) = ' + DecreaseMonth + ' $'+str(Decrease))


