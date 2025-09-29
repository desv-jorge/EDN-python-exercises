def calcular_desconto(preco_original: float, percentual: int) -> str:
    valor_desconto = preco_original * (percentual / 100)
    preco_final = preco_original - valor_desconto

    return (
        f"--- Calculadora de Desconto ---\n"
        f"Produto: Camiseta\n"
        f"Preço Original: R$ {preco_original:.2f} (Desconto de {percentual}%)\n"
        f"  - Valor do Desconto: R$ {valor_desconto:.2f}\n"
        f"  - Preço Final: R$ {preco_final:.2f}"
    )

preco = 50.00
desconto = 20

print(calcular_desconto(preco, desconto))