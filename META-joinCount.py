# joined read count

ls = list()
for i in range(1, 10):  # Case일 때는 range(1, 7)로 변경.
    # Case<->Nor, D0<->D30 바꿔가면서 python joinCount.py 4번 실행.
    filename = "Nor" + str(i) + "D30/fastqjoin.join.fastq"
    fr = open(filename, "r")
    lines = fr.readlines()
    fr.close()
    readCount = len(lines) / 4
    ls.append(readCount)
print(ls)
