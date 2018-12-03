import os, random

# need to generate:
#
# table with Hits *
# file with number of subtrees and trials
#
# table of results

# generate folder with results
try:
    os.makedirs("results")
except:
    pass

# generate table to count rows of (hits number)
f = open('results/hits.txt', 'w')

n_rows = random.randint(1,30)
for i in range(n_rows):
    f.write("{}\n".format(i))

f.close()

# generate pseudoconfig file with n of subtrees and Trials
subtrees = random.randint(3,6)
trials = random.randint(8,12)

g = open('results/parameters.txt', 'w')
g.write("Subtrees: {}\nTrials: {}\n".format(subtrees, trials))

g.close()
