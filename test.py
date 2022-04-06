import pandas as pd
import os
import json
from minio import Minio

os.environ["FILE_NAME"] = r'covid.csv'
os.environ["DATASET_ID"] = r'8fd2d3e0-352a-11ec-8bab-6194bb3a1754'
os.environ["DISTRIBUTION_ID"] = r'cf1fbe80-352c-11ec-8bab-6194bb3a1754'
os.environ["INPUTS"] = r'{"select_column": ["Date_reported", "Country_code", "Country", "New_deaths"]}'


# home path와 parameter를 path값으로 join
def data_path(dataset_id, distribution_id):
    home_path = os.getcwd()
    return os.path.join(home_path, 'data', dataset_id, distribution_id)


# flie을 읽어서 DataFrame으로 변환
def read_file(path):
    path_split = os.path.splitext(path)
    extension = {".csv": "csv"}.get(path_split[1], "unknown")
    df = pd.DataFrame()

    if extension == "csv":
        df = pd.read_csv(path)

    return df


# pandas dataframe과 filePath를 받아서 파일명에 'c_'를 붙인 뒤 저장
def output_file(dataframe, file_path):
    output_file_name = r'c_' + os.environ.get("FILE_NAME")
    output_file_path = os.path.join(file_path, output_file_name)
    dataframe.to_csv(output_file_path, index=False)


def main():
    file_path = data_path(os.environ.get("DATASET_ID"), os.environ.get("DISTRIBUTION_ID"))
    filename_path = os.path.join(file_path, os.environ.get("FILE_NAME"))
    print(filename_path)

    if os.path.isfile(filename_path):
        read_df = read_file(filename_path)
        print(read_df.columns.tolist())

        input_json = json.loads(os.environ.get("INPUTS"))
        print(input_json['select_column'])

        convert_df = read_df[input_json['select_column']]
        print(read_df[input_json['select_column']])
        output_file(convert_df, file_path)
    else:
        print("file not found")


if __name__ == '__main__':
    main()
