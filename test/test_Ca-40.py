ca40 = Yadro(20, 40, "Ca-40")

ca40_energy = ca40.energy()
ca40_mass = ca40.calculate_mass()
ca40_radius = ca40.calculate_radius()
ca40_is_beta = ca40.beta_static()
ca40_can_split = ca40.check_split()

print("\nУдельная энергия связи", ca40.name + ":", round(ca40_energy, 2), "МэВ")
print("Масса атома", ca40.name + ":", round(ca40_mass, 5), "а.е.м.")
print("Радиус атома", ca40.name + ":", round(ca40_radius, 2), "фм")

# Вывод состояния бета-распада и возможности деления
if ca40_is_beta:
    print("Устойчив ли", ca40.name + " к бета-распаду:", "Да")
else:
    print("Устойчив ли", ca40.name + " к бета-распаду:", "Нет")
if ca40_can_split:
    print("Возможно ли деление", ca40.name + " на 2 одинаковых четно-четных осколка:", "Да")
else:
    print("Возможно ли деление", ca40.name + " на 2 одинаковых четно-четных осколка:", "Нет")