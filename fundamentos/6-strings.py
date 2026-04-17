movieName = "Top Gun"
movieName2 = "top Gun"
print(movieName == movieName2) # False

movieDescription = """
    Top Gun Maverick é um
    filme de aviação e aventura
    muito consagrado na indústria
"""

print(movieName)
line = "="
print(line * 50)
print(movieDescription)


# Procurar palavras em uma string
print("Top" in movieName) # True
print("ação" in movieName) # False