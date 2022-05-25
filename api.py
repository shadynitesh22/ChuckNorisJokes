import requests
import csv

"""
@This code is open source so you can use this in your project 
"""
"""
Iam going to use Rapid Api to have some fun !!
This api will search for chuck noris jokes 
We will then learn how we can use this in django project !!

You can wrap this in a function or write the output to a csv file

"""


def get_chuck_norris_jokes_api(request):
    results = {}
    if request.method == 'GET':
        url = "https://matchilling-chuck-norris-jokes-v1.p.rapidapi.com/jokes/random"

        querystring = {
            "query": "random"
        }
        headers = {
            'accept': 'application/json',
            "X-RapidAPI-Host": "matchilling-chuck-norris-jokes-v1.p.rapidapi.com",
            "X-RapidAPI-Key": "c03b81535bmshbeb45f7af117155p10ac00jsnb0825e9a0176"
        }

        try:
            jokes_csv = open('chuk_noris.csv', 'w')
            csv_writer = csv.writer(jokes_csv)
            csv_writer.writerow(['JokeId', 'Joke', "ImageUrl"])
            x = 0
            while x <= 3:
                response = requests.request("GET", url, headers=headers, params=querystring)
                check_me = response.json()
                icon_url = check_me['icon_url']
                value = check_me['value']
                id_ = check_me['id']
                results = {"icon_url": icon_url, "jokes": value, "id": id_}
                print(results)
                print(f"JokeId:{id_} \nJoke:{value}\n Icon:{icon_url}")
                x += 1
                csv_writer.writerow([id_, value, icon_url])
            jokes_csv.close()
        except:
            Exception(KeyError())
            print(Exception, "Error Occurred ")

    return results


get_chuck_norris_jokes_api()


def get_location_api():
    url = "https://telize-v1.p.rapidapi.com/location/%7Bip_address%7D"
    # val = input("\nEnter What jokes you want to search")
    querystring = {
        "callback": "getlocation"
    }
    headers = {
        "X-RapidAPI-Host": "telize-v1.p.rapidapi.com",
        "X-RapidAPI-Key": "c03b81535bmshbeb45f7af117155p10ac00jsnb0825e9a0176"
    }

    try:
        # ip_csv = open('ip.csv', 'w')
        # csv_writer = csv.writer(ip_csv)
        # csv_writer.writerow(['JokeId', 'Joke', "ImageUrl"])
        x = 0
        while x <= 3:
            response = requests.request("GET", url, headers=headers, params=querystring)

            print(response.text)
            # icon_url = check_me['icon_url']
            # value = check_me['value']
            # id_ = check_me['id']
            # # results = {"icon_url": icon_url, "jokes": value, "id": id_}
            # # print(results)
            # print(f"JokeId:{id_} \nJoke:{value}\n Icon:{icon_url}")
            x += 1
            # csv_writer.writerow([id_, value, icon_url])
        # jokes_csv.close()
    except:
        Exception(KeyError())
        print(Exception, "Error Occurred ")


get_location_api()
