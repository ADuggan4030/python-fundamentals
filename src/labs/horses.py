""" This lab is a base example for OOP -- Task 1 and Task 2 """


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


def main():
    our_horse = Horse('spotted', 'Mesomorph', 'Brave')
    our_horse.fur_function()
    print(our_horse.body)


if __name__ == '__main__':
    main()
