def solution(pattern, source):
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    numberOfMatches = 0
    currentStrIndex = 0

    stoppingIndex = len(source) - len(pattern) #the index the counter reaches before stopping.
    
    while (currentStrIndex < len(source)):
        currentLetter = source[currentStrIndex]
        currentlyMatches = True
        letterIndexChecked = 0
        numberIndexChecked = 0
        
        while (currentlyMatches and numberIndexChecked <= len(pattern)):
            #if the iteration index is equal to the length of the pattern, meaning
            #if the pattern is 3 and we reached index 3 on the counter, then shut the loop.
            if (numberIndexChecked == len(pattern)):
                numberOfMatches += 1
                break
            
            elif (pattern[numberIndexChecked] == '0' and source[currentStrIndex + letterIndexChecked] in vowels):
                numberIndexChecked += 1
                letterIndexChecked += 1
                currentlyMatches = True
            elif (pattern[numberIndexChecked] == '1' and source[currentStrIndex + letterIndexChecked] not in vowels):
                numberIndexChecked += 1
                letterIndexChecked += 1
                currentlyMatches = True
            else:
                currentlyMatches = False

        if (currentStrIndex == stoppingIndex):
            break
        
        currentStrIndex += 1
        
    return numberOfMatches

def main():
    pattern = '010'
    source = 'amazing'
    
    numberOfMatches = solution(pattern, source)

    print(numberOfMatches)


main()
