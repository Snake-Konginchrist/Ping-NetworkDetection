import subprocess


def ping(target):
    try:
        result = subprocess.run(["ping", target], capture_output=True, text=True, check=True)
        print("Ping result:")
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print("Error executing ping command:", e)


# 测试代码
ping("www.baidu.com")
