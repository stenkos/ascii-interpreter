#******************************************************************************#
# Title:           ascii-interpreter                                           #
# Author:          stenkos                                                     #
# Git repository:  https://github.com/stenkos/ascii-interpreter.git            #
# Date:            2023-01-31                                                  #
# Version:         v1                                                          #
# Purpose:         Input ASCII, return string or char                          #
#******************************************************************************#

# This is a list of all OG ASCII characters
# The 32 None entries replace control characters that I cba working around
asciiConv = [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, ' ', '!', '"', '#', '$', '%', '&', '\'', '(', ')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', ';', '<', '=', '>', '?', '@', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '[', '\\', ']', '^', '_', '`', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~']

print("""This is stenkos's ASCII interpreter. To input characters, insert an ASCII
binary code and press ENTER. Please note that in this program control characters
are not included and will return "None".""")


# Input a binary code, return a character
def charMode():
    print()
    while True:
        try:
            character = int(input(), 2) # convert bin input to dec
        except ValueError:
            break # return to main menu
        print(asciiConv[character])


# Input binary codes, slowly build a string
def strMode():
    print()
    string = "" # initial state of string
    while True:
        try:
            character = int(input(), 2)
        except ValueError:
            break
        string = string + asciiConv[character] # build string
        print(string)


print("""
charMode is a simple mode, where you can test your knowledge of ASCII codes by
inputting codes to return single characters. strMode is fundamentally the same,
except you can construct fully-fledged strings.""")



# main looping program
while True:
    prompt = input("""
Would you like to use charMode or strMode? Please note that only binary input is
accepted and inputting strings will bring you back to this menu.

To exit type 'exit' at this prompt.
""")
    prompt = prompt.lower()
    if prompt == "strmode":
        strMode() # defined earlier
    elif prompt == "charmode":
        charMode() # defined earlier
    elif prompt == "exit":
        break
    else:
        continue
