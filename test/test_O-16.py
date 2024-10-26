o16 = Yadro(8, 16, "O-16")

o16_energy = o16.energy()
o16_mass = o16.calculate_mass()
o16_radius = o16.calculate_radius()
o16_is_beta = o16.beta_static()
o16_can_split = o16.check_split()

print("\nУдельная энергия связи", o16.name + ":", round(o16_energy, 2), "МэВ")
print("Масса атома", o16.name + ":", round(o16_mass, 5), "а.е.м.")
print("Радиус атома", o16.name + ":", round(o16_radius, 2), "фм")

# Вывод состояния бета-распада и возможности деления
if o16_is_beta:
    print("Устойчив ли", o16.name + " к бета-распаду:", "Да")
else:
    print("Устойчив ли", o16.name + " к бета-распаду:", "Нет")
if o16_can_split:
    print("Возможно ли деление", o16.name + " на 2 одинаковых четно-четных осколка:", "Да")
else:
    print("Возможно ли деление", o16.name + " на 2 одинаковых четно-четных осколка:", "Нет")
