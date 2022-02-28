import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
from googletrans import Translator


def takeCommand():
    recog = sr.Recognizer()
    with sr.Microphone() as src:
        recog.pause_threshold = 1
        recog.energy_threshold = 1000
        print("Listening...")
        audio = recog.listen(src)

    in_lang = "hi-in"
    out_lang = "de"
    try:
        print("Recognizing...")
        query = recog.recognize_google(audio, language=in_lang)
        print(query)

        translator = Translator()

        # print(googletrans.LANGUAGES)
        language = translator.detect(query).lang
        translated = translator.translate(query, dest=out_lang).text
        print(translated)
        language = out_lang
        if out_lang == "hindi" or out_lang == "french":
            language = "en"
        myobj = gTTS(text=translated, lang=language, slow=False)
        myobj.save("spokenContent.mp3")
        playsound("spokenContent.mp3")

    except Exception as e:
        return e

    return query


while True:
    takeCommand()
