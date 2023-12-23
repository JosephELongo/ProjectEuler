import pandas as pd

df = pd.read_csv('problem_22_names.txt', header=None)

alphabet = 'abcdefghijklmnopqrstuvwxyz'.upper()

dict = {}

for i in alphabet:
    dict[i] = ord(i) - 64

dict['!'] = 0
df = df.melt()

df.drop(axis=1, columns= ['variable'], inplace=True)



df.sort_values(by = ['value'], inplace=True, ignore_index=True)

def score_word(key, word):
    score = 0
    for char in word:
        score+= key[char]
    return score

answer = 0
df_2 = pd.read_csv('problem_22_names.txt', header=None)

test = []
for c in range(5163):
    test.append(list(df_2[c])[0])

vals = df['value'].items()
vals_2 = []
for i, j in vals:
    vals_2.append(j)

for i in test:
    if i not in vals_2:
        print(i)

print(df)
df.to_csv('/Users/joelongo/Project Euler/ProjectEuler/sample.csv')

for i, j in df['value'].items():

    res = (i+1) * score_word(dict, j)

    answer+= res

print(answer)

#3302