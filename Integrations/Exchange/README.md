
# Exchange

Integration provides support for Microsoft Exchange 2010 - 2019 and Microsoft Office365 mail servers. Integration uses Exchange Web Services (EWS) for communication. Integration includes a series of actions to send out emails and work with received emails, along with a connector to monitor specific mailboxes and ingest emails from that mailboxes as alerts to Google SecOps for further analysis.

Python Version - V3_11
#### Parameters
|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|ServerAddress|None|True|None||
|Mail Address|None|True|None||
|Domain|None|False|None||
|Use Domain For Authentication|None|False|None||
|Use Autodiscover Service|None|False|None||
|Use Delegated Access|If enabled, delegated access type will be used. Otherwise, impersonation access type is used. For details on impersonation/delegation and EWS, see the following link https://learn.microsoft.com/en-us/exchange/client-developer/exchange-web-services/impersonation-and-ews-in-exchange.|False|None||
|Username|None|False|None||
|Password|None|False|None||
|Client ID|None|False|None||
|Client Secret|None|False|None||
|Tenant (Directory) ID|None|False|None||
|Redirect URL|None|False|None||
|Refresh Token|None|False|None||
|Base64 Encoded Private Key|Specify a base64 encoded private key that will be used to decrypt the email.|False|None||
|Base64 Encoded Certificate|Specify a base64 encoded certificate that will be used to decrypt the email.|False|None||
|Base64 Encoded CA certificate|Specify a base64 encoded trusted CA certificate for signature verification.|False|None||
|Verify SSL|None|False|None||


#### Dependencies
| |
|-|
|anyio-4.8.0-py3-none-any.whl|
|pyparsing-3.2.1-py3-none-any.whl|
|requests_ntlm-1.3.0-py3-none-any.whl|
|proto_plus-1.26.0-py3-none-any.whl|
|pygments-2.18.0-py3-none-any.whl|
|soupsieve-2.6-py3-none-any.whl|
|html2text-2024.2.26.tar.gz|
|exchangelib-5.5.0-py3-none-any.whl|
|pycryptodome-3.21.0-cp36-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl|
|pcodedmp-1.2.6-py2.py3-none-any.whl|
|google_api_core-2.24.1-py3-none-any.whl|
|easygui-0.98.3-py2.py3-none-any.whl|
|EnvironmentCommon-1.0.1-py2.py3-none-any.whl|
|certifi-2025.1.31-py3-none-any.whl|
|oletools-0.60.2-py2.py3-none-any.whl|
|isodate-0.7.2-py3-none-any.whl|
|python_dateutil-2.9.0.post0-py2.py3-none-any.whl|
|pytest_runner-6.0.1-py3-none-any.whl|
|setuptools-80.9.0-py3-none-any.whl|
|defusedxml-0.7.1-py2.py3-none-any.whl|
|olefile-0.47-py2.py3-none-any.whl|
|requests_oauthlib-2.0.0-py2.py3-none-any.whl|
|oscrypto-1.3.0-py3-none-any.whl|
|cryptography-42.0.8-cp39-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl|
|googleapis_common_protos-1.68.0-py2.py3-none-any.whl|
|pycparser-2.22-py3-none-any.whl|
|lark-1.1.9-py3-none-any.whl|
|IMAPClient-2.1.0-py2.py3-none-any.whl|
|compressed_rtf-1.0.6.tar.gz|
|tzlocal-5.2-py3-none-any.whl|
|pyspnego-0.11.1-py3-none-any.whl|
|lxml-5.3.0-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl|
|ntlm_auth-1.5.0-py2.py3-none-any.whl|
|google_auth-2.38.0-py2.py3-none-any.whl|
|chardet-5.2.0-py3-none-any.whl|
|emaildata-0.3.4-py3-none-any.whl|
|sniffio-1.3.1-py3-none-any.whl|
|siemplify_html2text-2020.1.16-py3-none-any.whl|
|asn1crypto-1.5.1-py2.py3-none-any.whl|
|oauthlib-3.2.2-py3-none-any.whl|
|icalendar-6.0.1-py3-none-any.whl|
|RTFDE-0.1.2-py3-none-any.whl|
|TIPCommon-2.2.16-py2.py3-none-any.whl|
|extract_msg-0.52.0-py3-none-any.whl|
|urllib3-2.3.0-py3-none-any.whl|
|typing_extensions-4.12.2-py3-none-any.whl|
|charset_normalizer-3.4.1-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl|
|cached_property-2.0.1-py3-none-any.whl|
|pyasn1-0.6.1-py3-none-any.whl|
|pyOpenSSL-24.1.0-py3-none-any.whl|
|httplib2-0.22.0-py3-none-any.whl|
|tzdata-2024.2-py2.py3-none-any.whl|
|google_auth_httplib2-0.2.0-py2.py3-none-any.whl|
|google_api_python_client-2.161.0-py2.py3-none-any.whl|
|dnspython-2.7.0-py3-none-any.whl|
|idna-3.10-py3-none-any.whl|
|colorclass-2.2.2-py2.py3-none-any.whl|
|cachetools-5.5.2-py3-none-any.whl|
|python-smail-0.9.0.tar.gz|
|rsa-4.9-py3-none-any.whl|
|cffi-1.17.1-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl|
|msoffcrypto_tool-5.4.2-py3-none-any.whl|
|red-black-tree-mod-1.20.tar.gz|
|ebcdic-1.1.1-py2.py3-none-any.whl|
|requests-2.32.3-py3-none-any.whl|
|httpcore-1.0.7-py3-none-any.whl|
|pyth3-0.7-py3-none-any.whl|
|beautifulsoup4-4.12.3-py3-none-any.whl|
|pytz-2020.1-py2.py3-none-any.whl|
|httpx-0.28.1-py3-none-any.whl|
|six-1.16.0-py2.py3-none-any.whl|
|uritemplate-4.1.1-py2.py3-none-any.whl|
|protobuf-5.29.3-cp38-abi3-manylinux2014_x86_64.whl|
|h11-0.14.0-py3-none-any.whl|
|pyasn1_modules-0.4.1-py3-none-any.whl|



## Jobs

#### Oauth Token Expiry Notification Job
Note that the job is deprecated and will be removed in the next 6 months. Oauth Token Expiry Notification Job is recommended to use if integration is working with Oauth refresh tokens. Refresh tokens are valid only for 90 days, after that User will need to create a new refresh token to use in the integration. This job will send reminder emails to the configured recipient list when the token will expire in 10, 5 and 1 day. Once a new token is set in this job, the notification timer will start over.

|Name|IsMandatory|Type|DefaultValue|
|----|-----------|----|------------|
|Mail Server Address|True|None|outlook.office365.com|
|Mail Address for sending notifications|True|None||
|Notifications Recipients List|True|None||
|Client ID|True|None||
|Client Secret|False|None||
|Tenant (Directory) ID|True|None||
|Refresh Token|True|None||

#### Token Renewal Job
Token renewal job should be used to periodically update the refresh token configured for the integration. By default, the refresh token expires every 90 days, making integration unusable upon expiration. It is recommended to run this job every 7 or 14 days to make sure that refresh token will be up to date.

|Name|IsMandatory|Type|DefaultValue|
|----|-----------|----|------------|
|Integration Environments|False|None||
|Connector Names|False|None||



## Connectors
#### Exchange Mail Connector v2
Exchange Mail Connector v2

|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Environment Field Name|Describes the name of the field where the environment name is stored. If the environment field isn't found, the environment is the default environment.|False|None||
|Environment Regex Pattern|A regex pattern to run on the value found in the "Environment Field Name" field. Default is .* to catch all and return value unchanged. Used to allow the user to manipulate the environment field via regex logic. If regex pattern is null or empty, or the environment value is null, the final environment result is ""|False|None||
|Headers to add to events|Specify what headers from emails should be added to the events. Parameter accepts multiple values as a comma separated string. Provided values can be exact match or set as a regex.|False|None||
|Email exclude pattern|Regular expression to exclude specific emails from being ingested by the connector. Works with both subject and body part of email. Example is, to exclude mass mailing emails like news from being ingested.|False|None||
|Mail Server Address|Mail server IP address to connect to. If connecting to O365, server address should be set to outlook.office365.com|True|None||
|Verify SSL|If enabled, verify the SSL certificate for the connection to the Exchange server is valid.|False|None|false|
|Mail Address|Mail address to use in integration, to use for sending out emails and work with received emails for this email (mailbox)|True|None||
|Use Domain For Authentication|If enabled, value provided for domain parameter will be concatenated to authenticate on the mail server as username@domain. If “Username” is specified in the username@domain or domain\username formats, this parameter is ignored and values from “Domain” and “Username” parameters are not concatenated.|False|None|false|
|Use Delegated Access|If enabled, delegated access type will be used. Otherwise, impersonation access type is used. For details on impersonation/delegation and EWS, see the following link https://learn.microsoft.com/en-us/exchange/client-developer/exchange-web-services/impersonation-and-ews-in-exchange.|False|None|false|
|Domain|Specify the domain value to use for authentication.|True|None||
|Username|Specify Username to authenticate with on mail server. Username can be provided without the domain part or in either UPN (user@fully_qualified_DNS_domain_name) or Down-Level Logon Name (domain\username) format.|True|None||
|Password|A password to authenticate with on mail server|True|None||
|Folder to check for emails|Parameter can be used to specify email folder on the mailbox to search for the emails. Parameter should also accept comma separated list of folders to check the user response in multiple folders. Parameter is case sensitive. '/' separator can be used to specify a subfolder to search in, example: Inbox/Subfolder|True|None|Inbox|
|Unread Emails Only|If checked, cases will be pulled only from unread emails|False|None|false|
|Mark Emails as Read|If checked, after the emails have been pulled they will be marked as read|False|None|false|
|Attach Original EML|If checked, the original email will be attached to the case info as an eml file|False|None|false|
|Offset Time In Days|Number of days before the first connector iteration to retrieve emails from. This parameter applies to the initial connector iteration after you enable the connector for the first time, or used as a fallback value in cases where connector's last run timestamp expires.|True|None|5|
|Fetch Backwards Time Interval (minutes)|Time interval connector should use to fetch events from max hours backwards or connector last run timestamp. This parameter in minutes can be used to split max hours backwards on smaller segments and process them individually. Its recommended to adjust this value accordingly to the environment, for example 60 minutes or less.|False|None|0|
|Max Emails Per Cycle|Fetch x emails per connector cycle|True|None|10|
|Proxy Server Address|The address of the proxy server to use.|False|None||
|Proxy Username|The proxy username to authenticate with.|False|None||
|Proxy Password|The proxy password to authenticate with.|False|None||
|Extract urls from HTML email part?|Specify whether connector should additionally try to extract urls from html part of email. This will allow connector to extract complex urls, but urls from plain text part of email will not be extracted with this method. Extracted urls will be available in urls_from_html_part event field.|False|None|false|
|Disable Overflow|If enabled, the connector will ignore the overflow mechanism.|False|None|false|
|Original Received Mail Prefix|Prefix to add to the extracted event keys (to, from,subject,…) from the original email received in the monitored mailbox.|False|None|orig|
|Attached Mail File Prefix|Prefix to add to the extracted event keys (to, from,subject,…) from the attached mail file received with the email in the monitored mailbox.|False|None|attach|
|Create a Separate Siemplify Alert per Attached Mail File?|If enabled, connector will create multiple alerts, 1 alert per attached mail file. This behavior can be useful when processing email with multiple mail files attached and Siemplify event mapping set to create entities from attached mail file.|False|None|false|
|Case Name Template|When provided, connector will add a new key called "custom_case_name" to the Siemplify Event. It can used to have a customer case name. Please refer to the documentation portal for more details. You can provide placeholders in the following format: [name of the field]. Example: Phishing - [event_mailbox]. Note: connector will use first Siemplify Event for placeholders. Only keys that have string value will be handled.|False|None||
|Alert Name Template|If provided, connector will use this value for Siemplify Alert Name. Please refer to the documentation portal for more details. You can provide placeholders in the following format: [name of the field]. Example: Phishing - [event_mailbox]. Note: connector will use first Siemplify Event for placeholders. Only keys that have string value will be handled. If nothing is provided or user provides an invalid template, connector will use the default alert name.|False|None||
|Email Padding Period (minutes)|Specify an optional time period in minutes connector should fetch emails for prior to the latest timestamp.|False|None|0|
|URL Regex|The regex connector uses to parse URLs from the processed emails.|True|None|(?i)\[?(?:(?:(?:http|https)(?:://))|www\.(?!://))(?:[a-zA-Z0-9\-\._~:;/\?#\[\]@!\$&'\(\)\*\+,=%])+|
|Base64 Encoded Private Key|Specify a base64 encoded private key that will be used to decrypt the email.|False|None||
|Base64 Encoded Certificate|Specify a base64 encoded certificate that will be used to decrypt the email.|False|None||
|Base64 Encoded CA certificate|Specify a base64 encoded trusted CA certificate for signature verification.|False|None||
|Event Fields to Exclude|Comma-separated list of fields to exclude from events. Example: field1,field2|False|None||
|Exclude Attachments|If enabled, connector will not ingest email attachments and add them to cases.|False|None|false|


##### Allowlist
| |
|-|
||
||


#### Exchange EML Connector


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Server IP|Server IP|True|None|x.x.x.x|
|Domain|Specify the domain value to use for authentication.|True|None||
|Username|Specify Username to authenticate with on mail server. Username can be provided without the domain part or in either UPN (user@fully_qualified_DNS_domain_name) or Down-Level Logon Name (domain\username) format.|True|None||
|Password|Password|True|None||
|Mail Address|Mail Address|True|None||
|Verify SSL|If enabled, verify the SSL certificate for the connection to the Exchange server is valid.|False|None|false|
|Use Domain For Authentication|If enabled, value provided for domain parameter will be concatenated to authenticate on the mail server as username@domain. If “Username” is specified in the username@domain or domain\username formats, this parameter is ignored and values from “Domain” and “Username” parameters are not concatenated.|False|None|True|
|Use Delegated Access|If enabled, delegated access type will be used. Otherwise, impersonation access type is used. For details on impersonation/delegation and EWS, see the following link https://learn.microsoft.com/en-us/exchange/client-developer/exchange-web-services/impersonation-and-ews-in-exchange.|False|None|false|
|Folder Name|The field name used to determine the folder name. '/' separator can be used to specify a subfolder to search in, example: Inbox/Subfolder|True|None|Inbox|
|Environment Field Name|Environment Field Name|False|None||
|Environment Regex Pattern|Environment Regex Pattern|False|None||
|Unread Emails Only|Unread Emails Only|False|None|false|
|Mark Emails as Read|Mark Emails as Read|False|None|false|
|Max Days Backwards|Number of days before the first connector iteration to retrieve EML attachments from. This parameter applies to the initial connector iteration after you enable the connector for the first time, or used as a fallback value in cases where connector's last run timestamp expires.|False|None|1|
|Encode Data as UTF-8|Indicates whether to encode the email data with UTF-8 or not. Setting to True is recommended.|False|None|true|
|Attach EML or MSG File to the Case Wall|If checked, the forwarded EML or MSG file will be attached to the Case Wall.|False|None||
|Exclusion Body Regex|Exclude those emails, whose body matches this regex. For example '([N|n]ewsletter)|([O|o]ut of office)' finds all emails containing 'Newsletter' or 'Out of office' keywords.|False|None||
|Proxy Server Address|The address of the proxy server to use.|False|None||
|Proxy Username|The proxy username to authenticate with.|False|None||
|Proxy Password|The proxy password to authenticate with.|False|None||
|Extract urls from HTML email part?|Specify whether connector should additionally try to extract urls from html part of email. This will allow connector to extract complex urls, but urls from plain text part of email will not be extracted with this method. Extracted urls will be available in urls_from_html_part event field.|False|None|false|
|Event Fields to Exclude|Comma-separated list of fields to exclude from events. Example: field1,field2|False|None||
|Exclude Attachments|If enabled, connector will not ingest email attachments and add them to cases.|False|None|false|


#### Exchange Mail Connector v2 with Oauth Authentication
Connector can be used to monitor specific mailboxes on Office 365 mail servers that require Oauth authentication. Get Authorization and Generate Token actions can be used to obtain refresh token that should be set in the connector. Note: Make sure to configure the integration first for the Oauth authentication.

|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Environment Field Name|Describes the name of the field where the environment name is stored. If the environment field isn't found, the environment is the default environment.|False|None||
|Environment Regex Pattern|A regex pattern to run on the value found in the "Environment Field Name" field. Default is .* to catch all and return value unchanged. Used to allow the user to manipulate the environment field via regex logic. If regex pattern is null or empty, or the environment value is null, the final environment result is ""|False|None||
|Headers to add to events|Specify what headers from emails should be added to the events. Parameter accepts multiple values as a comma separated string. Provided values can be exact match or set as a regex.|False|None||
|Email exclude pattern|Regular expression to exclude specific emails from being ingested by the connector. Works with both subject and body part of email. Example is, to exclude mass mailing emails like news from being ingested.|False|None||
|Mail Server Address|Mail server IP address to connect to. If connecting to O365, server address should be set to outlook.office365.com|True|None|outlook.office365.com|
|Mail Address|Mail address to use for connector.|True|None||
|Client ID|For Office 365 Oauth authentication, Client (Application) ID of Azure Active Directory App that will be used for the integration.|True|None||
|Client Secret|For Office 365 Oauth authentication, secret can be provided for the auth flow.|False|None||
|Tenant (Directory) ID|For Office 365 Oauth authentication, Azure Tenant (Directory) ID.|True|None||
|Refresh Token|For Office 365 Oauth authentication, refresh token that was obtained from running “Get Authorization” and “Generate Token” actions.|True|None||
|Verify SSL|If enabled, verify the SSL certificate for the connection to the Exchange server is valid.|False|None|false|
|Folder to check for emails|Parameter can be used to specify email folder on the mailbox to search for the emails. Parameter should also accept comma separated list of folders to check the user response in multiple folders. Parameter is case sensitive. '/' separator can be used to specify a subfolder to search in, example: Inbox/Subfolder|True|None|Inbox|
|Unread Emails Only|If checked, cases will be pulled only from unread emails|False|None|false|
|Mark Emails as Read|If checked, after the emails have been pulled they will be marked as read|False|None|false|
|Use Delegated Access|If enabled, delegated access type will be used. Otherwise, impersonation access type is used. For details on impersonation/delegation and EWS, see the following link https://learn.microsoft.com/en-us/exchange/client-developer/exchange-web-services/impersonation-and-ews-in-exchange.|False|None|false|
|Attach Original EML|If checked, the original email will be attached to the case info as an eml file|False|None|false|
|Offset Time In Days|Number of days before the first connector iteration to retrieve mails from. This parameter applies to the initial connector iteration after you enable the connector for the first time, or used as a fallback value in cases where connector's last run timestamp expires.|True|None|5|
|Fetch Backwards Time Interval (minutes)|Time interval connector should use to fetch events from max hours backwards or connector last run timestamp. This parameter in minutes can be used to split max hours backwards on smaller segments and process them individually. Its recommended to adjust this value accordingly to the environment, for example 60 minutes or less.|False|None|0|
|Max Emails Per Cycle|Fetch x emails per connector cycle|True|None|10|
|Proxy Server Address|The address of the proxy server to use.|False|None||
|Proxy Username|The proxy username to authenticate with.|False|None||
|Proxy Password|The proxy password to authenticate with.|False|None||
|Extract urls from HTML email part?|Specify whether connector should additionally try to extract urls from html part of email. This will allow connector to extract complex urls, but urls from plain text part of email will not be extracted with this method. Extracted urls will be available in urls_from_html_part event field.|False|None|false|
|Disable Overflow|If enabled, the connector will ignore the overflow mechanism.|False|None|false|
|Original Received Mail Prefix|Prefix to add to the extracted event keys (to, from,subject,…) from the original email received in the monitored mailbox.|False|None|orig|
|Attached Mail File Prefix|Prefix to add to the extracted event keys (to, from,subject,…) from the attached mail file received with the email in the monitored mailbox.|False|None|attach|
|Create a Separate Siemplify Alert per Attached Mail File?|If enabled, connector will create multiple alerts, 1 alert per attached mail file. This behavior can be useful when processing email with multiple mail files attached and Siemplify event mapping set to create entities from attached mail file.|False|None|false|
|Case Name Template|When provided, connector will add a new key called "custom_case_name" to the Siemplify Event. It can used to have a customer case name. Please refer to the documentation portal for more details. You can provide placeholders in the following format: [name of the field]. Example: Phishing - [event_mailbox]. Note: connector will use first Siemplify Event for placeholders. Only keys that have string value will be handled.|False|None||
|Alert Name Template|If provided, connector will use this value for Siemplify Alert Name. Please refer to the documentation portal for more details. You can provide placeholders in the following format: [name of the field]. Example: Phishing - [event_mailbox]. Note: connector will use first Siemplify Event for placeholders. Only keys that have string value will be handled. If nothing is provided or user provides an invalid template, connector will use the default alert name.|False|None||
|Email Padding Period (minutes)|Specify an optional time period in minutes connector should fetch emails for prior to the latest timestamp.|False|None|0|
|URL Regex|The regex connector uses to parse URLs from the processed emails.|True|None|(?i)\[?(?:(?:(?:http|https)(?:://))|www\.(?!://))(?:[a-zA-Z0-9\-\._~:;/\?#\[\]@!\$&'\(\)\*\+,=%])+|
|Base64 Encoded Private Key|Specify a base64 encoded private key that will be used to decrypt the email.|False|None||
|Base64 Encoded Certificate|Specify a base64 encoded certificate that will be used to decrypt the email.|False|None||
|Base64 Encoded CA certificate|Specify a base64 encoded trusted CA certificate for signature verification.|False|None||
|Event Fields to Exclude|Comma-separated list of fields to exclude from events. Example: field1,field2|False|None||
|Exclude Attachments|If enabled, connector will not ingest email attachments and add them to cases.|False|None|false|


##### Allowlist
| |
|-|
||
||


#### Exchange Mail Connector
Exchange Mail Connector

|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Server Ip|x.x.x.x|True|None||
|Domain|Specify the domain value to use for authentication.|True|None||
|Username|Specify Username to authenticate with on mail server. Username can be provided without the domain part or in either UPN (user@fully_qualified_DNS_domain_name) or Down-Level Logon Name (domain\username) format.|False|None||
|Password|Password|True|None||
|Mail Address|Mail address to pull emails from. e.g. user@domain.com|True|None||
|Verify SSL|If enabled, verify the SSL certificate for the connection to the Exchange server is valid.|False|None|false|
|Use Domain For Authentication|If enabled, value provided for domain parameter will be concatenated to authenticate on the mail server as username@domain. If “Username” is specified in the username@domain or domain\username formats, this parameter is ignored and values from “Domain” and “Username” parameters are not concatenated.|False|None|True|
|Use Delegated Access|If enabled, delegated access type will be used. Otherwise, impersonation access type is used. For details on impersonation/delegation and EWS, see the following link https://learn.microsoft.com/en-us/exchange/client-developer/exchange-web-services/impersonation-and-ews-in-exchange.|False|None|false|
|Unread Emails Only|If checked, pull only unread mails|False|None|True|
|Mark Emails as Read|If checked, mark mails as read after pulling them|False|None|False|
|Attach Original EML|If checked, attach the original message as eml file.|False|None|false|
|Folder Name|The field name used to determine the folder name. '/' separator can be used to specify a subfolder to search in, example: Inbox/Subfolder|True|None|Inbox|
|Environment Field Name|If defined - connector will extract the environment from the specified event field. You can manipulate the field data using the Regex pattern field to extract specific string. In case the the extracted environment field and Siemplify environment name are not equal - you can map them in the map.json that is auto-generated on the first run, inside the <run-folder>.<run-folder> = C:\Siemplify_Server\Scripting\SiemplifyConnectorExecution<Connector_Folder>|False|None||
|Environment Regex Pattern|If defined - the connector will implement the specific RegEx pattern on the data from "envirnment field" to extract specific string. For example - extract domain from sender's address: "(?<=@)(\S+$)"|False|None||
|Max Days Backwards|Number of days before the first connector iteration to retrieve mails from. This parameter applies to the initial connector iteration after you enable the connector for the first time, or used as a fallback value in cases where connector's last run timestamp expires. e.g. 3|True|None|5|
|Exclusion Subject Regex|Exclude those emails, whose subject matches this regex. For example '([N|n]ewsletter)|([O|o]ut of office)' finds all emails containing 'Newsletter' or 'Out of office' keywords.|False|None||
|Exclusion Body Regex|Exclude those emails, whose body matches this regex. For example '([N|n]ewsletter)|([O|o]ut of office)' finds all emails containing 'Newsletter' or 'Out of office' keywords.|False|None||
|Proxy Server Address|The address of the proxy server to use.|False|None||
|Proxy Username|The proxy username to authenticate with.|False|None||
|Proxy Password|The proxy password to authenticate with.|False|None||
|Event Fields to Exclude|Comma-separated list of fields to exclude from events. Example: field1,field2|False|None||
|Exclude Attachments|If enabled, connector will not ingest email attachments and add them to cases.|False|None|false|




