import os
import bcrypt
import jwt
import datetime
from flask import Blueprint, request, jsonify, current_app
from server import mongo
from bson.objectid import ObjectId

auth_bp = Blueprint('auth_routes', __name__)

# get the users collection
def get_users_collection():
    return mongo.db.users

@auth_bp.route('/register', methods=['POST'])
def register():
    try:
        data = request.get_json()
        
        email = data.get('email')
        password = data.get('password')

        if not email or not password:
            return jsonify({"error": "Email and password are required"}), 400

        users_collection = get_users_collection()
        if users_collection.find_one({"email": email}):
            return jsonify({"error": "Email already registered"}), 409

        # Hash the password
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

        username = data.get('username')
        if not username:
            username = email.split('@')[0] # Default username from email

        # Create new user document
        new_user = {
            "email": email,
            "hashed_password": hashed_password,
            "username": username,
            "gender": data.get('gender') or None,
            "dob": data.get('dob') or None,
            "phone": data.get('phone') or None,
            "created_at": datetime.datetime.now(datetime.timezone.utc)
        }

        result = users_collection.insert_one(new_user)

        if result.inserted_id:
            return jsonify({"message": "User registered successfully"}), 201
        else:
            return jsonify({"error": "Failed to register user"}), 500

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@auth_bp.route('/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')

        if not email or not password:
            return jsonify({"error": "Email and password are required"}), 400

        # Find user
        users_collection = get_users_collection()
        user = users_collection.find_one({"email": email})

        if not user:
            return jsonify({"error": "Invalid credentials"}), 401
        
        user_password_bytes = password.encode('utf-8')
        stored_hash_bytes = user['hashed_password'].encode('utf-8')

        if bcrypt.checkpw(user_password_bytes, stored_hash_bytes):
            secret_key = current_app.config['JWT_SECRET_KEY']
            
            token = jwt.encode({
                'user_id': str(user['_id']),
                'email': user['email'],
                'exp': datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(days=1)
            }, secret_key, algorithm="HS256")

            return jsonify({"message": "Login successful", "token": token}), 200
        else:
            return jsonify({"error": "Invalid credentials"}), 401

    except Exception as e:
        return jsonify({"error": str(e)}), 500