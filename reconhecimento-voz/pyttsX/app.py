import pyttsx

test = pyttsx.init()

#Speed
test.setProperty('rate', 50)

#Volume
test.setProperty('volume',0.10)

#Voice
gender = 'male'
voice = 'brazil'
if gender == 'female':
    voice += '+f4'
test.setProperty('voice', voice )

#Speak
test.say('Oi Gabriel, seja bem-vindo!')

test.runAndWait()
