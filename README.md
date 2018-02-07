This prototype reads images in a directory, then uses google vision api to extract the text. For samples we are using driver's licenses.


* Create a new python virtual env e.g : `virtualenv -p python3 <any name>`
* Activate the newly created virtual env `source virtualenv/bin/activate`
* Install google vision client `pip install --upgrade google-cloud-vision`

Google Vision
* Create an account with google cloud.
* Create a service account, make sure the service account is a project owner.
* Download the service account credentionals.
*  Set the environment variable GOOGLE_APPLICATION_CREDENTIALS to the file path of the JSON file
*  e.g `export GOOGLE_APPLICATION_CREDENTIALS=...TestVision-0b985b3c0443.json`
