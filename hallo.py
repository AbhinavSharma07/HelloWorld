def fibonacci(n):
    """Generate Fibonacci sequence up to n."""
    fib_sequence = [0, 1]
    while fib_sequence[-1] + fib_sequence[-2] <= n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

def main():
    """Main function."""
    n = 1000000  # Define the upper limit for Fibonacci sequence
    fib_sequence = fibonacci(n)
    print("Fibonacci sequence up to", n, ":", fib_sequence)

if __name__ == "__main__":
    main()
