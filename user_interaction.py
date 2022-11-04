### Main Application ###

# Imports
import fire
import data_manipulation as dm
import models as ml


# Ask user to import a data
def import_data():


# Make user to choose a column as answer('y') value
def define_answer_value():


# Apply data cleaning process
def apply_data_modification():
    

# Go through "choosing the right estimator" and choose appropriate ML model(s)
def choose_ml_model():


# Apply the selected ML model(s) and store trained model
def ml_execution():


# Visualize machine learning performance(s)
def visualization():


# Get together all functions above
def run():


# Run the application
if __name__ == "__main__":
    try:
        fire.Fire(run)
    except Exception as e:
        print(f"You have some error.\nError Code: {e}")