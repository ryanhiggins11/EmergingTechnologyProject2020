# Flask web microservice import.
from flask import Flask, request, render_template
import tensorflow as tf

# Create a new web app.
app = Flask(__name__)

# Setting a constant for the index page
INDEX = "index.html"

# Add route to the root ('/') location, that calls the "hello_world()" function.
@app.route('/', methods=["GET", "POST"])
def root():
    if request.method == "POST":
        # Setting a wind speed that we want to predict the power output for
        speed = request.form["speed"]
        # Casting wind_speed to a float from a string
        speed = [float(speed)]
        # Grabbing the saved wind turbine tensorflow model
        Output_Model = tf.keras.models.load_model('Output_Model')
        # Testing the accuracy of the predictions (using the "wind_speed" guess)
        model_prediction = Output_Model.predict(speed)
        return render_template(INDEX, prediction=model_prediction[0])
    return render_template(INDEX)