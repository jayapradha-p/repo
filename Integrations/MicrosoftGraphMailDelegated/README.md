
# MicrosoftGraphMailDelegated

This integration version uses Delegated Authentication in Microsoft 365 and requires interactive login of the user on behalf of which integration should communicate with Microsoft 365. To configure this integration, provide all parameters except for Refresh Token, and save the integration configuration, then run “Get Authorization” and “Generate Token” actions to get the token and then provide it in integration configuration to finish the process. Microsoft 365 and Office 365 deliver the power of cloud productivity to businesses of all sizes, helping save time, money, and free up valued resources. The Microsoft 365 and Office 365 plans combine the familiar Microsoft Office desktop suite with cloud-based versions of Microsoft's next-generation communications and collaboration services (including Office for the web, Microsoft Exchange Online, Microsoft Teams, and Microsoft SharePoint Online) to help users be productive from virtually anywhere through the Internet. This integration uses Microsoft Graph Mail API to communicate with Microsoft 365 and Office 365 services.

Python Version - V3_11
#### Parameters
|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Microsoft Entra ID Endpoint|The Microsoft Entra ID endpoint to connect to (formerly known as Azure AD). The value can be different for different tenant types.|True|None||
|Microsoft Graph Endpoint|The Microsoft Graph Endpoint to connect to. The value can be different for different tenant types.|True|None||
|Client ID|The client (application) ID of the Microsoft Entra application to use in the integration.|True|None||
|Client Secret Value|The client secret value of the Microsoft Entra app to use in the integration.|True|None||
|Microsoft Entra ID Directory ID|The Microsoft Entra ID (tenant ID) value.|True|None||
|User Mailbox|The mailbox to use in the integration.|True|None||
|Refresh Token|The refresh token that is used to authenticate.|True|None||
|Verify SSL|If selected, the integration verifies that the SSL certificate for the connection to the Microsoft Graph server is valid. Selected by default.|False|None||
|Mail Field Source|If selected, the integration retrieves the mailbox address from the user details "mail" attribute. If not selected, the integration retrieves the mailbox address from the "userPrincipalName" field. Selected by default|False|None||
|Base64 Encoded Private Key|Specify a base64 encoded private key that will be used to decrypt the email.|False|None||
|Base64 Encoded Certificate|Specify a base64 encoded certificate that will be used to decrypt the email.|False|None||
|Base64 Encoded CA certificate|Specify a base64 encoded trusted CA certificate for signature verification.|False|None||
|Redirect URL|The Redirect URL that you configured when you created your Microsoft Entra ID application.|False|None||


#### Dependencies
| |
|-|
|PyJWT-2.9.0-py3-none-any.whl|
|googleapis_common_protos-1.73.1-py3-none-any.whl|
|protobuf-6.33.6-cp39-abi3-manylinux2014_x86_64.whl|
|soupsieve-2.6-py3-none-any.whl|
|google_auth_httplib2-0.3.0-py3-none-any.whl|
|TIPCommon-2.3.5-py3-none-any.whl|
|pycparser-3.0-py3-none-any.whl|
|google_api_python_client-2.188.0-py3-none-any.whl|
|pcodedmp-1.2.6-py2.py3-none-any.whl|
|requests_toolbelt-1.0.0-py2.py3-none-any.whl|
|easygui-0.98.3-py2.py3-none-any.whl|
|EnvironmentCommon-1.0.1-py2.py3-none-any.whl|
|exceptiongroup-1.2.2-py3-none-any.whl|
|oletools-0.60.2-py2.py3-none-any.whl|
|python_dateutil-2.9.0.post0-py2.py3-none-any.whl|
|setuptools-80.9.0-py3-none-any.whl|
|urllib3-2.6.3-py3-none-any.whl|
|olefile-0.47-py2.py3-none-any.whl|
|charset_normalizer-3.4.0-py3-none-any.whl|
|cryptography-42.0.8-cp39-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl|
|lark-1.1.9-py3-none-any.whl|
|charset_normalizer-3.4.6-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl|
|compressed_rtf-1.0.6.tar.gz|
|tzlocal-5.2-py3-none-any.whl|
|pyasn1_modules-0.4.2-py3-none-any.whl|
|chardet-5.2.0-py3-none-any.whl|
|emaildata-0.3.4-py3-none-any.whl|
|sniffio-1.3.1-py3-none-any.whl|
|anyio-4.13.0-py3-none-any.whl|
|siemplify_html2text-2020.1.16-py3-none-any.whl|
|icalendar-6.0.1-py3-none-any.whl|
|RTFDE-0.1.2-py3-none-any.whl|
|extract_msg-0.52.0-py3-none-any.whl|
|requests-2.32.5-py3-none-any.whl|
|h11-0.16.0-py3-none-any.whl|
|pyparsing-3.3.2-py3-none-any.whl|
|pycryptodome-3.23.0-cp37-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl|
|pyOpenSSL-24.1.0-py3-none-any.whl|
|tzdata-2024.2-py2.py3-none-any.whl|
|cachetools-5.5.0-py3-none-any.whl|
|cffi-2.0.0-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.whl|
|google_api_core-2.30.0-py3-none-any.whl|
|proto_plus-1.27.2-py3-none-any.whl|
|colorclass-2.2.2-py2.py3-none-any.whl|
|pyasn1-0.6.3-py3-none-any.whl|
|rsa-4.9.1-py3-none-any.whl|
|google_auth-2.47.0-py3-none-any.whl|
|msoffcrypto_tool-5.4.2-py3-none-any.whl|
|red-black-tree-mod-1.20.tar.gz|
|certifi-2026.2.25-py3-none-any.whl|
|idna-3.11-py3-none-any.whl|
|pyopenssl-25.3.0-py3-none-any.whl|
|ebcdic-1.1.1-py2.py3-none-any.whl|
|IMAPClient-3.0.1-py2.py3-none-any.whl|
|typing_extensions-4.15.0-py3-none-any.whl|
|pyth3-0.7-py3-none-any.whl|
|cryptography-46.0.6-cp311-abi3-manylinux_2_34_x86_64.whl|
|beautifulsoup4-4.12.3-py3-none-any.whl|
|httpx-0.28.1-py3-none-any.whl|
|six-1.16.0-py2.py3-none-any.whl|
|uritemplate-4.2.0-py3-none-any.whl|
|pytz-2024.2-py2.py3-none-any.whl|
|httpcore-1.0.9-py3-none-any.whl|
|httplib2-0.31.2-py3-none-any.whl|



## Jobs

#### Refresh Token Renewal Job
Token renewal job should be used to periodically update the refresh token configured for the integration. By default, the refresh token expires every 90 days, making integration unusable upon expiration. It is recommended to run this job every 7 or 14 days to make sure that refresh token will be up to date.

|Name|IsMandatory|Type|DefaultValue|
|----|-----------|----|------------|
|Integration Environments|False|None||
|Connector Names|False|None||



## Connectors
#### Microsoft Graph Mail Delegated Connector
Connector can be used to fetch emails from the Microsoft Graph Mail service. Connector dynamic list can be used to filter specific values from the email body and subject parts using regexes. By default, regex is used to filter out the urls from the email. This connector uses Delegated Authentication in Microsoft 365 and requires interactive login of the user on behalf of which integration should communicate with Microsoft 365. To configure the connector, make sure that the integration configuration is already finished, and the refresh token needed to communicate with Office 365 is generated.

|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Environment Field Name|The name of the field where the environment name is stored. If the environment field isn't found, the environment is the default environment. The default value is ""|False|None||
|Environment Regex Pattern|A regular expression pattern to run on the value found in the Environment Field Name field. This parameter lets you manipulate the environment field using the regular expression logic. Use the default value .* to retrieve the required raw Environment Field Name value. If the regular expression pattern is null or empty, or the environment value is null, the final environment result is the default environment.|False|None|.*|
|Email Exclude Pattern|A regular expression to exclude specific emails from ingestion, such as spam or news. This parameter works with both the subject and body of the email.|False|None||
|Microsoft Entra ID Endpoint|The Microsoft Entra endpoint to connect to. The default value is https://login.microsoftonline.com.|True|None|https://login.microsoftonline.com|
|Microsoft Graph Endpoint|The Microsoft Graph endpoint to connect to. The default value is https://graph.microsoft.com.|True|None|https://graph.microsoft.com|
|Mail Address|An email address for the connector to use.|True|None||
|Refresh Token|The refresh token that you obtained after you generated a token.|True|None||
|Client ID|For Microsoft 365 OAuth 2.0 authentication, the application (client) ID of the Microsoft Entra application that is used in the integration.|True|None||
|Client Secret Value|For Microsoft 365 OAuth 2.0 authentication, the client secret value that is provided for the authentication flow.|True|None||
|Microsoft Entra ID Directory ID|For Microsoft 365 OAuth authentication, the tenant (directory) ID of the Microsoft Entra ID application that you used in the integration.|True|None||
|Folder To Check For Emails|An email folder to search for the emails. This parameter accepts a comma-separated list of folders to check the user response in multiple folders. To specify a subfolder, use the “/” forward slash, such as {Inbox/Subfolder}. This parameter is case-sensitive. The default value is Inbox.|True|None|Inbox|
|Offset Time In Hours|The number of hours before the first connector iteration to retrieve the incidents from. This parameter applies to the initial connector iteration after you enable the connector for the first time. The connector can use this parameter as a fallback value when the timestamp from the latest connector iteration expires.|True|None|24|
|Max Emails Per Cycle|The maximum number of emails to fetch for every connector iteration.|True|None|10|
|Unread Emails Only|If selected, the connector creates cases only for unread emails.|False|None|false|
|Mark Emails as Read|If selected, the connector marks ingested emails as read.|False|None|false|
|Disable Overflow|If selected, the connector ignores the Google SecOps overflow mechanism.|False|None|false|
|Verify SSL|If selected, the integration verifies that the SSL certificate for connecting to the Microsoft Graph server is valid.|False|None|true|
|Base64 Encoded Private Key|Specify a base64 encoded private key that will be used to decrypt the email.|False|None||
|Base64 Encoded Certificate|Specify a base64 encoded certificate that will be used to decrypt the email.|False|None||
|Base64 Encoded CA certificate|Specify a base64 encoded trusted CA certificate for signature verification.|False|None||
|Mail Field Source|If selected, the connector retrieves the mailbox address from the user details “mail” attribute. If not selected, the integration retrieves the mailbox address from the “userPrincipalName” field. Selected by default.|False|None|true|
|Original Received Mail Prefix|A prefix to add to the extracted event keys (for example, to, from, or subject) from the original email received in the monitored mailbox. The default value is orig.|False|None|orig|
|Attached Mail File Prefix|A prefix to add to the extracted event keys (for example, to, from, or subject) from the attached email file received in the monitored mailbox. The default value is attach.|False|None|attach|
|Create a Separate Google SecOps Alert Per Attached Mail File|If selected, the connector creates multiple alerts, with one alert for every attached email file. This behavior is useful when you process emails with multiple email files attached and set the Google SecOps event mapping to create entities from attached email files.|False|None|false|
|Attach Original EML|If selected, the connector attaches the original email to the case info as an EML file.|False|None|false|
|Headers to add to events|A comma-separated string of email headers to add to Google SecOps events, such as “DKIM-Siganture”, “Received”, “From”. You can provide an exact match for headers or set this parameter value as a regular expression. The connector filters the configured values from the “internetMessageHeaders” list and adds them to the Google SecOps event. By default, the connector adds all available headers. To prevent the connector from adding headers to the event, set the parameter value as follows: None.|False|None||
|Case Name Template|A custom case name. When you configure this parameter, the connector adds a new key called custom_case_name to the Google SecOps event. You can provide placeholders in the following format: [name of the field]. Example: Phishing - [event_mailbox]. For placeholders, the connector uses the first Google SecOps event. The connector only handles keys that contain the string value.|False|None||
|Alert Name Template|A custom alert name. You can provide placeholders in the following format: [name of the field]. Example: Phishing - [event_mailbox]. For placeholders, the connector uses the first Google SecOps event. The connector only handles keys that contain the string value. If you configure an invalid template or don't set a value, the connector uses the default alert name.|False|None||
|Proxy Server Address|The address of the proxy server to use.|False|None||
|Proxy Username|The proxy server username to authenticate with.|False|None||
|Proxy Password|The proxy password to authenticate with.|False|None||




