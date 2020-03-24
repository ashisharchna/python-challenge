#import modules
import os
import csv

#create file path
budget_csv = os.path.join("../PyBank", "budget_data.csv")

#read csv file
with open(budget_csv) as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    header = next(reader)
    
    Change = 0
    Row_1= next(reader)
    Total_Months= 1
    Total_Profit_Loss = int(Row_1[1])
    Avg_Change = []
    Months = []
    Previous = Row_1[1]

    #looping through the rows in the csv file
    for row in reader:                      
      
      #calculate total number of months
        Total_Months += 1

        #Net Total of Profit and Loss
        Total_Profit_Loss += int(row[1])

        #Finding the change from one month to another and store in a list called Avg_Change

        Change = int(row[1])- int(Previous) # row[1] is the third row and previous is the 2nd row to begin with
        Avg_Change. append(Change)
        Previous= row[1]           # previous is updated to hold the new row value

        Months.append(row[0])
    
    #Average of the changes in profit and loss over the entire period
    Average = sum(Avg_Change)/len(Avg_Change)

    #Greatest decrease in losses
    Min_Change = min(Avg_Change)

    #Greatest increase in profits
    Max_Change= max(Avg_Change)

    Min_Index = Avg_Change.index(Min_Change)

    Max_Index = Avg_Change.index(Max_Change)

    #printing the output to the terminal

    print("Financial Analysis")

    print("-------------------")

    print("Total Months: " + str(Total_Months))

    print("Total:" + "$"+ str(Total_Profit_Loss))

    print(f"Average Change:${Average: .2f}")

    print(f"Greatest Increase in Profits:  {Months[Max_Index]}  (${Max_Change})")

    print(f"Greatest Decease in Profits:  {Months[Min_Index]}  (${Min_Change})")


    #Exporting the output to a text file called PyBank.text

    f = open("PyBank.txt", "w")
    
    print("Financial Analysis", file = f)

    print("-------------------", file = f)

    print("Total Months: " + str(Total_Months), file = f)

    print("Total:" + "$"+ str(Total_Profit_Loss), file = f)

    print(f"Average Change:${Average: .2f}", file = f)

    print(f"Greatest Increase in Profits:  {Months[Max_Index]}  (${Max_Change})", file = f)

    print(f"Greatest Decease in Profits:  {Months[Min_Index]}  (${Min_Change})", file = f )
  
    f.close()

    

    
