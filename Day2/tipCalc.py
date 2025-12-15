# =================================
# Day 2 - 100 Days of Code: Python
# =================================


print("Welcome to the tip calculator!")


def main():
    total_bill = float(input("What was the total bill? ").lstrip("$"))

    tip = percent_convert(
        int(input("Are we tipping 10, 12, or 15 percent? ").rstrip("%"))
    )

    split = int(input("How many people will be splitting the bill? "))
    total_bill = total_bill + (total_bill * tip)
    split_bill = total_bill / split
    print(f"Each person should pay: ${split_bill:.2f}")


def percent_convert(tip):
    return float(tip / 100)


main()


# We did this from memory. Keep it up! Good practice.
