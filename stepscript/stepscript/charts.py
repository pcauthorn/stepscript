import time

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def group_others():
    # https://stackoverflow.com/questions/48587997/matplotlib-pie-graph-with-all-other-categories
    countries = [
        'Albania',
        'Brazil',
        'Denmark',
        'France',
        'Mexico',
        'Nigeria',
        'Spain',
        'Germany',
        'Finland',
    ]

    # the full dataframe
    df = pd.DataFrame(
        data={'country': countries, 'value': np.random.rand(len(countries))},
    ).sort_values('value', ascending=False)

    # the top 5
    df2 = df[:5].copy()

    # others
    new_row = pd.DataFrame(data={
        'country': ['others'],
        'value': [df['value'][5:].sum()]
    })

    # combining top 5 with others
    df2 = pd.concat([df2, new_row])

    # plotting -- for comparison left all countries and right
    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(9, 4))
    df.plot(kind='pie', y='value', labels=df['country'], ax=axes[0])
    df2.plot(kind='pie', y='value', labels=df2['country'], ax=axes[1])
    axes[0].set_title('all countries')
    axes[1].set_title('top 5')
    plt.show()


def ascending_time_graph():
    plt.hlines(.8, 1, 5 + 1, lw=5, color='orange', label='sup')
    plt.hlines(2, 1, 5 + 1, lw=20, color='red')
    plt.hlines(4, 2.2, 4.2, lw=20, color='blue')
    plt.hlines(5, 1, 5 + 1, lw=20, color='red')
    plt.hlines(6, 2.2, 4.2, lw=20, color='blue')
    plt.hlines(7, 1, 5 + 1, lw=20, color='red')
    plt.hlines(8, 2.2, 4.2, lw=20, color='blue')

    plt.ylim(0, 1)
    # plt.yticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
    plt.yticks([0, 1, 2, 3, 4, 5, 6, 7],
               ['', 'two', 'three', '4', '5', '6', '7', '8', '9', '9!'])
    plt.legend(loc='best')
    plt.show()

def per_second_chart():
    labels = [2, 3, 4, 5, 8, 9, 10, 11, 12, 15, 16]
    seconds = [i.seconds for i in time_list]
    f = plt.figure()
    ax = f.add_subplot(1, 1, 1)
    ax.bar(labels, seconds)

    ax.yaxis.set_major_formatter(formatter)
    # this locates y-ticks at the hours
    ax.yaxis.set_major_locator(plt.ticker.MultipleLocator(base=3600))
    # this ensures each bar has a 'date' label
    ax.xaxis.set_major_locator(plt.ticker.MultipleLocator(base=1))

if __name__ == '__main__':
    # per_second_chart()
    # ascending_time_graph()
    # group_others()group_others
    time.sleep(5*60)
    print('done')