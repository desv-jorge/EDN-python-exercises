def converter_moedas(reais: float, taxa_dolar: float, taxa_euro: float) -> str:
    """Converte um valor em reais para dólares e euros."""
    
    # Cálculos e arredondamento
    valor_dolar = round(reais / taxa_dolar, 2)
    valor_euro = round(reais / taxa_euro, 2)
    
    # Retorna uma string com o resultado
    return (
        f"--- Conversor de Moeda ---\n"
        f"R$ {reais:.2f} equivalem a:\n"
        f"  - Dólar (USD): $ {valor_dolar:.2f}\n"
        f"  - Euro (EUR): € {valor_euro:.2f}"
    )

# Dados e Execução
valor = 100.00
dolar = 5.20
euro = 6.15

# Mínimo de prints: apenas o resultado final
print(converter_moedas(valor, dolar, euro))