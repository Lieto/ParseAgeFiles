import pandas as pd
from matplotlib import pyplot as plt


df = pd.read_csv("crowdsight_60.txt", names=["uid", "filepath", "min_age", "gender", "crowdsight_age"])
#print(df)

# Select female
females = df[df["gender"] == 'f']
males = df[df["gender"] == 'm']

#print females
# Scatter plot ?
ax = df.plot(kind='scatter', x='uid', y='crowdsight_age',
             color='DarkBlue', label='Men and Female', title="Age: 60-100 category");

summary = df["crowdsight_age"].describe()
print(summary)

plt.savefig("60_100.png")

plt.show(ax)
plt.close()


df = pd.read_csv("crowdsight_48.txt", names=["uid", "filepath", "min_age", "gender", "crowdsight_age"])
#print(df)

# Select female
females = df[df["gender"] == 'f']
males = df[df["gender"] == 'm']

#print females
# Scatter plot ?
ax = df.plot(kind='scatter', x='uid', y='crowdsight_age',
             color='DarkBlue', label='Men and Female', title="Age: 48-53 category");

summary = df["crowdsight_age"].describe()
print(summary)


plt.savefig("48_53.png")

plt.show(ax)
plt.close()

df = pd.read_csv("crowdsight_38.txt", names=["uid", "filepath", "min_age", "gender", "crowdsight_age"])
#print(df)

# Select female
females = df[df["gender"] == 'f']
males = df[df["gender"] == 'm']

#print females
# Scatter plot ?
ax = df.plot(kind='scatter', x='uid', y='crowdsight_age',
             color='DarkBlue', label='Men and Female', title="Age: 38-43 category");

summary = df["crowdsight_age"].describe()
print(summary)


plt.savefig("38_43.png")

plt.show(ax)
plt.close()
df = pd.read_csv("crowdsight_25.txt", names=["uid", "filepath", "min_age", "gender", "crowdsight_age"])
#print(df)

# Select female
females = df[df["gender"] == 'f']
males = df[df["gender"] == 'm']

#print females
# Scatter plot ?
ax = df.plot(kind='scatter', x='uid', y='crowdsight_age',
             color='DarkBlue', label='Men and Female', title="Age: 25-32 category");

summary = df["crowdsight_age"].describe()
print(summary)


plt.savefig("25_32.png")

plt.show(ax)
plt.close()

df = pd.read_csv("crowdsight_15.txt", names=["uid", "filepath", "min_age", "gender", "crowdsight_age"])
#print(df)

# Select female
females = df[df["gender"] == 'f']
males = df[df["gender"] == 'm']

#print females
# Scatter plot ?
ax = df.plot(kind='scatter', x='uid', y='crowdsight_age',
             color='DarkBlue', label='Men and Female', title="Age: 15-18 category");

summary = df["crowdsight_age"].describe()
print(summary)


plt.savefig("15_18.png")

plt.show(ax)
plt.close()

df = pd.read_csv("crowdsight_8.txt", names=["uid", "filepath", "min_age", "gender", "crowdsight_age"])
#print(df)

# Select female
females = df[df["gender"] == 'f']
males = df[df["gender"] == 'm']

#print females
# Scatter plot ?
ax = df.plot(kind='scatter', x='uid', y='crowdsight_age',
             color='DarkBlue', label='Men and Female', title="Age: 8-12 category");

summary = df["crowdsight_age"].describe()
print(summary)


plt.savefig("8_12.png")

plt.show(ax)
plt.close()

df = pd.read_csv("crowdsight_4.txt", names=["uid", "filepath", "min_age", "gender", "crowdsight_age"])
#print(df)

# Select female
females = df[df["gender"] == 'f']
males = df[df["gender"] == 'm']

#print females
# Scatter plot ?
ax = df.plot(kind='scatter', x='uid', y='crowdsight_age',
             color='DarkBlue', label='Men and Female', title="Age: 4-6 category");

summary = df["crowdsight_age"].describe()
print(summary)


plt.savefig("4_6.png")

plt.show(ax)
plt.close()

df = pd.read_csv("crowdsight_0.txt", names=["uid", "filepath", "min_age", "gender", "crowdsight_age"])
#print(df)

# Select female
females = df[df["gender"] == 'f']
males = df[df["gender"] == 'm']

#print females
# Scatter plot ?
ax = df.plot(kind='scatter', x='uid', y='crowdsight_age',
             color='DarkBlue', label='Men and Female', title="Age: 0-2 category");

summary = df["crowdsight_age"].describe()
print(summary)


plt.savefig("0_2.png")

plt.show(ax)
plt.close()








"""
ax = females.plot(kind='scatter', x='uid', y='crowdsight_age',
             color='Pink', label='Female', title="Age: 60-100 category females");

plt.show(ax)

ax = males.plot(kind='scatter', x='uid', y='crowdsight_age',
             color='Blue', label='Men', title="Age: 60-100 category females");

plt.show(ax)
"""

# x-axis: uid
# y-axis: crowdsight age estimate
# y-axis: correct age segment (60-100) maybe colored square ?