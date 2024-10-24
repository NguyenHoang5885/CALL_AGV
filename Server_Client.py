#code flask
from flask import Flask, request, jsonify

# Khởi tạo ứng dụng Flask
app = Flask(__name__)

# Định nghĩa route với phương thức POST
@app.route('/items', methods=['POST'])
def create_item():
    try:
    # Lấy dữ liệu JSON từ request body
        data = request.get_json()
        print(data)
        # Xử lý dữ liệu (ví dụ lưu vào database hoặc thực hiện tính toán)
        item_name = data.get('name')
        item_Value = data.get('Value')

        # Trả về dữ liệu dưới dạng JSON
        response = {
            'message': 'Item created successfully',
            'item': {
                'name': item_name, 
                'Value': item_Value
            }
        }
        return jsonify(response), 200  # Trả về HTTP status 201 (Created)
    except Exception as e :
        print(e)
        response = {
            'message': e
        }
        return jsonify(response), 400 

@app.route('/api/hello', methods=['GET'])
def hello():
    try:
        response = {"a" : "123"}
        return jsonify(response), 200  # Trả về HTTP status 201 (Created)
    except Exception as e :
        print(e)
        response = {
            'message': e
        }
        return jsonify(response), 400
if __name__ == '__main__':
    # Chạy ứng dụng Flask trên cổng 5000
    app.run(debug=True, host="0.0.0.0", port=5000)