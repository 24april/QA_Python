coins=[1,1,1,0.9,1,1,1,1]
coinpair=[]
coinpairs=[]
for coinofpair in coins:
  coinpair.append(coinofpair)
  if len(coinpair)==2:
    print(coinpair)
    coinpairs.append(coinpair)
    coinpair=[]
print(coinpairs)
for i in list(enumerate(coinpairs)):
  if i[1][0]==i[1][1]:
    continue
  else:
    print("Фальшивая монета №",2*i[0]+i[1].index(min(i[1]))+1)