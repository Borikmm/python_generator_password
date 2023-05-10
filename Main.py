from random import randint
import time
import tracemalloc
tracemalloc.start()

class generator:

    class debug:

        @staticmethod
        def check_col_register(value: str):
            col_low = 0
            col_up = 0
            for a in value:
                if a == a.lower():
                    col_low = col_low + 1
                else:
                    col_up = col_up + 1
            return f"UP: {col_up}\nLOW: {col_low}"

        @staticmethod
        def time_test(func, *args):
            now = time.time()
            func(*args)
            return time.time() - now

        @staticmethod
        def test_memory():
            current, peak = tracemalloc.get_traced_memory()
            per = f"Текущее использование памяти: {current} байт\nМаксимальное использование памяти: {peak} байт"
            tracemalloc.stop()
            return per

    __language = \
        {
            "ru": "йцукенгшщзхъфывапролджэячсмитьбю",
            "eng": "qwertyuiopasdfghjklzxcvbnm"
        }
    __numbers = "1234567890"
    __specific_symbols = "~`!@#$%^&*()_+-=?:;№[]{}.></*"

    def __init__(self, col_numbers: int = 5, col_specific_symbols: int = 5, register_up: int = 5, register_low: int = 5):
        self.__modificator_set_numbers = col_numbers
        self.__modificator_set_specific_symbols = col_specific_symbols
        self.__modificator_register = (register_up if register_up>=register_low else register_low-10+register_up) if register_up != 0 or register_low != 0 else 5

    def get_password(self, lenght: int = 10, numbers: bool = True, specific_symbols: bool = False, language: str = "eng", register: str = "low",  seed: int = None, word: str = None, del_symbols: str = None):
        seed_one = seed
        if del_symbols: self.__del_symbols(del_symbols, language)
        if seed == None:
            seed_two = randint(0, 10000)
            password = self.__get_seed_value(lenght, language, register, seed_two + lenght, self.__modificator_register)
            seed = seed_two + lenght
            seed_one = seed_two
        else:
            password = self.__get_seed_value(lenght, language, register, seed + lenght, self.__modificator_register)
            seed += lenght
        if specific_symbols:
            password = self.__set_symbol(password, "specific_symbols", self.__modificator_set_specific_symbols, seed)
        if numbers:
            password = self.__set_symbol(password, "numbers", self.__modificator_set_numbers, seed * 2)
        if word:
            password = self.__set_word(password, word, seed)
        return password, seed_one


    @classmethod
    def __del_symbols(cls, symbols: str, language: str):
        def del_sym(cont):
            for a in symbols.lower():
                cont = cont.replace(a, "")
            return cont
        cls.__language[language] = del_sym(cls.__language[language])
        cls.__specific_symbols = del_sym(cls.__specific_symbols)
        cls.__numbers = del_sym(cls.__numbers)
        return cls.__language[language], cls.__specific_symbols, cls.__numbers

    @classmethod
    def __set_symbol(cls, value: str, name: str, modificator: int, seed: int = None):
        store = cls.__numbers if name == "numbers" else cls.__specific_symbols if name == "specific_symbols" else ...
        for a in range(len(value)):
            if cls.__give_chance(seed, modificator):
                value = value[:a] + store[cls.__get_position_symbol(seed, len(store))] + value[a + 1:]
            seed *= 12 + 2321
        return value

    @classmethod
    def __give_chance(cls, seed: int, mod: int):
        per = int(str((seed + 12) * 32)[:10])
        per += 2131
        if per % 10 > mod:
            per = True
        else:
            per = False
        return per

    @classmethod
    def __set_word(cls, value: str, word: str, seed: int):
        if not seed: val = randint(0, 100000)
        else: val = seed
        value2 = value[:cls.__get_position_symbol(val, len(value))] + word + value[cls.__get_position_symbol(val, len(value)) + len(word):]
        if len(value) != len(value2): value2 = value2[len(value2)-len(value):] # for length true
        return value2

    @classmethod
    def __get_position_symbol(cls, seed: int, lenght: int):
        per = int(str((seed + 12) * 32)[:10])
        vib = per % 10 + (per % 100 - per % 10)
        while not (0 < vib < lenght):
            vib = per % 10 + ((per - per % 10) / 10) % 10
            per += 231342
        return int(vib)

    @classmethod
    def __get_seed_value(cls, lenght: int, language: str, register: str,  seed: int, modificator: int):
        container = ""
        for _ in range(lenght):
            seed1 = seed
            seed1 = cls.__get_position_symbol(seed1, len(cls.__language[language]))
            symbol = cls.__language[language][seed1]
            seed *= 12 + 2321
            if register == "all":
                if cls.__give_chance(seed, modificator):
                    symbol = symbol.lower()
                else:
                    symbol = symbol.upper()
            else:
                symbol = symbol.lower() if register == "low" else symbol.upper()
            container += symbol
        return container