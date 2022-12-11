from typing import Union
import doctest


class Person:
    """
    Класс описывает среднестатистического человека
    """

    def __init__(self, height: Union[int, float], weight: Union[int, float], age: int):
        """
        Инициализация экземпляров класса

        :param height: Рост человека в сантимаетрах
        :param weight: Вес человека в килограммах
        :param age: Возраст человека в годах

        Пример:
        >>> person = Person(177, 55, 20)
        """

        if not isinstance(height, (int, float)):
            raise TypeError
        if height < 0:
            raise ValueError('Рост не может быть отрицательным')
        if height > 251:
            raise ValueError('Рост не может быть выше самого высокого человека в мире. Султан Кесен')

        self.height = height

        if not isinstance(weight, (int, float)):
            raise TypeError
        if weight < 0:
            raise ValueError('Вес не может быть отрицательным')
        if weight > 486:
            raise ValueError('Вес не может быть больше веса самого тяжелого человека. Роберт Эрл Хьюз')

        self.weight = weight

        if not isinstance(age, int):
            raise TypeError
        if age < 0:
            raise ValueError('Возраст не может быть отрицательным')
        if age > 122:
            raise ValueError('Возраст не может быть больше чем у самого возрастного человека в истории. Жанна Кельман')

        self.age = age

    def person_getting_older(self, added_age: int) -> None:
        """
            Взросление человека на значение added_age

            :param added_age: добавляемый возраст
            :return: None

            :raise TypeError: Если добавляемый возраст нецелое число.
            :raise ValueError: Если добавляемый возраст меньше 0.
            :raise ValueError: Если суммарный возраст становится больше максимального возраста (122).

            Примеры:
            >>> person = Person(177, 55, 20)
            >>> person.person_getting_older(10)
            """
        ...

    def changes_of_weight(self, diff_weight: Union[int, float]) -> None:
        """
        Изменение веса человека на значение diff_weight

        :param diff_weight: Вес, который будет прибавлен или убран
        :return: None

        :raise TypeError: Если добавляемый вес не число.
        :raise ValueError: Если суммарный возраст становится больше максимального веса (486) или меньше 0.

        Примеры:
        >>> person = Person(177, 55, 20)
        >>> person.changes_of_weight(-10)
        """
        ...


class Bird:
    """
    Класс описывает птицу из мультфильма
    """
    def __init__(self, name: str, bird_type: str):
        """
        Инициализация экземпляров класса

        :param name: Имя птицы
        :param bird_type: Вид птицы

        Примеры:
        >>> eagle = Bird("Эдди", "Орел")
        """

        if not isinstance(name, str):
            raise TypeError

        self.name = name

        if not isinstance(bird_type, str):
            raise TypeError

        self.bird_type = bird_type

    def say_name_of_bird(self) -> None:
        """
        Птица произносит своё имя в формате "Привет, меня зовут name"

        :return: None

        Примеры:
        >>> eagle = Bird("Эдди", "Орел")
        >>> eagle.say_name_of_bird()
        """
        ...

    def say_my_name_by_bird(self, my_name: str) -> None:
        """
        Птица произносит заданное имя в формате "Привет, my_name"

        :param my_name: Любое имя, которое должна произнести птица
        :return: None

        :raise TypeError: Если введеное имя не типа str.

        Примеры:
        >>> eagle = Bird('Эдди', 'Орел')
        >>> eagle.say_my_name_by_bird('Коля')
        """
        ...


class Rectangle:
    """
    Класс описывает прямоугольник
    """
    def __init__(self, width: Union[int, float], height: Union[int, float], colour: str):
        """
        Инициализация экземпляра класса.

        :param width: Ширина прямоугольника, см
        :param height: Высота прямоугольника, см
        :param colour: Цвет прямоугольника

        Пример:
        >>> rectangle1 = Rectangle(50, 100, 'Синий')
        """

        if not isinstance(width, (int, float)):
            raise TypeError
        if width < 0:
            raise ValueError

        self.width = width

        if not isinstance(height, (int, float)):
            raise TypeError
        if height < 0:
            raise ValueError

        self.height = height

        if not isinstance(colour, str):
            raise TypeError

        self.colour = colour

    def change_colour(self, new_colour) -> None:
        """
        Меняет цвет прямоугольника

        :param new_colour: Новый цвет
        :return: None

        :raise TypeError: Если введеный цвет не типа str.

        Пример:
        >>> rectangle1 = Rectangle(50, 100, 'Синий')
        >>> rectangle1.change_colour('Красный')
        """
        ...

    def calculate_area(self) -> float:
        """
        Рассчитывает площадь прямоугольника

        :return: Возвращает площадь прямоугольника

        Пример:
        >>> rectangle1 = Rectangle(50, 100, 'Синий')
        >>> rectangle1.calculate_area()
        """
        ...


if __name__ == "__main__":
    doctest.testmod()
    pass
