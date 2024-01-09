'''
Functions and values for plotting that I prefer. These are useful for writing two-column
papers
'''

import matplotlib.pyplot as plt
from matplotlib import colors


def make_rgb_transparent(rgb, bg_rgb, alpha):
    '''
    determine transparent color equivalents
    https://stackoverflow.com/questions/33371939/calculate-rgb-equivalent-of-base-colors-with-alpha-of-0-5-over-white-background
    '''
    return [alpha * c1 + (1 - alpha) * c2 for (c1, c2) in zip(rgb, bg_rgb)]


def get_transparent_color(plot_object, bg_rgb=(1, 1, 1), alpha=0.2):
    '''
    Find the alpha transparency equivalent of an input object
    '''
    color = plot_object[0].get_color()  # get str value of color
    color = colors.colorConverter.to_rgb(color)  # convert to tuple value of color
    color = make_rgb_transparent(color, bg_rgb, alpha)
    return color


fontsize = 9
fontsize_ticks = fontsize - 2
fig_dim_x = 3.2
fig_dim_y = fig_dim_x * 0.75
alpha = 0.2


def plotter(
    df,
    independent_variable: str,
    dependent_variable: str,
    dependent_variable_halfband: str,
    legend_loc: str = 'best',
    show: bool = False,
    save_path=None,
):
    '''
    Plot multiple columns from a pandas dataframe
    '''
    # plot fitness vs iterations at fixed problem size
    unique_experiments = df.index.unique()
    fig = plt.figure()
    fig.set_size_inches(fig_dim_x, fig_dim_y)
    for idx, u_exp in enumerate(unique_experiments):
        df_temp = df.xs(u_exp)
        x = df_temp[independent_variable]
        y = df_temp[dependent_variable]
        band = df_temp[dependent_variable_halfband]

        # Plot
        p = plt.plot(x, y, label=str(u_exp))
        color = get_transparent_color(plot_object=p)
        plt.fill_between(x, y + band, y - band, color=color)

    # plt.xscale('log')
    # plt.yscale('log')
    plt.xlabel(independent_variable, fontsize=fontsize)
    plt.ylabel(dependent_variable, fontsize=fontsize)
    # plt.xlim([1, 1e3])
    # plt.ylim([0.1, 10])
    plt.xticks(fontsize=fontsize_ticks)
    plt.yticks(fontsize=fontsize_ticks)
    plt.tick_params(direction='in', which='both')
    plt.legend(loc=legend_loc, fontsize=fontsize_ticks)
    plt.tight_layout(pad=0)
    # fig.patch.set_facecolor('xkcd:mint green') # use to debug image sizing

    if isinstance(save_path, str):
        plt.savefig(save_path)
    if show:
        plt.show()
