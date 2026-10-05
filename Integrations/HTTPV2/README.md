
# HTTPV2

HTTP V2 integration was designed for you to build your own integrations, actions without the need of writing any code.

Python Version - V3_11
#### Parameters
|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Test URL|Test URL that can be used to validate the "Basic Auth" authentication or "API Key" authentication. Uses a GET request.|False|String||
|Basic Auth Username|If you provide "Basic Auth Username" and "Basic Auth Password" parameters then these parameters will be added as Basic Authentication headers to every action run. Note: you need to provide both "Basic Auth Password" and "Basic Auth Username".|False|String||
|Basic Auth Password|If you provide "Basic Auth Username" and "Basic Auth Password" parameters then these parameters will be added as Basic Authentication headers to every action run. Note: you need to provide both "Basic Auth Password”" and "Basic Auth Username".|False|Password|*****|
|API Key Field Name|Name of the header that will contain the API key. If you provide "API Key Field Name" and "API Key Secret" parameters then these parameters will be added to every action run. Note: you need to provide both "API Key Field Name" and "API Key Secret".|False|String||
|API Key Secret|API key secret. If you provide "API Key Field Name" and "API Key Secret" parameters then these parameters will be added to every action run. Note: you need to provide both "API Key Field Name" and "API Key Secret".|False|Password|*****|
|Dedicated Auth API Request Method|Method that will be used in the Dedicated Auth API flow to generate the access token.|False|String|Post|
|Dedicated Auth API Request URL|API request that will be used in the Dedicated Auth API flow to generate the access token.|False|String||
|Dedicated Auth API Request Headers|Headers that will be used in the Dedicated Auth API flow to generate the access token.|False|Password|*****|
|Dedicated Auth API Request Body|Request Body that will be used in the Dedicated Auth API flow to generate the access token.|False|Password|*****|
|Dedicated Auth API Request Token Field Name|Name of the field that contains the generated access token. This access token can be used inside the actions with {{integration.token}} placeholder. Note: that the response for token generation will be flattened with "_" as delimiter.|False|String||
|Verify SSL|If enabled, verify the SSL certificate for all of the connections done by integration.|False|Boolean|true|
|CA Certificate|CA certificate to use to validate the secure connection. Parameter accepts the CA certificate in a form of base64 encoded string.|False|String||
|Restrict Domain|If selected, integration will only allow API requests with the same domain as in "Test URL" parameter.|False|Boolean|false|


#### Dependencies
| |
|-|
|idna-3.20-py3-none-any.whl|
|pycryptodomex-3.23.0-cp37-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl|
|cffi-2.1.1-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.whl|
|google_api_core-2.30.3-py3-none-any.whl|
|cryptography-50.0.1-cp311-abi3-manylinux2014_x86_64.manylinux_2_17_x86_64.whl|
|google_auth_httplib2-0.4.2-py3-none-any.whl|
|pycparser-3.0-py3-none-any.whl|
|anyio-4.15.1-py3-none-any.whl|
|pyasn1-0.6.4-py3-none-any.whl|
|urllib3-2.4.0-py3-none-any.whl|
|pyasn1_modules-0.4.2-py3-none-any.whl|
|httplib2-0.32.0-py3-none-any.whl|
|requests-2.32.4-py3-none-any.whl|
|googleapis_common_protos-1.75.4-py3-none-any.whl|
|google_api_python_client-2.200.0-py3-none-any.whl|
|TIPCommon-2.2.16-py2.py3-none-any.whl|
|h11-0.16.0-py3-none-any.whl|
|protobuf-7.36.2-py3-none-any.whl|
|google_auth-2.59.0-py3-none-any.whl|
|typing_extensions-4.16.0-py3-none-any.whl|
|pycryptodome-3.23.0-cp37-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl|
|proto_plus-1.28.4-py3-none-any.whl|
|certifi-2026.7.22-py3-none-any.whl|
|httpx-0.28.1-py3-none-any.whl|
|EnvironmentCommon-1.0.2-py2.py3-none-any.whl|
|charset_normalizer-3.5.1-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl|
|uritemplate-4.2.0-py3-none-any.whl|
|httpcore-1.0.9-py3-none-any.whl|
|pyzipper-0.3.6-py2.py3-none-any.whl|
|pyparsing-3.3.3-py3-none-any.whl|


## Actions
#### Execute HTTP Request
Execute HTTP request.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Method|Specify the method for the request.|True|List|GET|
|URL Path|Specify the URL that needs to be executed.|True|String|https://|
|URL Params|Specify the parameters for the URL. Any value provided in this parameter will be used alongside the values that are directly provided in the URL path parameters.|False|String|{"URL Field Name": "URL Field Value"}|
|Headers|Specify headers for the HTTP request.|False|String|{"Content-Type": "application/json; charset=utf-8", "Accept": "application/json", "User-Agent" : "GoogleSecOps"}|
|Cookie|Specify the parameters that should be constructed into the "Cookie" header. This parameter will overwrite the cookie provided in the "Headers" parameter.|False|String|{"Cookie_1": "value_1"}|
|Body Payload|Specify body for the HTTP request.|False|String|{"Body Field Name": "Body Field Value"}|
|Expected Response Values|Specify the expected response values. If this parameter is not empty, then action will work in ASYNC mode and action will execute until the expected values will be seen or until timeout. Example input: {"key": "expected value"}|False|String||
|Follow Redirects|If enabled, action will follow the redirects.|False|Boolean|true|
|Fail on 4xx/5xx|If enabled, action will fail, if the status code of the response is 4xx or 5xx.|False|Boolean|true|
|Base64 Output|If enabled, action will convert the response to base64. This is useful when downloading files. Note: JSON result can't be bigger than 15 mb.|False|Boolean|false|
|Fields To Return|Specify what fields to return. Possible values: response_data, redirects, response_code,response_cookies,response_headers,apparent_encoding|True|String|response_data, redirects, response_code,response_cookies,response_headers,apparent_encoding|
|Request Timeout|How long to wait for the server to send data before giving up|True|String|120|
|Save To Case Wall|If enabled, action will save the file and attach it to the case wall. Note: the file will be archived with ".zip" extension. This zip will not be password protected.|False|Boolean|false|
|Password Protect Zip|If enabled, action will add an "infected" password to the zip created with "Save To Case Wall" parameter. Use this, when you are dealing with suspicious files.|False|Boolean|true|



##### JSON Results
```json
{"response_data": [{"id": 101, "username": "alice_admin", "email": "alice@example.com", "status": "Active", "role": "Administrator", "last_login": "2023-10-27T08:30:00Z", "risk_score": 85}, {"id": 102, "username": "bob_user", "email": "bob@example.com", "status": "Suspended", "role": "User", "last_login": "2023-10-25T14:15:00Z", "risk_score": 20}, {"id": 103, "username": "charlie_dev", "email": "charlie@example.com", "status": "Active", "role": "Developer", "last_login": "2023-10-27T09:00:00Z", "risk_score": 45}, {"id": 104, "username": "dave_ops", "email": "dave@example.com", "status": "Active", "role": "DevOps", "last_login": "2023-10-26T11:45:00Z", "risk_score": 10}], "redirects": ["http://api.example.com/v1/users", "https://api.example.com/v2/users"], "response_code": 200, "response_cookies": {"session_id": "xyz123abc456", "region": "us-east-1"}, "response_headers": {"Content-Type": "application/json", "Date": "Fri, 27 Oct 2023 10:00:00 GMT", "Server": "nginx/1.18.0", "X-RateLimit-Remaining": "99"}, "apparent_encoding": "utf-8"}
```



#### Ping
Test connectivity.
Timeout - 600 Seconds



##### JSON Results
```json
{"endpoint": "https://testendpoint.com"}
```









