# Example strings
string1 = "Some text"
string2 = "Some other text"

# Normalize (remove spaces, lowercase everything)
cleaned1 = string1.replace(" ", "").lower()
cleaned2 = string2.replace(" ", "").lower()

# Count letters in each string
counts1 = Counter(cleaned1)
counts2 = Counter(cleaned2)

# Merge counts across both strings
total_counts = counts1 + counts2

# TRUE letters
true_letters = ["t", "r", "u", "e"]
true_score = sum(total_counts.get(letter, 0) for letter in true_letters)

# LOVE letters
love_letters = ["l", "o", "v", "e"]
love_score = sum(total_counts.get(letter, 0) for letter in love_letters)

# Final calculation
final_score = (true_score * 10) + love_score

print(f"TRUE total = {true_score}")
print(f"LOVE total = {love_score}")
print(f"Final score = (TRUE * 10) + LOVE = {final_score}")