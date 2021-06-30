# PyPoll with Python - Election Analysis

## Project Overview
Tom, an employee of the Colorado Board of Elections, was tasked to do an election audit to report and certify the winner for a certain US congressional race. His manager, Seth, wants to know if the process can be automated using Python. If successful, the code can be used to audit other local elections. 
Below are the outlined steps used as a guide in creating the code:
1. Calculate total number of votes cast
2. Get list of candidates who received votes
3. Calculate percentage of votes each candidate won
4. Calculate total number of votes each candidate won
5. Determine the winner of the election based on popular vote

### The Challenge
Aside from the guideline above, the election commission requested additional information to complete the audit. Below are the added requirements:
1. Calculate voter turnout for each county
2. Calculate percentage of votes from each county out of the total vote count
3. Determine the county with the highest turnout

## Resources
- Data: [election_results.csv](https://github.com/samanthajpv/Election_Analysis/blob/4717f75adeafcb115012f059760e9bb883eb3bb4/Resources/election_results.csv)
- Software: Python 3.7.6, Visual Studio Code 1.56.2

## Election Audit Results
The *election_results.csv* file was read using Python. By making use of Python lists, dictionaries, decision and repetition statements, and printing/writing of output to a text file, the results are as follows:

- A total of 369,711 votes were cast in this congressional election. 
```
# Read csv and convert into list of dictionaries
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read header row
    headers = next(file_reader)

    # Print each row in the CSV file
    for row in file_reader:
        # Add to the total vote count
        total_votes += 1
```
After opening the file and skipping the header, for each row that was read, 1 was added to the ```total_votes``` tally where it was initialized with 0 as starting value.

- The election audit reported three counties and below is the breakdown:
    - Jefferson county with 10.5% of the total number of votes consisting of 38,855 votes.
    - Denver county with 82.8% of the total number of votes consisting of 306,055 votes.
    - Arapahoe county with 6.7% of the total number of votes consisting of 24,801 votes.
```
# 4a: If statement that checks if the county does not match any existing county in the county list
        if county_name not in county_list:
            # 4b: Add the county to the list of counties
            county_list.append(county_name)
            # 4c: Begin tracking the county's vote count
            county_votes[county_name] = 0
        # 5: Add a vote to that county's vote count.
        county_votes[county_name] += 1

# continuation...    

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
```
An empty list,```county_list```, was created to store the the county names as seen in code 4a above using an if statement. On the other hand, an empty dictionary ```county_votes``` was created to store the county names as keys and number of votes as values. Each time the if statement runs, a vote is added to the number of votes for the county name in the row being read.
The percentage was calculated by a for loop accessing the county name from the dictionary. The votes for each county was transformed into a float and was divided by the float of the total number of votes before multiplying by 100. Then, the results were written to a text file.

- The county that had the largest number of votes was Denver.
```
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
```
The variable ```largest_county``` was created and initially set as an empty string together with ```largest_county_ct``` set to 0. With an if statement, ```c_votes``` is being checked if it is greater than the county with the largest number of votes. If it is, it assigns it to the variable ```largest_county_ct``` and assigns the county name to ```largest_county```. Output is then printed and saved to the text file.

- The candidate results were:
    - Charles Casper Stockham received 23.0% of the total votes with 85,213 votes.
    - Diana DeGette received 73.8% of the total votes with 272,892 votes.
    - Raymon Anthony Doane received 3.1% of the total votes with 11,606 votes.

The audit reported three candidates. The code for getting the candidate results has the same logic with the code for getting the county results. An empty list and dictionary were created to store the names and votes for each candidate using decision and repetition statements.

- The winner of the election was:
    - Diana DeGette who received 73.8% of the total votes with 272,892 votes. 
```
# Determine winning vote count, winning percentage, and candidate
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage
```
Similar to the code for determining the county with the largest number of votes, the output for the election winner also kept track of the vote percentage.

## Summary

The script can be modified to further simplify and enhance its readability. A possible proposal to the election commission would be to use the get method not only to shorten the code but also make it cleaner. 
```
# Example:
# create empty dictionary before reading the file
counts = {}
# insert code to open file...
# Print each row in the CSV file
    for row in file_reader:
        # Extract the county name from each row
        county_name = row[1]
        # formula patterned after example in https://www.py4e.com/html3/09-dictionaries
        counts[county_name]=counts.get(county_name,0)+1
print(counts.items())

# The result would be:
dict_items([('Jefferson', 38855), ('Denver', 306055), ('Arapahoe', 24801)])
```
The get method simplifies the counting loop by using the dictionary and stores keys that are not yet in it. Another modification that can be done to improve the code is to sort the results in descending order. This will make the results easier to read and make it more presentable.

## References

(1) Trilogy Education Services. (2021, June). *Module 3 Challenge*. https://courses.bootcampspot.com/courses/626/assignments/13378?module_item_id=211904

(2) *Dictionaries*. (n.d.). PY4E. Retrieved on June 30, 2021 from https://www.py4e.com/html3/09-dictionaries
