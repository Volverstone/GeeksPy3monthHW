class Flying:
    def fly(self):
        self.state = 'в воздухе'
        print(f'Амфибия {self.state}')
class Swimming:
    def swim(self):
        self.state = 'в воде'
        print(f'Амфибия {self.state}')
class Amphibian(Flying, Swimming):
    def __init__(self):
        self.state = 'на земле'

    def land(self):
        self.state = 'на земле'
        print(f'Амфибия {self.state}')

    def current_state(self):
        print(f'Текущее состояние Амфибии: {self.state}')

amphibian = Amphibian()
amphibian.current_state()

amphibian.fly()
amphibian.current_state()

amphibian.land()
amphibian.current_state()

amphibian.swim()
amphibian.current_state()

amphibian.land()
amphibian.current_state()