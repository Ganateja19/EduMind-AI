import requests

url = 'http://127.0.0.1:5000/predictdata'
data = {
    'gender': 'female',
    'ethnicity': 'group B',
    'parental_level_of_education': 'bachelor\'s degree',
    'lunch': 'standard',
    'test_preparation_course': 'none',
    'reading_score': 72,
    'writing_score': 74
}

try:
    response = requests.post(url, data=data)
    print(f"Status Code: {response.status_code}")
    with open("verification_result.txt", "w", encoding="utf-8") as f:
        f.write(response.text)

    if response.status_code == 200:
        if "Predicted Math Score" in response.text:
            print("Verification SUCCESS: 'Predicted Math Score' found.")
        else:
            print("Verification FAILED: 'Predicted Math Score' NOT found.")
    else:
        print(f"Verification FAILED: Status {response.status_code}")
except Exception as e:
    print(f"Verification ERROR: {e}")
