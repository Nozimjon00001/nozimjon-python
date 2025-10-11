def bahola(ismlar):
    baholar = {}
    ismlar = ismlar
    while ismlar:
        ism = ismlar.pop()
        baho = input(f"Talaba {ism.title()}ning bahosini kiriting: ")
        baholar[ism]=baho
    return baholar

talabalar = ['ali', 'vali', 'hasan', 'husan']
talabalar = talabalar[:]
baholar = bahola(talabalar)
print(baholar)
print(talabalar)