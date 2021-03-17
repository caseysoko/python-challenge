# PyPoll 
# Calculate the following
# - total number of votes cast
# - complete list of candidates who received votes 
# - percentage of votes each candidate won
# - total number of votes each candidate won
# - winner of election based on popular vote 
# ouput the analysis to terminal and export to txt file

import os
import csv

total_votes = 0
candidates_col = 2
poll = {}
candidates = {}

csv_path = os.path.join('Desktop','python-challenge','PyPoll','Resources','election_data.csv')
with open(csv_path, newline="") as csvfile:
    csvreader=csv.reader(csvfile, delimiter=",")
    csv_header=next(csvreader)

    for row in csvreader:
        total_votes=total_votes+1

        if (row[candidates_col] in poll):
            poll[row[candidates_col]] = poll[row[candidates_col]] + 1
        else:
            poll[row[candidates_col]] = 1
    
    results = "Election Results"
    results = results + "--------------------"
    results = results + f"Total Votes:{total_votes}"
    results = results + "--------------------"

    if total_votes !=0:
        for key, value in poll.items():
            percentage = "{0:3f}".format(round(value/total_votes*100,3))
            results = results + f"{key}: {percentage}% ({value})"
        results = results + "-----------------"

        v=list(poll.values())
        k=list(poll.keys())
        winner = k[v.index(max(v))]
        results = results + f"Winner: {winner}"
    else:
        results = results + "Empty"
    results = results + "------------------"

    print(results)

    output_path=os.path.join("Analysis", "PyPollAnalysis.txt")
    output_file=open("PyPollAnalysis.txt","w")
    output_file.write(results)





    
