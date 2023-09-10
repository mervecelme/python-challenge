import os
import csv

budget_csv = os.path.join("..", "Resources", "budget_data.csv")

# open and read
with open (budget_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter= ",")
    
    
    # get header and skip next
    csv_header = next(csv_reader)

    total_months = 0
    total_value = 0
    average_change = 0
    
    first_value = 0
    last_value = 0

    greatest_increase = 0
    greatest_decrease = 0
    greatest_increase_date = ""
    greatest_decrease_date = ""
    value1 = 0
    
    # Loop data to calculate total months and print Total Months
    for row in csv_reader:
        # Months                     
        dates_list = {"dates": [row[0]]}
        total_months += int(len(dates_list["dates"]))

        # Total value
        total_value += int(row[1])
        
        # Average change
        if first_value == 0:
            first_value = int(row[1])
        last_value = int(row[1])

       # calculations of greatest values and dates 
        value2 = int(row[1])
        if value1 != 0:
            change = value2 - value1

            # Update greatest increase and greatest decrease
            if int(change) > int(greatest_increase):
                greatest_increase = change
                greatest_increase_date = row[0]

            if int(change) < int(greatest_decrease):
                greatest_decrease = change
                greatest_decrease_date = row[0]
        
        value1 = value2  

    
    print("\nFinancial Analysis\n-------------------------")
    print(f"Total Months: {total_months}")
    print(f"Total: ${total_value:,}")
    print(f"Average Change: ${round((last_value - first_value)/(total_months-1),2)}\n")
    print(f"Greatest Increase: {greatest_increase_date} (${greatest_increase})")
    print(f"Greatest Decrease: {greatest_decrease_date} (${greatest_decrease})")
