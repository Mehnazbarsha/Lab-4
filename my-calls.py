import httpx

url = "https://fuzzy-doodle-v66v776jv4g3wp4g-5000.app.github.dev/"

response = httpx.get(url)
print(response.status_code)
print(response)

response = httpx.get(url)
print(response.status_code)
print(response.text)

mydata = {
    "text": "Hello Mehnaz!",
    "param2": "Making a POST request",
    "body": "my own value"
}

response = httpx.post(url + "echo", data=mydata)
print(response.status_code)
print(response.text)

print("\n=== Testing Factor Endpoint ===\n")

print("Testing factor with number=12 (GET):")
response = httpx.get(url + "factor?number=12")
print(f"Status: {response.status_code}")
print(f"Response: {response.json()}")

print("\nTesting factor with number=12 (POST):")
response = httpx.post(url + "factor", data={"number": "12"})
print(f"Status: {response.status_code}")
print(f"Response: {response.json()}")

print("\nTesting factor with prime number=13:")
response = httpx.get(url + "factor?number=13")
print(f"Status: {response.status_code}")
print(f"Response: {response.json()}")

print("\nTesting factor with number=360:")
response = httpx.get(url + "factor?number=360")
print(f"Status: {response.status_code}")
print(f"Response: {response.json()}")

print("\nTesting factor with number=1:")
response = httpx.get(url + "factor?number=1")
print(f"Status: {response.status_code}")
print(f"Response: {response.json()}")

print("\nTesting error handling - missing parameter:")
response = httpx.get(url + "factor")
print(f"Status: {response.status_code}")
print(f"Response: {response.json()}")

print("\nTesting error handling - invalid number:")
response = httpx.get(url + "factor?number=abc")
print(f"Status: {response.status_code}")
print(f"Response: {response.json()}")