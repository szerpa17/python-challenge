# Python Challenge

Completed challenge to create Python scripts to analyze financial and voting records and export results as text files.

## PyBank

* Objective: Create a Python script for analyzing the financial records using financial data from [budget_data.csv](PyBank/Resources/budget_data.csv). The dataset is composed of two columns: `Date` and `Profit/Losses`. 

* The expected output analyzes the records and calculates the following: 

  * The total number of months included in the dataset

  * The net total amount of "Profit/Losses" over the entire period

  * The average of the changes in "Profit/Losses" over the entire period

  * The greatest increase in profits (date and amount) over the entire period

  * The greatest decrease in losses (date and amount) over the entire period

* In addition, the final script is to print the analysis to the terminal and export a text file with the results.

* Expected Output:

    ```text
    Financial Analysis
    ----------------------------
    Total Months: 86
    Total: $38382578
    Average  Change: $-2315.12
    Greatest Increase in Profits: Feb-2012 ($1926159)
    Greatest Decrease in Profits: Sep-2013 ($-2196167)
    ```

## Results
[PyBank Output](https://github.com/szerpa17/python-challenge/blob/master/PyBank/analysis/output.txt)
  ```text
Financial Analysis
----------------------------
Total Months: 86
Total: $38,382,578.00
Average Change: $-2,315.12
Greatest Increase in Profits: Jan-2012 $1,926,159.00
Greatest Decrease in Profits: Aug-2013 $-2,196,167.00
```

## PyPoll

* Objective: Create a Python script to review poll data within the [election_data.csv](PyPoll/Resources/election_data.csv) file. The dataset is composed of three columns: `Voter ID`, `County`, and `Candidate`. 

* The expected output analyzes the records and calculates the following: 

  * The total number of votes cast

  * A complete list of candidates who received votes

  * The percentage of votes each candidate won

  * The total number of votes each candidate won

  * The winner of the election based on popular vote.

* In addition, the final script is to both print the analysis to the terminal and export a text file with the results.

* Expected Output:

  ```text
  Election Results
  -------------------------
  Total Votes: 3521001
  -------------------------
  Khan: 63.000% (2218231)
  Correy: 20.000% (704200)
  Li: 14.000% (492940)
  O'Tooley: 3.000% (105630)
  -------------------------
  Winner: Khan
  -------------------------
  ```

## Results
[PyPoll Output](https://github.com/szerpa17/python-challenge/blob/master/PyPoll/analysis/output.txt)

```text
Election Results
-------------------------
Total Votes: 3521001
-------------------------
Khan: 63.0% (2218231)
Correy: 20.0% (704200)
Li: 14.0% (492940)
O'Tooley: 3.0% (105630)
-------------------------
Winner: Khan
-------------------------
```
