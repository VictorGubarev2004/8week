import matplotlib.pyplot as plt

class Yadro:
    
    # Константы формулы Вайзекера
    a = 15.75
    b = 17.8
    c = 0.711
    d = 23.7
    e = 34

    def __init__(self, z, a, name):
        self.z = z  # Число протонов
        self.a = a  # Массовое число
        self.name = name  # Имя атома
        self.n = a - z  # Число нейтронов
        self.energiya = None  # Удельная энергия связи
        self.mass = None  # Масса атома
        self.radius = None  # Радиус атома
        self.beta_stable = None  # Устойчивость к бета-распаду
        self.even_split = None  # Возможность четного деления

    def energy(self):
        # Энергия связи
        term1 = Yadro.a * self.a
        term2 = Yadro.b * self.a ** (2 / 3)
        term3 = Yadro.c * (self.z ** 2) / (self.a ** (1 / 3))
        term4 = Yadro.d * ((self.a - 2 * self.z) ** 2) / self.a
        term5 = Yadro.e / (self.a ** 0.75) if self.z % 2 == 0 and self.n % 2 == 0 else 0

        self.energiya = term1 - term2 - term3 - term4 + term5
        return self.energiya

    def calculate_mass(self):
        # Масса атома
        mp = 1.007825  # Масса протона
        mn = 1.008665  # Масса нейтрона
        deficit = self.energy() / 931.5  # Массовый дефект

        self.mass = self.z * mp + self.n * mn - deficit
        return self.mass

    def calculate_radius(self):
        # Радиус атома
        r0 = 1.25
        self.radius = r0 * (self.a ** (1 / 3))
        return self.radius

    def check_beta_stability(self):
        # Устойчивость к бета-распаду
        otn = self.n / self.z
        self.beta_stable = 1 <= otn <= 1.6
        return self.beta_stable

    def check_even_split(self):
        # Четно-четное деление
        self.even_split = self.a % 2 == 0 and self.z % 2 == 0 and self.n % 2 == 0
        return self.even_split


# Создаем список ядер
yadra = [
    Yadro(92, 238, "U-238"),
    Yadro(94, 239, "Pu-239"),
    Yadro(98, 252, "Cf-252"),
    Yadro(94, 238, "Pu-238"),
    Yadro(52, 135, "Te-135"),
    Yadro(28, 60, "Ni-60"),
    Yadro(8, 16, "O-16"),
    Yadro(7, 15, "N-15"),
]

# Вычисляем значения для графиков
z_values = [y.z for y in yadra]
radius_values = [y.calculate_radius() for y in yadra]
mass_values = [y.calculate_mass() for y in yadra]

# График зависимости радиуса от Z
plt.figure()
plt.plot(z_values, radius_values, marker='o', color = 'green')
plt.xlabel('Z (Количество протонов)')
plt.ylabel('Радиус (фм)')
plt.title('Зависимость радиуса атома от Z')
plt.grid(True)
plt.legend()
plt.show()

# График зависимости массы от Z
plt.figure()
plt.plot(z_values, mass_values, marker='o', color = 'red')
plt.xlabel('Z (Количество протонов)')
plt.ylabel('Масса (а.е.м.)')
plt.title('Зависимость массы атома от Z')
plt.grid(True)
plt.legend()
plt.show()