name = input("Digite o nome do filme:\n")
yearLaunch = int(input("Digite o ano de lançamento do filme:\n"))
noteMove = float(input("Digite a nota do filme:\n"))

print("Dados do filme:")
print("===================")

# Alternativa 1
# print("Nome do filme:",name)
# print("Ano de lançamento:", yearLaunch)
# print("Nota:", noteMove)

# Alternativa 2
# print("Nome do filme: ",  name, "\nAno de lançamento: ", yearLaunch, "\nNota: ", noteMove)

# Alternativa 3
print(f"Nome do filme: {name}\n"
      f"Ano de lançamento: {yearLaunch}\n"
      f"Nota: {noteMove}"
      )