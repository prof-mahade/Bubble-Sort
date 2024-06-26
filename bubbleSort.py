# BUBBLE SORT

# Initialize an empty list to store user inputs
li = []

# Get the number of inputs from the user
num = int(input("How many inputs will there be: "))
j = 0

# Collect user inputs
while j < num:
    user = int(input("Enter a number: "))
    li.append(user)
    j += 1

# Implement bubble sort to sort the list in ascending order
for _ in range(len(li) - 1):  # Outer loop for passes
    for i in range(len(li) - 1):  # Inner loop for comparisons
        if li[i] > li[i + 1]:
            # Swap if the current element is greater than the next element
            li[i], li[i + 1] = li[i + 1], li[i]

# Print the sorted list
print("Sorted list:", li)