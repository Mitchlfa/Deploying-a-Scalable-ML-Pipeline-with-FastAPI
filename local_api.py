import requests

r = requests.get("http://127.0.0.1:8000/")
print(f"GET Status Code: {r.status_code}")
print(f"Welcome Message: {r.json()}")

# Data with correct field names that match the aliases in main.py
data = {
    "age": 37,
    "workclass": "Private",
    "fnlgt": 178356,
    "education": "HS-grad",
    "education-num": 10,  
    "marital-status": "Married-civ-spouse",  # Match the alias defined in main.py
    "occupation": "Prof-specialty",
    "relationship": "Husband",
    "race": "White",
    "sex": "Male",
    "capital-gain": 0,  # Match the alias defined in main.py
    "capital-loss": 0,  # Match the alias defined in main.py
    "hours-per-week": 40,  # Match the alias defined in main.py
    "native-country": "United-States",  # Match the alias defined in main.py
}

# Send a POST request with the data above
r = requests.post("http://127.0.0.1:8000/data/", json=data)

# Print the status code
print(f"POST Status Code: {r.status_code}")

# Print the result from the POST request
print(f"Result: {r.json()}")