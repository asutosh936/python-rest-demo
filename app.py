from flask import Flask, jsonify, request
import logging

# Create a Flask application
app = Flask(__name__)

# Sample data to mimic a database
cars = [
    {"id": 1, "make": "Toyota", "model": "Camry", "year": 2020},
    {"id": 2, "make": "Honda", "model": "Civic", "year": 2021}
]

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


# Root endpoint
@app.route('/')
def home():
    logger.info('Handling root endpoint')
    return jsonify({"message": "Welcome to the Car API!"})


# Get all cars
@app.route('/cars', methods=['GET'])
def get_cars():
    logger.info('Handling Get All Cars endpoints %s', jsonify(cars))
    return jsonify(cars)


# Get a specific car by ID
@app.route('/cars/<int:car_id>', methods=['GET'])
def get_car(car_id):
    car = next((car for car in cars if car["id"] == car_id), None)
    if car:
        return jsonify(car)
    return jsonify({"error": "Car not found"}), 404


# Add a new car
@app.route('/cars', methods=['POST'])
def add_car():
    new_car = request.json
    cars.append(new_car)
    return jsonify(new_car), 201


# Update a car by ID
@app.route('/cars/<int:car_id>', methods=['PUT'])
def update_car(car_id):
    car = next((car for car in cars if car["id"] == car_id), None)
    if not car:
        return jsonify({"error": "Car not found"}), 404
    car.update(request.json)
    return jsonify(car)


# Delete a car by ID
@app.route('/cars/<int:car_id>', methods=['DELETE'])
def delete_car(car_id):
    global cars
    cars = [car for car in cars if car["id"] != car_id]
    return jsonify({"message": "Car deleted successfully"})


# Run the application
if __name__ == '__main__':
    app.run(debug=True, port=8001)
