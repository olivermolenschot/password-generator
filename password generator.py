import random
import string
import time
import os

# Please replace the following directory with the directory where you would like the passwords to be saved. Please remember
# that the directory name should have double backslashes and not single backslashes.

directory_of_interest = 'C:\\Users\\Documents'

def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_letters
    characters = string.ascii_letters + string.digits + string.punctuation

    result_str = ''.join(random.choice(characters) for i in range(length))
    print("Random password of length", length, "is:", result_str)
    return result_str
filename = ""
while len(filename) == 0:
    filename = input('name of file with password: ')
    filename += '.txt'
numberreceived = 0
while numberreceived < 12:
    numberreceived = int((input('Please state the number of characters that you desire as your passcode \n'
                                '(it should be at least 12 characters): ')))
output = get_random_string(numberreceived)
completeName = os.path.join(directory_of_interest,filename)
filecreated = open(completeName,'w')
filecreated.write(output)
filecreated.close()

print('File has been saved in respective folder')
print('This page will automatically close in ten minutes, starting now')
time.sleep(600)