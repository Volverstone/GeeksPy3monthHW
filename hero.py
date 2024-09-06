class SuperHero:
    people='people'
    def __init__(self,name,nickname,superpower,health_points,catchphrase,damage):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase
        self.damage = damage
        self.fly = False
    def hero_name(self):
        print(f"hero's name is {self.name}")
    def double_health(self):
        self.health_points *= 2
        print(f"{self.name}'s health is now {self.health_points}")
    def __str__(self):
        return f"Nickname: {self.name},\n" \
               f"Superpower: {self.superpower},\n" \
               f"Healthy: {self.health_points}"
    def __len__(self):
        return len(self.catchphrase)

hero = SuperHero("Bruce Wayne", "Batman", "High intelligence and combat skills", 100, "I am vengeance", 70)
hero.hero_name()
hero.double_health()
print(hero)
print(len(hero))


class AirHero(SuperHero):
    def __init__(self,name,nickname,superpower,health_points,catchphrase,damage):
        super().__init__(name,nickname,superpower,health_points,catchphrase,damage)
        self.element = "Air"
    def double_health(self):
        self.health_points **= 2
        self.fly = True
        print(f'Здоровье {self.name} возведен в степень "2" теперь его здоровье: {self.health_points}, умение летать: {self.fly}')
    def True_phrase(self):
        print(f'True in the True_phrase: {self.fly}')

class EarthHero(SuperHero):
    def __init__(self,name,nickname,superpower,health_points,catchphrase,damage):
        super().__init__(name,nickname,superpower,health_points,catchphrase,damage)
        self.element = "Earth"
    def double_health(self):
        self.health_points **= 2
        self.fly = True
        print(f'Здоровье {self.name} возведен в степень "2" теперь его здоровье: {self.health_points}, умение летать: {self.fly}')
    def true_phrase(self):
        print(f'True in the True_phrase: {self.fly}')
air_hero = AirHero("Tony Stark", "Iron Man", "Genius intellect and advanced suit", 300, "I am Iron Man.", 90)
earth_hero = EarthHero("Bruce Banner", "Hulk", "Superhuman strength", 500, "Hulk smash!", 100)

air_hero.double_health()
air_hero.True_phrase()
earth_hero.double_health()
earth_hero.true_phrase()

class Villian(SuperHero):
    people = 'monster'
    def __init__(self,name,nickname,superpower,health_points,catchphrase,damage):
        super().__init__(name,nickname,superpower,health_points,catchphrase,damage)
        self.damage = damage
    def gen_x(self):
        pass

    def crit(self, other):
        if hasattr(other, 'damage'):
            other.damage **= 2
            print(f"{other.name}'s damage after critical hit is now {other.damage}")

villian = Villian('Thanos', 'Mad Titan', 'Infinity Gauntlet', 600, 'I am inevitable!', 150)
villian.crit(air_hero)