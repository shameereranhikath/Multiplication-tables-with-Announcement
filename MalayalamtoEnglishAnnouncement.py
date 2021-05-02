# Google Translate text-to-speech API
from gtts import gTTS

# package for playing sounds
from playsound import playsound

tokenno = input("Enter the Token No:")
text = 'മലയാളം ടൈപ്പിംഗ് ' + tokenno

ob = gTTS(text, lang='ml')
ob.save('token.mp3')
