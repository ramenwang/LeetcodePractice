# print-in-order
class Foo:

    def __init__(self):
        import threading
        self.second_thr = threading.Event()
        self.third_thr = threading.Event()
        pass


    def first(self, printFirst: 'Callable[[], None]') -> None:

        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.second_thr.set()


    def second(self, printSecond: 'Callable[[], None]') -> None:
        self.second_thr.wait()
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        self.third_thr.set()


    def third(self, printThird: 'Callable[[], None]') -> None:
        self.third_thr.wait()
        # printThird() outputs "third". Do not change or remove this line.
        printThird()
