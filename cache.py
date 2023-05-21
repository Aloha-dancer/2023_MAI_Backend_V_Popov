

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

    def set(self, key: str, value: str) -> None:
        try:
            if len(self._storage) == self._capacity:
                raise MemoryError
            self._storage[key] = value
        except MemoryError:
#            print("Превышение лимита по памяти, для устранения ошики расширьте лимит")
            return
#        print("Добавление прошло успешно")
    
    def get(self, key: str) -> str:
        try:
            temp = self._storage[key]
        except KeyError:
#            print("Такого ключа не существует")
            return ''
        return temp
    
    def rescale(self, new_capacity: int) -> None:
        self._capacity = new_capacity
    
#    def get_information(self) -> None:
#        print(f"Текущая вместимость: {self._capacity}; \nТекущий размер хранилища: {len(self._storage)};")
    
    def rem(self, key: str) -> None:
        try:
            del self._storage[key]
        except KeyError:
#            print("Такого элемента не существует")
            return ''