import speech_recognition as sr

def speech_to_text():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        print("Ajustando o microfone...")
        recognizer.adjust_for_ambient_noise(source)
        print("Pode falar agora!")
        audio = recognizer.listen(source)
    
    try:
        text = recognizer.recognize_google(audio, language="pt-BR")
        print(f"Você disse: {text}")
        return text
    except sr.UnknownValueError:
        print("Não consegui entender o que você disse.")
        return ""
    except sr.RequestError:
        print("Erro ao tentar se conectar ao serviço de reconhecimento.")
        return ""
