import re


emails = [
    'n.john.smith@gmail.com',
    '87victory@hotmail.com',
    '!#mary-=@msca.net'
]

# Write a regex to match a valid email address
regex = r"[a-zA-Z0-9!#%&*$.]+@[a-z]+\.com"

for example in emails:
    # Match the regex to the string
    if re.match(regex, example):
        # Complete the format method to print out the result
        print("The email {email_example} is a valid email"
              .format(email_example=example))
    else:
        print("The email {email_example} is invalid"
              .format(email_example=example))
