import json
data = json.load(open("data.json"))
from difflib import get_close_matches
def finder (word):
    word = word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys(), n = 3, cutoff = 0.8)) > 0:
        yn = input("Did you mean %s instead? Enter Y if yes, or N if No: " %get_close_matches(word, data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(word, data.keys())[0]]
        elif yn == "N":
            return "The word entered doesn´t exist, please make sure you wrote it okey"
        else:
            return "We didn´t understand your entry"
    else:
        return "The word entered doesn´t exist, please make sure you wrote it okey"
word = input("Enter a word you want to look for: ")
output = finder(word)
if type (output) == list:
    for item in output:
        print(item)
else:
    print(output)
