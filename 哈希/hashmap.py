class Hash(object):
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def hashfunc(self,key):
        return key % self.size

    def rehash(self, index):
        return (index+1) % self.size

    def put(self, key, value):
        hash_index = self.hashfunc(key)

        if self.slots[hash_index] == None:
            self.slots[hash_index] = key
            self.data[hash_index] = value
        else:
            if self.slots[hash_index] == key:
                self.data[hash_index] = value

            else:
                next_hash_index = self.rehash(hash_index)
                while self.slots[next_hash_index] != None and self.slots[next_hash_index] != key:
                    next_hash_index = self.rehash(next_hash_index)

                if self.slots[next_hash_index] == None:
                    self.slots[next_hash_index] = key
                    self.data[next_hash_index] = value
                else:
                    self.data[next_hash_index] = value

    def get(self, key):
        hash_index = self.hashfunc(key)
        position = hash_index
        found = None
        data = None
        stop = None
        while self.slots[position] != None and not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position)
                if position == hash_index:
                    stop = True

        return data

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)


if __name__ == '__main__':
    H = Hash()
    H[54] = "cat"
    H[26] = "dog"
    H[93] = "lion"
    H[17] = "tiger"
    H[77] = "bird"
    H[31] = "cow"
    H[44] = "goat"
    H[55] = "pig"
    H[20] = "chicken"
    print(H.slots)
    print(H.data)
    # >> > H.slots
    # [77, 44, 55, 20, 26, 93, 17, None, None, 31, 54]
    # >> > H.data
    # ['bird', 'goat', 'pig', 'chicken', 'dog', 'lion',
    #  'tiger', None, None, 'cow', 'cat']
    print(H[20])
    H[20] = 'python'
    print(H[20])


