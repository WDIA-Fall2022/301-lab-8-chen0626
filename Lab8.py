
#Prompts the user for the number of Tests
#Note that this function will include call(s) to the input function
#Keep prompting until the number is an integer. Each grade is in between 0 and 100..
#Returns the number of Tests
def getNumberOfTests():
    while True:
        try:
            t = int(input("please enter number of your tests: "))
            if 0 <= t <= 100:
                break
            else:
                print("Enter an integer between 0 and 100")
        except ValueError:
            print("Sorry, I don't understand it.")
    return t

#Prompts the user for the weigth of Assignments
#Note that this function will include call(s) to the input function
#Keep prompting until the number is a float >= 0 and <= 1
#Returns the weight of assignments
def getWeightOfAssignments():
    while True:
        try:
            a = float(input("please enter the weight of assignments: "))
            if 0 <= a <= 1:
                break
            else:
                print("Enter an float between 0 and 1")
        except ValueError:
            print("Sorry, I don't understand it.")
    return a

#Prompts the user for the weigth of Midterms
#Note that this function will include call(s) to the input function
#Keep prompting until the number is a float >= 0 and <= 1
#Returns the weight of midterms
def getWeightOfMidTerms():
    while True:
        try:
            m = float(input("please enter the weight of Midterms: "))
            if 0 <= m <= 1:
                break
            else:
                print("Enter an float between 0 and 1")
        except ValueError:
            print("Sorry, I don't understand it.")
    return m

#Prompts the user for the weigth of the final
#Note that this function will include call(s) to the input function
#Keep prompting until the number is a float >= 0 and <= 1
#Returns the weight of final
def getWeightOfFinal():
    while True:
        try:
            f = float(input("please enter the weight of the final: "))
            if 0 <= f <= 1:
                break
            else:
                print("Enter an float between 0 and 1")
        except ValueError:
            print("Sorry, I don't understand it.")
    return f

#returns True if the sum of the 3 arguments is 1, False otherwise
#Assign the default values 0.4 0.35 0.25 to wAssign, wMidtern and wFinal respectively
def checkWeights(wAssign=0.4,wMidTerm=0.35,wFinal=0.25):
    if (wAssign + wMidTerm + wFinal) == 1:
        return True
    else:
        return False

#calculate the numeric grade as specified in the course outline
def calculateNumericGrade(AvgAssignments,AvgTests,final,wOfAssign,wOfMidTerms,wFinal):
    finalScore = AvgAssignments * wOfAssign + AvgTests * wOfMidTerms + final * wFinal
    return finalScore


#convert the numeric grade to a letter according to the conversion table
#in the course outline

def calculateLetterGrade(numericGrade):
    grade = ""
    if 90 <= numericGrade <= 100:
        grade = 'A+'
    elif 85 <= numericGrade <= 89:
        grade = 'A'
    elif 80 <= numericGrade <= 84:
        grade = 'A-'
    elif 77 <= numericGrade <= 79:
        grade = 'B+'
    elif 73 <= numericGrade <= 76:
        grade = 'B'
    elif 70 <= numericGrade <= 72:
        grade = 'B-'
    elif 67 <= numericGrade <= 69:
        grade = 'C+'
    elif 63 <= numericGrade <= 66:
        grade = 'C'
    elif 60 <= numericGrade <= 62:
        grade = 'C-'
    elif 57 <= numericGrade <= 59:
        grade = 'D+'
    elif 53 <= numericGrade <= 56:
        grade = 'D'
    elif 50 <= numericGrade <= 52:
        grade = 'D-'
    elif 0 <= numericGrade <= 49:
        grade = 'F'
    else:
        print("please enter an integer")

    return grade



#Get the weight value of the assignments (call the appropriate function)
#Get the weight value of tests (call the appropriate function)
#Get the weight value of the  final (call the appropriate function)
#Check the sum of weight values is 1 (call the appropriate function)
#Repeat the last four lines if not equal to 1
while True:
    wAssign = getWeightOfAssignments()
    wMidTerm = getWeightOfMidTerms()
    wFinal = getWeightOfFinal()
    if checkWeights(wAssign, wMidTerm, wFinal) == 1:
        break
    else:
        print('try again')
#Get the average grade obtained on the assignments
#Validate the input as a float between 0 and 100

while True:
    try:
        AvgAssignments = float(input("please enter your average assignments grade: "))
        if 0 <= AvgAssignments <= 100:
            break
        else:
            print("Enter a float between 0 and 100")
    except ValueError:
        print("Invalid")

#Get the number of tests (call the appropriate function)
#Prompt the user for each test grades and accumulate the value
#Validate the input as a float between 0 and 100
#Calculate the average test grade.

n = getNumberOfTests()
testGrade = []
i = 0
while i in range(n):
    if i < n:
        try:
            test = float(input('please enter your mark on the test: '))
            if 0 <= test <= 100:
                testGrade.append(test)
                i += 1
            else:
                print('Please enter a number between 0 and 100')
        except ValueError:
            print("Invalid")

total = sum(testGrade)
AvgTests = total/len(testGrade)


#Prompt and get the final grade
#Validate the input as a float between 0 and 100

while True:
    try:
        final = float(input("please enter your final grade: "))
        if 0 <= final <= 100:
            break
        else:
            print("Enter a float between 0 and 100")
    except ValueError:
        print("Invalid")

#Calculate and display the final numeric grade (call the appropriate function)
numericGrade = calculateNumericGrade(AvgAssignments,AvgTests,final,wAssign,wMidTerm,wFinal)

print(numericGrade)
#Calculate and display the final alphabetical grade (call the appropriate function)
print(calculateLetterGrade(numericGrade))
