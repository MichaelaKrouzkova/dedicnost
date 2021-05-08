class Kocka:
    def __init__(self):
        self.zivoty=9

    def zamnoukej(self):
        print('mnau')

    def je_ziva(self):
        return self.zivoty > 0

    def uber_zivot(self):
        self.zivoty -=1
        return self.zivoty

    def snez(self, jidlo):
        if not self.je_ziva():
            print('je zbytecne')
            return
        if jidlo=='ryba' and self.zivoty <9:
            self.zivoty +=1
            print ('mnam')
        else:
            print( 'mnam')
k1 = Kocka()
k1.snez('ryba')
