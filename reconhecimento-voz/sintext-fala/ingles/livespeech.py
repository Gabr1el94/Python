from pocketsphinx import LiveSpeech

for phrase in LiveSpeech():
    print("Você dizer: "+ str(phrase))