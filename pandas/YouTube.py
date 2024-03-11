from datetime import datetime
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.figure import Figure
import typing as tp
import matplotlib
matplotlib.use('TkAgg')


class YouTube:
    def __init__(self, path_to_df: str = "RUvideos_short.csv"):
        self.df = pd.read_csv(path_to_df)
        self.df['trending_date'] = pd.to_datetime(self.df['trending_date'], format='%y.%d.%m')

    def task1(self) -> pd.DataFrame:
        return  self.df['trending_date']

    def task2(self) -> pd.DataFrame:
        self.df = self.df.loc[:, ['trending_date', 'category_id', 'views', 'likes', 'dislikes', 'comment_count']]
        self.df['trending_date'] = self.df['trending_date'].apply(lambda x: x.day)
        return self.df

    def task3(self) -> Figure:
        fig, ax = plt.subplots(figsize=(25, 15))
        sns.boxplot(x='trending_date', y='views', data=self.df, ax=ax)
        ax.set_title('Количество просмотров в разные дни')
        return fig

    def task4(self) -> Figure:
        ...
        return plt.gcf()

    def task5(self) -> Figure:
        ...
        return plt.gcf()

    def task6(self) -> Figure:
        ...
        return plt.gcf()

youtube = YouTube()

print(youtube.task3().show())
