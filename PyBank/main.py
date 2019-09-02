# PyBank Homework
# Import os and csv reader
import os
import csv

# Open csv file
csvpath = os.path.join("budget_data.csv")

# Read with CSV Reader
# Skipping Header
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    file_header = next(csvreader)

    # Lists for iterating through "Date" and "Profit/Losses"
    number_months = []
    net_total_pl = []
    

    # Iterate through rows
    # First through "Date" columns
    # Second through the "Profit/Losses" Column
    for rows in csvreader:
        number_months.append(rows[0])
        net_total_pl.append(int(rows[1]))

    # calculates total number of months
    total_months = len(number_months)

    #calculate total net anoumt of profits and loses
    total_pl = sum(net_total_pl)

    # List for iterating through PL for "average change"
    average_change_pl = []
    
    # Iterate through rows to find "average change"
    for i in range(len(net_total_pl)-1):

        # Calculates change in PL
        average_change_pl.append(net_total_pl[i+1] - net_total_pl[i])

    # Calculates average change in PL
    # Round results to 2 decimals
    avg_change = round(sum(average_change_pl) / len(average_change_pl),2)

    # find Greates increase and decrease
    greatest_increase = max(average_change_pl)
    greatest_decrease = min(average_change_pl)
    
    # find Greatest incrase and decrease months in "month" list
    gi_month = number_months[average_change_pl.index(max(average_change_pl)) + 1]
    gd_month = number_months[average_change_pl.index(min(average_change_pl)) + 1]

# Print financial analys
print("Financial Analysis")
print("----------------------------------")
print("Total Months: "+ str(total_months))
print("Total Net Amount of Profit/Losses: $" + str(total_pl))
print("Average Change: $" + str(avg_change))
print("Greatest Increase in Profits: " + gi_month + " $" + str(greatest_increase))
print("Greatest Decrease in Profits: " + gd_month + " $" + str(greatest_decrease))


# Save as csv file

# Specifed the file to write to
output_path = os.path.join("financial_analysis.csv")

# Open file using Write mode
with open(output_path, 'w', newline='') as csvfile:
    
    # Initialize csv writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    csvwriter.writerow(['Financial Analysis'])
    csvwriter.writerow(['--------------------------------'])
    csvwriter.writerow(["Total Months: "+ str(total_months)])
    csvwriter.writerow(["Total Net Amount of Profit/Losses: $" + str(total_pl)])
    csvwriter.writerow(["Average Change: $" + str(avg_change)])
    csvwriter.writerow(["Greatest Increase in Profits: " + gi_month + " $" + str(greatest_increase)])
    csvwriter.writerow(["Greatest Decrease in Profits: " + gd_month + " $" + str(greatest_decrease)])
