import abc

class Sort(metaclass=abc.ABCMeta):
	@abstractmethod
	def sort(self):
            pass

	def recurse(self):
            self.sort(self) #not overriding this will result in sequential execution

    print("Hello")

	items = [] #should be in the form (item, int place)
