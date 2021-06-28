# The data needed to be retrieved:
# 1. The total # of votes cast
# 2. A complete list of candidates who received votes
# 3. The % of votes each candidate won
# 4. The total # of votes each candidate won
# 5. The winner of the election based on popular vote.

# Add our dependencies.
import csv
import os
# Assign variable to load file from path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign variable to save file to path.
file_to_save = os.path.join("Analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    # Print the header row.
    headers = next(file_reader)
    print(headers)
