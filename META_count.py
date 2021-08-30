# # Case1D0_1.fastq
# a = input("1 ~ 6: ")
# b = input("0 or 30: ")
# filename1 = "Case" + str(a) + "D" + str(b) + "_1.fastq"
# filename2 = "Case" + str(a) + "D" + str(b) + "_2.fastq"
# print(filename1)
# print(filename2)
# Nor1D0_1.fastq
a = input("1 ~ 9: ")
b = input("0 or 30: ")
filename1 = "Nor" + str(a) + "D" + str(b) + "_1.fastq"
filename2 = "Nor" + str(a) + "D" + str(b) + "_2.fastq"
print(filename1)
print(filename2)

# read1's read count
fr = open(filename1, "r")
lines = fr.readlines()
fr.close()
r1 = len(lines) / 4
print("read1's read count: ", r1)

# read1's total bases count
fr = open(filename1, "r")
lines = fr.readlines()
fr.close()
ls = list()
for i in range(1, len(lines), 4):
    ls.append(lines[i].strip())
ln1 = 0
for j in range(len(ls)):
    ln1 += len(ls[j])
print("read1's total bases count: ", ln1)

# read1's Q30%
fr = open(filename1, "r")
lines = fr.readlines()
fr.close()
ls1 = list()
for i in range(3, len(lines), 4):
    ls1.append(lines[i])
q = 0
for j in range(len(ls)):
    for k in range(len(ls1[j])):
        q30 = ord(ls1[j][k]) - 33
        if q30 >= 30:
            q += 1
q = float(q)
ln1 = float(ln1)
q30Percent1 = q / ln1 * 100
print("read1's Q30%: ", q30Percent1, "%")

# read2's Q30%
fr = open(filename2, "r")
lines = fr.readlines()
fr.close()
ls2 = list()
for i in range(3, len(lines), 4):
    ls2.append(lines[i])
q = 0
p = 0
for j in range(len(ls2)):
    for k in range(len(ls2[j])):
        q30 = ord(ls2[j][k]) - 33
        if q30 >= 30:
            q += 1
q = float(q)
ln1 = float(ln1)
q30Percent2 = q / ln1 * 100
print("read2's Q30%: ", q30Percent2, "%")

# read1's Nbase%
fr = open(filename1, "r")
lines = fr.readlines()
fr.close()
ls = list()
n = 0
for i in range(1, len(lines), 4):
    ls.append(lines[i])
for j in range(len(ls)):
    for k in ls[j]:
        if k == "N":
            n += 1
print(round((100 * n), 10) / ln1, "%")

# read2's Nbase%
fr = open(filename2, "r")
lines = fr.readlines()
fr.close()
ls = list()
n = 0
for i in range(1, len(lines), 4):
    ls.append(lines[i])
for j in range(len(ls)):
    for k in ls[j]:
        if k == "N":
            n += 1
print(round((100 * n), 10) / ln1, "%")
