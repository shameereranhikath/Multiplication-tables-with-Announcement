# package for the text to voice package
import pyttsx3
# initializing the  engine for the package
engine = pyttsx3.init()
# we want to take the input of Which Multiplication Table
number = input("Enter the Number")

dic = {
    '1': "ones",
    '2': "twos",
    '3': "threes",
    '4': "fours",
    '5': "fives",
    '6': "sixes",
    '7': "sevens",
    '8': "eights",
    '9': 'nines',
    '10': 'tens'
}
text = "";

for i in range(1, 11):
    multiplied_answer = i * int(number)
    text += str(i) + ' ' + dic[str(number)] + "  are " + str(multiplied_answer) + "\n"

engine.say(text)
engine.runAndWait()

