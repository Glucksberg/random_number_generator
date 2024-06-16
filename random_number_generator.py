import random
import sys

def generate_random_number(start, end):
    return random.randint(start, end)

def main():
    if len(sys.argv) != 3:
        print("Usage: random_number_generator.py <start> <end>")
        sys.exit(1)

    try:
        start = int(sys.argv[1])
        end = int(sys.argv[2])
    except ValueError:
        print("Both start and end values must be integers.")
        sys.exit(1)

    if start > end:
        print("Start value must be less than or equal to end value.")
        sys.exit(1)

    random_number = generate_random_number(start, end)
    print(f"Random number between {start} and {end}: {random_number}")

if __name__ == "__main__":
    main()
