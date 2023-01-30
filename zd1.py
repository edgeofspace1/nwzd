class Zadanie1():

    @staticmethod
    def podpunkt1():
        with open('kocham_inf.txt','r') as myfile:
            obj = myfile.read()
            print(obj)

    @staticmethod
    def dkl():
        with open('kocham_inf.txt','r') as myfile:
            for i in myfile:
                print(i)

    @staticmethod
    def dl():
        with open('kocham_inf.txt','r') as myfile:
            obj1 = myfile.read()
            for i in obj1:
                print(i)

    @staticmethod
    def cz():
        with open('kocham_inf.txt','r') as myfile:
            for i in myfile:
                print(i[:2])

    @staticmethod
    def tsci():
        inp = input()
        print()
        with open('kocham_inf.txt', 'r') as myfile:
            tekst = myfile.read()
            for cos in tekst:
                if inp == cos():
                    print(cos)

    @staticmethod
    def il():
        inp = input('')
        print()
        with open('kocham_inf.txt', 'r') as myfile:
            for l in myfile:
                if inp in l:
                    print(l)
    @staticmethod
    def pz():
        with open('kocham_inf.txt','r') as myfile:
            z = myfile.read()
            print(z[0:10])

    @staticmethod
    def oz():
        with open('kocham_inf.txt','r') as myfile:
            zn = myfile.read()
            print(zn[-1:-10:-1])

    @staticmethod
    def  iz():
        with open('plik.txt','r') as myfile:
            ia = 0
            ib = 0
            ic = 0
            for linia in myfile:
                for litera in linia:
                    if litera == 'a':
                        ia += 1
                    if litera == 'b':
                        ib += 1
                    if litera == 'c':
                        ic += 1
            print(ia)
            print(ib)
            print(ic)