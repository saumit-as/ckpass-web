import requests
import hashlib
import sys


def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(
            f"Error fetching {res.status_code} check API and try again.")
    return res


def get_password_leaks_count(hashes, hashes_to_check):
    # recived response from the API will be in a list[remaining characters that needed to be checked : count of times the hash found]
    recived_hash = (line.split(':') for line in hashes.text.splitlines())
    for h, count in recived_hash:
        # spliting hash and count recived from the api
        if h == hashes_to_check:

            return count


def pwned_api_check(password):

    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    # hashing the password
    first_5_char, tail = sha1password[:5], sha1password[5:]
    # spliting the password into a tuple(first five characters and the remaining characters)
    response = request_api_data(first_5_char)
    # requesting Api with first five characters

    return get_password_leaks_count(response, tail)
    # reciving response and getting count


def main(password):

    count = pwned_api_check(password)

    return count
