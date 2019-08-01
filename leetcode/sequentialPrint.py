from threading import Lock
class Foo:
    def __init__(self):
        self.mutex1 = Lock()
        self.mutex2 = Lock()
        self.mutex1.acquire()
        self.mutex2.acquire()


    def first(self, printFirst: 'Callable[[], None]') -> None:

        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.mutex1.release()


    def second(self, printSecond: 'Callable[[], None]') -> None:

        # printSecond() outputs "second". Do not change or remove this line.
        self.mutex1.acquire()
        printSecond()
        self.mutex2.release()


    def third(self, printThird: 'Callable[[], None]') -> None:

        # printThird() outputs "third". Do not change or remove this line.
        self.mutex2.acquire()
        printThird()