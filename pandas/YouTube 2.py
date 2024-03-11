import json
import typing as tp

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from datetime import datetime
from matplotlib.figure import Figure


class YouTube2:
    def __init__(  # task0
            self,
            trends_df_path: str = "RUvideos_short.csv",
            categories_df_path: str = "RU_category_id.json"
    ):
        self.trends_df =  pd.read_csv(trends_df_path)
        self.trends_df['trending_date'] = pd.to_datetime(self.trends_df['trending_date'], format='%y.%d.%m')

        with open(categories_df_path) as json_file:
            json_data = json.load(json_file)

        self.categories_df = pd.DataFrame(columns=['id', 'name'])

        for item in json_data['items']:
            self.categories_df = self.categories_df.append(
                {'id': int(item['id']),
                 'name': item['snippet']['title']},
                ignore_index=True
            )

        self.categories_df['id'] = self.categories_df['id'].astype(int)

    def task1(self) -> pd.DataFrame:
        return pd.merge(self.trends_df, self.categories_df, left_on='category_id', right_on='id')

    def task2(self) -> pd.DataFrame:
        return pd.pivot_table(data=self.task1(), values='views', index='name', columns='trending_date', aggfunc=np.sum)

    def task3(self) -> Figure:
        figure, ax = plt.subplots(figsize=(24, 15))
        data = self.task2()
        sns.heatmap(data / 10 ** 6, annot=True, fmt='.2f', ax=ax, cmap="crest")
        cbar = ax.collections[0].colorbar
        cbar.ax.tick_params(labelsize=18)

        ax.set_xticklabels(data.columns.strftime('%Y-%m-%d'), rotation=50)
        ax.tick_params(axis='x', labelsize=18)
        ax.tick_params(axis='y', labelsize=20)
        ax.set_ylabel('Категории', fontsize=25, fontweight='bold')
        ax.set_xlabel('Дни', fontsize=25, fontweight='bold')
        ax.set_title('Kоличество просмотров по дням для каждой категории', fontsize=35, fontweight='bold')
        ax.set_xlim(right=len(data.columns))
        figure.tight_layout()
        return figure

    def task4(self) -> pd.DataFrame:
        return pd.pivot_table(data=self.task1(), values='views', index='name', columns='trending_date', aggfunc=np.sum, margins=True, margins_name='2017-1-11')

    def task5(self) -> Figure:
        data = self.task4()
        new_index = data.index.tolist()
        new_index[-1] = "Всего просмотров"
        data.index = new_index
        figure, ax = plt.subplots(figsize=(24, 15))
        sns.heatmap(data / 10 ** 6, annot=True, fmt='.2f', cmap="crest", ax=ax, vmax=13)
        cbar = ax.collections[0].colorbar
        cbar.ax.tick_params(labelsize=18)

        all = data.columns.strftime('%Y-%m-%d').tolist()
        all[-1] = 'Всего просмотров'
        all = data.set_axis(all, axis=1)

        ax.set_xticklabels(all, rotation=50)

        ax.tick_params(axis='x', labelsize=19)
        ax.tick_params(axis='y', labelsize=21)

        ax.set_ylabel('Категории', fontsize=25, fontweight='bold')
        ax.set_xlabel('Дни', fontsize=27, fontweight='bold')
        ax.set_title('Kоличество просмотров по дням для каждой категории', fontsize=35, fontweight='bold')
        figure.tight_layout()
        return figure


youtube = YouTube2()

print(youtube.task3().show())