def get_city_data():
    cities = {}

    while True:
        city = input("Enter a city name (or 'done' to finish): ").strip()
        if city.lower() == "done":
            break

        # population validation 
        while True:
            pop = input(f"Enter the population of {city}: ")
            if pop.isdigit() and int(pop) > 0:
                cities[city] = int(pop)
                break
            else:
                print("Invalid population. Enter a positive whole number.")

    return cities



city_dict = get_city_data()

    # Search dictionary via comprehension for population over 2 million
big_cities = {city: pop for city, pop in city_dict.items() if pop > 2_000_000}

print("\nCities that have populations over 2 million:")
if big_cities:
    for city, pop in big_cities.items():
        print(f"{city}: {pop:,}")
else:
    print("None found.")



