menu = ["kola", "fanta", "shashlik", "baliq"]
zakazlar = []
for n in range(3):
    zakazlar.append(input(f"{n+1}-zakaz "))

print(zakazlar)
for taom in zakazlar:
    if taom in menu:
        print(f"bu taomlar {taom} bor")
    else:
        print(f"bu taomlar {taom} yo'q")