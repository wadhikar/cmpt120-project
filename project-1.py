'''
    Group Members: Nimesh Shrestha, Krish Dutt, Wilson Adhikari
    Revision date: Nov 28, 2014
'''
import random

def readFile(fileName):

    '''
    #returns a list with each line of the file in a seperate string
    
    #filename: name of the file to open with the extention attached to it
    '''
    
    #open file in read mode
    openedFile = open(fileName, "rU")

    #extract lines and place into list
    lines = []
    currentLine = openedFile.readline()
    
    while(currentLine != ""):

        #each line ends in '\n' so ignore the last character
        #important note, the last line in the text file might not end in a newline if you
        #don't add a newline in the text file, so it will cut off the last digit instead of cutting off the trailing \n.
        #Make sure the text document has an extra blank line at the end
        lines += [currentLine[: len(currentLine) - 1]]
        currentLine = openedFile.readline()
        
    openedFile.close()
    
    return lines

def selectRandomFormula(formulaList):

    '''
    returns a random formula selected from the given list of formulas

    formulaList: a list of formulas
    '''
    
    index = random.randint(0, len(formulaList) - 1)

    return formulaList[index]

def generateRandomFormula():

    '''
    returns a random formula generated from a text document
    '''
    
    formulas = readFile("fmlas.txt")
    return selectRandomFormula(formulas)

#return a string containing the expanded formula
def expandFormula(condensed):

    '''
    returns given condensed formula after expanding it

    condensed: the condensed formula as a string
    '''
    #extract the symbols before hand
    symbols = [condensed[0], condensed[1]]

    expanded = ""

    for i in range(2, len(condensed)):

            #even positioned digits are followed by the first symbol
            #odd positioned digits are followed by the second symbol
            expanded += condensed[i] + condensed[i % 2]

    #expanded formula has an unnessecary symbol after the last digit
    #get rid of it before sending
    return expanded[:len(expanded) - 1]

def solveMultiplication(formula):

    '''
    solve all the multiplication statements in the given formula
    returns a list where all of the multiplication statements are replaced with the product

    formula: the expanded formula in list format
    '''
    
    index = 0
    
    while(index < len(formula)):

        #found a multiplication statement
        #replace the numbers being multiplied and the multiplication symbol with product
        if(formula[index] == "*"):

            product = int(formula[index - 1]) * int(formula[index + 1])
            formula[index - 1] = str(product)

            formula.pop(index)
            formula.pop(index)

        else:

            index += 1

    return formula

    
#solve the expanded formula
def solveExpanded(expanded):

    '''
    returns the solution to the given expanded formula

    expanded: the expanded formula as a string
    '''

    expanded = list(expanded)
    
    #first solve all multiplication statements because multiplication comes before addition
    formula = solveMultiplication(expanded)

    #multiplication is completed, only thing left is to sum the digits
    sum = 0

    for digit in formula:

        #add all the characters that aren't addition symbols
        if digit.isdigit():
            
            sum += int(digit)

    return sum

def solveCompressed(compressed):

    '''
    returns the solution to the given compressed formula

    compressed: the compressed formula as a string
    '''
    
    return solveExpanded(expandFormula(compressed))

def indicateWrongGuess(totalGuesses, remainingGuesses):
    
    '''
    tells the user he guessed wrong, and shows a visual representation of the number of guesses used and has remaining

    totalGuesses: the initial total number of guesses the user had as an integer
    remainingGuesses: the number of guesses the user has remaining as an integer
    '''
    
    guessesUsed = totalGuesses - remainingGuesses
    print "Wrong Guess.    " + remainingGuesses * "*" + guessesUsed * "~"

def handleCorrectGuess(incompleteFormula, completeFormula, guessedChar):

    '''
    Handles the case when the user correctly guesses a single character in the formula
    Fills in the dashes in the locations where the guessedChar should appear in the formula the user is trying to guess

    returns the formula that the user has guessed so far with the guessedChar filled in at the correct spots as a string

    incompleteFormula: the formula that the player has guessed so far, as a string
    completeForula: the formula that the player is trying ot guess, as a string
    guessedChar: the character the player just guessed, as a string
    '''

    #figure out all positions in completeFormula where the character occurs
    occurances = []

    for i in range(len(completeFormula)):

            if completeFormula[i] == guessedChar:

                    occurances.append(i)
		
    #turn the partial formula into a list to easily change characters
    incompleteFormula = list(incompleteFormula)

    #replace characters in the partial_fmla with symbol
    for index in occurances:

            incompleteFormula[index] = guessedChar

    #turn back to a string
    return ''.join(incompleteFormula)

def receiveValidGuess():

    '''
    make player enter a guess for the formula, and ensures the player only types in single digits, or + or *
    
    returns the player's guess as a string
    '''

    allowedInput = "0123456789+*"

    playerInput = raw_input("Please guess a single digit or allowed symbol: ")

    #make player input a single valid character
    while(playerInput not in allowedInput or len(playerInput) != 1):

        playerInput = raw_input("That is an invalid guess, please guess another single digit or allowed symbol: ")

    return playerInput

def receiveIntegerInput(initialInputMessage):

    '''
    get the player to input a number and uses the given string as a input prompt
    the built in input() function crashes if the user doesn't input an integer so use this function to prevent crashing
    
    returns the players integer input

    initialInputMessage: the message displayed to the player when he is first asked to input the number; a string
    '''
    
    #use input as a string so program doesn't crash if player inputs symbols
    playerInput = raw_input(initialInputMessage + ": ")

    while(not playerInput.isdigit()):

        playerInput = raw_input("That is not a valid input, please enter a valid number: ")

    return int(playerInput)

def askToPlayGame(playMessage):

    '''
    asks the user, using the given message, if he wants to play the game
    makes the user type in either y for yes he wants to play, or n for no he doesn't

    returns True if he wants to play, False otherewise

    playMessage: the message that's displayed to the player when asked to play the game
    '''

    #ask player to play again and make sure player either answers y, or n
    playerInput = raw_input(playMessage + ": ")

    while(playerInput.lower() != 'y' and playerInput.lower() != 'n'):

        print playerInput
        playerInput = raw_input("Please enter 'Y' for yes and 'N' for no:")

    return True if playerInput.lower() == 'y' else False

def printSavedGuesses(savedGuesses):

    '''
    prints all of the user's saved guesses
    '''

    for guess in savedGuesses:

        print "You guessed", guess

def binaryToDecimal(binaryNumberList):

    '''
    converts the given binary number in list format to decimal

    returns the given binary number as decimal integer

    binaryNumberList: a list where each element is a digit in a binary number
    '''
    
    decimal = 0

    #reverse the given list of binary numbers so the position in the list is equal to the power you need to raise 2 by
    reversedList = binaryNumberList[::-1]

    for index in range(len(reversedList)):

            decimal += reversedList[index] * 2 ** index

    return decimal

def sumList(stringList):

    '''
    sums up all of the integer like items in the given list, if an element is an integer, or a string representation of an integer it will be added to the sum, otherwise it's ignored

    returns the sum of all of integer like objects in the list

    stringList: a list of any elements
    '''

    sum = 0

    for item in stringList:

        if type(item) == int or (type(item) == str and item.isdigit()):
     
            sum += int(item)

    return sum

def calculateFirstLuckyNum(compressedFormula):

    '''
    calculates the first lucky number by creating a binary number based on each digit in the compressedFormula and converting the binary to decimal

    returns an integer containing the first lucky number calculated as specified by the requirements

    compressedFormula: the compressedFormula as a string
    '''

    #get rid of symbols
    compressedFormula = compressedFormula[2: len(compressedFormula)]

    binaryNumberList = []

    for char in compressedFormula:

        binaryNumberList.append(int(char) % 2)

    print "\nBased on the binary list:", binaryNumberList
    print "Your first lucky number is:", binaryToDecimal(binaryNumberList)

def calculateSecondLuckyNum(compressedFormula):

    '''
    creates a list where an element at the Ith position is the sum of all of the digits from the Ith position in the compressedFormula (after removign the symbols) to the end of the formula

    returns the sum of each element in the list of sums

    compressedFormula: the compressed formula as a string
    '''

    #get rid of symbols
    compressedFormula = compressedFormula[2: len(compressedFormula)]

    listOfSums = []

    for index in range(len(compressedFormula)):

        sumToEnd = sumList(list(compressedFormula[index: len(compressedFormula)]))
        listOfSums.append(sumToEnd)

    print "\nBased on the list with digits:", list(compressedFormula)
    print "and the list with the added values:", listOfSums
    print "Your second lucky number is:", sumList(listOfSums)

def playFirstSection(gameNumber, formulaToGuess, playerStats, currentPoints):

    '''
    plays the first section of the game where the user needs to guess each character in the formula

    returns whether the user guessed the entire formula or not

    gameNumber: the number of this game in order to tell the player how many games he has played, an integer
    formulaToGuess: the formula the player is trying to guess as a string
    playerStats: list of the player's statistics for this game
    currentPoints: how many points the player currently has as an integer
    '''

    print "\nPlaying game #:",  gameNumber
    print "----------------"
    print "Your points so far are:", currentPoints

    #maximum number of wrong guesses the player is allowed to have
    maxWrongGuesses = receiveIntegerInput("Maximum number of wrong-guesses you want to have allowed?")

    if maxWrongGuesses < 1:

        print "You can't have less than 1 attempt so you will start off with 1 allowable wrong-guess."
        maxWrongGuesses = 1

    print "\nThe formula you will have to guess has", len(formulaToGuess), "symbols:", "-" * len(formulaToGuess)
    print "You can use digits 0 to 9 and symbols + * \n"

    solved = runGuessLoop(maxWrongGuesses, formulaToGuess, playerStats)
        
    if solved:

        print "You guessed the entire formula."
        
    else:

        print "You guessed incorrectly", maxWrongGuesses, "time(s)."
        print "You cannot continue guessing, better luck next time."

    return solved

def playSecondSection(playerStats, points, formulaToSolve):

    '''
    plays the second section of the game
    user is asked to solve the formula

    returns the number of points he has

    playerStats: list of player's stats for last game he played
    points: the number of points the player currently has
    formulaToSolve: the compressed unsolved formula as a string
    '''
    
    #get the users formula solution and if he was correct, tell him so
    print "\nNow you have to calculate the result of the formula"
    playerSolution = receiveIntegerInput("Please enter the solution to the formula (integer)")

    actualSolution = solveCompressed(formulaToSolve)
        
    if(playerSolution != actualSolution):

        print "\nYou have guessed the whole formula but not the result."
        print "You lose 2 points."

        points -= 2
        playerStats[solvedFormula] = False
                
    else:

        print "\nYou have guessed the whole formula and the result!"
        print "you have earned 10 points\n"

        points += 10
        playerStats[solvedFormula] = True

    return points

def runGuessLoop(maxWrongGuesses, formulaToGuess, playerStats):

    '''
    runs the loop where the player is asked to input a guess, and his guess is checked
    runs until the player is out of guesses or until he guesses the entire formula

    returns True if he guessed the formula, false otherwise

    maxWrongGuesses: max number of times player is allowed to guess wrong as an integer
    formulaToGuess: the formula the player is trying to guess as a string
    playerStats: list of the player's stats
    '''

    #create a list of dashes that represent the user's solved formula
    #that way if the user guesses a character a dash can be replaced with the guessed character
    guessedFormula = "-" * len(formulaToGuess)

    remainingGuesses = maxWrongGuesses

    solved = False
    
    #get the player to guess the formula
    while(remainingGuesses > 0 and not solved):

        guessedChar = receiveValidGuess()
        
        playerStats[savedGuesses].append(guessedChar)

        if guessedFormula.count(guessedChar) != 0:

            #user guesses a number that is correct but he guessed it previously
            print "You have already found this character before."
            print "This does not count as an incorrect guess.\n"

            #this guessed isn't taken into account so remove from the list of characters the user has guessed
            playerStats[savedGuesses].pop(-1)

        elif formulaToGuess.count(guessedChar) == 0:

            #user guesses wrong
            remainingGuesses -= 1
            indicateWrongGuess(maxWrongGuesses, remainingGuesses)

        else:

            #user guesses correctly
            guessedFormula = handleCorrectGuess(guessedFormula, formulaToGuess, guessedChar)
            
            print "Yes! correct guess!"

            solved = (guessedFormula == formulaToGuess)

        print "\nThe formula you have guessed so far is:", guessedFormula, "\n"

    return solved

def gameLoop(points, playerStats):

    '''
    runs the loop where the player actually plays the game
    loops until player has less than 2 points or he chooses to not play anymore
    runs the first and second section of the game

    returns the number of points the player currently has, and the number of games he has played as a 2-tuple

    points: number of points the player chose to start off with
    playerStats: list of the player's stats for the last game he played
    '''

    #keep track of the number of games played to inform the user about how many games he has played
    gamesPlayed = 0
    playGame = askToPlayGame("Do you want to play? Y - yes, N - no")

    while(points >= 2 and playGame):

        #reset all player stats at beginning of each play session
        playerStats[savedGuesses] = []
        playerStats[guessedFormula] = False
        playerStats[solvedFormula] = False
        playerStats[formulaSolution] = 0
        playerStats[initialPoints] = points
        
        #generate a random formula to use, its also saved into the player stats for later use
        playerStats[unsolvedFormula] = generateRandomFormula()
        
        gamesPlayed += 1

        print "\n***(TRACE), the program selected the mystery formula:", playerStats[unsolvedFormula]
        print "***(TRACE), formula", playerStats[unsolvedFormula], "expands to:", expandFormula(playerStats[unsolvedFormula])
        print "***(TRACE), formula", playerStats[unsolvedFormula], "evaluates to:", solveCompressed(playerStats[unsolvedFormula]), "\n"
        
        clearedFirstSection = playFirstSection(gamesPlayed, playerStats[unsolvedFormula], playerStats, points)
        playerStats[guessedFormula] = clearedFirstSection

        if clearedFirstSection:

            print "For correctly guessing the formula you gain 2 points.\n"
            points += 2
            
            points = playSecondSection(playerStats, points, playerStats[unsolvedFormula])
            
        else:

            print "You lose 2 points."
            points -= 2
        
        if points < 2:

            print "Unfortunately you have run out of points so you are unable to play again."

        else:
            
            playGame = askToPlayGame("Do you want to play again? Y - yes, N - no")

    return points, gamesPlayed

def displayStats(playerStats, gamesPlayed, points):

    '''
    displays the player's statistics about the last game he has played

    playerStats: list of the statistics for the last game player played
    gamesPlayed: number of games player has played, as an integer
    points: current number of points the player has, as an integer
    '''

    print "\n\n*****ALL GAMES ARE OVER*****"
    print "Here is your final information:\n\n"

    print "After playing", gamesPlayed, "game(s), you have in total", points, "points.\n"
    
    print "The history of the last game played is...\n"

    print "Started with:", playerStats[initialPoints], "point(s)"
    print "the mystery formula was:", playerStats[unsolvedFormula]
    
    printSavedGuesses(playerStats[savedGuesses])

    if(playerStats[guessedFormula]):

        print "You guessed the whole formula."

        if(playerStats[solvedFormula]):

            print "You correctly solved the formula,",

        else:

            print "You failed to solve the formula,",

        print "the answer was:", solveCompressed(playerStats[unsolvedFormula])

    else:

        print "You did not guess the correct formula."

    print "you now have:", points, "points"

    calculateFirstLuckyNum(playerStats[unsolvedFormula])
    calculateSecondLuckyNum(playerStats[unsolvedFormula])

#keep track of the player's statistics from the last game he played, save all data in a list and access them with the appropriate index
#order = [savedGuesses, whether player guessed the formula, whether player solved formula, solution to formula, initial poitns for the round, the unsolved formula]
lastGameStatistics = [ [], False, False, 0, 0, ""]

#indices to access statistic in the list of statisitcs for the last game the player Played
savedGuesses = 0
guessedFormula = 1
solvedFormula = 2
formulaSolution = 3
initialPoints = 4
unsolvedFormula = 5

#start the game
print "Now starting the Math Training game."
print "====================================\n"

points = receiveIntegerInput("Enter the number of points -minimum 2- you would like to start the game with")

if points < 2:

    print "You have chosen less than 2 points so you will start off with 2 points.\n"
    points = 2

points, gamesPlayed = gameLoop(points, lastGameStatistics)

#if player played a game then display his stats for the last game
#don't display if he hasn't played a game
if gamesPlayed > 0:

    displayStats(lastGameStatistics, gamesPlayed, points)

print "\nGood bye."

