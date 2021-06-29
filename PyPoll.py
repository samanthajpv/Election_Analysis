# Add dependencies
import csv
import os

# Assign variable to load file from path
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign variable to save the file to path
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize total vote counter
total_votes = 0

# Candidate options and candidate votes
candidate_options = []
candidate_votes = {}

# 1: County list and county votes dictionary
county_list = []
county_votes = {}

# Track the winning candidate, vote count, and percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# 2: Track the largest county and county voter turnout
largest_county = ""
largest_county_ct = 0

# Read csv and convert into list of dictionaries
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read header row
    headers = next(file_reader)

    # Print each row in the CSV file
    for row in file_reader:
        # Add to the total vote count
        total_votes += 1
        # Get the candidate name from each row
        candidate_name = row[2]

        # 3: Extract the county name from each row
        county_name = row[1]

        # If the candidate does not match any existing candidate, add it to the candidate list
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list
            candidate_options.append(candidate_name)
            # Begin tracking that candidate's voter count
            candidate_votes[candidate_name] = 0
        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1
        
        # 4a: If statement that checks if the county does not match any existing county in the county list
        if county_name not in county_list:
            # 4b: Add the county to the list of counties
            county_list.append(county_name)
            # 4c: Begin tracking the county's vote count
            county_votes[county_name] = 0
        # 5: Add a vote to that county's vote count.
        county_votes[county_name] += 1

# Save the results to a text file
with open(file_to_save, "w") as txt_file:

    # Print final vote count
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n"
        f"County Votes:\n")
    print(election_results, end="")
    # Save final vote count to the text file
    txt_file.write(election_results)

    # 6a: For loop to get the county from the county dictionary
    for county_name in county_votes:
        # 6b: Retrieve the county vote count
        c_votes = county_votes[county_name]
        # 6c: Calculate the percentage of votes for the county
        c_vote_percentage = float(c_votes) / float (total_votes) * 100
        # 6d: Print the county results
        county_results = (f"{county_name}: {c_vote_percentage:.1f}% ({c_votes:,})\n")
        print(county_results)
        # 6e: Save the county results to the text file
        txt_file.write(county_results)

        # 6f: If statement to determine the winning county and get its vote count
        if (c_votes > largest_county_ct):
            largest_county_ct = c_votes
            largest_county = county_name

    # 7: Print the county with the largest turnout
    largest_county_turnout = (
        f"-------------------------\n"
        f"Largest County Turnout: {largest_county}\n"
        f"-------------------------\n")
    print(largest_county_turnout)
    # 8: Save the county with the largest turnout to the text file
    txt_file.write(largest_county_turnout)

    # Save the final candidate vote count to the text file
    for candidate_name in candidate_votes:
        # Retrieve vote count and percentage
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        # Print each candidate, their voter count, and percentage 
        print(candidate_results)
        #  Save the candidate results to the text file
        txt_file.write(candidate_results)

        # Determine winning vote count, winning percentage, and candidate
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage

    # Print the winning candidate's results
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    # Save the winning candidate's results to the text file
    txt_file.write(winning_candidate_summary)
