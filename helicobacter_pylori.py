import matplotlib.pyplot as plt

myfile = open('UP000000429_85962.fasta').readlines()

# search how many sequences are present:
n_of_seq = 0

def number_of_seq(myfile, n_of_seq):
    for line in myfile:
        if '>' in line:
            n_of_seq +=1
    return n_of_seq

print(number_of_seq(myfile, n_of_seq))

# to check how many sequences are from SwissProt and how many from Tremble:
sp_count = 0
tr_count= 0
for line in myfile:
    if '>sp' in line: # this means that we have a sequences coming from SwissProt
        sp_count += 1
    elif '>tr' in line: # from Tremble
        tr_count += 1
print(f"The number of sequences coming from SwissProt is: {sp_count} and the number of sequences coming from Tremble is: {tr_count}.")

# how many amino acids:
def amino_acids(myfile, res_count):
    for line in myfile:
        res_count += len(line.strip("\n"))
    return res_count

res_count=0
print(amino_acids(myfile, res_count))

res_dict = {}
res_count = 0 # need to compute the total residues and do the proportions
for line in myfile:
    if ">" not in line:
        for el in line.strip("\n"): 
            res_count += 1
            if el not in res_dict:
                res_dict[el] = 0
            res_dict[el] += 1
print(res_dict)

av_dict = {} # dictionary for relative abundance
for key in res_dict:
    av_dict[key] = res_dict[key]/res_count

# to make the plot with matplotlib I create the lists for frequencies and residues
res_list = []
for key in res_dict:
    res_list.append(key)
    
freq_list = []
for values in av_dict.values():
    freq_list.append(values)

# to color the graph based on the physicochemical properties of the residues
non_polar = ['G', 'A', 'V', 'P', 'L', 'I', 'M'] # gray
aromatic = ['F', 'W', 'Y'] # yellow
polar = ['S', 'T', 'C', 'N', 'Q', 'H'] # blue
charged = ['D', 'E', 'K', 'R'] # orange

colors = []
for el in res_list:
    if el in non_polar:
        colors.append('grey')
    elif el in aromatic:
        colors.append('yellow')
    elif el in polar:
        colors.append('blue')
    elif el in charged:
        colors.append('orange')

plt.title('Relative abundance of residues in the Helicobacter Pylori Proteome')
plt.bar(res_list, freq_list, color=colors)
plt.show()
