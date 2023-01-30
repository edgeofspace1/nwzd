class Zadanie3():
    @staticmethod
    def d():
        i = int(input())
        for i in range(i):
            with open(f'plik4{i+1}.txt','w') as myfile:
                myfile.write(f'kocham_inf.txt{i+1}')