import csv
import os

#Assign a variable for the file to load from a path
file_to_load = os.path.join("Resources", "election_results.csv")

#Assign a variable for the file to save to a path
file_to_save = os.path.join("analysis","elections_analysis.txt")

#initialize total vote counter
total_votes = 0

#candidate options list
candidate_options = []

#create empty dictionary to hold candidate name and votes
candidate_votes = {}

#winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0 

#Open the election results and read the file
with open(file_to_load) as election_data:

    #To do: read and analyze the data here
    file_reader = csv.reader(election_data)

    #read the header row
    headers = next(file_reader)

    #print each row in the CSV file
    for row in file_reader:
        
        #add to total vote count
        total_votes += 1

        #get candidates name
        candidate_name = row[2]

        #if candidate name does not match existing candidate
        if candidate_name not in candidate_options:

            candidate_options.append(candidate_name)

            #track candidates votes
            candidate_votes[candidate_name] = 0

        #add a vote to the candidates count
        candidate_votes[candidate_name] += 1

#save results to text file
with open(file_to_save,"w") as txt_file:

    #print final vote count to terminal
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")

    #save final count to text file
    txt_file.write(election_results)

    #iterate through the candidate list
    for candidate_name in candidate_votes:
        
        #retrieve vote count of candidate
        votes = candidate_votes[candidate_name]

        #calculate % of votes
        vote_percentage = float(votes)/float(total_votes) * 100

        #print candidates' names, votes, percentage
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        #print candidate results to terminal
        print(candidate_results)

        #save candidate results to text file
        txt_file.write(candidate_results)

        #determine if vote is greater than winning count
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name 

    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

    #save winning candidate to text file
    txt_file.write(winning_candidate_summary)