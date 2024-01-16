def simple_interest(principal, rate, time):
    return round(principal * rate * time / 100, 2)


def compound_interest(principal, rate, time, compounding_frequency=1):
    # Calculate compound interest with specified compounding frequency
    compounded_rate = rate / (100 * compounding_frequency)
    total_compounds = compounding_frequency * time

    return round(principal * (1 + compounded_rate) ** total_compounds - principal, 2)


def main():
    print("Welcome to the Interest Calculator!")

    print("Select interest type:")
    print("1. Simple Interest")
    print("2. Compound Interest")

    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        principal = float(input("Enter the principal amount: "))
        rate = float(input("Enter the rate of interest per annum: "))
        time = float(input("Enter the time in years: "))
        result = simple_interest(principal, rate, time)
        print("Simple Interest: {:.2f}".format(result))
        print("Updated Principal: {:.2f}".format(principal + result))

    elif choice == "2":
        principal = float(input("Enter the principal amount: "))
        rate = float(input("Enter the rate of interest per annum: "))
        time = float(input("Enter the time in years: "))
        compounding_frequency = int(
            input("Enter compounding frequency (default is 1): ") or 1
        )
        result = compound_interest(principal, rate, time, compounding_frequency)
        print("Compound Interest: {:.2f}".format(result))
        print("Updated Principal: {:.2f}".format(principal + result))

    else:
        print("Invalid choice. Please enter 1 or 2.")


if __name__ == "__main__":
    main()
