# Made by Alex

# Fibonacci Sequence Generator
def fibGen(value):
    for i in range(value):
        yield fib(i)

# Get Fibonacci number at value
def fib(value):
    # Base case
    if value == 0:
        return 0
    elif value == 1:
        return 1
    
    # General case
    a = fib(value - 1)
    b = fib(value - 2)

    return a + b

# Main Function
def main():
    # Error handling
    try:
        userInput = -1

        while userInput < 0:
            userInput = int(input("Please enter a whole number: "))
    # Error
    except:
        print("Bad input.")
        return # Exits function
    
    # Calculations
    fibSeq = fibGen(userInput)

    # Using a generator to display the Fibonacci Sequence
    for fibNum in fibSeq:
        print(fibNum)
        
    return # Exits function

# Execution Check
if __name__ == '__main__':
    # Main loop
    while True:
        main()
        userInput = input("Press q to quit: ") # Prompt
        if userInput.lower() == 'q':
            break # Ends loop
        print() # Formatting
    quit() # Exits program