# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input().strip())

# Initialize dictionary
phone_book = {}

for i in range(n):
    entry_data = input().strip()
    # Use split method split input data into name and telephone
    entry = entry_data.split(" ")
    # Add name and telephone to dict
    phone_book[entry[0]] = entry[1]

# Continuously read queries until there is no more input
while True:
    try:
        query = input().strip()

        # Check if query is not empty
        if query:
            # Check if query name exists in dict
            if query in phone_book:
                print(query + "=", end="")
                print(phone_book[query])
            else:
                # Print "Not found" if the query name is not in dict
                print("Not found")

    # Exit loop if an exception occurs (no more input)
    except:
        break
