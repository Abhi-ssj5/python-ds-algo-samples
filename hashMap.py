class HashMap:
    def __init__(self):
        self.size = 6
        self.map = [None] * self.size
    
    def __getHash(self, key):
        return hash(key) % self.size

    def __getitem__(self, key):
        keyValue = self.__getHash(key)
        if self.map[keyValue] is not None:
            for pair in self.map[keyValue]:
                if pair[0] == key:
                    return pair[1]
        return None

    def __setitem__(self, key, value):
        keyValue = self.__getHash(key)

        if self.map[keyValue] is None:
            self.map[keyValue] = list([[key, value]])
        else:
            for pair in self.map[keyValue]:
                if pair[0] == key and value is not None:
                    pair[1] == value
                    return
                elif pair[0] == key and value is None:
                    self.map[keyValue].remove(pair)
                    return
            
            self.map[keyValue].append([key, value])

    def remove(self, key):
        keyValue = self.__getHash(key)

        if self.map[keyValue] is None:
            return
        else:
            for pair in self.map[keyValue]:
                if pair[0] == key:
                    self.map[keyValue].remove(pair)
                    return
    
    def print(self):
        for list in self.map:
            if list is not None:
                for pair in list:
                    print("key:", pair[0], ", value:", pair[1])


if __name__ == "__main__":
    hashMap = HashMap()
    hashMap["yolo"] = 5
    hashMap["pokemon"] = "turtle"

    hashMap.print()


