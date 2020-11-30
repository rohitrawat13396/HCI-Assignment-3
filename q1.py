import pandas as pd
from scipy.stats import f_oneway
from scipy.stats import ttest_ind
from statsmodels.stats.oneway import anova_oneway
import statsmodels.api as sm
from statsmodels.formula.api import ols

data = pd.read_csv("dataset1.csv")

#Between Subjects
# ANOVA
#Using OLS and anova_lm
model = ols('time ~ C(menu)', data = data).fit()
anova_table = sm.stats.anova_lm(model, typ=2)
print(anova_table)

df = dict(list(data.groupby(["menu"])))

# Pairwise t-test
menus = df.keys()
statistics, pvalue = [],[]
rel_dic = {}
for m1 in df.keys():
    for m2 in df.keys():
        stats, p = ttest_ind(df[m1].time,df[m2].time)
        rel_dic[m1+'_'+ m2] = (stats, p)
        statistics.append(stats)
        pvalue.append(p)
for x in rel_dic:
    print(x,':', rel_dic[x])
