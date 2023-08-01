import pandas as pd
import os.path
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def combine_results(results):
    """Write participants results in combined csv file."""
    if os.stat('combined.csv').st_size == 0:
        results.to_csv(os.path.join( "combined.csv"), index=False)
    else:
        combined_data = pd.read_csv('combined.csv')
        combined_data = pd.concat([combined_data, results], ignore_index=True)
        combined_data.to_csv(os.path.join( "combined.csv"), index=False)

def plot_your_time(data_you):
    """Return participants reaction time as barplot, congruent vs incongruent trials.

    Keyword arguments:
    data_you -- participants trial data
    """
    mean_con_you = data_you.loc[(data_you.Type=='con'), 'Time'].mean()
    mean_incon_you = data_you.loc[(data_you.Type=='incon'), 'Time'].mean()

    trials = ("Congruent Trials", "Incongruent Trials")

    means = (mean_con_you, mean_incon_you)

    fig, ax = plt.subplots(figsize=(5,3))

    bars= ax.bar(trials, means,
            width = 0.4)

    ax.set_ylabel('Reaction time (s)')
    ax.set_title('Your reaction time')
    ax.bar_label(bars)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)    

    return fig, ax

def plot_time(data_you):
    """Return participants reaction time against overall time data as barplot, congruent vs incongruent trials.

    Keyword arguments:
    data_you -- participants trial data
    """
    data_all = pd.read_csv('combined.csv')
    mean_con_you = data_you.loc[(data_you.Type=='con'), 'Time'].mean()
    mean_incon_you = data_you.loc[(data_you.Type=='incon'), 'Time'].mean()
    mean_con_all = data_all.loc[(data_all.Type=='con'), 'Time'].mean()
    mean_incon_all = data_all.loc[(data_all.Type=='incon'), 'Time'].mean()

    trials = ("Congruent Trials", "Incongruent Trials")
    means = {
        'you': (mean_con_you, mean_incon_you),
        'all': (mean_con_all, mean_incon_all),
    }

    x = np.arange(len(trials)) 
    width = 0.25 
    multiplier = 0

    fig, ax = plt.subplots(figsize=(5,3))

    for attribute, measurement in means.items():
        offset = width * multiplier
        rects = ax.bar(x + offset, measurement, width, label=attribute)
        ax.bar_label(rects, padding=3)
        multiplier += 1

    ax.set_ylabel('Reaction time (s)')
    ax.set_title('Your reaction time in comparison')
    ax.set_xticks(x + width, trials)
    ax.legend(loc='lower right', fontsize='x-small', framealpha=1)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    return fig, ax


def plot_true(data_you):
    """Return participants accuracy against overall accuracy as barplot, congruent vs incongruent trials.

    Keyword arguments:
    data_you -- participants trial data
    """
    data_all = pd.read_csv('combined.csv')

    #data you
    count_con_you = data_you.loc[(data_you.Type=='con') & (data_you.Correct== True), 'Type'].count()
    count_incon_you = data_you.loc[(data_you.Type=='incon') & (data_you.Correct== True), 'Type'].count()

    count_all_con_you = data_you.loc[(data_you.Type=='con'), 'Type'].count()
    count_all_incon_you = data_you.loc[(data_you.Type=='incon'), 'Type'].count()

    #data all
    count_con_all = data_all.loc[(data_all.Type=='con')& (data_all.Correct== True), 'Correct'].count()
    count_incon_all = data_all.loc[(data_all.Type=='incon')& (data_all.Correct== True), 'Correct'].count()

    count_all_con_all = data_all.loc[(data_all.Type=='con'), 'Type'].count()
    count_all_incon_all = data_all.loc[(data_all.Type=='incon'), 'Type'].count()

    #checks for devison by 0
    if count_all_con_you==0:
        prop_con_you = 100
    else:
        prop_con_you = count_con_you/count_all_con_you*100
    if count_all_con_all==0:
        prop_con_all = 100
    else:
        prop_con_all= count_con_all/count_all_con_all*100
    if count_all_incon_you==0:
        prop_incon_you = 100
    else:
        prop_incon_you=count_incon_you/count_all_incon_you*100
    if count_all_incon_all==0:
        prop_incon_all = 100
    else: 
        prop_incon_all=count_incon_all/count_all_incon_all*100


    trials = ("Congruent Trials", "Incongruent Trials")
    means = {
        'you': (prop_con_you, prop_incon_you),
        'all': (prop_con_all, prop_incon_all),
    }

    x = np.arange(len(trials))  
    width = 0.25  
    multiplier = 0
    col=['green', 'darkorange']

    fig, ax = plt.subplots(figsize=(5,3))

    for attribute, measurement in means.items():
        offset = width * multiplier
        rects = ax.bar(x + offset, measurement, width, label=attribute, color =col[multiplier])
        ax.bar_label(rects, padding=3)
        multiplier += 1


    ax.set_ylabel('correct responses (%)')
    ax.set_title('Your accuracy in comparison')
    ax.set_xticks(x + width, trials)
    ax.legend(loc='lower right', fontsize='x-small', framealpha=1)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    return fig, ax


def plot_true_you(data_you):
    """Return participants accuracy as barplot, congruent vs incongruent trials.

    Keyword arguments:
    data_you -- participants trial data
    """    
    count_all_con = data_you.loc[(data_you.Type=='con'), 'Type'].count()
    count_all_incon = data_you.loc[(data_you.Type=='incon'), 'Type'].count()

    count_all_correct = data_you.loc[(data_you.Correct== True), 'Correct'].count()
    count_all_trials = count_all_con + count_all_incon

    count_correct_con = data_you.loc[(data_you.Type == 'con') & (data_you.Correct == True), 'Correct'].count()
    count_correct_incon = data_you.loc[(data_you.Type== 'incon')& (data_you.Correct == True), 'Correct'].count()

    trials = ("Congruent Trials", "Incongruent Trials", "All trials")
    means = {
        'correct': (count_correct_con, count_correct_incon, count_all_correct),
        'total': (count_all_con, count_all_incon, count_all_trials),
    }

    x = np.arange(len(trials)) 
    width = 0.25 
    multiplier = 0
    col=['green', 'red']

    fig, ax = plt.subplots(figsize=(5,3))

    for attribute, measurement in means.items():
         offset = width * multiplier
         rects = ax.bar(x + offset, measurement, width, label=attribute, color = col[multiplier])
         ax.bar_label(rects, padding=3)
         multiplier += 1

    ax.set_ylabel('Number of trials')
    ax.set_title('Your accuracy')
    ax.set_xticks(x + width, trials)
    ax.legend(loc='lower right', fontsize='x-small', framealpha=1)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    return fig, ax