import os
import json
import shutil

class TransactionalFileSystem:
    def __init__(self, root_dir):
        self.root_dir = root_dir
        self.index_file = os.path.join(self.root_dir, 'index.json')
        self.transactions_dir = os.path.join(self.root_dir, 'transactions')
        
        self.load_index()

    def load_index(self):
        if os.path.exists(self.index_file):
            with open(self.index_file, 'r') as index_file:
                self.index = json.load(index_file)
        else:
            self.index = {}

    def save_index(self):
        with open(self.index_file, 'w') as index_file:
            json.dump(self.index, index_file, indent=2)

    def begin_transaction(self, transaction_id):
        transaction_dir = os.path.join(self.transactions_dir, str(transaction_id))
        os.makedirs(transaction_dir, exist_ok=True)
        return transaction_dir

    def commit_transaction(self, transaction_id):
        transaction_dir = os.path.join(self.transactions_dir, str(transaction_id))
        for root, dirs, files in os.walk(transaction_dir):
            for file in files:
                src_path = os.path.join(root, file)
                dest_path = os.path.join(self.root_dir, file)
                shutil.move(src_path, dest_path)
        shutil.rmtree(transaction_dir)

        self.update_index(transaction_id)
        self.save_index()

    def rollback_transaction(self, transaction_id):
        transaction_dir = os.path.join(self.transactions_dir, str(transaction_id))
        shutil.rmtree(transaction_dir)

    def update_index(self, transaction_id):
        transaction_dir = os.path.join(self.transactions_dir, str(transaction_id))
        for root, dirs, files in os.walk(transaction_dir):
            for file in files:
                file_path = os.path.join(root, file)
                file_name = os.path.relpath(file_path, self.root_dir)
                self.index[file_name] = transaction_id

    def get_file_contents(self, file_name):
        transaction_id = self.index.get(file_name)
        if transaction_id is not None:
            transaction_dir = os.path.join(self.transactions_dir, str(transaction_id))
            file_path = os.path.join(transaction_dir, file_name)
            with open(file_path, 'r') as file:
                return file.read()
        else:
            file_path = os.path.join(self.root_dir, file_name)
            with open(file_path, 'r') as file:
                return file.read()

    def index_query(self, query):
        result = []

        for file_name in os.listdir(self.root_dir):
            if query in file_name:
                result.append(file_name)

        for transaction_id in self.index.values():
            transaction_dir = os.path.join(self.transactions_dir, str(transaction_id))
            for file_name in os.listdir(transaction_dir):
                if query in file_name and file_name not in result:
                    result.append(file_name)

        return result

tfs = TransactionalFileSystem('data')
transaction_id = 1
transaction_dir = tfs.begin_transaction(transaction_id)
file_name = 'example.txt'
file_content = 'This is an example content.'
file_path = os.path.join(transaction_dir, file_name)
with open(file_path, 'w') as file:
    file.write(file_content)
tfs.commit_transaction(transaction_id)
query_result = tfs.index_query('example')
print('Query Result:', query_result)
contents = tfs.get_file_contents(file_name)
print('File Contents:', contents)