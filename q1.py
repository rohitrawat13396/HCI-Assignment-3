import pandas as pd
from scipy.stats import ttest_ind
import statsmodels.api as sm
from statsmodels.formula.api import ols
from collections import defaultdict

data = pd.read_csv("dataset1.csv")

# ANOVA
#Using OLS and anova_lm
model = ols('time ~ C(menu)', data = data).fit()
anova_table = sm.stats.anova_lm(model, typ=2)
print("\nANOVA Between Subjects:\n", anova_table)

# Pairwise t-test
df = dict(list(data.groupby(["menu"])))
menus = df.keys()
statistics, pvalue = [],[]
rel_dic = defaultdict(list)

for m1 in df.keys():
    for m2 in df.keys():
        stats, p = ttest_ind(df[m1].time,df[m2].time)
        rel_dic[m1].append(p)
        statistics.append(stats)
        pvalue.append(p)

df_new = pd.DataFrame(rel_dic)
df_new["menu"] = list(df_new.columns)
df_new = df_new.set_index(keys = "menu")
print("\nt-test Between Subjects:\n")
print(df_new)
