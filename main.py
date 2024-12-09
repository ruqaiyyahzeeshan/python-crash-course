#------------------------------------These are the variables and inputs to get started.-------------------------------------------
#the variables in the next 6 lines had their name changed from codesnip 6 on slide 17 to match multiplication vocabulary.
startingFactor1Str = input("What is the starting factor1 number? ")
endingFactor1Str = input("What is the ending factor1 number? ")
factor2MaxNumberStr = input(" How far do you want each product to go up for factor2 ? ")  #Factor 2’s value
#convert all Str variables to Int variables
startingFactor1Int = int(startingFactor1Str)
endingFactor2Int = int(endingFactor1Str)
factor2MaxNumberInt = int(factor2MaxNumberStr)
loopIncrement1 = 1	#This is the variable that is hardcoded for your outer for loop and to be used in extension
loopIncrement2 = 1	#this is the variable that is hardcoded for your inner for loop and to be used in extension
#--------------------------------This is the part you add your code to below------------------------------------------------------
#Take your logic from slide 17, CodeSnip 6 (x,y) coordinates, adapt it to the multiplication table. Specifically the nested for loops.
#change inputValueXInt to factor1Int in outside for loop and outputValueY to factor2Int in inside for loop from codeSnip6



for w in range(startingFactor1Int, endingFactor2Int + 1):
    for i in range(1, factor2MaxNumberInt + 1):
        print(str(w) + "*" + str(i) + "=" + str(w * i))
