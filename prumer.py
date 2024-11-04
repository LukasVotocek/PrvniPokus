"""def prumer(seznam):
    soucet=0
    prum=0
    if seznam==0:
        return prum
    for cislo in seznam:
        soucet+=cislo
        prum=soucet/len(seznam)
    return prum

print(prumer([]))"""


def bubblesort(seznam):
    delka=len(seznam)-1  
    for i in range(delka-1):  
        for j in range(delka-i-1): 
            if seznam[j]>seznam[j+1]:
                seznam[j],seznam[j+1]=seznam[j+1],seznam[j]
    return seznam

seznam=[5,8,5,1,4,6,3,9]
print(bubblesort(seznam))