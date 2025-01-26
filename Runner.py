import csv
import os

import numpy as np
import pandas
from numpy.ma.core import append
from scipy import stats

IMPORTANT_YEARS = [2008 + i * 4 for i in range(5)]
PATH = "extra"

UNDERDOG_NUM = 3

def main():

    # Finds all file names in the extra folder.
    all_files = os.scandir(PATH)

    underdog_countries = find_unddog(all_files)

    und_sum = sum(underdog_countries)

    all_files = os.scandir(PATH)
    all_med = get_all_medals(all_files)

    print(und_sum/all_med)

def find_unddog(all_files):
    """
    Given a list of file names, find and return a list of
    countries that are arbitrarily considered an underdog.
    """

    selected_countries = []

    for file in all_files:
        current_df = get_file(file.name)
        current_total = get_total_medals(current_df)
        print(current_total)

        if current_total <= UNDERDOG_NUM:
            selected_countries.append(current_total)

    return selected_countries

def get_file(fp):
    return pandas.read_csv(PATH +"/"+ fp)

def get_total_medals(data_frame):
    return data_frame.iloc[0][-1]

def get_all_medals(all_files):
    total = 0
    for file in all_files:
        current_df = get_file(file.name)
        total += get_total_medals(current_df)

    return total

main()