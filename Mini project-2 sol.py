from itertools import combinations


ProductList = {'p1':10, 'p2':15, 'p3':20, 'p4':25, 'p5':30, 'p6':35, 'p7':50,
               'p8':40, 'p9':55, 'p10':60, 'p11':65, 'p12':75, 'p13':70,
               'p14':45}

for i in range(1,15):
    comb = combinations(ProductList.values(), i)
    
    for item in comb:
        if sum(item) <= 310 and sum(item) >= 290:
            
            print(item)
    
    