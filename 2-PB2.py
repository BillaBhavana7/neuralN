file1 = open('input.txt', 'r')
counts = dict()
data = file1.read()
words = data.split()
for word in words:
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1
print(counts)

f = open('output.txt', 'w')
f.write(data)
f.write('\nword_count:\n')
for key, value in counts.items():
    f.write(f"{key}: {value}\n")
f.close()