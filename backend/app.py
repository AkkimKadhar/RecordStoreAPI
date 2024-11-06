from flask import Flask, request, jsonify
from pymongo import MongoClient
from bson import ObjectId
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"/records": {"origins": "*"},r"/records/*": {"origins": "*"}},support_credentials=True, methods=['GET', 'POST', 'PUT', 'DELETE'])
app.config['CORS_HEADERS'] = 'Content-Type'


client = MongoClient('mongodb://localhost:27017/')
db = client['mydatabase']
collection = db['records']


def record_serializer(record):
   return {
        'id': str(record['_id']),
        'name': record.get('name', 'Unknown'),
        'email': record.get('email', 'Unknown'),
        'age': record.get('age', 0),
        'role': record.get('role', 'Unknown')
    }


@app.route('/records', methods=['GET'])
def get_records():
    records = list(collection.find())
    return jsonify([record_serializer(record) for record in records])


@app.route('/records', methods=['POST'])
def add_record():
    data = request.json
    new_record = {
        'name': data.get('name', ''),
        'email': data.get('email', ''),
        'age': data.get('age', 0),
        'role': data.get('role', 'Unknown')
    }
    result = collection.insert_one(new_record)
    return jsonify({'id': str(result.inserted_id)}), 201


@app.route('/records/<id>', methods=['PUT'])
def update_record(id):
    data = request.json
    updated_record = {
        'name': data.get('name', ''),
        'email': data.get('email', ''),
        'age': data.get('age', 0),
        'role': data.get('role', 'Unknown')
    }
    result = collection.update_one({'_id': ObjectId(id)}, {'$set': updated_record})

    if result.matched_count == 0:
        return jsonify({'error': 'Record not found'}), 404

    return jsonify({'msg': 'Record updated successfully'})


@app.route('/records/<id>', methods=['DELETE'])
def delete_record(id):
    result = collection.delete_one({'_id': ObjectId(id)})

    if result.deleted_count == 0:
        return jsonify({'error': 'Record not found'}), 404

    return jsonify({'msg': 'Record deleted successfully'})

if __name__ == '__main__':
    app.run(debug=True)
