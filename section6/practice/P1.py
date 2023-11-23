# TASK: Print the second word of the string with all letters in UPPERCASE.
# MAKE SURE TO READ THE FULL INSTRUCTIONS ABOVE CAREFULLY, AS THE EVALUATION SCRIPT IS VERY STRICT.
# Link to Solution: Solution: https://gist.github.com/b4shy/575282ef3c7abf9714167bcc44498627

'''input_string = "I love programming with python!"

upperstring = input_string[2 : 3].upper()

print (input_string[0:2] + upperstring + input_string[3:])'''

input_string = "I love programming with python!"
rst = input_string.split()
print (rst[1].upper())