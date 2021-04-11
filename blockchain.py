import random
import time
import ti103_2021_03_17 as pm

class Block:
    def __init__(self, index, previous_hash):
        self. index = index
        self.transactions = pm.PatriciaMerkleTrie('')
        self.time = time.time()
        self.previous_hash = previous_hash

    def hash(self):
        return  hash(hash(self.index) + self.transactions.hash() + hash(self.time) + self.previous_hash)

class BlockChain:
    def __init__(self):
            self.chain = [Block(1, random.random())]

    def head(self):
        return self.chain[-1]

    def new (self):
        self.index += 1
        self.chain.append(Block(self.index, self.head().hash()))

b = BlockChain()
print (b.head().hash())
b.new()
print(b.head().hash())
print(b.head().previous_hash)
pm. add_new_word(b.chain[0].transactions, "romane")


print(b.chain[0].hash())