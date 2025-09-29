def calcular_volume(Comprimento:float, Largura:float, Altura:float) -> str:
    volume = Comprimento * Largura * Altura
    volume_formatado = str(volume) + "cm³"
    return volume_formatado

volume = calcular_volume(12,14,6)

print(volume)