def converter_temperatura(valor: float, origem: str, destino: str) -> str:
    """Converte temperatura entre Celsius (C), Fahrenheit (F) e Kelvin (K)."""
    
    origem = origem.upper()
    destino = destino.upper()
    
    if origem == destino:
        return f"Origem e destino são iguais. Resultado: {valor:.2f} {origem}"
        
    temp_celsius = 0.0 # Valor intermediário em Celsius para facilitar a conversão
    
    # 1. Converter ORIGEM para CELSIUS
    if origem == 'C':
        temp_celsius = valor
    elif origem == 'F':
        temp_celsius = (valor - 32) / 1.8
    elif origem == 'K':
        temp_celsius = valor - 273.15
    else:
        return "Unidade de origem inválida. Use C, F ou K."

    # 2. Converter CELSIUS para DESTINO
    if destino == 'C':
        resultado = temp_celsius
    elif destino == 'F':
        resultado = temp_celsius * 1.8 + 32
    elif destino == 'K':
        resultado = temp_celsius + 273.15
    else:
        return "Unidade de destino inválida. Use C, F ou K."

    return (
        f"--- Conversor de Temperatura ---\n"
        f"Valor Original: {valor:.2f} {origem}\n"
        f"Valor Convertido: {resultado:.2f} {destino}"
    )

# Exemplo de Uso (Converter 25 C para Fahrenheit)
valor_exemplo = 25
origem_exemplo = 'C'
destino_exemplo = 'F'

print(converter_temperatura(valor_exemplo, origem_exemplo, destino_exemplo))