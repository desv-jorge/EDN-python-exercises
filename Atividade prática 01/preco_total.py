def processar_lista_de_compras(lista: dict) -> str:
    output ="--- Detalhes da Lista de Compras ---\n"
    for produto in lista:
        preco_total = produto["preço unitário"] * produto["quantidade"]
        
        output = output + f"""
            \nProduto: {produto['nome do produto'].title()}\n
    - Preço Unitário: R$ {produto['preço unitário']:.2f}\n
    - Quantidade: {produto['quantidade']}\n
    - Preço Total: R$ {preco_total:.2f}\n
        """
        
    return output

lista_de_compra = [{"nome do produto":"cadeira infantil",
                    "preço unitário": 56.20,
                    "quantidade":1},
                   {"nome do produto":"vassoura",
                    "preço unitário": 8.40,
                    "quantidade":3},
                   {"nome do produto":"bolacha maria",
                    "preço unitário": 4.50,
                    "quantidade":5}]

lista_processada = processar_lista_de_compras(lista_de_compra)

print(lista_processada)