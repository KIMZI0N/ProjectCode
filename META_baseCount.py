# 400bp read count
n = 0
for i in range(1, 10):  # Case일 때는 range(1, 7)로 변경.
    # Case<->Nor, D0<->D30 바꿔가면서 python baseCount.py 4번 실행.
    filename = "Nor" + str(i) + "D30/fastqjoin.join.fastq"
    fr = open(filename, "r")
    lines = fr.readlines()
    fr.close()
    for i in range(1, len(lines), 4):
        ls = len(lines[i].strip())
        if ls < 400:
            n += 1
    print(n)
    n = 0
