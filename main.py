from flask import Flask, request, jsonify
import schedule
import time
import sys

app = Flask(__name__)

# Route for /auth/login endpoint
@app.route('/v2/products/phoenix-duels/auth/login', methods=['POST'])
def login():
   # Return a response including:
   # - The current version: which is the same as in the code (to always return latest)
   # - A fake auth token (dummy_token)
   # - A super super fake expiry date (31th December 2099, but in UNIX epoch time format)
   # - A super fake signature and etc, kinda self-explanatory
   # Since the code doesn't attempt to further verify these, I was able to successfully
   # 'crack' the program.
    response = {
        'status': 'ok',
        'body': {
            'current_version': '1.5',
            'auth_token': 'dummy_token',
            'auth_token_expiry': 4102444799000,
            'grace_period_signature': 'yourassstinks',
            'grace_period_expiry': 4102444799000
        }
    }
    return jsonify(response), 200

@app.route('/v2/products/phoenix-duels/auth/renew', methods=['POST'])
def renew():
   # Same explanation as above, this time as a token renew request.
    response = {
        'status': 'ok',
        'body': {
            'current_version': '1.5',
            'auth_token': 'dummy_token',
            'auth_token_expiry': 4102444799000,
            'grace_period_signature': 'yourassstinks',
            'grace_period_expiry': 4102444799000
        }
    }
    return jsonify(response), 200

@app.route('/v2/products/phoenix-duels/auth/logout', methods=['POST'])
def logout():
   # The logout request doesn't require anything other than the 'status' which is always set to return 'ok'
    response = {
        'status': 'ok'
    }
    return jsonify(response), 200

def exit_program():
    print("Exiting program with error code 0.")
    sys.exit(0)

if __name__ == '__main__':
   # The program is discoverable with all addresses, on port 5000 (which doesn't require root)
    app.run(host='0.0.0.0', port=5000)

    # Schedule the exit at the 30th minute of every hour
    schedule.every().hour.at(":30").do(exit_program)

    while True:
        schedule.run_pending()
        time.sleep(1)
