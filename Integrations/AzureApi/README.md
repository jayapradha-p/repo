
# AzureApi

Azure API integration was designed for you to execute Azure API without the need of writing any code. This integration version uses Impersonated/Delegated Authentication in Microsoft 365 and requires interactive login of the user on behalf of which integration should communicate with Microsoft 365. To configure this integration, provide all parameters except for Refresh Token, and save the integration configuration, then run “Get Authorization” and “Generate Token” actions to get the token and then provide it in integration configuration to finish the process. Microsoft 365 and Office 365 deliver the power of cloud productivity to businesses of all sizes, helping save time, money, and free up valued resources. The Microsoft 365 and Office 365 plans combine the familiar Microsoft Office desktop suite with cloud-based versions of Microsoft's next-generation communications and collaboration services (including Office for the web, Microsoft Exchange Online, Microsoft Teams, and Microsoft SharePoint Online) to help users be productive from virtually anywhere through the Internet. This integration uses Microsoft Graph Mail API to communicate with Microsoft 365 and Office 365 services.

Python Version - V3_11
#### Parameters
|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Test URL|Test URL that will be used to validate the authentication to Azure API. Uses a GET request.|True|None||
|Microsoft Login API Root|The API root of the Microsoft identity platform login service used for Azure API authentication.|True|None||
|Microsoft Graph API Root|The API root of the Microsoft Graph service used for Azure API operations.|True|None||
|Client ID|The Client ID for the Azure API account.|True|None||
|Client Secret|The Client Secret for the Azure API account.|True|None||
|Tenant ID|The Tenant ID for the Azure API account.|True|None||
|Refresh Token|The Refresh Token for the Azure API account.|False|None||
|Scopes|The scopes for the Azure API authentication.|True|None||
|Verify SSL|If selected, the integration validates the SSL certificate when connecting to the Azure API server. Disabled by default.|False|None||
|Redirect URL|The Redirect URL associated with the Microsoft Entra ID application.|False|None||


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



## Jobs

#### Refresh Token Renewal Job
Token renewal job should be used to periodically update the refresh token configured for the integration. By default, the refresh token expires every 90 days, making integration unusable upon expiration. It is recommended to run this job every 7 or 14 days to make sure that refresh token will be up to date.

|Name|IsMandatory|Type|DefaultValue|
|----|-----------|----|------------|
|Integration Environments|False|None||



