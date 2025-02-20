import pyttsx3

def text_to_speech(text):
    engine = pyttsx3.init()  # Inicializa o engine do pyttsx3
    engine.say(text)  # Diz o texto
    engine.runAndWait()  # Aguarda o término da fala

# Exemplo de uso
text_to_speech("Olá! Eu sou o seu assistente virtual.")
