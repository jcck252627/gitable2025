word_dict = {}   # empty dictionary data structure

with open("data\\quote.txt") as file:
    for line_num, line in enumerate(file, start=1):   # read file line by line using enumerate, start with line count 1
        words = line.split() # extract each word

        for word in words:  # save each word into dictionary
            if word in word_dict:
                word_dict[word].append(line_num)
            else:
                word_dict[word] = [line_num]

# output from dictionary
for word in word_dict:  # print each word per line
    print(word, end=" ")
    for num in word_dict[word]: # print line number where this word appeared 
        print(num, end=" ")
    print()