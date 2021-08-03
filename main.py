f = open('dataset_24465_4.txt', 'r')
s = f.read().splitlines()
f.close()

f = open('result.txt', 'w')
for i in range(-1, -len(s) - 1, -1):
    f.write(s[i] + '\n')
f.close()
