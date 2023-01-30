class Zadanie4():
    @staticmethod
    def o():
        with open('plik.txt','r') as p1:
            czyt = p1.read()
        with open('plik5.txt','w') as p2:
            p2.write(czyt[::-1])