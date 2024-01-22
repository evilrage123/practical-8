fh = open('practical8.txt', 'w')
a = [3, 2, 1.5, 5, 7, 6, 4, 3, 8, 56, 7858]

a.sort()
fh.write(f'ascending order, a = {a}\n')

print('-------------------------')

a.sort(reverse=True)
fh.write(f'descending order, a = {a}\n')

fh.close()
