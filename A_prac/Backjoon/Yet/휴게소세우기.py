def make_H(location,l):
    pass

def find_distance(location):
    distance = [0] * len(location)
    for i in range(len(distance)-1):
        distance[i] = location[i + 1] - location[i]
    distance[-1] = L - location[-1]
    return distance

N,M,L = map(int,input().split())
where = list(map(int,input().split()))
where.sort()
dis = find_distance(where)
