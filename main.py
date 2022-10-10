def removeDuplicatesAndSortDesc(listOfDigits: list) -> list:
    # Delete duplications from the list
    newList = removeDuplicates(listOfDigits)
    # Sort list in descending order
    newList.sort(reverse=True)
    return newList

def removeDuplicates(listOfDigits: list) -> list:
    newList = []
    for n in listOfDigits:
        if n not in newList:
            newList.append(n)
    return newList

# CODE EXAMPLE


# Read the list of 10 digits in range 1-100
digits = [1, 2, 2, 4, 5, 6, 7, 8, 9, 9]
print(removeDuplicatesAndSortDesc(digits))
