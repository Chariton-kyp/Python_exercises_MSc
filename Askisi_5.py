from collections import Counter

with open("two_cities_ascii.txt", "r") as f:
    contents = f.read()

contents = contents.lower()

# γίνεται ο διαχωρισμός με βάση τους ASCII χαρακτήρες
for i in range(128):
    if i==32 or 97<=i<=122:
        continue
    else:
        contents = contents.replace(chr(i),"")

list_without_spaces = contents.split(" ")

counter = len(list_without_spaces)

# Για μεγαλύτερη ταχύτητα εκτέλεσης έγινε εισαγωγή του Counter από το collections. Ο άλλος τρόπος για να υλοποιηθεί 
# θα ήταν με την αφαίρεση των duplicates είτε με χρήση sets είτε με comprehession

# μετατροπή σε dictionary για να μπορεί να γίνει sort με βάση το πλήθος. Η Counter επιστρέφει object
words_with_counter = dict(Counter(list_without_spaces))

list_sorted_words = sorted([(value,key) for (key,value) in words_with_counter.items()], reverse=True)

# α) ποιες είναι οι δέκα δημοφιλέστερες λέξεις;
print("\nA) Here, are printed, the 10 most appeared words in the whole document, after removing special characters!\n")
for i in range(0,10):
    print(f'{i+1}. "{list_sorted_words[i][1]}" appears {list_sorted_words[i][0]} times from totally {counter} times!')


# β) Ποιοι είναι οι τρεις πρώτοι συνδυασμοί δύο πρώτων γραμμάτων που αρχίζουν οι περισσότερες λέξεις;
letters_2 = []
for i in list_without_spaces:
    letters_2.append(i[:2])

letters_2_with_counter = dict(Counter(letters_2)) 

letters_2_with_counter_sorted = sorted([(value,key) for (key,value) in letters_2_with_counter.items()], reverse=True)

print("\nB) Here, are printed, the first two characters of all the words that appear the most times in the whole document!\n")
for i in range(3):
    print(f'{i+1}. 2 first letters "{letters_2_with_counter_sorted[i][1]}" appear {letters_2_with_counter_sorted[i][0]} times from totally {len(letters_2)} times!')
   

# γ) Ποιοι είναι οι τρεις πρώτοι συνδυασμοί τριών πρώτων γραμμάτων που αρχίζουν οι περισσότερες λέξεις;
letters_3 = []
for i in list_without_spaces:
    letters_3.append(i[:3])

letters_3_with_counter = dict(Counter(letters_3)) 

letters_3_with_counter_sorted = sorted([(value,key) for (key,value) in letters_3_with_counter.items()], reverse=True)

print("\nC) Here, are printed, the first three characters of all the words that appear the most times in the whole document!\n")
for i in range(3):
    print(f'{i+1}. 3 first letters "{letters_3_with_counter_sorted[i][1]}" appear {letters_3_with_counter_sorted[i][0]} times from totally {len(letters_3)} times!')

