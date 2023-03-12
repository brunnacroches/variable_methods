class Store:
    rate = 1.03
    
    def __init__(self, address: str) -> None:
        self.__address = address
    
    def show_address(self) -> None:
        print(self.__address)
    
    @classmethod
    def sell(cls) -> int:
        return 40 * cls.rate
    
    @classmethod
    def rate_change(cls, rate_new: int) -> None:
        cls.rate = rate_new

beach_store = Store('Beach')
center_store = Store('Center')

beach_store.show_address()

print(beach_store.sell())
print(center_store.sell())

center_store.rate_change(1.50)

print(beach_store.sell())
print(center_store.sell())