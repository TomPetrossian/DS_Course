import pandas as pd
import matplotlib.pyplot as plt
from googletrans import Translator
import decimal
import numpy as np


def to_int(number):
    s = str(number)
    if not '.' in s:
        return number
    deg = len(s) - s.index('.') - 1
    return float(round(number * (10 ** deg)))

def get_data():
    df = pd.read_csv("../project_2_data.csv")
    decimal_points = []
    df['number'] = df['number'].apply(to_int)
    return df

def visualize(df):
    df_splited = np.array_split(df, 5)
    for df_small in df_splited:
        arr = np.array(df_small['number'])
        # print(max(arr))
        srs = pd.Series(arr, df_small['date'])
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
        ax.plot(srs)
        fig.autofmt_xdate()
    plt.show()


def remove_zeros(df):
    df.loc[df['number'] == 0, 'number'] = np.nan
    return df.dropna()


def group_by(df):
    months = (df['month'].drop_duplicates())
    gb = df.groupby('month')['number'].sum()
    return gb.reindex(months)


def translate_months_to_english(gb):
    translator = Translator()
    months = [translator.translate(month, src = 'pt').text for month in list(gb.index)]
    gb.index = months
    return gb


def visualize_last_data(gb):
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.plot(gb)
    fig.autofmt_xdate()
    plt.show()

def main_funct():
    df = get_data()
    # visualize(df)
    df = remove_zeros(df)
    gb = group_by(df)
    gb = translate_months_to_english(gb)
    visualize_last_data(gb)

main_funct()
