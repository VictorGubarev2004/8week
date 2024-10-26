hg201 = Yadro(80, 201, "Hg-201")

hg201_energy = hg201.energy()
hg201_mass = hg201.calculate_mass()
hg201_radius = hg201.calculate_radius()
hg201_is_beta = hg201.beta_static()
hg201_can_split = hg201.check_split()

print("\nУдельная энергия связи", hg201.name + ":", round(hg201_energy, 2), "МэВ")
print("Масса атома", hg201.name + ":", round(hg201_mass, 5), "а.е.м.")
print("Радиус атома", hg201.name + ":", round(hg201_radius, 2), "фм")

# Вывод состояния бета-распада и возможности деления
if hg201_is_beta:
    print("Устойчив ли", hg201.name + " к бета-распаду:", "Да")
else:
    print("Устойчив ли", hg201.name + " к бета-распаду:", "Нет")
if hg201_can_split:
    print("Возможно ли деление", hg201.name + " на 2 одинаковых четно-четных осколка:", "Да")
else:
    print("Возможно ли деление", hg201.name + " на 2 одинаковых четно-четных осколка:", "Нет")