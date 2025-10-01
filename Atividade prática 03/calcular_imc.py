def calcular_imc(peso: float, altura: float) -> str:
    if altura <= 0 or peso <= 0:
        return "Valores de peso ou altura devem ser positivos."

    imc = peso / (altura ** 2)
    
    if imc < 18.5:
        classificacao = "Abaixo do peso"
    elif imc < 25:
        classificacao = "Peso normal"
    elif imc < 30:
        classificacao = "Sobrepeso"
    else:
        classificacao = "Obeso"

    return (
        f"--- Calculadora de IMC ---\n"
        f"Peso: {peso} kg, Altura: {altura} m\n"
        f"IMC calculado: {imc:.2f}\n"
        f"Classificação: {classificacao}"
    )

peso_exemplo = 75.0
altura_exemplo = 1.75
imc = calcular_imc(peso_exemplo, altura_exemplo)

print(imc)