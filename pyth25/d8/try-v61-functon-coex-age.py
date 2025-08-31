def life_in_weeks(age):
    year_left = 90 - age
    weeks = year_left * 52
    print("You have " + str(weeks) + " weeks to live........")


age = input("Enter your current age:  ")

life_in_weeks(int(age))



def life_in_weeks(age):
    year_left = 90 - age
    weeks = year_left * 52
    print("You have " + str(weeks) + " weeks left.")


age = 53

life_in_weeks(int(age))
