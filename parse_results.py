import datetime

# read report template
report_template = open("sample.md", 'r').read()

# get today's date
date = datetime.datetime.now()
today = "{year} - {month} - {day}\n".format(year = date.year, month = date.month, day = date.day)

# get subtrees and trials
(subtrees, trials) = [i.split()[1] for i in open("results/parameters.txt", 'r').readlines()]

# get number of hits
n_hits = len(open("results/hits.txt", 'r').readlines())

# open report file
r = open('sample_compiled.md', 'w')
r.write(report_template.format(date = date, subtrees = subtrees, trials = trials, hits = n_hits))

r.close()
