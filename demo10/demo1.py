class queue:
    member = []
    length = 0
    def __init__(self, li):
        self.member = li
        self.length = len(li)
    def insert(self, n):
        self.member.append(n)
        self.length += 1
    def out(self):
        n = self.member[0]
        self.member.pop(0)
        self.length -= 1
        return n
    def delete(self, n):
        self.member.pop(n)
        self.length -= 1

class queue_exception(Exception):
    def __init__(self, err):
        Exception.__init__(self)
        self.err = err

err = queue_exception("noexist_the_element")



if __name__=="__main__":
    a = queue([1, 2, 4, 5, 6, 7, 8])
    a.insert(9)
    b = a.out()
    try:
        a.delete(100)
    except IndexError as e:
        print(err.err)
    print(a.length)
    print(a.member)

