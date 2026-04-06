import webbrowser

import requests

BASE_URL = "https://api.watchmode.com/v1"

API_KEY = "fpzkqlGygYVA2zuTckH6wshM4Wj951vdJNVMtkCJ"

watch_types_dictionary = {1: "movie", 2: "tv"}


# User input and validation functions
# original name was ask_for, changed to ask_for_int to match starter code
def ask_for(data_type, prompt, low, high):
    while True:
        try:
            x = data_type(input(prompt))
            if x < low or x > high:
                print(f"Must print a value between {low} and {high}")
            else:
                return x
        except ValueError:
            print("Invalid value, try again")


# valid values not being used, but could be to check for specific strings
def ask_for_str(prompt, valid_values):
    if valid_values is not None:
        lower_valid_values = {value.lower() for value in valid_values}
    while True:
        x = input(prompt)
        if valid_values is None:
            break
        if x.lower() in lower_valid_values:
            break
        else:
            print("You must enter one of the following", valid_values)
    return x


def search_by_title(title, types):
    print("\nNow sending request to WatchMode for", title, ". . . ")
    search_field = "name"
    url = f"{BASE_URL}/search/?apiKey={API_KEY}&search_value={title}&search_field={search_field}&types={types}"
    response = requests.get(url)
    response.raise_for_status()  # if don't get back 2xx code

    json_results = response.json()
    print("\nSuccess!  Received JSON results back: ")
    print(json_results)

    # get the value for key 'title_results'
    title_results = json_results["title_results"]
    # get the 0th element
    zeroth_element = title_results[0]
    # get the value for key 'id'
    title_results_id = zeroth_element["id"]
    # return the value
    return title_results_id


def display_details(item_id):
    print("\nNow getting more details from WatchMode based on id . . . ")
    url = f"{BASE_URL}/title/{item_id}/details/?apiKey={API_KEY}"
    response = requests.get(url)
    response.raise_for_status()  # if donâ€™t get back 2xx code

    # print the whole JSON
    json_results = response.json()
    print("\nSuccess!  Received JSON results back: \n")
    for key, value in json_results.items():
        print(f"{key}:  {value}")

    # TODO - get and print the 'user_rating'
    print(
        f"\nThe user rating for {json_results['title']} is {json_results['user_rating']}."
    )
    # TODO - get and print the 'trailer'

    input("\nPress the Enter key to now open in a browser: ")

    # TODO - open the trailer in a browser
    trailer_url = json_results["trailer"]
    webbrowser.open(trailer_url)


def main():

    # ask user for the type
    x = ask_for(int, "\nEnter 1 to lookup a Movie or 2 to lookup a TV Show: ", 1, 2)
    movie_or_tv_show = watch_types_dictionary.get(x)

    # ask the user for the title
    title = input("Enter the title: ")

    # search by a title
    item_id = search_by_title(title, movie_or_tv_show)

    print("\nWatchMode's unique id for this is", item_id)

    # display the details
    display_details(item_id)


main()
