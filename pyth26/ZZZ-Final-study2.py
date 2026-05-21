class Movie:
    def __init__(self, name):
        # Constructor: sets the movie name, initializes review dictionary, and review count
        self._name = name
        self.reviews = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
        self.num_reviews = 0

    # ----- Property Getter -----
    @property
    def name(self):
        return self._name

    # ----- Property Setter -----
    @name.setter
    def name(self, new_name):
        self._name = new_name

    # ----- Add Review Method -----
    def add_review(self, stars):
        # Only allow values 1–5
        if stars in self.reviews:
            self.reviews[stars] += 1
            self.num_reviews += 1
        else:
            print("Invalid rating. Must be 1–5 stars.")

    # ----- Average Rating Method -----
    def get_average(self):
        if self.num_reviews == 0:
            return 0
        
        total = 0
        for stars, count in self.reviews.items():
            total += stars * count
        
        return total / self.num_reviews

    # ----- String Representation -----
    def __str__(self):
        output = f"{self._name}\n"
        for stars, count in self.reviews.items():
            if stars == 1:
                output += f"{stars} Star: {count}\n"
            else:
                output += f"{stars} Stars: {count}\n"
        return output


# ============================================================
# MAIN PROGRAM (Hard‑coded test data)
# ============================================================

def main():
    # Create two Movie objects
    movie1 = Movie("The Great Adventure")
    movie2 = Movie("Space Journey")

    # Add reviews (hard-coded)
    movie1.add_review(5)
    movie1.add_review(4)
    movie1.add_review(5)
    movie1.add_review(3)

    movie2.add_review(2)
    movie2.add_review(3)
    movie2.add_review(4)
    movie2.add_review(4)
    movie2.add_review(5)

    # Print movie details and averages
    print(movie1)
    print("Average Rating:", round(movie1.get_average(), 2))
    print()

    print(movie2)
    print("Average Rating:", round(movie2.get_average(), 2))


# Run the program
main()
