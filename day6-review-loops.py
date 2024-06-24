# Enter your code here. Read input from STDIN. Print output to STDOUT

# Number of test cases:
test_cases = int(input())

# Loop through number of test cases:
for test_case in range(test_cases):

    # Input string
    s = input().strip()

    even = []
    odd = []

    # For char/index in string
    for index in range(len(s)):
        # If index is even
        if index % 2 == 0:
            even.append(s[index])
        # If index is odd
        else:
            odd.append(s[index])

    # Use join() method to transform array into string
    print("".join(even) + " " + "".join(odd))
