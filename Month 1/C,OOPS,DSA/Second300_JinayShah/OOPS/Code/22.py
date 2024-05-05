from threading import Lock

class TransactionalMemory:
    def __init__(self):
        self.data = {}
        self.lock = Lock()

    def read(self, key):
        with self.lock:
            return self.data.get(key)

    def write(self, key, value):
        with self.lock:
            self.data[key] = value

    def begin_transaction(self):
        return Transaction(self)

class Transaction:
    def __init__(self, transactional_memory):
        self.transactional_memory = transactional_memory
        self.local_data = {}
        self.committed = False

    def read(self, key):
        if key in self.local_data:
            return self.local_data[key]
        else:
            return self.transactional_memory.read(key)

    def write(self, key, value):
        self.local_data[key] = value

    def commit(self):
        with self.transactional_memory.lock:
            self.transactional_memory.data.update(self.local_data)
            self.committed = True

    def rollback(self):
        self.local_data.clear()

tm = TransactionalMemory()

tm.write('key1', 'value1')
tm.write('key2', 'value2')

transaction = tm.begin_transaction()

value1 = transaction.read('key1')
transaction.write('key2', 'new_value2')

transaction.commit()

print("After transaction:")
print("key1:", tm.read('key1'))
print("key2:", tm.read('key2'))
