phonebook = {}
phonebook["Allison"] = "(520)555-6789"
phonebook["Allison"] = "(444)555-8800"

print(phonebook["Allison"])


phonebook = {}
phonebook["Allison"] = "(520)555-6789"
phonebook["Steve"] = phonebook["Allison"]

phonebook["Jack"] = "(220)785-3979"
phonebook["Martin"] = "(570)474-5639"
phonebook["Alford"] = "(312)665-9079"
phonebook["Mary"] = "(560)145-5579"

print(phonebook["Allison"])
print(phonebook["Steve"])
print(phonebook)