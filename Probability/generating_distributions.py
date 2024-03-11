import numpy as np
import matplotlib.pyplot as plt

import scipy.stats as sps

coin = sps.bernoulli(p=0.5).rvs
uniform_pdf = sps.uniform.pdf
norm_pdf = sps.norm.pdf
expon_pdf = sps.expon.pdf


def uniform(size=1, precision=30):
    if type(size) is int:
        binary_arr = 2.0 ** np.arange(-precision, 0)
        shape = (size, precision)
        bernoulli = coin(shape)
        shape = (size, 1)
        res = np.tile(binary_arr, shape)
        return np.sum(bernoulli * res, axis=1)
    elif type(size) is tuple:
        numbers = 2.0 ** np.arange(-precision, 0)
        shape = size + (precision,)
        bernoulli = coin(shape)
        shape = size + (1,)
        res = np.tile(numbers, shape)
        return np.sum(bernoulli * res, axis=len(size))
def plot_uniform_density(size=200):
    grid = np.linspace(-0.25, 1.25, 500)  # равномерная сетка от -0.25 до 1.25 из 500 точек
    plt.figure(figsize=(10, 5))
    x = uniform(size)

    plt.scatter(x=x, y=np.zeros(size), color='red', alpha=0.4, label='случайная величина')
    plt.hist(x, alpha=0.4, density=True, bins=10, label='Экспериментально вычисленная плотность')
    plt.plot(grid, uniform_pdf(grid), alpha=0.4, linewidth=5, label='Теоретически вычисленная плотность')

    plt.title('Равномерное распределение', fontsize=22)
    plt.xlabel('случайная величина', fontsize=16)
    plt.ylabel('Плотность', fontsize=16)

    plt.tick_params(axis='x', labelsize=15)
    plt.tick_params(axis='y', labelsize=15)

    plt.legend()
    return plt.gcf()

def plot_uniform_different_precision(size=100):
    plt.figure(figsize=(15, 9))
    plt.suptitle('Выборки для разных точностей', fontsize=20)

    for i, precision in enumerate([1, 2, 3, 5, 10, 30]):
        plt.subplot(3, 2, i + 1)

        plt.scatter(
           uniform(size, precision),
           np.zeros(size),
           alpha=0.4
        )

        plt.tick_params(axis='x', labelsize=15)
        plt.tick_params(axis='y', labelsize=15)

        plt.title('Precision = ' + str(precision), fontsize=15)
        plt.yticks(np.arange(-0.05, 0.1, step=0.1))
        if i < 4:
            plt.xticks(np.arange(0, 1, step=0.1))
        plt.xlabel('Значения выборки', fontsize=15)

    plt.subplots_adjust(hspace=0.6, wspace=0.4)
    plt.tight_layout()
    return plt.gcf()

def normal(size=1, loc=0, scale=1, precision=30):
    distribution1 = uniform(size, precision)
    distribution2 = uniform(size, precision)
    z1 = np.sqrt(-2 * np.log(distribution1)) * np.cos(2 * np.pi * distribution2)
    x = loc + z1 * scale
    return x

def plot_normal_density(size=200):
    grid = np.linspace(-3, 3, 500)  # равномерная сетка от -0.25 до 1.25 из 500 точек
    plt.figure(figsize=(10, 5))
    x = normal(size)

    plt.scatter(x=x, y=np.zeros(size), color='red', alpha=0.4, label='случайная величина')
    plt.hist(x, alpha=0.4, density=True, bins=10, label='Экспериментально вычисленная плотность')
    plt.plot(grid, norm_pdf(grid), alpha=0.4, linewidth=5, label='Теоретически вычисленная плотность')

    plt.title('Нормальное распределение', fontsize=22)
    plt.xlabel('случайная величина', fontsize=16)
    plt.ylabel('Плотность', fontsize=16)

    plt.tick_params(axis='x', labelsize=15)
    plt.tick_params(axis='y', labelsize=15)

    plt.legend()
    return plt.gcf()

def expon(size=1, lambd=1, precision=30):
    return -np.log(uniform(size, precision)) / lambd

def plot_expon_density(size=100):
    grid = np.linspace(-0.5, 5, 500)  # равномерная сетка от -0.25 до 1.25 из 500 точек
    plt.figure(figsize=(10, 5))
    x = expon(size)

    plt.scatter(x=x, y=np.zeros(size), color='red', alpha=0.4, label='случайная величина')
    plt.hist(x, alpha=0.4, density=True, bins=10, label='Экспериментально вычисленная плотность')
    plt.plot(grid, expon_pdf(grid), alpha=0.4, linewidth=5, label='Теоретически вычисленная плотность')

    plt.title('Экспонециальное распределение', fontsize=22)
    plt.xlabel('случайная величина', fontsize=16)
    plt.ylabel('Плотноть', fontsize=16)

    plt.tick_params(axis='x', labelsize=15)
    plt.tick_params(axis='y', labelsize=15)

    plt.legend()
    return plt.gcf()

