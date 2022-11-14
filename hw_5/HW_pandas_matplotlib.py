#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import math
import matplotlib.ticker as tck


# In[2]:


plt.rcParams['font.size'] = '20'
plt.rcParams['figure.figsize'] = (20, 10)


# # Task1

# In[3]:


def read_gff(path):
    df = pd.read_csv(path, delimiter='\t', header=1, names=['chromosome', 'source','type', 'start', 'end', 'score', 'strand', 'phase', 'attributes'])
    return df


# In[4]:


def read_bed6(path):
    df = pd.read_csv(path, delimiter='\t', names=['chromosome', 'start_bed', 'end', 'name', 'score', 'strand'])
    return df


# In[5]:


gff = read_gff('data/rrna_annotation.gff')
gff['attributes'] = gff['attributes'].str[5:8].str.replace('_','')
gff


# In[6]:


bed = read_bed6('data/alignment.bed')
bed


# In[7]:


rRNA_count = gff.groupby(['chromosome', 'attributes'], as_index=False).size()
rRNA_count.columns = ['Sample', 'rRNA type', 'Count']
rRNA_count


# In[8]:


plt.subplots(figsize = (20,10))
sns.barplot(data = rRNA_count, x = 'Sample', hue = 'rRNA type', y = 'Count')
plt.xticks(rotation=90)


# In[9]:


intersect = gff.merge(bed, on = 'chromosome', suffixes = ('_gff', '_bed')).drop_duplicates()
intersect_rRNA = intersect.query('start > start_bed & end_gff < end_bed')
intersect_rRNA


# # Task2

# In[10]:


df = pd.read_csv('data/diffexpr_data.tsv.gz', delimiter='\t')
df


# In[11]:


sd = df.query('logFC < 0 & pval_corr < 0.05')
su = df.query('logFC > 0 & pval_corr < 0.05')
nd = df.query('logFC < 0 & pval_corr >= 0.05')
nu = df.query('logFC > 0 & pval_corr >= 0.05')


# In[12]:


plt.rc("font", weight="bold")

plt.figure(figsize = (20, 12))
plt.scatter(x = sd['logFC'], y = sd['log_pval'], label = 'Significantly downregulated', s = 30)
plt.scatter(x = su['logFC'], y = su['log_pval'], label = 'Significantly upregulated', s = 30)
plt.scatter(x = nd['logFC'], y = nd['log_pval'], label = 'Non-significantly downregulated', s = 30)
plt.scatter(x = nu['logFC'], y = nu['log_pval'], label = 'Non-significantly uownregulated', s = 30)
plt.axhline(-math.log10(0.05), linestyle = '--', color = 'grey', lw = 2)
plt.text(7, 3, s = 'p value = 0.05', color = 'grey')
plt.axvline(0, linestyle = '--', color = 'grey', lw = 2)
plt.legend(shadow=True, markerscale = 3, fontsize = 18)
plt.xlabel('log$_{2}$(fold change)', style='italic', weight="bold")
plt.ylabel('-log$_{10}$(p value corrected)', style='italic', weight="bold")
plt.axes().xaxis.set_minor_locator(tck.AutoMinorLocator(5))
plt.axes().yaxis.set_minor_locator(tck.AutoMinorLocator(5))
plt.tick_params(which='major', size = 5)
plt.tick_params(which='minor', size = 3)
plt.xlim([df['logFC'].min() - 1, df['logFC'].max() + 1])
plt.ylim([df['log_pval'].min() - 4, df['log_pval'].max() + 4])

plt.annotate(xy  = (sd.sort_values(by='logFC').iloc[0]['logFC'], sd.sort_values(by='logFC').iloc[0]['log_pval']),
             xytext = (sd.sort_values(by='logFC').iloc[0]['logFC'] - 0.5, sd.sort_values(by='logFC').iloc[0]['log_pval'] + 10), 
             text = sd.sort_values(by='logFC').iloc[0]['Sample'],
             arrowprops = dict(facecolor='red', shrink = 0.05),
             weight = 'bold', size = 15)

plt.annotate(xy  = (sd.sort_values(by='logFC').iloc[1]['logFC'], sd.sort_values(by='logFC').iloc[1]['log_pval']),
             xytext = (sd.sort_values(by='logFC').iloc[1]['logFC'] - 0.5, sd.sort_values(by='logFC').iloc[1]['log_pval'] + 10), 
             text = sd.sort_values(by='logFC').iloc[1]['Sample'],
             arrowprops = dict(facecolor='red', shrink = 0.05),
             weight = 'bold', size = 15)

plt.annotate(xy  = (su.sort_values(by='logFC').iloc[-1]['logFC'], su.sort_values(by='logFC').iloc[-1]['log_pval']),
             xytext = (su.sort_values(by='logFC').iloc[-1]['logFC'] - 0.5, su.sort_values(by='logFC').iloc[-1]['log_pval'] + 10), 
             text = su.sort_values(by='logFC').iloc[-1]['Sample'],
             arrowprops = dict(facecolor='red', shrink = 0.05),
             weight = 'bold', size = 15)

plt.annotate(xy  = (su.sort_values(by='logFC').iloc[-2]['logFC'], su.sort_values(by='logFC').iloc[-2]['log_pval']),
             xytext = (su.sort_values(by='logFC').iloc[-2]['logFC'] - 0.5, su.sort_values(by='logFC').iloc[-2]['log_pval'] + 10), 
             text = su.sort_values(by='logFC').iloc[-2]['Sample'],
             arrowprops = dict(facecolor='red', shrink = 0.05),
             weight = 'bold', size = 15)

plt.title('Volcano plot', style='italic', weight="bold", size=35, pad=30)

