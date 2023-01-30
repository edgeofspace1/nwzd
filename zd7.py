class Zadanie7():
    @staticmethod
    def tab():
        inp = int(input())
        with open('plik6.txt','w') as myfile:
            for i in range(1,inp+1):
                for n in range(1,inp+1):
                    myfile.write(f'{i*n}\t')
                myfile.write('\n')