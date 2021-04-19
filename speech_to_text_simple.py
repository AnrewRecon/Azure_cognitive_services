import azure.cognitiveservices.speech as speechsdk

def from_mic():
    speech_key, service_region = "3c236e183b574f138845948fd63ea658", "brazilsouth"

    speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)
    speech_config.speech_recognition_language="es-ES"

    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)
    
    print("Speak into your microphone.")
    result = speech_recognizer.recognize_once_async().get()
    print(result.text)

from_mic()

# phrase_list_grammar = speechsdk.PhraseListGrammar.from_recognizer(reco)
# phrase_list_grammar.addPhrase("Supercalifragilisticexpialidocious")