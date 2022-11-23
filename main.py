import requests as requests

# TODO: Generate Token - https://bit.ly/3V8RP52
TOKEN = 'xyz'


def upload_package(package):
    api = "https://us-kcs-api.samsungknox.com/kcs/v1/kc/assets"

    if TOKEN is None:
        return None

    auth_header = {
        'X-KNOX-APITOKEN': TOKEN,
        'Content-Type': 'multipart/form-data'
    }

    file = "path-and-filename-of-media-file"
    # REQUEST INFO - from https://bit.ly/3GE7PHE
    response = requests.post(f"{api}", headers=auth_header, timeout=10, files=file)
    if response.status_code == 200:
        return response.json()
    else:
        return None


if __name__ == '__main__':
    # TODO: package validation, local and remote.
    for i in range(1, 2, 1):  # (initial,final but not included,gap)
        upload_package(f"/home/luiza/Documents/app-rztech-debug{1}.apk")
