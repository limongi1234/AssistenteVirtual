def assistente_virtual():
    while True:
        print("Diga um comando.")
        command = speech_to_text().lower()  # Captura e converte o comando para minúsculas
        
        if "wikipedia" in command:
            query = command.replace("pesquisar no wikipedia", "").strip()
            search_wikipedia(query)
        
        elif "youtube" in command:
            query = command.replace("abrir youtube", "").strip()
            open_youtube(query)
        
        elif "farmácia" in command:
            find_nearest_pharmacy()
        
        elif "sair" in command:
            print("Saindo do assistente.")
            text_to_speech("Saindo do assistente. Até logo!")
            break
        
        else:
            print("Comando não reconhecido.")
            text_to_speech("Desculpe, não entendi o comando.")

# Iniciar o assistente
assistente_virtual()
