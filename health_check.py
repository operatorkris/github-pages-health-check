import requests

def check_website_status(url):
    print(f"Attempting to check the status of {url}...")
    try:
        response = requests.get(url, timeout=5)  # Set a timeout of 5 seconds
        print(f"Received response with status code: {response.status_code}")
        if response.status_code == 200:
            print(f"{url} is up! Status code: {response.status_code}")
        else:
            print(f"{url} might be down. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while trying to reach {url}. Error: {e}")

if __name__ == "__main__":
    website_url = "https://operatorkris.github.io"
    print("Starting website status check...")
    check_website_status(website_url)
    print("Finished website status check.")
