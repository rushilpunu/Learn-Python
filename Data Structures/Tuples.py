language = ("French", "German", "English", "Polish")
print(language)

print(language[1])  # Output: German
print(language[3])  # Output: Polish
print(language[-1])  # Output: Polish

language = ("French", "German", "English", "Polish")
del language

# NameError: name 'language' is not defined
print(language)
