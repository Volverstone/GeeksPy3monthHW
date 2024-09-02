class SuperHero:
    people='people'
    def __init__(self,name,nickname,superpower,health_points,catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase
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

hero = SuperHero("Bruce Wayne", "Batman", "High intelligence and combat skills", 100, "I am vengeance.")
hero.hero_name()
hero.double_health()
print(hero)
print(len(hero))