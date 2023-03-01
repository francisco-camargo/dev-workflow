"""
This code is based off of my Georgia Tech CS7641 Machine Learning p2-randomized optimization code
    https://bitbucket.org/GT-OMSCS/p2-randomized-optimization/src/master/

"""

import os
import matplotlib.pyplot as plt
from matplotlib import colors

# determine transparent color equivalents
# https://stackoverflow.com/questions/33371939/calculate-rgb-equivalent-of-base-colors-with-alpha-of-0-5-over-white-background
def make_rgb_transparent(rgb, bg_rgb, alpha):
    return [alpha * c1 + (1 - alpha) * c2
            for (c1, c2) in zip(rgb, bg_rgb)]

fontsize = 9
fontsize_ticks = fontsize - 2
fig_dim_x = 3.2
fig_dim_y = fig_dim_x * 0.75
    
def plot_Fitness(df, num_samples, dependant_variable='Iteration', legend_loc='best', show=False):
    if dependant_variable == 'Time_mean':
        x_label = dependant_variable + ' (s)'
    else:
        x_label = dependant_variable
    # plot fitness vs iterations at fixed problem size
    unique_experiments = df.index.unique()
    fig = plt.figure()
    fig.set_size_inches(fig_dim_x, fig_dim_y)
    for idx, u_exp in enumerate(unique_experiments):
        df_temp = df.xs(u_exp)
        x = df_temp[dependant_variable]
        y = df_temp['Fitness_mean']
        std_of_mean = df_temp['Fitness_std']/(num_samples-1)**0.5
        z_score = 1.96 # 1.96 for 95% confidence
        p = plt.plot(x, y, label=str(u_exp))
        color = p[0].get_color()
        color = colors.colorConverter.to_rgb(color)
        plt.fill_between(x,y+z_score*std_of_mean,y-z_score*std_of_mean, color=make_rgb_transparent(color, (1,1,1), alpha=0.3))
        
    plt.xscale('log')
    plt.yscale('log')
    plt.xlabel(x_label, fontsize=fontsize)
    plt.ylabel('Fitness', fontsize=fontsize)
    # plt.xlim([1, 1e3])
    # plt.ylim([0.1, 10])
    plt.xticks(fontsize=fontsize_ticks)
    plt.yticks(fontsize=fontsize_ticks)
    plt.tick_params(direction='in', which='both')
    plt.legend(loc=legend_loc)
    plt.tight_layout(pad=0)
    # fig.patch.set_facecolor('xkcd:mint green') # use to debug image sizing
    
    path = os.path.join('data', 'results', f'{dependant_variable}.eps')
    plt.savefig(path)
    if show:
        plt.show()
    