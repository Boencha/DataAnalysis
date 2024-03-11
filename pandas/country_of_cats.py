import pandas as pd
import matplotlib.pyplot as plt
import typing as tp
from matplotlib.axes import Axes

class CatExam:
    def __init__(self, path_to_df: str = "cat_exam_data.csv"):  # task0
        self.df = pd.read_csv(path_to_df)

    def task1(self) -> pd.DataFrame:
        return self.df.head(5)

    def task2(self) -> tp.List[str]:
        cols_without_skips = self.df.dropna(axis='columns').columns
        all_cols = self.df.columns
        return list(all_cols.difference(cols_without_skips))

    def task3(self) -> pd.DataFrame:
        self.df.dropna(inplace=True)
        return self.df

    def task4(self) -> pd.DataFrame:
        return self.df.describe()

    def task5(self) -> int:
        return self.df[self.df.test_score == 100].count().test_score

    def task6(self) -> pd.DataFrame:
        balls_100 = self.df[self.df.test_score == 100]
        balls_100 = balls_100.groupby('school').agg(number_of_students=('number_of_students', 'first'),
                                                    cnt_100=('test_score', 'count')).reset_index()
        balls_100 = balls_100.sort_values(['cnt_100', 'school'], ascending=[False, False])
        return balls_100

    def task7(self) -> pd.DataFrame:
        average_score = self.df.groupby('school').agg({'test_score' : 'mean', 'number_of_students' : 'first'}).reset_index()
        average_score = average_score.sort_values('test_score', ascending=False)
        return average_score.head(10)

    def task8(self) -> pd.DataFrame:
        average_score = self.df.groupby('school').agg({'test_score' : 'mean', 'number_of_students' : 'first'}).reset_index()
        average_score = average_score.sort_values('test_score', ascending=True)
        return average_score.head(10)

    def task9(self) -> Axes:
        df = pd.read_csv('cat_exam_data.csv')

        small_schools = df[df['number_of_students'] <= 1000]
        large_schools = df[df['number_of_students'] > 1000]

        bins = 10
        alpha = 0.5

        plt.hist(small_schools['test_score'], bins=bins, alpha=alpha, label='Small Schools')
        plt.hist(large_schools['test_score'], bins=bins, alpha=alpha, label='Big Schools')

        plt.title('Test scores by type of school')
        plt.xlabel('Test score')
        plt.ylabel('Amount students')
        plt.legend()

        ax = plt.gca()
        plt.show()
        return ax

exam = CatExam()
print(exam.task9())