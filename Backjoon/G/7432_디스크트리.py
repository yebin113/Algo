N = int(input())
tri = dict()

for i in range(N):
    directory = input().split('\\')
    directories = tri
    for j in range(len(directory)):
        if directory[j] not in directories:
            directories[directory[j]] = dict()
        directories = directories[directory[j]]
# print(tri)


def print_tri(trie, depth=0):
    for key in sorted(trie.keys()):
        print(' '*depth + key)
        next_key = trie[key]

        if isinstance(next_key,dict):
            print_tri(next_key,depth+1)
print_tri(tri)
