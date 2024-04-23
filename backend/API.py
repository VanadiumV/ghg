from infermedica_api import InfermedicaApi

# Replace 'your_app_id' and 'your_app_key' with your actual API credentials
api = InfermedicaApi(app_id='your_app_id', app_key='your_app_key')

# Provide the user's age, sex, and initial symptoms
age = 30
sex = 'male'  # or 'female'
initial_symptoms = [
    {'id': 's_98', 'choice_id': 'present'},  # Fever symptom ID
]

# Create a request with the user's data
request_data = {
    'sex': sex,
    'age': age,
    'evidence': initial_symptoms,
}

# Get the diagnosis based on the provided symptoms
response = api.diagnosis(request_data)

# Print out the list of possible conditions
for condition in response.conditions:
    print(f"Possible condition: {condition.common_name} ({condition.probability}% probability)")
