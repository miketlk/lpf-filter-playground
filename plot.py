#!/usr/bin/env python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import csv

x = []
sig_in = []
sig_out = []

with open('output.csv', 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for i, row in enumerate(plots):
        x.append(i)
        sig_in.append(float(row[0]))
        sig_out.append(float(row[1]))

plt.plot(x, sig_in, label='Input signal')
plt.plot(x, sig_out, label='Output signal')
plt.xlabel('sample')
plt.ylabel('value')
plt.title('Step response of LPF filter')
plt.legend()
plt.show()
