import webbrowser

def open_youtube(query):
    search_url = f"https://www.youtube.com/results?search_query={query.replace(' ', '+')}"
    webbrowser.open(search_url)
    text_to_speech(f"Abrindo o YouTube para {query}")
