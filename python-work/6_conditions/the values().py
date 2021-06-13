#now we are using the statement values(), it is used to call out the values of the keys.
favorite_language = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

print("The folloowing languages have been mentioned:")
for languages in favorite_language.values():
    print(f"\t{languages.title()}")

"""Since in there is a repetition of languages in the dictionary we can use the statement SET
to avoid repetition during the output"""
print("\n")

print("No repetition in this output:")
for languages in set(favorite_language.values()):
    print(f"\t{languages.title()}")