def load_swimmers(filename):
    """
    Loads swimmer data into a dictionary.
    Key: swimmer's full name
    Value: list of years participated
    """
    swimmers = {}

    with open(filename, "r") as file:
        for line in file:
            parts = line.strip().split()

            # First name + last name
            name = parts[0] + " " + parts[1]

            # Remaining parts are years (convert to int)
            years = list(map(int, parts[2:]))

            swimmers[name] = years

    return swimmers


def main():
    # Keep asking until a valid file is entered
    while True:
        filename = input("Enter the filename: ").strip()

        try:
            swimmers = load_swimmers(filename)
            break  # exit loop if successful
        except FileNotFoundError:
            print("File not found. Please try again.\n")

    # Dictionary comprehension:
    # Only swimmers with more than 2 participations
    frequent_swimmers = {
        name: len(years)
        for name, years in swimmers.items()
        if len(years) > 2
    }

    # Print original data
    print("\nAll Swimmers:")
    for name, years in swimmers.items():
        print(f"{name}: {years}")

    # Print filtered data
    print("\nSwimmers with more than 2 Olympic participations:")
    for name, count in frequent_swimmers.items():
        print(f"{name}: {count} times")


if __name__ == "__main__":
    main()