# Azure Security Center - Security Alerts Connector
Pull security alerts from Azure Security Center. Note: whitelist works with alertType field.


Integration: AzureSecurityCenter

Integration Version: 17.0

Device Product Field: Product Name

Event Name Field: properties_entities_type
### Parameters
|Name|Description|Is Mandatory|Value|
|----|-----------|------------|-----|
|Environment Field Name|Describes the name of the field where the environment name is stored. If the environment field isn't found, the environment is the default environment.|False||
|Environment Regex Pattern|A regex pattern to run on the value found in the "Environment Field Name" field. Default is .* to catch all and return the value unchanged. Used to allow the user to manipulate the environment field via regex logic. If the regex pattern is null or empty, or the environment value is null, the final environment result is the default environment.|False|.*|
|Client ID|Client ID of the Microsoft Azure application. |True|cec69cfd-f149-432f-ba95-d535cdc4005a|
|Client Secret|Client Secret of the Microsoft Azure application.|True|***************|
|Username|Username of the Microsoft Azure account.|False|labops1@siemplifycyarx.onmicrosoft.com|
|Password|Password of the Microsoft Azure account.|False|***************|
|Subscription ID|Subscription ID of the Microsoft Azure application.|True|a052d33b-b7c4-4dc7-9e17-5c89ea594669|
|Tenant ID|Tenant ID of the Microsoft Azure application.|True|d48f52ca-5b1a-4708-8ed0-ebb98a26a46a|
|Refresh Token|Refresh token for the OAuth authorization.|False|***************|
|Max Hours Backwards|Number of hours before the first connector iteration to retrieve alerts from. This parameter applies to the initial connector iteration after you enable the connector for the first time, or used as a fallback value in cases where connector's last run timestamp expires.|False|1|
|Max Alerts To Fetch|How many alerts to process per one connector iteration.|False|50|
|Lowest Severity To Fetch|Lowest severity that will be used to fetch Alert. Possible values: Low, Medium, High|True|Low|
|Use whitelist as a blacklist|If enabled, whitelist will be used as a blacklist.|False|false|
|Verify SSL|If enabled, verify the SSL certificate for the connection to the Azure Security Center server is valid.|False|false|
|Proxy Server Address|The address of the proxy server to use.|False||
|Proxy Username|The proxy username to authenticate with.|False||
|Proxy Password|The proxy password to authenticate with.|False|***************|

