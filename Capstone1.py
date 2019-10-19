import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


essays = pd.read_csv('essays.csv')
projects = pd.read_csv('projects.csv')
outcomes = pd.read_csv('outcomes.csv')


def get_unique(series):
    return len(series.unique())

def get_count(series):
    return np.size(series)

def get_max(series):
    return ('Not Applicable' if series.dtypes == np.dtype('O')
            else np.max(series))

def get_min(series):
    return ('Not Applicable' if series.dtypes == np.dtype('O')
            else np.min(series))

def get_std(series):
    return ('Not Applicable' if series.dtypes == np.dtype('O')
            else np.std(series))

def get_mean(series):
    return ('Not Applicable' if series.dtypes == np.dtype('O')
            else np.mean(series))

def get_missing(series):
    return series.isnull().sum()

def get_quantile(series, quantile):
    return (['Not Applicable' ] *len(quantile) if series.dtypes == np.dtype('O')
            else np.nanquantile(series, quantile))

def get_data_audit1(dataframe):
    data_types = dataframe.dtypes
    idx = data_types.index.copy()
    results = {}
    results['mean' ] =[]
    results['std_dev' ] =[]
    results['obs' ] =[]
    results['missing' ] =[]
    results['missing_perc' ] =[]
    results['min' ] =[]
    results['max' ] =[]
    results['unique' ] =[]
    results['q5'] =[]
    results['q10'] = []
    results['q25'] = []
    results['q50'] = []
    results['q75'] = []
    results['q85'] = []
    results['q95'] = []
    results['q99'] = []
    print(results)
    for row in idx:
        results['mean'].append(get_mean(dataframe[row]))
        results['std_dev'].append(get_std(dataframe[row]))
        results['obs'].append(get_count(dataframe[row]))
        results['missing'].append(get_missing(dataframe[row]))
        results['missing_perc'].append(results['missing'][-1] / results['obs'][-1])
        results['min'].append(get_min(dataframe[row]))
        results['max'].append(get_max(dataframe[row]))
        results['unique'].append(get_unique(dataframe[row]))
        quantiles = get_quantile(dataframe[row], [.05, .1, .25, .5, .75, .85, .95, .99])
        results['q5'].append(quantiles[0])
        results['q10'].append(quantiles[1])
        results['q25'].append(quantiles[2])
        results['q50'].append(quantiles[3])
        results['q75'].append(quantiles[4])
        results['q85'].append(quantiles[5])
        results['q95'].append(quantiles[6])
        results['q99'].append(quantiles[7])
    df = pd.DataFrame(results)
    df.index = idx
    return df


essays_audit = get_data_audit1(essays)
projects_audit = get_data_audit1(projects)
outcomes_audit = get_data_audit1(outcomes)

