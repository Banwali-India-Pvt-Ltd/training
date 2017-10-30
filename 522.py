inputs = 'city code people zip'.split()
for year in data.keys():
    outputs = sorted(data[year][0].keys())
    ytok[year] = dict(zip(inputs, outputs))

print(ytok)