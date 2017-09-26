    
def replacement(wa,wb):
    if(wa == 'a' and (wb == 'e' or wb == 'i' or wb =='o' or wb =='u')):
        r = 0
    elif(wa == 'a' and wb == 's'):
        r = -1
    elif(wa == 'c' and wb =='h'):
        r = 1
    elif(wa == 'f' and (wb == 'h' or wb == 'p')):
        r = 0
    elif(wa == 'g' and wb == 'q'):
        r = 1
    elif(wa == 'h' and wb == 'e'):
        r = 0
    elif(wa == 'j' and (wb == 'd' or wb == 'e' or wb =='g')):
        r = 0
    elif(wa == 'k' and wb == 'c'):
        r = 1
    elif(wa == 'q' and wb == 'g'):
        r = 1
    elif(wa == 's' and (wb == 'e' or wb == 'c' or wb =='x')):
        r = -1
    elif(wa == 's' and (wb == 'h' or wb == 't')):
        r = -2
    elif(wa == 'v' and wb == 'w'):
        r = 1
    elif(wa == 'v' and (wb == 'o' or wb == 'u')):
        r = 0
    elif(wa == 'x' and (wb == 'a' or wb == 'c' or wb =='h')):
        r = 0
    elif(wa == 'x' and wb == 'd'):
        r = -1
    elif(wa == 'x' and wb == 'k'):
        r = 1
    elif(wa == 'y' and wb == 'i'):
        r = 1
    elif(wa == 'y' and wb == 'u'):
        r = 0
    elif(wa == 'z' and wb == 's'):
        r = 1
    elif(wa == 'z' and wb == 'j'):
        r = 0
    elif(wa == '\'' and wb == 'a'):
        r = 1
    elif(wa == '\'' and wb == 'u'):
        r = 0
    elif(wa != 'x' and wa == wb):
        r = 1
    elif(wa == 'x' and wb == 'x'):
        r = -3
    else:
        r = -3
 
    
    return r

def maxDistance(f, t):
    lf = len(f) + 1; lt = len(t) + 1
    A = [[0 for k in range(lf)] for j in range(lt)]
    A[0][0] = 0
    for k in range(lf):
        A[0][k] = k * d
    for j in range(lt):
        A[j][0] = j * i;
    for j in range(1, lt):
        for k in range(1, lf):
            A[j][k] = max(A[j][k-1] + d,
                          A[j-1][k] + i,
                          A[j-1][k-1] + replacement(t[j-1],f[k-1]))

    if(t[0] == 'a' and t[1] == 's' and f[0] == 's'):
        return (A[lt-1][lf-1] + 2)
    elif(t[0] !='m' and f[0] =='m'):
        return (A[lt-1][lf-1] - 2)
    elif(t[0] =='a' and ((t[1]=='y' and f[0] == 'i') or (t[1]=='v'and f[0]=='o'))):
        return (A[lt-1][lf-1] + 1)
    elif(t[0]=='v'and (f[0]=='v' or f[0]=='w')):
        return (A[lt-1][lf-1] + 2)
    elif(t[0] == 'z' and (f[0] == 'z' or f[0] == 'j')):
        return (A[lt-1][lf-1] + 1)
    else:
        return A[lt-1][lf-1]



i = -1
d = -1
a = open('train.txt')
file = open('result_r change.txt','w')
latin_library = []
with open('names.txt') as b:
    for line in b.readlines():
        line = line.strip('\n')
        latin_library.append(line)
persian_name = []
for each_line in a:
    (persian, latin) = each_line.split()
    persian_name.append(persian.lower())
for j in range(len(persian_name)):
    max_initial = -len(persian_name) - 1
    t = list(persian_name[j])
    for k in range(len(latin_library)):
        f = list(latin_library[k])
        max_return = maxDistance(f, t)
        if max_return > max_initial:
            max_initial = max_return
            latin = latin_library[k]
    file.write(persian_name[j].upper() + '\t' + latin + '\n')
    print(persian_name[j].upper() + '\t' + latin)
file.close()
a.close()
b.close()
