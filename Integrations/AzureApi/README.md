
# AzureApi

Azure API integration was designed for you to execute Azure API without the need of writing any code. This integration version uses Impersonated/Delegated Authentication in Microsoft 365 and requires interactive login of the user on behalf of which integration should communicate with Microsoft 365. To configure this integration, provide all parameters except for Refresh Token, and save the integration configuration, then run “Get Authorization” and “Generate Token” actions to get the token and then provide it in integration configuration to finish the process. Microsoft 365 and Office 365 deliver the power of cloud productivity to businesses of all sizes, helping save time, money, and free up valued resources. The Microsoft 365 and Office 365 plans combine the familiar Microsoft Office desktop suite with cloud-based versions of Microsoft's next-generation communications and collaboration services (including Office for the web, Microsoft Exchange Online, Microsoft Teams, and Microsoft SharePoint Online) to help users be productive from virtually anywhere through the Internet. This integration uses Microsoft Graph Mail API to communicate with Microsoft 365 and Office 365 services.

Python Version - V3_11
#### Parameters
|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Test URL|Test URL that will be used to validate the authentication to Azure API. Uses a GET request.|True|String||
|Microsoft Login API Root|The API root of the Microsoft identity platform login service used for Azure API authentication.|True|String||
|Microsoft Graph API Root|The API root of the Microsoft Graph service used for Azure API operations.|True|String||
|Client ID|The Client ID for the Azure API account.|True|String||
|Client Secret|The Client Secret for the Azure API account.|True|Password||
|Tenant ID|The Tenant ID for the Azure API account.|True|String||
|Refresh Token|The Refresh Token for the Azure API account.|False|Password||
|Scopes|The scopes for the Azure API authentication.|True|String||
|Verify SSL|If selected, the integration validates the SSL certificate when connecting to the Azure API server. Disabled by default.|False|Boolean||
|Redirect URL|The Redirect URL associated with the Microsoft Entra ID application.|False|String||


#### Dependencies
| |
|-|
|pycryptodomex-3.23.0-cp37-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl|
|googleapis_common_protos-1.73.1-py3-none-any.whl|
|protobuf-6.33.6-cp39-abi3-manylinux2014_x86_64.whl|
|google_auth_httplib2-0.3.0-py3-none-any.whl|
|cachetools-6.2.2-py3-none-any.whl|
|TIPCommon-2.3.5-py3-none-any.whl|
|google_api_core-2.28.1-py3-none-any.whl|
|anyio-4.12.0-py3-none-any.whl|
|pycparser-3.0-py3-none-any.whl|
|google_api_python_client-2.188.0-py3-none-any.whl|
|requests_toolbelt-1.0.0-py2.py3-none-any.whl|
|setuptools-80.9.0-py3-none-any.whl|
|urllib3-2.6.3-py3-none-any.whl|
|charset_normalizer-3.4.6-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl|
|pyasn1_modules-0.4.2-py3-none-any.whl|
|certifi-2025.11.12-py3-none-any.whl|
|sniffio-1.3.1-py3-none-any.whl|
|anyio-4.13.0-py3-none-any.whl|
|google_api_python_client-2.187.0-py3-none-any.whl|
|requests-2.32.5-py3-none-any.whl|
|cryptography-46.0.3-cp311-abi3-manylinux_2_34_x86_64.whl|
|h11-0.16.0-py3-none-any.whl|
|pyparsing-3.3.2-py3-none-any.whl|
|pycryptodome-3.23.0-cp37-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl|
|cffi-2.0.0-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.whl|
|google_api_core-2.30.0-py3-none-any.whl|
|proto_plus-1.27.2-py3-none-any.whl|
|charset_normalizer-3.4.4-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl|
|pyasn1-0.6.3-py3-none-any.whl|
|rsa-4.9.1-py3-none-any.whl|
|google_auth-2.47.0-py3-none-any.whl|
|certifi-2026.2.25-py3-none-any.whl|
|idna-3.11-py3-none-any.whl|
|pyopenssl-25.3.0-py3-none-any.whl|
|typing_extensions-4.15.0-py3-none-any.whl|
|cryptography-46.0.6-cp311-abi3-manylinux_2_34_x86_64.whl|
|httpx-0.28.1-py3-none-any.whl|
|EnvironmentCommon-1.0.2-py2.py3-none-any.whl|
|uritemplate-4.2.0-py3-none-any.whl|
|httpcore-1.0.9-py3-none-any.whl|
|httplib2-0.31.2-py3-none-any.whl|
|pyzipper-0.3.6-py2.py3-none-any.whl|


## Actions
#### Get Authorization
Use the Get Authorization action to initiate the OAuth flow and obtain a link that contains the required access code for delegated authentication. This action doesn't run on Google SecOps entities.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Oauth Scopes|A comma-separated list of permissions requested for the access and refresh tokens. These scopes define the level of access the integration has to the user's data and resources.|True|None||



#### Execute HTTP Request
Use the Execute HTTP Request action to construct and execute a customized HTTP API request against a target URL. Note: This action operates in an asynchronous mode when polling an endpoint is necessary to wait until a specific success or failure condition is met in the response body.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Method|The HTTP method (verb) used for the request.|True|None||
|URL Path|The API endpoint where the request executes. This path can optionally include query parameters.|True|None||
|URL Params|The query parameters (GET parameters) for the URL, provided as a JSON object where each key-value pair is a parameter. This is the recommended input method. These values are used in addition to any query parameters included in the URL Path.|False|None||
|Headers|The headers for the HTTP request, specified as a JSON object. Headers control aspects such as authentication and define the format of the Body Payload (using Content-Type).|False|None||
|Cookie|The cookies constructed into the HTTP Cookie header, specified as a JSON object. This parameter overrides any cookie values provided in Headers.|False|None||
|Body Payload|The content payload for the HTTP request, specified as a JSON object. The request's format (JSON or form-urlencoded) is determined by the Content-Type set in Headers.|False|None||
|Expected Response Values|The JSON object containing the field-value pairs that define the required successful state of the response. If provided, the action runs in asynchronous  mode and repeatedly executes the request until the expected values appear in the response or until the action times out. Example input: {"key": "expected value"}|False|None||
|Follow Redirects|If selected, the action automatically follows any HTTP redirect responses (such as 301 or 302 status codes) to the final destination URL.|False|None||
|Fail on 4xx/5xx|If selected, the action explicitly fails the step when the HTTP response returns a Client Error (4xx) or Server Error (5xx) status code.|False|None||
|Base64 Output|If selected, the action converts the entire HTTP response body to a Base64 encoded string. This is useful when you download files that need to be processed or stored. Note: The resulting Base64 string cannot exceed 15 MB.|False|None||
|Fields To Return|A comma-separated list of fields that the action returns in the output. Possible values: response_data, redirects, response_code, response_cookies, response_headers, apparent_encoding.|True|None||
|Request Timeout|The maximum time, in seconds, the action waits for the server to send data before the request is aborted.|True|None||
|Save To Case Wall|If selected, the action saves the file and attaches it to the case wall. Note: The file is archived with “.zip” extension. This zip isn't password protected.|False|None||
|Password Protect Zip|If selected, the action encrypts the downloaded ZIP archive (created using Save To Case Wall) with a password (such as infected). Use this option when dealing with suspicious or potentially malicious files to prevent accidental execution.|False|None||



#### Ping
Test connectivity.
Timeout - 600 Seconds



#### Generate Token
Use the Generate Token action to obtain a persistent refresh token required for delegated authentication. This token is generated using the authorization URL received from the Get Authorization action. This action doesn't run on Google SecOps entities.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Authorization URL|The full authorization URL, containing the access code, received from the Get Authorization action. This URL is required to request and generate the refresh token.|True|None||






## Jobs

#### Refresh Token Renewal Job
Token renewal job should be used to periodically update the refresh token configured for the integration. By default, the refresh token expires every 90 days, making integration unusable upon expiration. It is recommended to run this job every 7 or 14 days to make sure that refresh token will be up to date.

|Name|IsMandatory|Type|DefaultValue|
|----|-----------|----|------------|
|Integration Environments|False|None||



