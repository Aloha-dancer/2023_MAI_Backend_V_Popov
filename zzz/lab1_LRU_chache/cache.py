from typing import Any

class LRUcache:
    '''
    Properties
    '''
    _capacity: int
    _storage: dict
    '''
    Methods
    '''

    def __init__(self, capacity: int = 10) -> None:
        self._capacity = capacity
        self._storage = {}

    def set(self, key: str, value: Any) -> None:
        try:
            if len(self._storage) == self._capacity:
                self._storage.pop(next(reversed(self._storage)))
            self._storage[key] = value
        except KeyError:
            print("Неправильный ключ")
            return
        print("Добавление прошло успешно")
    
    def get(self, key: str) -> tuple[str, Any]:
        try:
            temp = self._storage.pop(key)
            self._storage[key] = temp
        except KeyError:
            print("Такого ключа не существует")
            return ''
#        print([key, temp])
#        print(self._storage)
        return temp
    
    def get_information(self) -> None:
        print(f"Текущая вместимость: {self._capacity}; \nТекущий размер хранилища: {len(self._storage)};")
    
    def rem(self, key: str) -> None:
        try:
            del self._storage[key]
        except KeyError:
            print("Такого элемента не существует")
            return ''