
li = [0, 1, 2]

def deal_var(var):
    #var.append(3)
    var = [0, 1, 2, 3]
    print("id(var) = {0}, {1}".format(var, id(var)))


print("id(li) = {0}, {1}".format(li, id(li)))
deal_var(li)
print("id(li) = {0}, {1}".format(li, id(li)))
