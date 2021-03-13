my_votes = int(input("How many votes did you get in the election? "))
total_votes = int(input("What is the total votes in the election? "))
percentage_votes = (my_votes / total_votes) * 100
print(f"I received {percentage_votes}% of the total votes.")

#multi-line f-strings 
candidate_votes = int(input("How many votes did the candidate get in this election? "))
total_tally_votes = int(input("What is the total number of votes in the election?" ))
message_to_cand = (
    f"You received {candidate_votes:,} number of votes. "
    f"The total number of votes was {total_tally_votes:,}. "
    f"You received {candidate_votes/total_tally_votes * 100:.2f}% of total votes. "
)

print(message_to_cand)