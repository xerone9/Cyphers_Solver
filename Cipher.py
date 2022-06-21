import re

def listToStringWithoutBrackets(value):
    return str(value).replace('[','').replace(']','').replace(',','').replace("'","").replace('  ','1').replace(' ','')


def listToStringWithoutBrackets1(value):
    return str(value).replace('1',' ')


def get(letter: str, delta: int):
    return chr((ord(letter) - 97 + delta) % 26 + 97)


print(" ")
word = input("Enter Sentence/Word: ").lower()
girl = ""
limit = 26
game = 0
list = []
input = []
breaking_word = word.split(" ")
for words in breaking_word:
    input.append(words)


while game < limit:
    game += 1
    for alpha in word:
        if alpha == "Z" or alpha == "z":
            girl += "a"
        elif alpha ==" ":
            girl += " "
        else:
            girl += chr(ord(alpha) + 1)

    word = girl

    wordList = re.sub("[^\w]", " ", word).split()
    if len(word) == 0:
        print("You have not entered any value")
        break
    else:
        large = wordList[0]
    for truth in wordList:
        if len(truth) > len(large):
            large = truth

    string1 = large

    file1 = open("words.txt", "r")

    flag = 0
    index = 0


    for line in file1:
        index += 1


        if string1 in line:
            flag = 1
            break


    if flag == 0:
        pass
    else:
        list.append(girl.lower())


    file1.close()


    girl = ""

matches = []

if len(input) > 1:
    for value in list:
        words = value.split(" ")
        match = 0
        for word in words:
            file1 = open("usman.txt", "r")
            for line in file1:
                if word == line.replace("\n" , ""):
                    match += 1
                    break
                else:
                    pass
        matches.append(match)
    file1.close()
    most_matches = max(range(len(matches)), key=matches.__getitem__)
    print(list[most_matches])
    word = ""

else:
    for word in list:
        print(word)
        word = ""



