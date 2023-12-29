import requests

if __name__ == "__main__":
    URL = "http://spelli-publi-ijlxfutr2ajd-1656619316.eu-west-1.elb.amazonaws.com/api/puzzle"
    # for i in range(100):
    #     print(f"Request #{i + 1}")
    #     response = requests.post(
    #         url=URL,
    #         json={"letters": "abcdefg", "main_letter": "a"},
    #     )
    #     print(f"Response code: {response.status_code}")

    response = requests.post(
        url=URL,
        json={"letters": "", "main_letter": ""},
    )
    print(response.json())
