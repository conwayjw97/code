choice = input("what mg would you like?:\t")
mg_to_key = 30

def mg_to_keys(mg):
    # return number of recommended keys
    return ("%d keys" % int(mg//mg_to_key))


print(mg_to_keys(choice))
