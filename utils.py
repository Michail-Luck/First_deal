def decor(ff):
    def wrapper(* args):
        print("What is it ?")
        ff(* args)
        print("Oooh!? it is function!")
    return wrapper

@decor
def funca(n,z):
    print([x for x in range(z,n)] )

if __name__ == '__main__':
  funca(8,1)