function startPing() {
    const target = document.getElementById('targetInput').value;
    const interval = document.getElementById('intervalSelect').value;

    fetch('/start', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        body: new URLSearchParams({
            'target': target,
            'interval': interval
        })
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);
    })
    .catch(error => {
        console.error('Error starting ping:', error);
    });
}

function fetchResults() {
    // 定期从后端获取PING结果并更新页面
     fetch('/results')
        .then(response => response.json()) // 解析响应的JSON数据
        .then(data => {
            // 更新页面显示PING结果
            updateResults(data);
        })
        .catch(error => {
            console.error('Error fetching results:', error);
        });
}

// 更新页面显示PING结果的函数
function updateResults(data) {
    // 找到用于显示结果的HTML元素
    const resultsElement = document.getElementById('results');

    // 清空原有内容
    resultsElement.innerHTML = '';

    // 遍历结果数据，并将每个结果显示在页面上
    data.forEach(result => {
        // 创建新的结果元素
        const resultElement = document.createElement('div');
        resultElement.textContent = result; // 设置结果文本内容

        // 将结果元素添加到结果容器中
        resultsElement.appendChild(resultElement);
    });

    // 如果结果为空，则添加一个空行元素
    if (data.length === 0) {
        const emptyLineElement = document.createElement('div');
        resultsElement.appendChild(emptyLineElement);
    }
}

// 定时调用fetchResults函数，每隔一段时间获取一次结果并更新页面
setInterval(fetchResults, 500); // 每隔0.5秒获取一次结果

function stopPing() {
    fetch('/stop', { method: 'POST' });
}