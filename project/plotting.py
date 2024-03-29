# Drawing utilities -- its me and its good
import glob
import json
import os
import sys

import numpy as np

import matplotlib.pyplot as plt
from models.Model import Model
from utils import create_dir


def draw(name):
    plt.rcParams['agg.path.chunksize'] = 10000
    path_name = create_dir('plots', Model.RUN_ID)
    try:
        plt.savefig(f"{path_name}/{name}", dpi=800)
    except FileNotFoundError as e:
        print('\033[93m' + str(e) + '\033[0m')
        sys.exit(2)
    except ValueError as e:
        print('\033[93m' + str(e) + '\033[0m')
        sys.exit(2)
    print('[DONE]')


def find_file(name):
    list_of_dirs = glob.glob(f'output_files/{name}/*')
    curr_dir = max(list_of_dirs, key=os.path.getctime)
    list_of_files = glob.glob(f'{curr_dir}/*.json')
    file = max(list_of_files, key=os.path.getctime)
    try:
        with open(file, "r") as f:
            scores = json.load(f)
    except FileNotFoundError as e:
        print('\033[93m' + "An error occurred while creating graphs. Error:" + str(e) + '\033[0m')
        sys.exit(2)
    return scores


def plot_scores_progress():
    name = 'classifiers_scores'
    print('Drawing ' + name)
    scores = find_file(name)
    fig, ax = plt.subplots()
    x = np.array([i for i in range(len(scores))])
    y = np.array(scores)
    ax.plot(x, y, label="fitness scores")
    ax.grid()
    ax.set_xlabel('Numer osobnika')
    ax.set_ylabel('Współczynnik przystosowania')
    draw(name)


def plot_best_phenotype_genes_progress():
    name = 'gen_stats'
    print('Drawing ' + name)
    scores = find_file(name)
    fig, ax = plt.subplots()
    keys = []
    values = []
    for k, v in scores.items():
        keys.append(k)
        values.append(v)
    for i in range(len(keys)):
        try:
            ax.scatter([keys[i] for _ in range(len(values[i]))], values[i], label='populacja ' + str(i), marker='x')
        except IndexError:
            pass
    ax.grid()
    ax.set_xlabel('Numer populacji')
    ax.set_ylabel('Numer klasyfikatora')
    draw(name)


def plot_genes_in_last_gen():
    name = 'population_dump'
    print('Drawing ' + name)
    scores = find_file(name)
    labels = []
    false_l = []
    true_l = []
    for k, v in scores.items():
        trues = 0
        falses = 0
        labels.append(k)
        for val in v:
            if val:
                trues += 1
            else:
                falses += 1
        false_l.append(falses)
        true_l.append(trues)
    x = np.arange(len(labels))
    width = 0.35
    fig, ax = plt.subplots()

    ax.bar(x - width / 2, true_l, label='True ')
    ax.bar(x + width / 2, false_l, label='False ')
    ax.grid()
    ax.set_ylabel('Liczba genów pozytywnych (' + str(sum(true_l) / len(true_l)) + ') i negatywnych (' +
                  str(sum(false_l) / len(false_l)) + ')')
    fig.tight_layout()
    draw(name)


def plot_avg_max_distance_progress():
    name = 'validation_res'
    print('Drawing ' + name)
    fig, ax = plt.subplots()
    keys = []
    values_max = []
    values_avg = []
    labels = []
    scores = find_file(name)
    for k, v in scores.items():
        keys.append(k)
        values_max.append(scores[k]['max'])
        values_avg.append(scores[k]['avg'])
        labels.append(k)
    dist = [abs(values_max[i] - values_avg[i]) for i in range(len(values_max))]
    ax.plot(keys, dist, label='dystans', marker='o')
    ax.plot(keys, values_max, label='maksymalny wynik', marker='x')
    ax.plot(keys, values_avg, label='średni wynik', marker='^')
    ax.grid()
    ax.set_xlabel('Numer generacji')
    ax.set_ylabel('Dystans max - avg')
    ax.legend()
    draw(name)
