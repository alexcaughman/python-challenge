import csv
import os

file_path = os.path.join('Resources' , 'budget_data.csv')

with open(file_path) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    
    line_count = 0

    months_detected = []
    profit_loss_aggregate = 0

    greatest_increase_month = ''
    greatest_increase_value = 0

    greatest_decreese_month = ''
    greatest_decrease_value = 0

    previous_profit_loss = None
    total_change_in_profit_loss = 0

    for row in csv_reader:
        line_count += 1

        # continue if header row
        if line_count == 1:
            continue

        month = row[0]
        profit_loss = int(row[1])

        # task 1 - accumulate months & determine total count 
        if month not in months_detected:
            months_detected.append(month)

        # task 2 - aggregate total profit/loss value
        profit_loss_aggregate += profit_loss

        # task 3 - average change
        if previous_profit_loss is not None:
            total_change_in_profit_loss += (profit_loss - previous_profit_loss)

        # task 4 - greatest increase
        if profit_loss > greatest_increase_value:
            greatest_increase_value = profit_loss
            greatest_increase_month = month

        # task 5 - greatest decrease
        if profit_loss < greatest_decrease_value:
            greatest_decrease_value = profit_loss
            greatest_decrease_month = month

        previous_profit_loss = profit_loss

    total_months = len(months_detected)
    average_change_precise = total_change_in_profit_loss / total_months

    print(f'Total Months: {len(months_detected)}')
    print(f'Total: ${profit_loss_aggregate}')
    print(f'Average Change: ${round(average_change_precise, 2)}')
    print(f'Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase_value})')
    print(f'Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease_value})')

    #output analysis

    output_path = os.path.join('Analysis' , 'results.txt')

    with open (output_path, 'w') as txtfile:
        txtfile.write(f'Total Months: {len(months_detected)}\n')
        txtfile.write(f'Total: ${profit_loss_aggregate}\n')
        txtfile.write(f'Average Change: ${round(average_change_precise, 2)}\n')
        txtfile.write(f'Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase_value})\n')
        txtfile.write(f'Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease_value})\n')
