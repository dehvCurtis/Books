from sys import argv

script, user_name = argv
prompt = '>'

print(f'Hi {user_name} I\'m the {script} script')
print(f'I would like to ask some questions')
print(f'Do you like me {user_name}?')
likes = input(prompt)

print(f'Where do you live {user_name}')
lives = input(prompt)

print(f'What kind of computer do you have?')
computer = input(prompt)

print(f"""
You said {likes} about liking me.
You live in {lives}.
And you have a {computer}. 
""")