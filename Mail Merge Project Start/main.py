PLACEHOLDER = "[name]"

with open("/eisha/python/Mail Merge Project Start/Input/Names/invited_names.txt") as name:
    invited_names = name.readlines()

with open("/eisha/python/Mail Merge Project Start/Input/Letters/starting_letter.txt") as letter:
    content = letter.read()
    for name in invited_names:
        stripped_name = name.strip()
        new_letter = content.replace(PLACEHOLDER, stripped_name)
        with open(f"/eisha/python/Mail Merge Project Start/Output/ReadyToSend/{stripped_name}.txt", mode='w') as l:
          l.write(new_letter)

# for i in range (0,8):
#
#     new_file = open(f"/eisha/python/Mail Merge Project Start/Output/ReadyToSend/{file_names[i]}.txt", mode='w')
#     new_file.replace("[name]", invited_name)
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp