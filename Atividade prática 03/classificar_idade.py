def classificar_idade(idade: int) -> str: 
    if 0 <= idade <= 12:
        return "Criança"
    elif 13 <= idade <= 17:
        return "Adolescente"
    elif 18 <= idade <= 59:
        return "Adulto"
    elif idade >= 60:
        return "Idoso"
    else:
        return "Idade inválida"

idade_exemplo = 35
resultado = classificar_idade(idade_exemplo)

print(f"--- Classificador de Idade ---\nIdade: {idade_exemplo} anos")
print(f"Classificação: {resultado}")