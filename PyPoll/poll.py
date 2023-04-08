# import dependencies
import csv
import os

# open the data file
# csvfile = "/Users/deronpayton/Desktop/PythonPractice/election_analysis/election_results.csv"

csvfile = os.path.join("Resources", "election_data.csv")
results = os.path.join("Analysis", "election_analysis.txt")

# assign a variable to count total votes and set it to 0, putting above the main body of code to be called back on later
# assign a variable to count the number of candidates and set it to an empty list to be filled in when I iterate through the csv
# declare an empty dictionary to hold the vote count for the candidates. Using a dictionary here so I can save the key value pairs of candidate and votes
total_votes = 0
candidate_options = []
candidate_votes = {}
# Declare variables to help calculate the winning candidate, count and percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# open the election results and save to a variable. Use the reader function to open the file object we named and read the header rows (and skip them?)for when we iterate through the file later. 
with open(csvfile) as election_data:
    file_reader = csv.reader(election_data)
    headers = next(file_reader)
    for row in file_reader:
        # adds 1 to the vote count for each row in the csv, += means it adds another value to the variables value and assigns that new value back to the variable and continues the 
        # count until there are no entries left
        total_votes += 1
        # sets a variable to count the candidates and set this variable to the value in index 2, which is column 3
        candidate_name = row[2]
        # If statement saying that if the candidate does not match any existing entries, add him to the candidate_options list
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
        # Start tracking the condidates votes and set the initial value to 0
            candidate_votes[candidate_name] = 0
        # Start counting each candiates votes and adding 1 to the total every time the name matches a candidate
        candidate_votes[candidate_name] += 1
with open(results, "w") as txt_file:
    # print(f"\n")
    # print("Election Results")
    # print("==========================")
    # print(total_votes)
    # print("==========================")
    election_results = (
        f"\nElection Results\n"
        f"\n==============================\n"
        f"\nTotal Votes: {total_votes:,}\n"
        f"\n==============================\n")
    print(election_results, end="")
    txt_file.write(election_results)
# Print the total amount of candidate votes in the candidate votes dictionary
# print(candidate_votes)

    # Determine the percentage of votes for each candidate by looping through the counts
    # Iterate through the cadidate list
    for candidate_name in candidate_votes:
            # retrieve vote count of a candidate
        votes = candidate_votes[candidate_name]
            # Calculate the percentage of votes
        vote_percentage = float(votes) / float(total_votes) * 100

        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)
        txt_file.write(candidate_results)
            # To Do: print out each candidate's name, vote count, and percentage of votes to the terminal
        if (votes > winning_count) and (vote_percentage > winning_percentage):
                # if true then set winning_count = votes and winning_percent = vote_percentage
            winning_count = votes
            winning_percentage = vote_percentage
                # And set the winning_candidate equal to the candidate's name
            winning_candidate = candidate_name
            #To Do: print out the winning candidate, vote count and percentage to terminal
            # print(f"{candidate_name}: received {vote_percentage:.2f}% of the vote")

    winning_candidate_summary = (
        f"\n==============================\n"
        f"\nWinner: {winning_candidate}\n"
        # f"Winning Vote Count: {winning_count:,}\n"
        # f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"\n==============================\n")
    print(winning_candidate_summary)

    txt_file.write(winning_candidate_summary)