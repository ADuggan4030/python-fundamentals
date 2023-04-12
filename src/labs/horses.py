""" This lab is a base example for OOP -- Task 1 and Task 2 """


# Inheritance and Polymorphism Lab

class Horse:
    def __init__(self, fur_color: str, body_style: str,
                 personality_type: str):
        self._fur_color = fur_color
        self._body_style = body_style
        self._personality_type = personality_type

    @property
    def fur_color(self) -> str:
        return self._fur_color

    @fur_color.setter
    def fur_color(self, fur_color: str):
        self._fur_color = fur_color

    @property
    def body(self) -> str:
        return self._body_style

    @body.setter
    def body(self, body_style):
        self._body_style = body_style

    @property
    def personality_type(self) -> str:
        return self._personality_type

    @personality_type.setter
    def personality_type(self, type):
        self._personality_type = type

    def fur_function(self):
        print(f'The {self._fur_color} horse is spirited.')


class Takhi(Horse):
    def __init__(self, fur_color: str, body_style: str,
                 personality_type: str, location: str, movement: str):
        super().__init__(fur_color, body_style, personality_type)
        self._location = location
        self._movement = movement

    @property
    def location(self) -> str:
        return self._location

    @location.setter
    def location(self, location: str):
        self._location = location

    @property
    def movement(self) -> str:
        return self._movement

    @movement.setter
    def movement(self, movement: str):
        self._movement = movement

    def roaming(self):
        print(f' The Takhi is a {self._movement} creature.')

    def fur_function(self):
        print(f' The {self._fur_color} Takhi is always the same colors.')


def main():
    our_horse = Horse('spotted', 'Mesomorph', 'Brave')
    our_horse.fur_function()
    print(our_horse.body)
    my_takhi = Takhi('always brown gray gradient color', 'muscular', 'wild', 'Mongolia',
                     'nomadic')
    my_takhi.fur_function()
    my_takhi.roaming()


if __name__ == '__main__':
    main()
