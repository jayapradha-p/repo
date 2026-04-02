
# AzureSecurityCenter

Azure Security Center is a unified infrastructure security management system that strengthens the security posture of your data centers, and provides advanced threat protection across your hybrid workloads in the cloud - whether they're in Azure or not - as well as on premises.

Python Version - V3_11
#### Parameters
|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Client ID|None|True|None||
|Client Secret|None|True|None||
|Username|None|False|None||
|Password|None|False|None||
|Subscription ID|None|False|None||
|Tenant ID|None|True|None||
|Refresh Token|None|False|None||
|Verify SSL|None|False|None||


#### Dependencies
| |
|-|
|googleapis_common_protos-1.73.1-py3-none-any.whl|
|protobuf-6.33.6-cp39-abi3-manylinux2014_x86_64.whl|
|google_auth_httplib2-0.3.0-py3-none-any.whl|
|TIPCommon-2.3.5-py3-none-any.whl|
|pycparser-3.0-py3-none-any.whl|
|google_api_python_client-2.188.0-py3-none-any.whl|
|requests_toolbelt-1.0.0-py2.py3-none-any.whl|
|setuptools-80.9.0-py3-none-any.whl|
|urllib3-2.6.3-py3-none-any.whl|
|charset_normalizer-3.4.6-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl|
|pyasn1_modules-0.4.2-py3-none-any.whl|
|sniffio-1.3.1-py3-none-any.whl|
|anyio-4.13.0-py3-none-any.whl|
|requests-2.32.5-py3-none-any.whl|
|h11-0.16.0-py3-none-any.whl|
|pyparsing-3.3.2-py3-none-any.whl|
|pycryptodome-3.23.0-cp37-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl|
|cffi-2.0.0-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.whl|
|google_api_core-2.30.0-py3-none-any.whl|
|proto_plus-1.27.2-py3-none-any.whl|
|pyasn1-0.6.3-py3-none-any.whl|
|cachetools-5.5.2-py3-none-any.whl|
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


## Actions
#### Get OAuth Authorization Code
Generate an OAuth authorization code in Azure Security Center. Please refer to the documentation portal for more information.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Redirect URL|Specify the redirect URL that was used when the app was created.|True|None||



#### Get OAuth Refresh Token
Generate the refresh token that is needed for the integration configuration. Authorization code can be generated using "Get OAuth Authorization Code". Please refer to the documentation portal for more information.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Redirect URL|Specify the redirect URL that was used when the app was created.|True|None||
|Authorization Code|Specify the authorization code from action "Get OAuth Authorization Code"|True|None||



#### List Regulatory Standard Controls
List available controls related to standards in Microsoft Azure Security Center.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Subscription ID|Specify the ID of the subscription for which you want to query information. Note: if subscription ID is provided at the integration level and action level, priority will be given to action configuration.|False|None||
|Standard Names|Specify a comma-separated list of standard names for which you want to retrieve details. Example: Azure-CIS-1.1.0|True|None||
|State Filter|Specify the comma-separated list of states. Example: Failed, Skipped. Only standards with the matching state will be returned. For example, if you specify “Failed”, action will only return failed standards. Possible values: Passed, Failed, Unsupported, Skipped|False|None||
|Max Standards To Return|Specify how many controls to return per standard.|False|None||



#### Update Alert Status
Update status of the alert in Microsoft Azure Security Center.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Subscription ID|Specify the ID of the subscription for which you want to query information. Note: if subscription ID is provided at the integration level and action level, priority will be given to action configuration.|False|None||
|Alert ID|Specify an ID of the alert, where you want to update status.|True|None||
|Location|Specify the location of the alert. Example: centralus.|True|None||
|Status|Specify the status for the alert.|True|None||



#### Ping
Test connectivity to Azure Security Center with parameters provided at the integration configuration page on Marketplace tab.
Timeout - 600 Seconds



#### List Regulatory Standards
List available regulatory standards in Microsoft Azure Security Center
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Subscription ID|Specify the ID of the subscription for which you want to query information. Note: if subscription ID is provided at the integration level and action level, priority will be given to action configuration.|False|None||
|State Filter|Specify the comma-separated list of states. Example: Failed, Skipped. Only standards with the matching state will be returned. For example, if you specify “Failed”, action will only return failed standards. Possible values: Passed, Failed, Unsupported, Skipped|False|None||
|Max Standards To Return|Specify how many standards to return.|False|None||






## Jobs

#### Refresh Token Renewal Job
Token renewal job should be used to periodically update the refresh token configured for the integration. By default, the refresh token expires every 90 days, making integration unusable upon expiration. It is recommended to run this job every 7 or 14 days to make sure that refresh token will be up to date.

|Name|IsMandatory|Type|DefaultValue|
|----|-----------|----|------------|
|Integration Environments|False|None||
|Connector Names|False|None||



## Connectors
#### Azure Security Center - Security Alerts Connector
Pull security alerts from Azure Security Center. Note: whitelist works with alertType field.

|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Environment Field Name|Describes the name of the field where the environment name is stored. If the environment field isn't found, the environment is the default environment.|False|None||
|Environment Regex Pattern|A regex pattern to run on the value found in the "Environment Field Name" field. Default is .* to catch all and return the value unchanged. Used to allow the user to manipulate the environment field via regex logic. If the regex pattern is null or empty, or the environment value is null, the final environment result is the default environment.|False|None|.*|
|Client ID|Client ID of the Microsoft Azure application. |True|None||
|Client Secret|Client Secret of the Microsoft Azure application.|True|None||
|Username|Username of the Microsoft Azure account.|False|None||
|Password|Password of the Microsoft Azure account.|False|None||
|Subscription ID|Subscription ID of the Microsoft Azure application.|True|None||
|Tenant ID|Tenant ID of the Microsoft Azure application.|True|None||
|Refresh Token|Refresh token for the OAuth authorization.|False|None||
|Max Hours Backwards|Number of hours before the first connector iteration to retrieve alerts from. This parameter applies to the initial connector iteration after you enable the connector for the first time, or used as a fallback value in cases where connector's last run timestamp expires.|False|None|1|
|Max Alerts To Fetch|How many alerts to process per one connector iteration.|False|None|50|
|Lowest Severity To Fetch|Lowest severity that will be used to fetch Alert. Possible values: Low, Medium, High|True|None|Low|
|Use whitelist as a blacklist|If enabled, whitelist will be used as a blacklist.|False|None|false|
|Verify SSL|If enabled, verify the SSL certificate for the connection to the Azure Security Center server is valid.|False|None|false|
|Proxy Server Address|The address of the proxy server to use.|False|None||
|Proxy Username|The proxy username to authenticate with.|False|None||
|Proxy Password|The proxy password to authenticate with.|False|None||




