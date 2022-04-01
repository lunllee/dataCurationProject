import pandas as pd
import pathlib
import os


def data_path(dataset_id, distribution_id):
    home_path = os.getcwd()
    return os.path.join(home_path, 'data', dataset_id, distribution_id)


def main():
    home = data_path('8fd2d3e0-352a-11ec-8bab-6194bb3a1754', 'cf1fbe80-352c-11ec-8bab-6194bb3a1754')
    print(home)


if __name__ == '__main__':
    main()
