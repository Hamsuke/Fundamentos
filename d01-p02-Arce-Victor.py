#practica 2

print("Practica 2");

def e1():
    t1=10
    t2=60
    t3=70
    e=80

    proM=((t1*.70+t2*.70+t3*.70)/3+(e*.30))
    proF=((t1*.60+t2*.60+t3*.60+t1*.60+t2*.60)/5+(e*.40))
    proQ=((t1*.15+t2*.15+t3*.15+t1*.15+t2*.15+t3*.15+t1*.15+t2*.15+t3*.15)/9+(e*.85))
    proG=(proM+proF+proQ)/3

    print("El promedio de Matematicas es", proM);
    print("El promedio de Fisica es", proF);
    print("El promedio de Quimica es", proQ);
    print("El promedio general de las 3 materias es",proG);
          
def e2():
    cap_inv=1000
    gan=cap_inv*0.07

    print("La ganancia es de",gan);


def e3():
    sb=500
    v1=10
    v2=20
    v3=30
    v4=40
    v5=50
    v6=60
    v7=70
    v8=80
    v9=90
    v10=100

    tot_vta=v1+v2+v3+v4+v5+v6+v7+v8+v9+v10
    com=tot_vta*0.10
    com_men=com/12
    tpag=sb+com_men
    


    print("El sueldo mensual con las comisiones incluidas es de",tpag);

def e4():
    tc=1600
    d=tc*0.15
    tp=tc-d

    print("El total de la compra es de",tp);

def e5():
    c1=70
    c2=90
    ef=80
    tf=100

    prom=(c1+c2)/2
    ppar=prom*0.55
    pef=ef*0.30
    ptf=tf*0.15
    cf=ppar+pef+ptf

    print("Su calificación final fue de",cf);

def e6():
    nh=69
    nm=34
    ta=nh+nm
    ph=nh*100/ta
    pm=nm*100/ta

    print("el porcentaje de hombres es del",ph, "y el de mujeres de", pm);

def e7():
    fnac=1999
    fact=2018
    edad=fact-fnac

    print("La edad es de",edad,"años");

def e8():
    presupuesto=20000
    pgine=20000*0.40
    ptrau=20000*0.30
    ppedi=20000*0.30

    print("el dinero a ginecologia es",pgine, " el destinado a traumatologia es de",ptrau, " y el destinado pediatria es de", ppedi);


def e9():
    prcompra=600
    porcentaje=600*0.36
    prventa=prcompra+porcentaje

    print("Debe vender el objeto a un precio de",prventa, "pesos");

def e10():
    tls=15
    tms=24
    tvs=13
    ttotal=tls+tms+tvs
    tpromedio=ttotal/3

    print("el tiempo promedio que tarda en recorrer la ruta es de",tpromedio, "minutos");

def e11():
    pedro=5000
    jose=6300
    luis=5200
    ttd=pedro+jose+luis
    ppedro=pedro*100/ttd
    pjose=jose*100/ttd
    pluis=luis*100/ttd

    print("Pedro aportó el",ppedro,"%, Jose el",pjose,"% y luis el",pluis,"%");
e1()
e2()
e3()
e4()
e5()
e6()
e7()
e8()
e9()
e10()
e11()