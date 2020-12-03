import pandas as pd
import numpy as np
from scipy.stats import ttest_rel
from statsmodels.stats.anova import AnovaRM
from collections import defaultdict
import warnings
warnings.filterwarnings("ignore")

data = pd.read_csv("dataset2.csv")

# ANOVA
#Using Independent VAriable: time
F_time = AnovaRM(data, depvar= "time",subject = "user", within= ["menu"]).fit()
print("\nANOVA Within Subjects for Independent Variable:time:\n", F_time)

#Using Independent VAriable: error
F_error = AnovaRM(data, depvar= "error",subject = "user", within= ["menu"]).fit()
print("\nANOVA Within Subjects for Independent Variable: error:\n", F_error)

# Pairwise t-test
df = dict(list(data.groupby(["menu"])))
menus = df.keys()
statistics, pvalue = [],[]
rel_dic = defaultdict(list)

for m1 in df.keys():
    for m2 in df.keys():
        stats, p = ttest_rel(df[m1].time,df[m2].time)
        rel_dic[m1].append(p)
        statistics.append(stats)
        pvalue.append(p)

df_new = pd.DataFrame(rel_dic)
df_new["menu"] = list(df_new.columns)
df_new = df_new.set_index(keys = "menu")
print("\nt-test Within Subjects:\n")
print(df_new)
