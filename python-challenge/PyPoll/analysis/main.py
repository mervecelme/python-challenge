import os
import csv

election_data = os.path.join("..","Resources","election_data.csv")

# open and read
with open(election_data) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ",")
    csv_header = next(csv_reader)
    
    total_votes = 0
    each_candidates = []
    value_ch = 0
    value_dd = 0
    value_ra = 0
    
    # Loop data
    for row in csv_reader:
        
        # Use length to calculate total votes
        ballotID_list = {"BallotID": [row[1]]}
        total_votes += int(len(ballotID_list["BallotID"]))
        
        # Name of each candidate
        candidate = row[2]
        if candidate not in each_candidates:
            each_candidates.append(candidate)

        # Total votes for candidate 1
        if candidate == "Charles Casper Stockham":
            value_ch += 1

        # Total votes for candidate 2
        if candidate == "Diana DeGette":
            value_dd += 1
        
        # Total votes for candidate 3
        if candidate == "Raymon Anthony Doane":
            value_ra += 1

    # Calculating each percentage votes
    percent_ch = round(float(value_ch/total_votes*100),3)
    percent_dd = round(float(value_dd/total_votes*100),3)
    percent_ra = round(float(value_ra/total_votes*100),3)

    # Printing values
    print("\nElection Results\n\n-------------------------\n")
    print(f"Total Votes: {total_votes}")
    print("\n-------------------------\n")
    print(each_candidates[0], ": ", "%", percent_ch, " ", "(", int(value_ch), ")", "\n")
    print(each_candidates[1], ": ", "%", percent_dd, " ", "(", int(value_dd), ")", "\n")
    print(each_candidates[2], ": ", "%", percent_ra, " ", "(", int(value_ra), ")", "\n")
    
    print("-------------------------\n")
    
    # Printing the winner
    if percent_ch > percent_dd and percent_ch > percent_ra:
        print("Winner: Charles Casper Stockham")
    elif percent_dd > percent_ch and percent_ra:
        print("Winner: Diana DeGette")
    elif percent_ra > percent_ch and percent_ra > percent_dd:
        print("Winner: Raymon Anthony Doane")
    
    print("\n-------------------------\n")
    

        
        


