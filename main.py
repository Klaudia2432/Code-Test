# Read the list of 10 digits in range 1-100
digits = [1, 2, 2, 4, 5, 6, 7, 8, 9, 9]
# Delete duplications from the list
newDigits = []
for n in digits:
    if n not in newDigits:
        newDigits.append(n)

# Sort list in descending order
newDigits.sort(reverse=True)

# Display output by calling function