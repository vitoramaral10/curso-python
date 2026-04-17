filmesTuple = ("Matrix", "Inception", "Interstellar", "Tenet", "Dunkirk")

print(type(filmesTuple)) # <class 'tuple'>

print(filmesTuple[:2]) # ('Matrix', 'Inception')
print(filmesTuple[-1]) # Interstellar
print(filmesTuple[:3]) # ('Matrix', 'Inception', 'Interstellar')
print(filmesTuple[2:]) # ('Interstellar',)
print(filmesTuple.index("Tenet")) # 3

