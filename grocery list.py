# add items to a grocery list
# control plus Z exits the loop


shopping=[]

def main():
    while True:
        try:
            item=input("testing:")
            shopping.append(item)
        except KeyboardInterrupt:
            break
        except EOFError:
            break
    print(shopping)

main()
