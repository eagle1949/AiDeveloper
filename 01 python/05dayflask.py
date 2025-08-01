# 构建一个简单的 API 服务（基于Flask）

from flask import Flask, jsonify, request;

app = Flask(__name__)
users = [];

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.json
    users.append(data)
    return jsonify({"msg": "用户添加成功"})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)