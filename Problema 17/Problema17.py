import random

mass_aa = {
    57.02146: ["G"], 71.03711: ["A"], 87.03203: ["S"], 97.05276: ["P"], 99.06841: ["V"],
    101.04768: ["T"], 103.00919: ["C"], 113.08406: ["I", "L"], 114.04293: ["N"], 115.02694: ["D"],
    128.05858: ["Q"], 128.09496: ["K"], 129.04259: ["E"], 131.04049: ["M"], 137.05891: ["H"],
    147.06841: ["F"], 156.10111: ["R"], 163.06333: ["Y"], 186.07931: ["W"],
    }

# Inferring Peptide from Full Spectrum with Dynamic Programming.
def inferring_peptide(n, p, l, peptide=[""]):

    if len(peptide[0])==n:
        return peptide

    BYions = [] # store all possible aa between the postion i and j of l.
    for i in range(len(l)-1):
        for j in range(i+1, len(l)):
            aa = mass_aa.get(round(l[j]-l[i], 5), 0)
            if aa:
                BYions.append([i, j, aa])
    
    if BYions[0]:        
        new_l = l[BYions[0][1]:] # update l
        new_p = BYions[0][2] # add new aa need to be added into candidate peptide
        new_peptide = [p+np for np in new_p for p in peptide] # update candidate peptide
        peptide =inferring_peptide(n, p, new_l, new_peptide)

    return peptide

if __name__ == "__main__":
    # load data
    with open("rosalind_full.txt", "r") as f:
        L = [float(line.strip()) for line in f]
        # p: parent mass. l: represent the masses of some b-ions and y-ions
        p, l = L[0], L[1:]
    # length of protein string t
    n = (len(l) - 2) // 2
    # peptide
    t = inferring_peptide(n, p, l)
    print("totally {} possible multiple solutions exist.".format(len(t)))
    print("randomly select 1 solution:\n{}".format(random.sample(t, k=1)[0]))