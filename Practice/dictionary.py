shoplist={}
shoplist['яблоки']=5
shoplist['молоко']=10
shoplist['баклажан']=10
shoplist['хлеб']=0
print('список покупок')
slist=list(shoplist.items())
print(slist)
for i,q in shoplist.items():
    if q>0:
        print(i,q)
    else:
        print(i,q)