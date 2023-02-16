import doctest


class Reactor:
    """
    Класс описывает реактор
    """
    MAX_POWER = 1500

    def __init__(self, purpose_of_reactor: str, power: int):
        """
        Инициализация экземпляра класса

        :param purpose_of_reactor: Назначение реактора, является защищенным для невозможности его корректировки
        :param power: Мощность реактора, является защищенным для невозможности его корректировки

        Пример:
        >>> common_reactor = Reactor("Энегетический", 1200)
        """
        self._purpose_of_reactor = purpose_of_reactor
        if power > Reactor.MAX_POWER:
            raise ValueError
        self._power = power

    @property
    def power(self):
        return self._power

    @property
    def purpose_of_reactor(self):
        return self._purpose_of_reactor

    def __str__(self):
        return f'Назначение реактора: {self._purpose_of_reactor}, Мощность реактора: {self._power}'

    def __repr__(self):
        return f'purpose_of_reactor({self._purpose_of_reactor!r}), power({self._power!r})'

    def increase_power(self, additional_power: int) -> None:
        """
        Метод повышает мощность реактора, но не более значения max_power

        :param additional_power: Дополнительная мощность, которую необходимо добавить
        :return: None

        Пример:
        >>> common_reactor = Reactor("Энегетический", 1200)
        >>> common_reactor.increase_power(100)
        """
        max_power = 1500
        if not isinstance(additional_power, int):
            raise TypeError
        if (self._power + additional_power) > max_power:
            raise ValueError
        self._power += additional_power

    def change_purpose(self, new_purpose: str) -> None:
        """
        Метод меняет назначение реактора

        :param new_purpose: Новое назначение реактора
        :return: None

        Пример:
        >>> common_reactor = Reactor("Энегетический", 1200)
        >>> common_reactor.change_purpose("Промышленный")
        """
        if not isinstance(new_purpose, str):
            raise TypeError
        self._purpose_of_reactor = new_purpose


class ThermalReactor(Reactor):
    """
    Класс описывает реактор на тепловых нейтронах

    :param LIST_OF_REACTORS_THERMAL: список реакторов на тепловых нейтронах
    :param LIST_OF_COOLANTS_THERMAL: список теплоносителей реактора на тепловых нейтронах
    :param LIST_OF_MODERATORS: список замедлителей реактора на тепловых нейтронах
    """
    LIST_OF_REACTORS_THERMAL = ('pwr', 'bwr', 'gcr', 'lwgr', 'phwr', 'htgr', 'hwcgr', 'hwlwr', 'pbmr', 'sghwr')
    LIST_OF_COOLANTS_THERMAL = ('water', 'heavy water', 'gas')
    LIST_OF_MODERATORS = ('water', 'graphite')

    def __init__(self, purpose_of_reactor: str, type_of_reactor: str, power: int, coolant: str, moderator: str):
        """
        Инициализация экземпляра класса

        :param purpose_of_reactor: Назначение реактора
        :param type_of_reactor: Тип реактора, должен соответствовать LIST_OF_REACTORS_THERMAL,
        является защищенным для невозможности его корректировки
        :param power: Мощность реактора
        :param coolant: Тип теплоносителя, должен соответствовать LIST_OF_COOLANTS_THERMAL,
        является защищенным для невозможности его корректировки
        :param moderator: Тип замедлителя, должен соответствовать LIST_OF_MODERATORS,
        является защищенным для невозможности его корректировки

        Пример:
        >>> VVER = ThermalReactor('Энергетический', 'PWR', 1200, 'water', 'water')
        """
        super().__init__(purpose_of_reactor, power)
        self._type_of_reactor = type_of_reactor
        self._coolant = coolant
        self._moderator = moderator

        self.validation(self._type_of_reactor, self._coolant, self._moderator)

    @property
    def type_of_reactor(self):
        return self._type_of_reactor

    @property
    def coolant(self):
        return self._coolant

    @property
    def moderator(self):
        return self._moderator

    @classmethod
    def validation(cls, type_of_reactor: str, coolant: str, moderator: str) -> None:
        """
        Осуществляет проверку вводимых параметров

        :param type_of_reactor: Тип реактора
        :param coolant: Теплоноситель
        :param moderator: Замедлитель
        :return: None
        """
        if not isinstance(type_of_reactor, str):
            raise TypeError
        if type_of_reactor.lower() not in cls.LIST_OF_REACTORS_THERMAL:
            raise ValueError
        if not isinstance(coolant, str):
            raise TypeError
        if coolant.lower() not in cls.LIST_OF_COOLANTS_THERMAL:
            raise ValueError
        if not isinstance(moderator, str):
            raise TypeError
        if moderator.lower() not in cls.LIST_OF_MODERATORS:
            raise ValueError

    def __str__(self):
        return f'Тип реактора: {self._type_of_reactor}, Назначение реактора: {self.purpose_of_reactor}, ' \
               f'Мощность реактора: {self.power}, Теплоноситель: {self._coolant}, Замедлитель: {self._moderator}'

    def __repr__(self):
        return f'purpose_of_reactor({self.purpose_of_reactor!r}), type_of_reactor({self._type_of_reactor!r}),' \
               f' power({self.power!r}), coolant({self._coolant!r}), moderator({self._moderator!r})'

    def increase_power(self, additional_power: int) -> None:
        """
        Метод повышает мощность реактора, но не более значения max_power. Здесь присутствует перегрузка, 
        так как возможно повышенеие сверх предела на 1% для тепловых реакторов

        :param additional_power: Дополнительная мощность, которую необходимо добавить
        :return: None

        Пример:
        >>> VVER = ThermalReactor('Энергетический', 'PWR', 1200, 'water', 'water')
        >>> VVER.increase_power(100)
        """
        max_power = 1500 * 1.01
        if not isinstance(additional_power, int):
            raise TypeError
        if (self._power + additional_power) > max_power:
            raise ValueError
        self._power += additional_power


class FastReactor(Reactor):
    """
       Класс описывает реактор на быстрых нейтронах

       :param LIST_OF_REACTORS_FAST: список реакторов на быстрых нейтронах
       :param LIST_OF_COOLANTS_FAST: список теплоносителей реактора на быстрых нейтронах
       """
    LIST_OF_REACTORS_FAST = ('fbr', 'brest')
    LIST_OF_COOLANTS_FAST = ('lead', 'sodium', 'bismuth')

    def __init__(self, purpose_of_reactor: str, type_of_reactor: str, power: int, coolant: str):
        """
        Инициализация экземпляра класса

        :param purpose_of_reactor: Назначение реактора
        :param type_of_reactor: Тип реактора, должен соответствовать LIST_OF_REACTORS_FAST,
        является защищенным для невозможности его корректировки
        :param power: Мощность реактора
        :param coolant: Тип теплоносителя, должен соответствовать LIST_OF_COOLANTS_FAST,
        является защищенным для невозможности его корректировки

        Пример:
        >>> BREST = FastReactor('Опытный', 'brest', 300, 'lead')
        """
        super().__init__(purpose_of_reactor, power)
        self._type_of_reactor = type_of_reactor
        self._coolant = coolant

        self.validation(self._type_of_reactor, self._coolant)

    @classmethod
    def validation(cls, type_of_reactor, coolant):
        """
        Осуществляет проверку вводимых параметров

        :param type_of_reactor: Тип реактора
        :param coolant: Теплоноситель
        :return: None
        """
        if not isinstance(type_of_reactor, str):
            raise TypeError
        if type_of_reactor.lower() not in cls.LIST_OF_REACTORS_FAST:
            raise ValueError
        if not isinstance(coolant, str):
            raise TypeError
        if coolant.lower() not in cls.LIST_OF_COOLANTS_FAST:
            raise ValueError

    def __str__(self):
        return f'Тип реактора: {self._type_of_reactor}, Назначение реактора: {self.purpose_of_reactor}, ' \
               f'Мощность реактора: {self.power}, Теплоноситель: {self._coolant}'

    def __repr__(self):
        return f'purpose_of_reactor({self.purpose_of_reactor!r}), type_of_reactor({self._type_of_reactor!r}),' \
               f' power({self.power!r}), coolant({self._coolant!r})'


if __name__ == "__main__":
    doctest.testmod()
    pass
