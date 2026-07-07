print("\nmodulo04 - estrutura de dados - dicionario\n")
print("-" * 40)

cardapio_da_semana = {
    "segunda-feira": "Arroz com feijão",
    "terça-feira": "panqueca de carne",
    "quarta-feira": "feijoada", 
    "quinta-feira": "sopa de legumes",
    "sexta-feira": "peixe grelhado", 
    "sabado": "pizza",
    "domingo": "macarrão",
}

cardapio_da_semana["quarta-feira"] = "feijoada com couve" 

print("bem-vindo ao programa de verificação  de cardapio! \n")
 
dia_escolhido = input("digite um dia da semana para saber o menu:").lower().strip()

if dia_escolhido in cardapio_da_semana:
    
    comida = cardapio_da_semana[dia_escolhido]
    print(f"no {dia_escolhido}, o prato do dia é: {comida}!")

    print
    f'desculpe, {dia_escolhido} não é um dia válido no nosso cardapio. tente usar o hifen (ex: segunda-feira.'
