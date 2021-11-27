 # Desperado api
 Simple api where you can post a string and get a "Rövarspråket" string in return.
 so all consonants will be appended with o and the same consonant (ajusted to casing). Everything else will be returned as is.
 "Hello World" will return "HoHelollolo WoWororloldod"

 ## The functionality is not the main point
 The main point is to try building a simple api and putting it into a container. The actual function is of lesser importance.
 ## Starting locally
 To start the application from the project root folder:
 ``` bash
 ~/.local/bin/uvicorn app.main:app --host 0.0.0.0 --port 5000 --reload
 ```
 Visit /docs/ for OpenAPI interactive api documentation. (Swagger-like experience)