import requests

API_URL = "https://jsonplaceholder.typicode.com/posts"

def get_post(post_id):
    response = requests.get(f"{API_URL}/{post_id}")
    if response.status_code == 200:
        print("✅ GET Post:", response.json())
    else:
        print(f"❌ GET failed with status code {response.status_code}")

def create_post():
    data = {
        "title": "foo",
        "body": "bar",
        "userId": 1
    }
    response = requests.post(API_URL, json=data)
    if response.status_code == 201:
        print("✅ POST Created:", response.json())
        return response.json().get("id")
    else:
        print(f"❌ POST failed with status code {response.status_code}")
        return None

def update_post(post_id):
    data = {
        "id": post_id,
        "title": "foo updated",
        "body": "bar updated",
        "userId": 1
    }
    response = requests.put(f"{API_URL}/{post_id}", json=data)
    if response.status_code == 200:
        print("✅ PUT Updated:", response.json())
    else:
        print(f"❌ PUT failed with status code {response.status_code}")

def delete_post(post_id):
    response = requests.delete(f"{API_URL}/{post_id}")
    if response.status_code == 200:
        print(f"✅ DELETE Post {post_id} successful")
    else:
        print(f"❌ DELETE failed with status code {response.status_code}")

if __name__ == "__main__":
    get_post(1)
    new_post_id = create_post()
    if new_post_id:
        update_post(new_post_id)
        delete_post(new_post_id)
