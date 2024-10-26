br80 = Yadro(35, 80, "Br-80")

br80_energy = br80.energy()
br80_mass = br80.calculate_mass()
br80_radius = br80.calculate_radius()
br80_is_beta = br80.beta_static()
br80_can_split = br80.check_split()

print("\nУдельная энергия связи", br80.name + ":", round(br80_energy, 2), "МэВ")
print("Масса атома", br80.name + ":", round(br80_mass, 5), "а.е.м.")
print("Радиус атома", br80.name + ":", round(br80_radius, 2), "фм")

# Вывод состояния бета-распада и возможности деления
if br80_is_beta:
    print("Устойчив ли", br80.name + " к бета-распаду:", "Да")
else:
    print("Устойчив ли", br80.name + " к бета-распаду:", "Нет")
if br80_can_split:
    print("Возможно ли деление", br80.name + " на 2 одинаковых четно-четных осколка:", "Да")
else:
    print("Возможно ли деление", br80.name + " на 2 одинаковых четно-четных осколка:", "Нет")