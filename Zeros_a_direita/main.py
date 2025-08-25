def zeros(n):
    count = 0
    while n > 0:
        n //= 5
        count += n
    return count


def main():
    print("Factorial Trailing Zeros Counter")
    print("Enter positive numbers (0 to exit).")
    while True:
        try:
            number = int(input("\nEnter a number: "))
            if number == 0:
                print("Stopping...")
                break
            if number < 0:
                print("Please enter a positive number!")
                continue

            response = zeros(number)
            print(f"{number}! has {response} trailing zeros")

        except ValueError:
            print("Enter a valid number!")

if __name__ == "__main__":
    main()