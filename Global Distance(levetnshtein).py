def minDistance(f, t):
    lf = len(f) + 1; lt = len(t) + 1
    A = [[0 for k in range(lf)] for j in range(lt)]
    A[0][0] = 0
    for k in range(lf):
        A[0][k] = k * d
    for j in range(lt):
        A[j][0] = j * i;
    for j in range(1, lt):
        for k in range(1, lf):
            A[j][k] = min(A[j][k-1] + d,
                          A[j-1][k] + i,
                          A[j-1][k-1] +(m if f[k-1] == t[j-1] else r))
    min_return = A[lt-1][lf-1]
    return min_return

i = 1
d = 1
m = 0
r = 1
a = open('train.txt')
file = open('result_Global Distance(levenshtein).txt','w')
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
    min_initial = len(persian_name) + 1
    t = list(persian_name[j])
    for k in range(len(latin_library)):
        f = list(latin_library[k])
        min_return = minDistance(f, t)
        if min_return < min_initial:
            min_initial = min_return
            latin = latin_library[k]
    file.write(persian_name[j].upper() + '\t' + latin + '\n')
    print(persian_name[j].upper() + '\t' + latin)
file.close()
a.close()
b.close()
