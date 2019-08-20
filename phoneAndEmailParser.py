import re
import pyperclip

# Phone Number and Email Address Extractor

# Define template for phone number and email address separately

phoneNumberRegex = re.compile(r'''(
(\d{3}|\(\d\))?                      # area code as 400 or (400). Is optional.
(\s|-|\.)?                           # Separator. As \s character, -, . . Is optional.
(\d{3})                              # first 3 digits
(\s|-|\.)                            # Separator. As \s character, -, . .
(\d{4})                              # last 4 digits
(\s*(ext|x|ext.)\s*(\d{2,5}))?       # Extension
)''', re.VERBOSE)

emailAddressRegex = re.compile(r'''(
[a-zA-Z0-9._%+-]+
@
[a-zA-Z0-9._-]+
\.[a-zA-Z]{2,4}
)''', re.VERBOSE)


# Take input from clipboard

text = pyperclip.paste()

# Find matches in clipboard text

phoneMatchesRaw = phoneNumberRegex.findall(text)
emailMatchesRaw = emailAddressRegex.findall(text)

phoneMatches = []
emailMatches = []

# Nicely format everything before pasting into clipboard

for groups in phoneMatchesRaw:
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    phoneMatches.append(phoneNum)

for groups in emailMatchesRaw:
    emailMatches.append(groups)

# Copy the str into clipboard

pyperclip.copy(str('\n'.join(phoneMatches + emailMatches)))  # Concatenate the two lists instead of join([[],[]]), because that'd treat it as a list only.

# Show what all was copied

print("The following data was copied: \n")
print(pyperclip.paste())


