#python sceipt for reading csv file, running through every row and then exporting summary data into a txt file


#import modules needed for script
import os
import csv

#set file location path
csvpath = os.path.join('resources', 'budget_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #print(csvreader)

    csv_header = next(csvreader)
    #print(f"CSV Header: (csv_header)")

    #sets initial storage variables for for loop
    net_total = 0
    months = 0
    min = 0
    max = 0

    #for loop which runs through entire csv file by rows
    for row in csvreader:
        net_total = net_total + int(row[1])
        months = months + 1
        if int(row[1]) > max:
            max = int(row[1])
            max_date = row[0]
        elif int(row[1]) < min:
            min = int(row[1])
            min_date = row[0]

    # Generate financial output summary text file
    summary = (
        f"Financial Analysis\n"
        f"---------------------------------------\n"
        f"Total Months: {months}\n"
        f"Total: ${net_total}\n"
        f"Average Change: ${(round(net_total/months,2))}\n"
        f"Greatest Increase in Profits: {max_date} (${max})\n"
        f"Greatest Decrease in Profits: {min_date} (${min})\n")


    #prints summary to terminal
    print(summary)

    #creates text file in analysis sub folder
    file_to_output = os.path.join("analysis", "budget_analysis.txt")

    #writes financial summary to txt file
    with open(file_to_output, "w") as txt_file:
        txt_file.write(summary)
