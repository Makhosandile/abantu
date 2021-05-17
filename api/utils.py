import pandas as pd
import numpy as np

population_df = pd.read_csv('data/population.csv')
population_df = population_df.fillna(0)
population_df['Population'] = population_df['Population'].astype(int)


def male_population():
    df = population_df.query('Series == "Population, male"')
    df = df.drop('Series', axis=1)
    return df


def population():
    df = population_df.query('Series == "Population, total"')
    df = df.drop('Series', axis=1)
    return df


def female_population():
    df['Female Population'] = population()['Population'] - male_population()['Population']
    df = df.drop(['Series', 'Population'], axis=1)
    return df


def male_perc():
    df['Male Percentage'] = male_population()['Population'] / population()['Population'] * 100
    return df


def female_perc():
    df['Female Percentage'] = female_population()['Female Population'] / population()['Population'] * 100
    return df