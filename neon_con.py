from flask import Flask, jsonify, request
import mysql.connector

app = Flask(__name__)

# ✅ MySQL Database Configuration
db_config = {
    "host": "127.0.0.1",  # Your MySQL server (localhost)
    "user": "root",        # Your MySQL username
    "password": "a2F2aQ==",        # Your MySQL password
    "database": "rewards_db",  # Your database name
    "port": 3306           # Default MySQL port
}

# ✅ API Endpoint to fetch user rewards by name
@app.route("/rewards", methods=["GET"])
def get_user_rewards():
    username = request.args.get("username")  # Get the username from the query

    if not username:
        return jsonify({"status": "error", "message": "Username is required"}), 400

    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)

        cursor.execute("SELECT name, reward_points, email FROM user WHERE name = %s", (username,))
        user = cursor.fetchone()

        conn.close()

        if user:
            return jsonify({"status": "success", "user": user})
        else:
            return jsonify({"status": "error", "message": "User not found"}), 404

    except mysql.connector.Error as err:
        return jsonify({"status": "error", "message": f"Database error: {err}"}), 500
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

# ✅ Run the server
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
