import os
import sys
import json
import pyperclip

json_object = {}


def search(search_string):
    stream = os.popen(f"bw list items --search {search_string} --pretty")
    return stream.read()


def iterate_json():
    global json_object
    json_object = json.loads(search_result_raw)
    for idx, entry in enumerate(json_object):
        print(f"{idx}. {entry['name']} - {entry['login']['username']}")


def get_user_input():
    entry_number = 0
    input_text = input('Choose: ')
    try:
        entry_number = int(input_text)
    except ValueError:
        print("That's not a valid selection. Exiting...")
        exit(-1)

    return json_object[entry_number]


def copy_to_clipboard():
    print('Copying password to clipboard')
    pyperclip.copy(selected_entry['login']['password'])


if __name__ == '__main__':
    os.environ["NODE_NO_WARNINGS"] = "1"
    search_result_raw = search(sys.argv[1])
    iterate_json()
    selected_entry = get_user_input()
    copy_to_clipboard()
