def checkIthSet(n,i):
    if((n>>i & 1)== 0):
        print("UNSET bit")
    else:
        print("SET bit")

checkIthSet(6,0)
