import requests as requests

# TODO: Generate Token - https://bit.ly/3V8RP52
TOKEN = 'TOKEN'


def upload_apk(apk_path):
    api = "https://us-kcs-api.samsungknox.com/kcs/v1/kc/assets"

    if TOKEN is None:
        return None

    auth_header = {
        'X-KNOX-APITOKEN': TOKEN,
        'Content-Type': 'multipart/form-data'
    }

    # REQUEST INFO - from https://bit.ly/3GE7PHE
    with open(apk_path, 'rb') as filedata:
        response = requests.post(f"{api}", headers=auth_header, timeout=500, files={'file': filedata})
        if response.status_code == 200:
            return response.json()
        else:
            return f"{response.status_code}:  {response.text}"


if __name__ == '__main__':
    # TODO: package validation, local and remote.
    for i in range(1, 2, 1):  # (initial,final but not included,gap)
        response = upload_apk(f"/Users/luizzabuscka/Downloads/MobileApp-1.0.9.{i}.apk")
        print(response)
