import os
import csv
bank_csv = os.path.join('..', '..', 'Instructions', 'PyBank', 'Resources', 'budget_data.csv')
with open(bank_csv, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    date = []
    prof_loss = []
    current_month_value = 0
    monthly_difference = []

    for row in csvreader:
        date.append(row[0])
        prof_loss.append(int(row[1]))
        if current_month_value == 0:
            current_month_value = int(row[1])
            previous_month_value = current_month_value
        current_month_value = int(row[1])
        monthly_difference.append(int(current_month_value) - int(previous_month_value))
        previous_month_value = current_month_value
    
    total_sum_profits = sum(prof_loss)
    total_sum_profits = '${:,.2f}'.format(total_sum_profits)
    avg_change = sum(monthly_difference) / (len(monthly_difference) - 1)
    avg_change = '${:,.2f}'.format(avg_change)
    max_change = max(monthly_difference)
    max_change = '${:,.2f}'.format(max_change)
    max_change_index = monthly_difference.index(max(monthly_difference))
    max_change_date = date[max_change_index]
    min_change = min(monthly_difference)
    min_change = '${:,.2f}'.format(min_change)
    min_change_index = monthly_difference.index(min(monthly_difference))
    min_change_date = date[min_change_index]
print(f'Financial Analysis')
print(f'--------------------------------------------------')
print(f'Total Months: {len(date)}')
print(f'Total: ${(total_sum_profits)}')
print(f'Average Change: {avg_change}')
print(f'Greatest Increase in Profits: {max_change_date} ({max_change})')
print(f'Greatest Decrease in Profits: {min_change_date} ({min_change})')
output = open('output.txt', 'w')
print(f'Financial Analysis', file=output)
print(f'--------------------------------------------------', file=output)
print(f'Total Months: {len(date)}', file=output)
print(f'Total: ${(total_sum_profits)}', file=output)
print(f'Average Change: {avg_change}', file=output)
print(f'Greatest Increase in Profits: {max_change_date} ({max_change})', file=output)
print(f'Greatest Decrease in Profits: {min_change_date} ({min_change})', file=output)


