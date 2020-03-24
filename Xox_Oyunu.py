yazi_tahtasi=[
    ["---","---","---"],
    ["---","---","---"],
    ["---","---","---"]
]
x_durumu= []
o_durumu= []
kazanma_olcutleri=[
    [[0,0],[0,1],[0,2]],
    [[1,0],[1,1],[1,2]],
    [[2,0],[2,1],[2,2]],
    [[0,0],[1,0],[2,0]],
    [[0,1],[1,1],[2,1]],
    [[0,2],[1,2],[2,2]],
    [[0,0],[1,1],[2,2]],
    [[0,2],[1,1],[2,0]]
]
kazanma_olcutleri.sort()
sira=0
while 1:
    sira +=1
    for i in yazi_tahtasi:
        print("\t\t\t\t\t\t",*i,end="\n\n")
    if sira%2==1:
        isaret="X".center(3)
    else:
        isaret="O".center(3)
    print("OYUN SIRASI:{} OYUNCUSUNDA".format(isaret))
    print(50*"*",end="\n\n")
    x = input("SOLDAN SAGA X KONUMUNU GIRINIZ(1,2,3):")
    print()
    y = input("YUKARIDAN ASAGIYA Y KONUMUNU GIRINIZ(1,2,3):")
    print()
    try:
        x=int(x)
        y=int(y)
    except ValueError:
        print("!!!!!!!!!!!!!!!! HATALI GIRIS YAPTINIZ !!!!!!!!!!!!!!!!\n\n:( :( :( :( SIRANIZI KAYBETTINIZ :( :( :( :(")
        print("\n\n")
        continue
    if ((x>3 or x<0) or (y>3 or y<0)):
        print("!!!!!!!!!!!!!!!! HATALI GIRIS YAPTINIZ !!!!!!!!!!!!!!!!\n\n:( :( :( :( SIRANIZI KAYBETTINIZ :( :( :( :(")
        print("\n\n")
    x -=1
    y -=1
    try:
        yazi_tahtasi[y][x]=isaret
    except IndexError:
        continue
    x_durumu.sort()
    o_durumu.sort()
    if sira%2==1:
        x_durumu +=[[y,x]]
    else:
        o_durumu +=[[y,x]]
    for i in kazanma_olcutleri:
        if x_durumu ==i:
            for i in yazi_tahtasi:
                print("\t\t\t\t\t\t", *i)
            print("\n************************** TEBRIKLER X OYUNCUSU KAZANMISTIR **************************")
            exit()
        elif o_durumu ==i:
            for i in yazi_tahtasi:
                print("\t\t\t\t\t\t", *i,end="\n\n")
            print("\n************************** TEBRIKLER O OYUNCUSU KAZANMISTIR **************************")
            exit()



