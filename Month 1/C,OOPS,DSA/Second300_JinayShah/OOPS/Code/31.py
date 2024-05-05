import threading
import time

class Observable:
    def __init__(self):
        self._observers = []
        self._lock = threading.Lock()

    def add_observer(self, observer):
        with self._lock:
            if observer not in self._observers:
                self._observers.append(observer)

    def remove_observer(self, observer):
        with self._lock:
            self._observers.remove(observer)

    def notify_observers(self, message):
        with self._lock:
            for observer in self._observers:
                observer.notify(message)

class Observer:
    def __init__(self, name):
        self.name = name

    def notify(self, message):
        print(f"{self.name} received message: {message}")


observable = Observable()

observer1 = Observer("Observer 1")
observer2 = Observer("Observer 2")

observable.add_observer(observer1)
observable.add_observer(observer2)

thread1 = threading.Thread(target=observable.notify_observers, args=("Message from Thread 1",))
thread2 = threading.Thread(target=observable.notify_observers, args=("Message from Thread 2",))

thread1.start()
thread2.start()

thread1.join()
thread2.join()
