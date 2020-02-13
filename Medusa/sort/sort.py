import abc
import multiprocessing


class Sort(metaclass=abc.ABCMeta):
    def __init__(self, array, up):
        self.items = array
        self.order = up

    @abc.abstractmethod
    def sort(self):
        pass

    items = []  # should be in the form (item, int place)
    order = True

def main():
    pass


if __name__ == '__main__':
    main()
