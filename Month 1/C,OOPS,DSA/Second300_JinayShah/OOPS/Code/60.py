import hashlib
import time

class Block:
    def __init__(self, index, previous_hash, timestamp, data, nonce=0):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.nonce = nonce
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_data = f"{self.index}{self.previous_hash}{self.timestamp}{self.data}{self.nonce}"
        return hashlib.sha256(block_data.encode()).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(index=0, previous_hash="0", timestamp=time.time(), data="Genesis Block")

    def get_last_block(self):
        return self.chain[-1]

    def add_block(self, new_block):
        new_block.previous_hash = self.get_last_block().hash
        new_block.hash = new_block.calculate_hash()
        self.chain.append(new_block)

    def proof_of_work(self, block, difficulty=2):
        while block.hash[:difficulty] != "0" * difficulty:
            block.nonce += 1
            block.hash = block.calculate_hash()
        print("Block mined:", block.hash)

if __name__ == "__main__":
    my_blockchain = Blockchain()
    for i in range(1, 6):
        new_block_data = f"Block {i} Data"
        new_block = Block(index=i, previous_hash=my_blockchain.get_last_block().hash, timestamp=time.time(), data=new_block_data)
        my_blockchain.proof_of_work(new_block)
        my_blockchain.add_block(new_block)
    for block in my_blockchain.chain:
        print(f"Index: {block.index}, Previous Hash: {block.previous_hash}, Hash: {block.hash}, Data: {block.data}")
