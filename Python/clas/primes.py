class Primes:
    """Представляет класс-итератор, который принимает максимальное число N
    и выдаёт все простые числа от 1 до N.

    """
    
    end: int
    num: int

    def __init__(self, end: int):
        self.end = end

    def __iter__(self):
        self.num = 1
        return self

    def __next__(self) -> int:
        while True:
            if self.num >= self.end:
                raise StopIteration
            self.num += 1
            for quant in range(2, ((self.num + 1) // 2) + 1):
                if self.num % quant == 0:
                    break
            else:
                return self.num


prime_nums = Primes(50)

for i_elem in prime_nums:
    print(i_elem, end=' ')
