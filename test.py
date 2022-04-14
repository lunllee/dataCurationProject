import pandas as pd
import os
import json
from minio import Minio
from minio.error import InvalidResponseError
import requests
from config.env_config import args

env = 'development' if 'APP_ENV' not in os.environ else os.environ['APP_ENV']
args = args[env]


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
    output_file_name = r'c_' + args['input1']['fileName']
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


# MinIO에 업로드 하기 위한 option
options_minio_data = {
    'url': 'http://' + args['output1']['baseUrl'] + '/api/v1/devops/development/environment/get',
    'headers': {
        'accept': 'application/json',
        'Authorization': 'Bearer ' + args['output1']['accessToken']
    },
    'params': {
        'id': args['output1']['storageId']
    }
}


# MinIO 연결
def minio_connection(options) -> dict:
    res = requests.get(options['url'],
                       headers=options['headers'],
                       params=options['params'])
    if res.status_code == 401:
        raise Exception('There is no valid authentication token')
    elif res.status_code != 200:
        raise Exception('Cannot access API')
    storage = json.loads(res.content.decode('ascii'))
    connection = {
        'endPoint': list(filter(lambda x: x['servicePort'] == 9000, storage['sandbox']['ingress']))[0]['host'],
        'port': list(filter(lambda x: x['servicePort'] == 9000, storage['sandbox']['ingress']))[0]['clusterAccessPort'],
        'useSSL': False,
        'accessKey': list(
            filter(lambda x: x['name'] == 'MINIO_ACCESS_KEY', storage['config']['environments'])
        )[0]['value'],
        'secretKey': list(
            filter(lambda x: x['name'] == 'MINIO_SECRET_KEY', storage['config']['environments'])
        )[0]['value']
    }
    return connection


# MinIO file 업로드
def upload_data_file(minio_client, bucket_name, object_name, file_path):
    minio_client.fput_object(bucket_name, object_name, file_path)
    print('The file uploads successfully.')


# sodas+ 호출 option
def sodas_option(url, access_token, params) -> dict:
    return {
        'url': url,
        'headers': {
            'accept': 'application/json',
            'Authorization': 'Bearer ' + access_token
        },
        'params': params
    }


# distribution 파일명 받기
def found_distribution_file_name(options) -> str:
    res = requests.get(options['url'],
                       headers=options['headers'],
                       params=options['params'])
    if res.status_code == 400:
        raise Exception('The input value is invalid')
    elif res.status_code == 401:
        raise Exception('There is no valid authentication token')
    elif res.status_code != 200:
        raise Exception('Cannot access API')
    result_list = json.loads(res.content.decode('ascii'))

    file_name = list(
        filter(lambda x: x['id'] == args['input1']['distributionId'], result_list['results'])
    )[0]['fileName']
    return file_name


# distribution 파일을 파일 명을 포함한 path 를 받아서 저장
def download_data_file(filename_path, options):
    with open(filename_path, "wb") as file:
        res = requests.get(options['url'],
                           headers=options['headers'],
                           params=options['params'])
        file.write(res.content)
        print('The file downloads successfully.')


def main():
    try:
        list_option = sodas_option(
            'http://' + args['input1']['baseUrl'] + '/api/v1/data-management/distribution/list',
            args['input1']['accessToken'],
            {
                'datasetId': args['input1']['datasetId'],
                'offset': 0,
                'limit': 10,
                'sort': 'issued',
                'ordered': 'ASC'
            }
        )
        distribution_file_name = found_distribution_file_name(list_option)
        args['input1']['fileName'] = distribution_file_name

        file_path = data_path(args['input1']['datasetId'], args['input1']['distributionId'])
        filename_path = os.path.join(file_path, args['input1']['fileName'])
        print(filename_path)

        download_option = sodas_option(
            'http://' + args['input1']['baseUrl'] + '/api/v1/data-management/distribution/download',
            args['input1']['accessToken'],
            {'id': args['input1']['distributionId']}
        )
        download_data_file(filename_path, download_option)

        if os.path.isfile(filename_path):
            read_df = read_file(filename_path)
            print(read_df.columns.tolist())

            working_set = algorithm_work(args['input1']['params'])

            convert_df = read_df[working_set]
            print(read_df[working_set])
            output_file(convert_df, file_path)

            connection_info = minio_connection(options_minio_data)
            minio_client = Minio(endpoint=connection_info['endPoint'] + ':' + str(connection_info['port']),
                                 secure=connection_info['useSSL'],
                                 access_key=connection_info['accessKey'],
                                 secret_key=connection_info['secretKey'])

            upload_data_file(minio_client, args['output1']['bucketName'], args['output1']['objectName'], filename_path)
        else:
            print("file not found")

    except InvalidResponseError as err:
        print(err)


if __name__ == '__main__':
    main()
