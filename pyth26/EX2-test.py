def load_data(filename):
    """
    Loads NBA champions into a dictionary.
    Key: team name
    Value: list of years that team won
    """
    champions = {}

    try:
        with open(filename, "r") as file:
            for year, team in enumerate(file, 1947):
                team = team.strip()

                if team not in champions:
                    champions[team] = []

                champions[team].append(year)

    except FileNotFoundError:
        print("Error: File not found.")
    
    return champions


def find_wins(champions, team_name):
    """
    Prints the years the given team won the championship.
    """
    if team_name in champions:
        years = champions[team_name]
        print(f"{team_name} won the championship in:")
        print(", ".join(map(str, years)))
    else:
        print("Team not found.")


def main():
    filename = "data/NBAChampions.txt"
    
    champions = load_data(filename)

    while True:
        team_name = input("Enter a team name (or 'q' to quit): ").strip()

        if team_name.lower() == 'q':
            print("Goodbye!")
            break

        find_wins(champions, team_name)


if __name__ == "__main__":
    main()