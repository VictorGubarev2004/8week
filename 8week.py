import matplotlib.pyplot as plt

class Yadro:
    
    # Константы формулы Вайзекера
    a = 15.7
    b = 17.8
    c = 0.71
    d = 23.7
    e = 34

    def __init__(self, z, a, name):
        self.z = z  # протоны
        self.a = a  # нуклоны
        self.name = name  # название атома
        self.n = a - z  # нейтроны
        self.energiya = None  # удельная энергия связи
        self.mass = None  # масса 
        self.radius = None  # радиус 
        self.beta = None  # устойчив ли к бета-распаду
        self.split = None  # деление на 2 осколка

    def energy(self):
        # Энергия связи
        a1 = Yadro.a * self.a
        a2 = Yadro.b * self.a ** (2 / 3)
        a3 = Yadro.c * (self.z ** 2) / (self.a ** (1 / 3))
        a4 = Yadro.d * ((self.a - 2 * self.z) ** 2) / self.a
        a5 = Yadro.e / (self.a ** (3 / 4)) if self.z % 2 == 0 and self.n % 2 == 0 else 0
        # Условия для a5
        if self.n % 2 == 0 and self.z % 2 == 0:  # чётное-чётное ядро
            a5 = Yadro.e / (self.a ** (3 / 4)) 
        elif self.a % 2 == 1:  # Ннчётное количество нуклонов
            a5 = 0
        else:  # нечётное-нечетное ядро
            a5 = - Yadro.e / (self.a ** (3 / 4))  
        self.energiya = (a1 - a2 - a3 - a4 + a5) / self.a # удельная энергия
        return self.energiya

    def calculate_mass(self):
        # масса атома
        mp = 1.007825  
        mn = 1.008665  
        defect = self.energy() / 931.5  # дефект массы

        self.mass = self.z * mp + self.n * mn - defect
        return self.mass

    def calculate_radius(self):
        # радиус атома
        r0 = 1.4
        self.radius = r0 * (self.a ** (1 / 3))
        return self.radius

    def beta_static(self):
        # устойчив ли к бета-распаду
        otnoshenie = self.n / self.z
        self.beta = 1 <= otnoshenie <= 1.6
        return self.beta

    def check_split(self):
        # может ли делиться на два чётно-чётных
        self.split = self.a % 2 == 0 and self.z % 2 == 0 and self.n % 2 == 0
        return self.split


# Создаем список ядер
yadra = [
    Yadro(98, 252, "Cf-252"),
    Yadro(94, 238, "Pu-238"),
    Yadro(74, 184, "W-184"),
    Yadro(52, 135, "Te-135"),
    Yadro(35, 80, "Br-80"),
    Yadro(28, 60, "Ni-60"),
    Yadro(22, 48, "Ti-48"),
    Yadro(13, 27, "Al-27"),
    Yadro(8, 16, "O-16"),
    Yadro(3, 7, "Li-7")
]

# Вычисляем значения для графиков
z_values = [y.z for y in yadra]
radius_values = [y.calculate_radius() for y in yadra]
mass_values = [y.calculate_mass() for y in yadra]
# График зависимости массы от количества протонов
plt.figure()
plt.plot(z_values, mass_values, marker='.', color = 'red')
plt.xlabel('Количество протонов')
plt.ylabel('Масса (а.е.м.)')
plt.title('Зависимость массы атома от количества протонов')
plt.grid(True)
plt.show()

# График зависимости радиуса от количества протонов
plt.figure()
plt.plot(z_values, radius_values, marker='.', color = 'green')
plt.xlabel('Количество протонов')
plt.ylabel('Радиус (Фм)')
plt.title('Зависимость радиуса атома от количества протонов')
plt.grid(True)
plt.show()