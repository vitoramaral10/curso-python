dict = [
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
]


# {'Arroz': 15.5, 'Feijão': 8.9, 'Macarrão': 6.75}
print({item["nome"]: item["preco"] for item in dict})

print(dict[0]["nome"])

# média de preço 10.38 (2 casas decimais)
print(f"{sum(item['preco'] for item in dict) / len(dict):.2f}")