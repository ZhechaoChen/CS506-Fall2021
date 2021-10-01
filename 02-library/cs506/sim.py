def euclidean_dist(x, y):
    res = 0
    for i in range(len(x)):
        res += (x[i] - y[i])**2
    return res**(1/2)

def manhattan_dist(x, y):
    res=0
    for i in range(len(x)):
        res+=abs(x[i]-y[i])
    return res

def jaccard_dist(x, y):
    size_x=len(x)
    size_y=len(y)
    intersect=x&y
    size_intersect=len(intersect)
    res=1-size_intersect/(size_x+size_y-size_intersect)
    return res

def cosine_sim(x, y):
    sumxx, sumxy, sumyy = 0, 0, 0
    for i in range(len(x)):
        a = x[i]; b = y[i]
        sumxx += a*b
        sumyy += a*b
        sumxy += a*b
    return sumxy/math.sqrt(sumxx*sumyy)

# Feel free to add more
