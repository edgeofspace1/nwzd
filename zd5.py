class Zadanie5():
    @staticmethod
    def inpy():
        lp= int(input())
        jn= str(input())
        il= int(input())
        zw= str(input())

        for lp in range(inpn):
            with open(f'{jn}{lp+1}.txt','w') as myfile:
                lin = lp
                for lin in range(lp):
                    myfile.write(f'{zw} \n')