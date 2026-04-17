produtos = {
    {
        "nome": "Arroz",
        "preco": 15.50
    },
    {
        "nome": "Feijão",
        "preco": 8.90
    },
    {
        "nome": "Macarrão",
        "preco": 6.75
    }
}

for _ in range(3):
    nome = input("Nome do produto: ")
    preco = float(input("Preço: "))
    produtos[nome] = preco

print(produtos)
print(max(produtos, key=produtos.get))
print(f"{sum(produtos.values()) / len(produtos):.2f}")
