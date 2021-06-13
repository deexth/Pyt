#Using a list in a dictionary
favorite_languages = {
    'jen' : ['python', 'ruby'],
    'sarah': ['c'],
    'edward' : ['javascript', 'react'],
    'phil': ['java']
}

for name, languages in favorite_languages.items():
    if len(languages) < 2: #This if statement is to check if the length of the list is less than 2
        for language in languages: #Since the value is still a list we have to use a for loop.
            print(f"\n{name.title()}'s favorite language is {language.title()}")
    else:
        print(f"\n{name.title()}'s favorite language is:")
        for language in languages:
            print(f"\t{language.title()}")

"""When using lists in dictionaries make sure to make all the values lists, even if its only one values
per key. Otherwise every character is considered a list of its own."""