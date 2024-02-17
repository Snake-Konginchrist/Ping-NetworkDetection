import datetime
import time

import pytz


def log_result(result):
    # 获取当前时间的 UTC 时间戳
    timestamp = time.time()
    utc_time = datetime.datetime.utcfromtimestamp(timestamp)

    # 将 UTC 时间转换为北京时间
    beijing_timezone = pytz.timezone('Asia/Shanghai')
    beijing_time = utc_time.replace(tzinfo=pytz.utc).astimezone(beijing_timezone)
    formatted_timestamp = beijing_time.strftime('%Y-%m-%d %H:%M:%S')

    # formatted_timestamp = utc_time.strftime('%Y-%m-%d %H:%M:%S')

    # 将结果写入日志文件，附带时间戳
    result_with_timestamp = f"{formatted_timestamp}: {result.strip()}"
    with open('results.txt', 'a') as file:
        file.write(result_with_timestamp + '\n\n')


def get_results():
    results = []
    with open('results.txt', 'r') as file:
        for line in file:
            results.append(line.rstrip('\n'))
    return results
