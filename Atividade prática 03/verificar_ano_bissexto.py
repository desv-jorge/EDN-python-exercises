def verificar_ano_bissexto(ano: int) -> str:
    """Determina se um ano é bissexto."""
    
    # Se o ano for menor que 0 ou não for um inteiro, retorna erro
    if ano <= 0:
        return "O ano deve ser um valor positivo."
    
    # Aplica a regra do ano bissexto
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        e_bissexto = True
    else:
        e_bissexto = False
        
    status = "É Bissexto" if e_bissexto else "Não é Bissexto"
    
    return (
        f"--- Verificador de Ano Bissexto ---\n"
        f"Ano consultado: {ano}\n"
        f"Resultado: {status}"
    )

# Exemplo de Uso (2024 é bissexto, 1900 não é, 2000 é)
ano_exemplo_1 = 2024
ano_exemplo_2 = 1900

print(verificar_ano_bissexto(ano_exemplo_1))
print(verificar_ano_bissexto(ano_exemplo_2))