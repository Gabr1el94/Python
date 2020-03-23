import pyttsx

test = pyttsx.init()
gender = 'male'
#Voice
voice = 'brazil'

if gender == 'female':
    voice += '+f4'
test.setProperty('voice', voice )
#Speak
test.say('Oi Gabriel, seja bem-vindo!')

test.runAndWait()
