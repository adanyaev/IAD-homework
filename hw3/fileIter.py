import os

class file_iter:

    def __init__(self, path):
        self.strs = []
        os.walk(path)
        for i in next(os.walk(path))[2]:
            h = open(path + '\\' + i)
            if len(h.read()) > 140:
                h.seek(0)
                self.strs.extend(h.readlines())
                h.close()


    def __iter__(self):
        self.counter = 0
        return self


    def __next__(self):
        if len(self.strs) > self.counter:
            self.counter += 1
            return self.strs[self.counter - 1]
        else:
            raise StopIteration


strs = file_iter(r'D:\other\code\PyCode\IAD\hw3\test')

for i in strs:
    print (i)