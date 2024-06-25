# add items to a grocery list
# control plus Z exits the loop
# Note that this seems to work as requested for https://cs50.harvard.edu/python/2022/psets/3/grocery/ but doesn't get accepted.
# Returns error ":( input of EOF halts program expected exit code 0, not 1"


shopping={}


while True:
    try:
        item=input("")
        item=item.upper()
        check_item=shopping.get(item)
        if check_item is not None:
            shopping[item]=(shopping.get(item))+1
        else:
            shopping[item]=1
        sorted_shopping=dict(sorted(shopping.items()))
    except (KeyboardInterrupt, EOFError):
        break

print("")
for key, value in sorted_shopping.items():
    print(f"{value} {key}")
