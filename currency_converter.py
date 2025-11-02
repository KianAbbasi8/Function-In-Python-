def converter(coin):
    pkr= coin*280.9750 # usa 
    b= coin*39.50  #chinees 
    c=coin*3.49 # russian 


    print(coin,"USA = " , "PKR =", pkr)
    print(coin,"Chinees = " , "PKR =", b)
    print(coin,"Russian = " , "PKR =", c)


def main():
    value=float(input("cover pkr into OTHER curnties  "))
    converter(value)
 
main()


