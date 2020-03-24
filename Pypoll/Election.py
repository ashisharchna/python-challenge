#import the modules
import os
import csv

#set the file path
Poll_csv = os.path.join("../Pypoll", "election_data.csv")

with open(Poll_csv) as csvfile:
    reader = csv.reader(csvfile, delimiter = ',')
    header = next(reader)

    Total_Voters=0

    Votes_Khan= 0
    Votes_Correy = 0
    Votes_Li = 0
    Votes_Tooley = 0
    
#looping through each row in the data file
    for row in reader:
        
        Total_Voters += 1

        if(row[2]=="Khan"):
            Votes_Khan +=1
        elif(row[2]=="Correy"):
            Votes_Correy +=1
        elif(row[2] == "Li"):
            Votes_Li +=1
        else:
            Votes_Tooley +=1

        
    Per_Khan = (Votes_Khan/Total_Voters)*100
    Per_Correy = (Votes_Correy/Total_Voters)*100
    Per_Li = (Votes_Li/Total_Voters)*100
    Per_Tooley = (Votes_Tooley/Total_Voters)*100


    #Printing the output to the terminal
    print("Election Results")
    print("-------------------")
    print(" Total Votes: " +  str(Total_Voters)) 
    print("-------------------")
    print(f" Khan: {Per_Khan: .3f}% ({Votes_Khan})") 
    print(f" Correy: {Per_Correy: .3f}% ({Votes_Correy})") 
    print(f" Li: {Per_Li: .3f}% ({Votes_Li})") 
    print(f" O'Tooley: {Per_Tooley: .3f}% ({Votes_Tooley})") 
    print("-------------------")

#Checking for the winner
    Winner = max(Votes_Khan, max(Votes_Correy, max(Votes_Li, Votes_Tooley)))

    if(Winner == Votes_Khan):
        print(" Winner: Khan")
    elif(Winner == Votes_Correy):
        print(" Winner: Correy")
    elif(Winner == Votes_Li):
        print(" Winner: Li")
    else:
        print(" Winner: O'Tooley")
    
    print("-------------------")


#writing the output to a text file, "PyPoll.text"
    f= open("PyPoll.text", "w")

    print("Election Results", file = f)

    print("-------------------", file = f)
    
    print(" Total Votes: " +  str(Total_Voters), file = f)
    
    print("-------------------", file = f)

    print(f" Khan: {Per_Khan: .3f}% ({Votes_Khan})", file = f) 

    print(f" Correy: {Per_Correy: .3f}% ({Votes_Correy})", file = f) 

    print(f" Li: {Per_Li: .3f}% ({Votes_Li})", file = f) 

    print(f" O'Tooley: {Per_Tooley: .3f}% ({Votes_Tooley})", file = f) 

    print("-------------------", file = f)

    if(Winner == Votes_Khan):
        print(" Winner: Khan", file = f)
    elif(Winner == Votes_Correy):
        print(" Winner: Correy", file = f)
    elif(Winner == Votes_Li):
        print(" Winner: Li", file = f)
    else:
        print(" Winner: O'Tooley", file = f)

    f.close()
    
