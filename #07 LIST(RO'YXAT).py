print("#07 LIST(RO'YXAT)\n")

ismlar = ["Abror","Mahmud","Ali"]
print(f"Salom {ismlar[0]}, bugun choyxonaga bordingmi?")
print(f"{ismlar[1]}, choyxonaga bordingmi?")
print(f"{ismlar[2]}, choyxonaga bordingmi?\n")

sonlar = [45,-23,21,12.3]
print(sonlar[0]+sonlar[1])
print(sonlar[1]-sonlar[3])
print(sonlar[2]*sonlar[1])
print(sonlar[1]/sonlar[2],"\n")

t_shaxslar = ["Imom Buxoriy","Amir Temur"]
z_shaxslar = ["Shavkat Mirziyoyev","Mahmud Murodov"]
print(f"Men tarixiy shaxslardan {t_shaxslar.pop(0)} bilan,\nzamonaviy shaxslardan esa {z_shaxslar.pop(0)} bilan\nsuhbat qilishni istar edim\n")

friends = []
friends.append("Ali")
friends.append("Bobur")
friends.append("Said")
friends.append("Donyor")
friends.append("Eldor")
friends.append("Frdavs")
print(f"Mehmonga chaqirganlarim {friends}")
friends.remove("Ali")
friends.remove("Said")
friends.remove("Eldor")
print(f"kelib bilganlar {friends} qolganlar esa kololmadi\n")

mehmonlar = []
mehmonlar.append(friends.pop(0))
mehmonlar.append(friends.pop(1))
#mehmonlar.append(friends.pop(2))
print(f"mehmonga kelganlar {mehmonlar}")