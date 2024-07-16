import requests


def get_posts():
    # Define the API endpoint URL
    url = 'https://sunwater.freshservice.com/api/v2/tickets/88040/notes'

    try:
        # Make a GET request to the API endpoint using requests.get()
        response = requests.get(url)
        print(response)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            posts = response.json()
            return posts
        else:
            print('Error:', response.status_code)
            return None
    except ValueError:
        print("error")