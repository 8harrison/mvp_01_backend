# Formata a resposta em caso de sucesso
def response_formatter(data, message):
    return {"message": message, "data": data}

# Construir mensagem de erro
def gerar_mensagem_de_erro(message):
    return {"message": message}