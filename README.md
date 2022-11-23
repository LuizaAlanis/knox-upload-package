### Docs

- [Post Request tutorial](https://docs.samsungknox.com/devref/knox-configure/index.htm#tag/Content-Management-Application-APIs/operation/uploadInHouseApplicationUsingPOST "Upload package")

- [Generate token tutorial](https://docs.samsungknox.com/dev/knox-cloud-authentication/tutorial.htm "Knox Auth")

### Clone project

<pre>
 git@github.com:LuizaAlanis/knox-upload-package.git
</pre>

### Curl 

<pre>
 curl --location --request POST \
  'https://us-kcs-api.samsungknox.com/kcs/v1/kc/applications/upload' \
  --header 'X-KNOX-APITOKEN: <insert-token-here>' \
  --header 'Content-Type: multipart/form-data' \
  --form 'file=<path-and-filename-of-package>'
</pre>

![Postman](https://img.shields.io/badge/Postman-FF6C37?style=for-the-badge&logo=postman&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
