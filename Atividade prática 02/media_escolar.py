def calcular_media(nota1: float, nota2: float, nota3: float) -> str:
    """Calcula a média aritmética de três notas escolares."""
    
    # Cálculos e arredondamento
    media = (nota1 + nota2 + nota3) / 3
    media_arredondada = round(media, 2)
    
    # Retorna uma string com o resultado
    return (
        f"--- Calculadora de Média Escolar ---\n"
        f"Notas: {nota1}, {nota2}, {nota3}\n"
        f"  - Média Final: {media_arredondada:.2f}"
    )

# Dados e Execução
n1 = 7.5
n2 = 8.0
n3 = 6.5

# Mínimo de prints: apenas o resultado final
print(calcular_media(n1, n2, n3))