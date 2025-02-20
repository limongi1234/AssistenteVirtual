import wikipedia

def search_wikipedia(query):
    try:
        result = wikipedia.summary(query, sentences=1)
        print(f"Resultado do Wikipedia: {result}")
        text_to_speech(result)
    except wikipedia.exceptions.DisambiguationError as e:
        print(f"Ambiguidade encontrada: {e.options}")
        text_to_speech("Desculpe, houve um erro ao tentar buscar no Wikipedia.")
