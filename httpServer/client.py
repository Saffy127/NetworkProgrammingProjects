import requests
import json

BASE_URL = 'http://localhost:8000'

def get_users():
    try:
        response = requests.get(BASE_URL)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("GET Response:", response.json())
    except requests.exceptions.RequestException as e:
        print(f"GET request failed: {e}")

def add_user():
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    try:
        response = requests.post(BASE_URL, json={"name": name, "age": age})
        response.raise_for_status()
        print("POST Response:", response.json())
    except requests.exceptions.RequestException as e:
        print(f"POST request failed: {e}")

def update_user():
    user_id = int(input("Enter user ID to update: "))
    name = input("Enter new name (leave blank to skip): ")
    age = input("Enter new age (leave blank to skip): ")
    try:
        data = {"id": user_id}
        if name:
            data["name"] = name
        if age:
            data["age"] = int(age)
        response = requests.put(BASE_URL, json=data)
        response.raise_for_status()
        print("PUT Response:", response.json())
    except requests.exceptions.RequestException as e:
        print(f"PUT request failed: {e}")

def delete_user():
    user_id = int(input("Enter user ID to delete: "))
    try:
        response = requests.delete(BASE_URL, json={"id": user_id})
        response.raise_for_status()
        print("DELETE Response:", response.json())
    except requests.exceptions.RequestException as e:
        print(f"DELETE request failed: {e}")

def main():
    while True:
        print("\nMenu:")
        print("1. Get all users")
        print("2. Add a user")
        print("3. Update a user")
        print("4. Delete a user")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            get_users()
        elif choice == '2':
            add_user()
        elif choice == '3':
            update_user()
        elif choice == '4':
            delete_user()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
