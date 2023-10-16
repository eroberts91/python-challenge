#python sceipt for reading csv file, running through every row and then exporting summary data into a txt file


#import modules needed for script
import os
import csv

#set file location path
csvpath = os.path.join('resources', 'election_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #print(csvreader)

    csv_header = next(csvreader)
    #print(f"CSV Header: (csv_header)")

    #sets initial storage variables for for loop
    vote_total = 0
    candidate_list = []
    cand1_count = 0
    cand2_count = 0
    cand3_count = 0


    #for loop which runs through entire csv file by rows to sum total votes and create candidate list
    for row in csvreader:
        #sums total number of votes
        vote_total = vote_total + 1
        #add candidates  to list if not already added
        if row[2] not in candidate_list:
            candidate_list.append(row[2])
        #print(row[2])
    
        #conditional to total up each candidate vote total
        if row[2] == candidate_list[0]:
            cand1_count = cand1_count + 1
        elif row[2] == candidate_list[1]:
            cand2_count = cand2_count + 1
        elif row[2] == candidate_list[2]:
            cand3_count = cand3_count + 1
 
    if cand1_count > cand2_count and cand3_count:
        winner = candidate_list[0]
    elif cand2_count > cand1_count and cand3_count:
        winner = candidate_list[1]
    else:
        winner = candidate_list[2]
    
    #create summary file for terminal and .txt output
    summary = (
        f"Election Results\n"
        f"---------------------------------------\n"
        f"Total Votes: {vote_total}\n"
        f"---------------------------------------\n"
        f"{candidate_list[0]}: {round((100*cand1_count/vote_total),3)}% ({cand1_count})\n"
        f"{candidate_list[1]}: {round((100*cand2_count/vote_total),3)}% ({cand2_count})\n"
        f"{candidate_list[2]}: {round((100*cand3_count/vote_total),3)}% ({cand3_count})\n"
        f"---------------------------------------\n"
        f"Winner: {winner}\n"
        f"---------------------------------------")
    
    print(summary)

        #creates text file in analysis sub folder
    file_to_output = os.path.join("analysis", "election_analysis.txt")

    #writes financial summary to txt file
    with open(file_to_output, "w") as txt_file:
        txt_file.write(summary)