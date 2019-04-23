# chi-squared test with similar proportions
import pandas as pd
from scipy.stats import chi2_contingency
from scipy.stats import chi2

def chi2CatAnalysis(dataFrame, cat_vars, target_var, prob = 0.95, verbose=False):
    indepdent_vars = []
    depedent_vars = []
    for feature in cat_vars:
        stat, p, dof, expected = chi2_contingency(pd.crosstab(dataFrame[feature], columns=dataFrame[target_var]).values)
        critical = chi2.ppf(prob, dof)
        if verbose == True:
            print('probability=%.3f, critical=%.3f, stat=%.3f, p-value=%.3f, dof=%.3f' % (prob, critical, stat, p, dof))
        if (stat >= critical) & (p <= (1 - prob)):
            if verbose == True:
                print (target_var, 'is dependent on ', feature)
            depedent_vars.append(feature)
        else:
            if verbose == True:
                print (target_var, 'is Independent off ', feature)
            indepdent_vars.append(feature)
        if verbose == True:
            print('--------\n')
        
    print (target_var, 'is dependent on ', depedent_vars)
    print (target_var, 'is Independent off ', indepdent_vars)