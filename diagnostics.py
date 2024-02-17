import subprocess
import time
from logger import log_result


def ping(target, interval, is_pinging):
    print("diagnostics里面的is_ping是", is_pinging)
    while is_pinging:
        try:
            print("Ping Target", target)
            result = subprocess.run(["ping", "-c", "4", target], capture_output=True, text=True)  # Linux系统
            # result = subprocess.run(["ping", "-n", "4", target], capture_output=True, text=True)  # Windows系统
            print("Ping result:")
            print(result.stdout)
            log_result(result.stdout)
            time.sleep(int(interval))
        except subprocess.SubprocessError as e:
            print("Error executing ping command:", e)
    print("PING探测已停止")
