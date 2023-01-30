class Zadanie6():
    @staticmethod
    def lp2():
        list = [i for i in range(1,10+1)]
        inp= int(input())
        with open('generator.txt','w') as myfile:
            for i in range(inp):
                myfile.write(f'{list} \n')