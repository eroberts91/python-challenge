#python sceipt for reading csv file, running through every row and then exporting summary data into a txt file


#import modules needed for script
import os
import csv

#set file location path
csvpath = os.path.join('PyBank', 'resources', 'budget_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #print(csvreader)

    csv_header = next(csvreader)
    #print(f"CSV Header: (csv_header)")

    #sets initial storage variables for for loops
    net_total = 0
    months = 0
    
    #set blank lists for iterating through for delta values
    date_set = []
    income_set =[]

    #for loop which runs through entire csv file by rows, creates list of incomes, total montths and net income
    for row in csvreader:
        date_set.append(row[0])
        income_set.append(row[1])
        net_total = net_total + int(row[1])
        months = months + 1
    
    #set initial variables for for loop to determine min/max delta in profits
    net_delta = 0
    min = 0
    max = 0
    
    #for loop to find min and max difference between each month and preceeding month
    for i in range(0, len(income_set)-1):
        net_delta = net_delta + int(income_set[i+1]) - int(income_set[i])
        if int(income_set[i+1]) - int(income_set[i]) > max:
            max = int(income_set[i+1]) - int(income_set[i])
            max_date = date_set[i+1]
        elif int(income_set[i+1]) - int(income_set[i]) < min:
            min = int(income_set[i+1]) - int(income_set[i])
            min_date = date_set[i+1]

    # Generate financial output summary text file
    summary = (
        f"Financial Analysis\n"
        f"---------------------------------------\n"
        f"Total Months: {months}\n"
        f"Total: ${round(net_total,2)}\n"
        f"Average Change: ${(round(net_delta/(months-1),2))}\n"
        f"Greatest Increase in Profits: {max_date} (${max})\n"
        f"Greatest Decrease in Profits: {min_date} (${min})\n")
    #prints summary to terminal
    print(summary)

    #creates text file in analysis sub folder
    file_to_output = os.path.join('PyBank','analysis', "budget_analysis.txt")

    #writes financial summary to txt file
    with open(file_to_output, "w") as txt_file:
        txt_file.write(summary)