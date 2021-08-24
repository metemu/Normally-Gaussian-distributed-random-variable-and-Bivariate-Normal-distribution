# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 11:45:43 2020

@author: METE
"""
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

mu, sigma = 5, 6

X = np.random.normal(mu, sigma, 5000)
plt.plot(X, 'go')
plt.title("Plot of the 5000 samples", pad=10)
plt.xlabel("X", labelpad=10)
plt.ylabel("Frequency")
plt.savefig('5000samples.png', dpi = 300)
plt.show()

Y = np.random.normal(mu, sigma, 50)
plt.plot(Y, 'ro')
plt.title("Plot of the 50 samples", pad=10)
plt.xlabel("Y", labelpad=10)
plt.ylabel("Frequency")
plt.savefig('50samples.png', dpi = 300)
plt.show()


sns.distplot(X, norm_hist=True, kde=False, 
             color = 'blue', label = "X",
             hist_kws={'edgecolor':'black'})

sns.distplot(Y, norm_hist=True, kde=False, 
             color = 'red', label = "Y",
             hist_kws={'edgecolor':'black'})

plt.title('Histogram')
plt.xlabel('Class Intervals')
plt.ylabel('Frequency')
plt.legend()
plt.savefig('pdfcdfhistogram.png', dpi = 300)
plt.show()

fig, ax1 = plt.subplots()
sns.distplot(X, label='PDF', norm_hist=True, kde=True, 
             color = 'blue',
             hist_kws={'edgecolor':'black'}, ax=ax1)
ax2 = ax1.twinx()
sns.kdeplot(X, cumulative=True, color = 'green', label = 'CDF', ax=ax2)
ax1.set_xlabel('Class Intervals')
ax1.set_ylabel('Frequency (PDF)')
ax2.set_ylabel('Frequency (CDF)')
plt.title('PDF, CDF, and Histogram of the random variable (X)')
fig.tight_layout()
plt.savefig('Xpdfcdfhistogram.png', dpi = 300)
plt.legend()
plt.show()

fig, ax1 = plt.subplots()
sns.distplot(Y, norm_hist=True, kde=True,
             color = 'red',
             hist_kws={'edgecolor':'black'}, ax=ax1)
ax2 = ax1.twinx()
sns.kdeplot(Y, cumulative=True, color = 'green', label = 'CDF', ax=ax2)
ax1.set_xlabel('Class Intervals')
ax1.set_ylabel('Frequency (PDF)')
ax2.set_ylabel('Frequency (CDF)')
plt.title('PDF, CDF, and Histogram of the random variable (Y)')
fig.tight_layout()
plt.savefig('Ypdfcdfhistogram.png', dpi = 300)
plt.legend()
plt.show()
