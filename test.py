import pandas as pd
import os
import json
from minio import Minio
import requests
from config.env_config import args

env = 'development' if 'APP_ENV' not in os.environ else os.environ['APP_ENV']
args = args[env]
print(args['input1'])


# home path 와 parameter 를 path 값으로 join
def data_path(dataset_id, distribution_id) -> str:
    home_path = os.getcwd()

    return os.path.join(home_path, 'data', dataset_id, distribution_id)


# 파일을 읽어서 DataFrame 으로 변환
def read_file(path) -> pd.core.frame.DataFrame:
    path_split = os.path.splitext(path)
    extension = {".csv": "csv"}.get(path_split[1], "unknown")
    df = pd.DataFrame()

    if extension == "csv":
        df = pd.read_csv(path)

    return df


# pandas dataframe 과 filePath 를 받아서 파일명 에 'c_'를 붙인 뒤 저장
def output_file(dataframe, file_path):
    output_file_name = r'c_' + args['input1']['file_name']
    output_file_path = os.path.join(file_path, output_file_name)
    dataframe.to_csv(output_file_path, index=False)


# test algorithm 작업
def algorithm_work(params) -> list:
    params_list = params[0]
    # sum_list = list(filter(lambda x: x['command'] == 'sum', params_list))

    params_list.sort(key=lambda x: x['order'])

    cp_object = filter(lambda x: x['command'] == 'cp', params_list)
    column_list = list(map(lambda x: x['selectedColumn'][0], cp_object))

    return column_list


def main():
    # file_path = data_path(os.environ.get("DATASET_ID"), os.environ.get("DISTRIBUTION_ID"))
    file_path = data_path(args['input1']['dataset_id'], args['input1']['distribution_id'])
    filename_path = os.path.join(file_path, args['input1']['file_name'])
    print(filename_path)

    if os.path.isfile(filename_path):
        read_df = read_file(filename_path)
        print(read_df.columns.tolist())

        working_set = algorithm_work(args['input1']['params'])

        convert_df = read_df[working_set]
        print(read_df[working_set])
        output_file(convert_df, file_path)
    else:
        print("file not found")


if __name__ == '__main__':
    main()
