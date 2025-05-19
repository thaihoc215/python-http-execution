import base64
import uuid

from http_client import async_request


async def get_by_query_param():
    url = "http://localhost:8080/api/breeds/search"
    params = {"id": "abys", "name": "Abyssinian"}
    print(
        f"Performing async GET request with query params to {url}... (params: {params})"
    )
    await async_request(url=url, method="GET", params=params)


async def post_body_json():
    url = "http://localhost:8080/api/breeds"
    headers = {"Content-Type": "application/json"}
    body = {
        "id": str(uuid.uuid4()),
        "name": "Bengal",
        "origin": "United States",
        "description": "The Bengal is a domestic cat breed developed to look like exotic jungle cats.",
        "life_span": "12 - 16",
        "temperament": "Alert, Agile, Energetic, Demanding, Intelligent",
    }
    print(f"Performing async POST request with JSON body to {url}...")
    await async_request(
        url=url, method="POST", headers=headers, body=body, content_type="json"
    )


async def post_body_form_data():
    url = "http://localhost:8080/api/breeds/form"
    # headers = {"Content-Type": "multipart/form-data"}
    headers = {}
    # To send multipart/form-data, use 'files' param for all fields (even text fields)
    files = [
        ("id", (None, "beng")),
        ("name", (None, "Bengal")),
        ("origin", (None, "United States")),
        ("description", (None, "The Bengal is a domestic cat breed developed to look like exotic jungle cats.")),
        ("life_span", (None, "12 - 16")),
        ("temperament", (None, "Alert, Agile, Energetic, Demanding, Intelligent")),
    ]
    print(f"Performing async POST request with multipart/form-data body to {url}...")
    await async_request(
        url=url, method="POST", headers=headers, files=files
    )


async def post_body_raw():
    url = "http://localhost:8080/api/breeds/raw"
    headers = {"Content-Type": "text/plain"}
    body = '{"name":"Bengal","description":"A spotted breed","intelligence":5}'
    print(f"Performing async POST request with raw text body to {url}...")
    await async_request(
        url=url, method="POST", headers=headers, body=body, content_type="raw"
    )


async def post_form_data_file():
    url = "http://localhost:8080/api/breeds/aege/images"
    file_path = "/Users/hocha/Desktop/Screenshot 2025-03-26 at 19.04.16.png"
    field_name = "file"
    headers = {"accept": "application/json"}
    files = {field_name: open(file_path, "rb")}
    try:
        print(
            f"Performing async POST request with file upload (multipart/form-data) to {url}..."
        )
        await async_request(url=url, method="POST", headers=headers, files=files)
    finally:
        files[field_name].close()

async def post_form_data_file_using_param():
    url = "http://localhost:8080/api/breeds/aege/images"
    headers = {"accept": "application/json"}
    file_path = "/Users/hocha/Desktop/Screenshot 2025-03-26 at 19.04.16.png"
    # 'files' can mix file uploads and regular text fields
    params = [
        ("file", (open(file_path, "rb"))),
        # ("file", ("Screenshot.png", open(file_path, "rb"), "image/png")),
    ]
    try:
        print(f"Performing async POST request with mixed file and text form-data to {url}...")
        await async_request(url=url, method="POST", headers=headers, files=params)
    finally:
        # # Close the file after upload
        # for f in params:
        #     if hasattr(f[1][1], "close"):
        #         f[1][1].close()
        # Close the file after upload
        for f in params:
            file_obj = f[1]
            if hasattr(file_obj, "close"):
                file_obj.close()

async def post_form_data_with_file_and_text():
    url = "http://localhost:8080/api/breeds/mix"
    headers = {"accept": "application/json"}
    file_path = "/Users/hocha/Desktop/Screenshot 2025-03-26 at 19.04.16.png"
    # 'files' can mix file uploads and regular text fields
    files = [
        ("id", (None, "beng")),
        ("name", (None, "Bengal")),
        ("origin", (None, "United States")),
        ("description", (None, "The Bengal is a domestic cat breed developed to look like exotic jungle cats.")),
        ("life_span", (None, "12 - 16")),
        ("temperament", (None, "Alert, Agile, Energetic, Demanding, Intelligent")),
        ("image", ("Screenshot.png", open(file_path, "rb"), "image/png")),
    ]
    try:
        print(f"Performing async POST request with mixed file and text form-data to {url}...")
        await async_request(url=url, method="POST", headers=headers, files=files)
    finally:
        # Close the file after upload
        for f in files:
            if hasattr(f[1][1], "close"):
                f[1][1].close()
    
async def put_body_json():
    url = "http://localhost:8080/api/breeds/abys"
    headers = {"Content-Type": "application/json"}
    body = {
        "name": "abys Supreme",
        "weight": {
            "imperial": "8 - 12",
            "metric": "4 - 5"
        }
    }
    print(f"Performing async PUT request with JSON body to {url}...")
    await async_request(
        url=url, method="PUT", headers=headers, body=body, content_type="json"
    )

async def delete_by_id():
    url = "http://localhost:8080/api/breeds/aege"
    print(f"Performing async DELETE request to {url}...")
    await async_request(url=url, method="DELETE")
    
async def get_with_basic_auth():
    url = "http://localhost:8080/api/breeds"
    headers = {
        "accept": "application/json",
        "Authorization": "Basic dXNlcjpwYXNzd29yZA=="
    }
    print(f"Performing async GET request with Basic Auth to {url}...")
    await async_request(url=url, method="GET", headers=headers)
    
async def get_with_bearer_token():
    url = "http://localhost:8080/api/breeds"
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer abcdefgh"
    }
    print(f"Performing async GET request with Bearer token to {url}...")
    await async_request(url=url, method="GET", headers=headers)
    
async def get_with_api_key():
    url = "http://localhost:8080/api/breeds"
    headers = {
        "accept": "application/json",
        "api-key": "valuepass"
    }
    print(f"Performing async GET request with API Key to {url}...")
    await async_request(url=url, method="GET", headers=headers)
    
async def get_secure_breeds():
    url = "http://localhost:8080/api/secure/breeds"
    user = "user"
    password = "password"
    token = base64.b64encode(f"{user}:{password}".encode()).decode()
    headers = {
        "accept": "application/json",
        "Authorization": f"Basic {token}"
    }
    print(f"Performing async GET request with Basic Auth (curl -u) to {url}...")
    await async_request(url=url, method="GET", headers=headers)