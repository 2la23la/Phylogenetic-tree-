import numpy as np
import matplotlib.pyplot as plt
import scipy.cluster.hierarchy as shc
from scipy.cluster.hierarchy import dendrogram, linkage

number = int(input("Please enter the number of sequences: "))
distance = []
gene_names = []
print("please enter gene names: ")
entries = input().split(' ')
for i in range(0, number):
    try:
        if entries[i] == ' ':
            gene_names.append("x" + str(i))
        else:
            gene_names.append((entries[i]))
    except IndexError:
        gene_names.append("x" + str(i))
print(gene_names)
print("Please enter the number of distance matrix separated by comma between each entry: ")
for i in range(0, number):
    row = []
    entries = input().split(',')

    for j in range(0, number):
        try:
            row.append(int(entries[j]))
        except ValueError:
            row.append(0)
        except IndexError:
            row.append(0)
    distance.append(row)

print(distance)