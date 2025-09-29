def calcular_consumo_combustivel(distancia_km: float, combustivel_litros: float) -> str:
    consumo_medio = distancia_km / combustivel_litros
    consumo_arredondado = round(consumo_medio, 2)

    return (
        f"--- Calculadora de Consumo de Combustível ---\n"
        f"Viagem: {distancia_km} km / {combustivel_litros} litros\n"
        f"  - Consumo Médio: {consumo_arredondado:.2f} km/l"
    )

distancia = 300
litros = 25

print(calcular_consumo_combustivel(distancia, litros))