import os
import shutil

class TransactionalFileSystem:
    def __init__(self, base_path):
        self.base_path = base_path
        self.transaction_path = None

    def begin_transaction(self):
        if self.transaction_path:
            raise RuntimeError("Transaction already in progress.")
        
        self.transaction_path = os.path.join(self.base_path, ".transaction")
        os.makedirs(self.transaction_path)

    def commit_transaction(self):
        if not self.transaction_path:
            raise RuntimeError("No transaction in progress.")

        for root, dirs, files in os.walk(self.transaction_path):
            for file in files:
                src_path = os.path.join(root, file)
                dest_path = os.path.relpath(src_path, self.transaction_path)
                dest_path = os.path.join(self.base_path, dest_path)

                shutil.move(src_path, dest_path)

        shutil.rmtree(self.transaction_path)
        self.transaction_path = None

    def rollback_transaction(self):
        if not self.transaction_path:
            raise RuntimeError("No transaction in progress.")

        shutil.rmtree(self.transaction_path)
        self.transaction_path = None

    def create_file(self, filename, content):
        if not self.transaction_path:
            raise RuntimeError("No transaction in progress.")

        file_path = os.path.join(self.transaction_path, filename)
        with open(file_path, 'w') as file:
            file.write(content)

file_system = TransactionalFileSystem(base_path="my_data")

file_system.begin_transaction()

try:
    file_system.create_file("example.txt", "Hello, world!")

    file_system.commit_transaction()

    print("Transaction committed successfully.")
except Exception as e:
    file_system.rollback_transaction()
    print(f"Transaction rolled back due to error: {e}")
