def acceptare(stare, pozitie_litera, cuvant):
    if pozitie_litera < len(cuvant):
        starile_urm = matrice[stare][pozitie_alfabet[cuv[pozitie_litera]]]
        starile_lambda_urm = matrice[stare][m]
        if pozitie_litera == len(cuvant) - 1 :
            for i in sf :
                if i in starile_urm :
                    return True
        ok = False
        if len(starile_urm) != 0 :
            for i in starile_urm :
                ok = ok or acceptare(i, pozitie_litera + 1, cuvant)
        if len(starile_lambda_urm) != 0 :
            for i in starile_lambda_urm :
                ok = ok or acceptare(i, pozitie_litera, cuvant)
        return ok
    starile_lambda_urm = matrice[stare][m]
    for i in starile_lambda_urm:
        if i in sf:
            return True
    ok = False
    for state in starile_lambda_urm:
        ok = ok or acceptare(state, pozitie_litera, cuvant)
    return ok

f = open("date.in")
n = int(f.readline())  #nr de stari
m = int(f.readline())  #nr de caractere din alfabet
a = [x for x in f.readline().split()]
pozitie_alfabet = {a[i] : i for i in range(len(a))}
pozitie_alfabet["$"] = m
q0 = int(f.readline())
nsf = int(f.readline())  #nr stari finale
sf = [int(x) for x in f.readline().split()]  #starile finale
nt = int(f.readline())  #nr translatii
matrice = [[[] for j in range(m+1)] for i in range(n)]
for i in range(nt):
    L = f.readline().split()
    a = int(L[0])
    b = pozitie_alfabet[L[1]]
    c = int(L[2])
    matrice[a][b].append(c)  #matrice de forma [stare][pozitie litera in alfabet][starile urmatoare]
for i in range(7):
    cuv = f.readline()
    cuv = cuv[:len(cuv)-1]
    print(cuv, end=" ")
   # breakpoint()
    if acceptare(q0, 0, cuv) == True :
        print("acceptat")
    else :
        print("neacceptat")