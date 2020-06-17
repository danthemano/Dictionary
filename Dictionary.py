import json
#is used to get similar matches for a word
from difflib import get_close_matches

#imports the json file into a dictionary
data = json.load(open("data.json", "r"))

#returns the definition of a requested word
def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]

    #gets a close match to the misspelled word
    elif len(get_close_matches(word, data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(word, data.keys())[0]).upper()
        if yn == "Y":
            return data[get_close_matches(word, data.keys())[0]]
        elif yn == "N":
            return "The word doesn't exist. Please double check it."
    else:
        return "Incorrect word entered."

word = input("Enter a word: ")
output = translate(word)

#if there are multiple definitions, display all of them individually
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)