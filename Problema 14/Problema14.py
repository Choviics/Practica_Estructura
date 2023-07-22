def two_sum(a, target2=0):
    tmp_dict = {}
    for i in range(len(a)):
        if a[i] in tmp_dict:
            return (tmp_dict[a[i]]+1, i+1)
        else:
            tmp_dict[target2-a[i]] = i
    return -1

def three_sum(a, target3=0):
    for i in range(len(a)):
        res = two_sum(a[i+1:], target2=target3-a[i])
        if res != -1:
            print(i+1, i+1+res[0], i+1+res[1])
            return (i+1, i+1+res[0], i+1+res[1])
    print(-1)
    return -1

if __name__ == "__main__":
    with open("rosalind_3sum.txt", "r") as f:
        k, n = map(int, f.readline().strip().split())
        A = [[int(i) for i in line.strip().split()] for line in f]
    for i in range(k):
        r = three_sum(A[i])