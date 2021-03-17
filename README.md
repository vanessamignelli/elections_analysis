# Elections_Analysis

## Project Overview
The purpose of this project was to complete an elections audit for the Coldorado Board of Elections to better examine the results of a recent local congressional election. To understand the election results, the following was completed:

1. Calculate the total number of votes cast. 
2. Get a complete list of candidates who received votes. 
3. Calculate the total number of votes each candidate received. 
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on popular vote. 

## Resources
- Data Source: election_results.csv
- Software: Python 3.76, Visual Studio Code

## Summary
The analysis of the election shows that:
- There were 369,711 votes cast in the election
- The county results were:
  - Jefferson county cast 38,855 votes (10.5% of all votes)
  - Denver county cast 306,055 votes (82.8% of all votes)
  - Arapahoe county cast 24,801 votes (6.7% of all votes)
- The county with the largest number of votes was:
  - Denver with 306,055 votes (82.8%)
- The candidate results were:
  - Charles Casper Stockham recieved 23.0% of the vote and 85,213 votes total.
  - Diana DeGette recieved 73.8% of the vote and 272,892 votes total.
  - Raymond Anthony Doane recieved 3.1% of the vote and 11,606 votes total.
- The winner of the election was:
  - Diana DeGette who received 73.8% of the vote and 272,892 number of votes.

## Election-Audit Summary
Since the code for the election audit creates a lot of empty lists, dictionaries and variables to use in our calculations are formulas, we can applying this code to any election, as long as the data in the csv file is formatted in the same way. The various loops and if statements in the code are written to extract the unique candidate names and county names, and use them to create a list to be later used within the code. Because we do not use predefined list, this methodology can be used with a completely new dataset. This further applies to the for loops and if statements that help to calculate total votes and vote percentages. 
