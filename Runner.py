import csv
import os

import numpy as np
import pandas
from numpy.ma.core import append

YEARS = [1896 + i * 4 for i in range(34)]
PATH = "extraExtraFull"

def main():
    percent_new_winners = []
    for y in YEARS:
        current_new_winners = get_num_of_non_winners(y)
        total_part = total_participants(y)

        if total_part != 0:
            current_chance = current_new_winners/total_part
            percent_new_winners.append(current_chance)

    print(percent_new_winners)
    # 5 - 0.02531886
def get_num_of_non_winners(year):
    # Finds all file names in the extra folder.
    all_files = os.scandir(PATH)

    total = 0

    all_df = get_data_frames(all_files)
    all_files = os.scandir(PATH)

    count = 1
    for country in all_df:

        if previous_underdog(country, year) and won_a_medal(country, year):
            total += 1


    return total

def previous_underdog(c_df, y):
    olympics_left = (y - 1896) / 4
    for i in range(int(olympics_left)):
        years = c_df.iloc[0]
        last_year = (y - (i + 1) * 4)
        was_in_year = last_year in years.values
        if was_in_year and get_column_sum(c_df, last_year) > 0:
            return False

    return True

def won_a_medal(c_df, y):
    was_in_year = y in c_df.iloc[0].values
    return was_in_year and get_column_sum(c_df, y) > 0

def get_column_sum(c_df, y):
    column = get_column(c_df, y)
    total = column.sum()[0] - y

    return total

def get_column(c_df, y):
    years = c_df.iloc[0]
    count = 0
    for current_y in years:
        if y == current_y:
            return c_df[[str(count)]]

        count += 1

    return None

def total_participants(year):
    # Finds all file names in the extra folder.
    all_files = os.scandir(PATH)

    total = 0

    all_df = get_data_frames(all_files)

    for country in all_df:
        if country.isin([year]).any().any():
            total += 1

    return total

def get_data_frames(all_files):
    all_df = []

    for file in all_files:
        all_df.append(get_file(file.name))

    return all_df

def get_file(fp):
    return pandas.read_csv(PATH +"/"+ fp + "/total.csv")

main()