from utils import decor as decor

if __name__ == "__main__" :
    gen_list = [i for i in range(0,100) if i % 3 == 0]
    print(gen_list)
    '''
    gen_gen = (i for i in range(0, 100) if i % 5 == 0)
    print(gen_gen)
    for i in gen_gen:
        print (i)
    '''
    class People:
        def __init__ (self, x,y,z):
            self.life = x
            self.age = y
            self.sex = z

        def __str__(self):
           return (f'People {self.sex }, age {self.age}, value life  - {self.life}  ' )


    Dima = People('good', 33,'male')
    print(Dima)

    @decor
    def testing(x):
        print(x**5)


    testing(5)
    testing(4)
    testing(3)
    testing(2)
