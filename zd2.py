class Zadanie2():
    @staticmethod
    def p():
        with open('kocham_inf.txt','r') as p2:
            tekst = p1.read()
        with open('kocham_inf.txt','w') as p22:
            p2.txt.write(tekst)
    @staticmethod
    def np():
        with open('kocham_inf2.txt','r') as p22:
            tekst = p2.read()
        with open('kocham_inf3.txt','w') as p3:
            p3.write(tekst[::2])
    @staticmethod
    def ds():
        with open('kocham_inf2.txt','r') as p2:
            tekst = p2.read()
        with open('kocham_inf4.txt','w') as p4:
            inp = int(input())
            for i in range(inp):
                p4.write(tekst)