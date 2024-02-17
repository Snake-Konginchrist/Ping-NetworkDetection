from flask import Flask, render_template, jsonify, request
import threading
import diagnostics
import logger

app = Flask(__name__, static_folder='static')

# 用于控制探测任务的标志
is_pinging = False


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/start', methods=['POST'])
def start_ping():
    global is_pinging
    if not is_pinging:
        is_pinging = True
        target = request.form['target']
        interval = request.form['interval']
        # 在调用 ping 函数时传递 is_pinging 参数
        threading.Thread(target=diagnostics.ping, args=(target, interval, is_pinging)).start()
        return jsonify({"message": "PING探测已开始"})
    else:
        return jsonify({"message": "PING探测已在进行中"})


@app.route('/stop', methods=['POST'])
def stop_ping():
    global is_pinging
    is_pinging = False
    return jsonify({"message": "PING探测已停止"})


@app.route('/results', methods=['GET'])
def results():
    return jsonify(logger.get_results())


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
