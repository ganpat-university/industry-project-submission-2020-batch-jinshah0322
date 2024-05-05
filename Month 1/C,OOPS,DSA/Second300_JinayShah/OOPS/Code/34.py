class MemoryBlock:
    def __init__(self, size, next_block=None):
        self.size = size
        self.next_block = next_block

class MemoryPoolAllocator:
    def __init__(self, pool_size):
        self.pool_size = pool_size
        self.memory_pool = bytearray(pool_size)
        self.free_blocks = MemoryBlock(pool_size)

    def allocate(self, size):
        size = self.align_size(size)
        current_block = self.free_blocks
        prev_block = None

        while current_block:
            if current_block.size >= size:
                if current_block.size - size > 0:
                    remaining_block = MemoryBlock(current_block.size - size, current_block.next_block)
                    current_block.size = size
                    current_block.next_block = remaining_block

                if prev_block:
                    prev_block.next_block = current_block.next_block
                else:
                    self.free_blocks = current_block.next_block

                return self.memory_pool[id(current_block):id(current_block) + size]

            prev_block = current_block
            current_block = current_block.next_block

        raise MemoryError("Out of memory")

    def deallocate(self, memory_block):
        block_start = id(memory_block)
        block_size = len(memory_block)

        current_block = self.free_blocks
        prev_block = None

        while current_block and id(current_block) < block_start:
            prev_block = current_block
            current_block = current_block.next_block

        new_block = MemoryBlock(block_size, current_block)
        if prev_block:
            prev_block.next_block = new_block
        else:
            self.free_blocks = new_block

    def align_size(self, size):
        return (size + 7) & ~7

pool_size = 1024
allocator = MemoryPoolAllocator(pool_size)

block1 = allocator.allocate(16)
block2 = allocator.allocate(32)

print(f"Allocated Block 1: {block1}")
print(f"Allocated Block 2: {block2}")

allocator.deallocate(block1)
allocator.deallocate(block2)

block3 = allocator.allocate(24)
print(f"Allocated Block 3: {block3}")
