<p align="center"><img src="./Resources/CrowdStrikeFalcon.svg" 
     alt="CrowdStrikeFalcon" width="200"/></p>

# CrowdStrikeFalcon

CrowdStrike Falcon is the leader in next-generation endpoint protection, threat intelligence and incident response through cloud-based endpoint protection.

Python Version - V3_11


#### Dependencies
| |
|-|
|PyJWT-2.9.0-py3-none-any.whl|
|httpcore-1.0.6-py3-none-any.whl|
|pycryptodome-3.21.0-cp36-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl|
|requests_toolbelt-1.0.0-py2.py3-none-any.whl|
|EnvironmentCommon-1.0.1-py2.py3-none-any.whl|
|filelock-3.15.4-py3-none-any.whl|
|httpx-0.27.2-py3-none-any.whl|
|pycparser-2.22-py3-none-any.whl|
|googleapis_common_protos-1.66.0-py2.py3-none-any.whl|
|requests_file-2.1.0-py2.py3-none-any.whl|
|chardet-5.2.0-py3-none-any.whl|
|sniffio-1.3.1-py3-none-any.whl|
|pyasn1-0.6.1-py3-none-any.whl|
|httplib2-0.22.0-py3-none-any.whl|
|cachetools-5.5.0-py3-none-any.whl|
|google_auth_httplib2-0.2.0-py2.py3-none-any.whl|
|cryptography-43.0.1-cp39-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl|
|certifi-2024.8.30-py3-none-any.whl|
|google_api_core-2.23.0-py3-none-any.whl|
|idna-3.10-py3-none-any.whl|
|charset_normalizer-3.4.0-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl|
|protobuf-5.28.3-cp38-abi3-manylinux2014_x86_64.whl|
|TIPCommon-2.0.4-py2.py3-none-any.whl|
|anyio-4.6.2.post1-py3-none-any.whl|
|rsa-4.9-py3-none-any.whl|
|cffi-1.17.1-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl|
|google_api_python_client-2.152.0-py2.py3-none-any.whl|
|pyparsing-3.2.0-py3-none-any.whl|
|requests-2.32.3-py3-none-any.whl|
|urllib3-2.2.2-py3-none-any.whl|
|tldextract-5.1.2-py3-none-any.whl|
|google_auth-2.36.0-py2.py3-none-any.whl|
|uritemplate-4.1.1-py2.py3-none-any.whl|
|pyOpenSSL-24.2.1-py3-none-any.whl|
|h11-0.14.0-py3-none-any.whl|
|proto_plus-1.25.0-py3-none-any.whl|
|pyasn1_modules-0.4.1-py3-none-any.whl|


## Actions
#### Download File
Download files from the hosts in Crowdstrike Falcon. Supported entities: File Name, IP Address and Hostname. Note: action requires both File Name and IP Address/Hostname entity to be in the scope of the Siemplify alert. The downloaded file will be in password-protected zip. Password is "infected".
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
||Specify the ID of the customer for which you want to execute the action.||None||
||Specify the path to the folder, where you want to store the threat file.||None||
||If enabled, action will overwrite the file with the same name.||None||



#### Add Alert Comment
Add a comment to alert in Crowdstrike. 
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
||Specify the ID of the alert that needs to be updated.||None||
||Specify the comment for the alert.||None||



#### Add Identity Protection Detection Comment
Add a comment to identity protection detection in Crowdstrike.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
||Specify the ID of the detection that needs to be updated.||None||
||Specify the comment for the detection.||None||



#### Add Incident Comment
Deprecated. Add comment to incident in Crowdstrike.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
||Specify the ID of the incident that needs to be updated.||None||
||Specify the comment for the incident.||None||



#### Close Detection
Deprecated. Close a Crowdstrike Falcon detection. Note: Action "Update Detection" is the best practice for this use case.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
||Specify the id of the detection that needs to be closed.||None||
||If enabled, action will hide the detection in the UI.||None||



#### Add Comment to Detection
Deprecated. Add a comment to the detection in Crowdstrike Falcon.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
||Specify the id of the detection to which you want to add a comment.||None||
||Specify the comment that needs to be added to the detection.||None||



#### Delete IOC
Delete custom IOCs in Crowdstrike Falcon. Supported entities: Hostname, URL, IP address and Hash. Note: Hostname entities are treated as domain IOCs and action will extract domain part out of URLs. Only MD5 and SHA-256 hashes are supported.
Timeout - 600 Seconds



#### Contain Endpoint
Contain endpoint in Crowdstrike Falcon. Supported entities: Hostname and IP address.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
||Specify the ID of the customer for which you want to execute the action.||None||
||If enabled, action will be failed, if not all of the endpoints were contained.||None||



#### Get Hosts by IOC
DEPRECATED. List hosts related to the IOCs in Crowdstrike Falcon. Supported entities: Hostname, URL, IP address and Hash. Note: Hostname entities are treated as domain IOCs and action will extract domain part out of URLs. Only MD5 and SHA-256 hashes are supported.
Timeout - 600 Seconds



#### On-Demand Scan
Scan the endpoint on demand in Crowdstrike. Note: only Windows hosts are supported. Supported entities: IP Address, Hostname. Note: Action is running as async, please adjust script timeout value in Chronicle SecOps IDE for action, as needed.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
||Specify the ID of the customer for which you want to execute the action.||None||
||Comma-separated list of paths to scan.||None||
||Comma-separated list of paths to exclude from scanning.||None||
||Comma-separated list of host group names to initiate scanning for. Note: Separate scanning process is created for each host group.||None||
||Description for the scan. If no value is provided, the action sets the description to the following: "Scan initialized by Chronicle SecOps."||None||
||The amount of CPU to  use for the underlying host during scanning.||None||
||Specify the sensor anti-malware detection level. Note: Detection level must be equal to or higher than the Prevention level.||None||
||Specify the sensor anti-malware prevention level. Note: Detection level must be equal to or higher than the Prevention level.||None||
||Specify the cloud anti-malware detection level. Note: Detection level must be equal to or higher than the Prevention level.||None||
||Specify the cloud anti-malware prevention level. Note: Detection level must be equal to or higher than the Prevention level.||None||
||If enabled, underlying hosts are quarantined as part of scanning.||None||
||If enabled, the scanning process creates an endpoint notification.||None||
||Number of hours for a scan to run. If no value is provided, the scan runs continuously.||None||
||Comma-separated list of hostnames on which you want to execute the action. Note: action will run the action on both entities + this parameter values.||None||



#### Update Alert
Update an alert in Crowdstrike.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
||Specify the ID of the alert that needs to be updated.||None||
||Specify the status for the alert.||None||
||Specify the verdict for the alert.||None||
||Specify the name of the analyst to whom the alert needs to be assigned. If "Unassign" is provided, action will remove assignment from the alert. Note: API will accept any value that is provided, even if the underlying user doesn’t exist.||None||



#### Get Host Information
Retrieve information about the hostname from Crowdstrike Falcon. Supported entities: Hostname, IP Address.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
||Specify the ID of the customer for which you want to execute the action.||None||
||If enabled, action will create insights containing information regarding entities.||None||



#### Lift Contained Endpoint
Lift endpoint containment in Crowdstrike Falcon. Supported entities: Hostname and IP address.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
||Specify the ID of the customer for which you want to execute the action.||None||
||If enabled, action will be failed, if containment was not lifted on all endpoints.||None||



#### Hide Hosts
Use the Hide Hosts action to hide one or more hosts from the CrowdStrike Falcon console. Supported entities: IP Address, Hostname.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
||A comma-separated list of hostnames to hide in CrowdStrike Falcon. The action processes both the input values provided in this parameter and the Hostname and IP Address entities attached to the case.||None||
||The unique CrowdStrike Customer ID (CID) used to target a specific tenant. This parameter is required in Falcon Flight Control or multi-tenant environments to perform the action on a specific child CID.||None||



#### Ping
Test Connectivity
Timeout - 600 Seconds



#### Run Script
Execute a powershell script on the endpoints in Crowdstrike. Supported entities: IP Address, Hostname. Note: Action is running as async, please adjust script timeout value in Google SecOps IDE for the action, as needed.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
||Specify the ID of the customer for which you want to execute the action.||None||
||The name of the script file that needs to be executed. Note: either “Script Name” or “Raw Script” should be provided. If both “Script Name” and “Raw Script” are provided, then “Raw Script” will have the priority.||None||
||Raw powershell script payload that needs to be executed on the endpoints. Note: either “Script Name” or “Raw Script” should be provided. If both “Script Name” and “Raw Script” are provided, then “Raw Script” will have the priority.||None||
||Comma-separated list of hostnames on which you want to execute the action. Note: action will run the action on both entities + this parameter values.||None||
||If enabled, commands targeting offline hosts are queued and executed once the host reconnects to the network.||None||



#### Get Event Offset
Action will retrieve the event offset that is used by the Event Streaming Connector. Note: action starts processing events from 30 days ago.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
||Specify how many events the action needs to process starting from the offset from 30 days ago.||None||



#### Get Process Name By IOC
DEPRECATED. Retrieve processes related to the IOCs and provided devices in Crowdstrike Falcon. Supported entities: Hostname, URL, IP address and Hash. Note: Hostname entities are treated as domain IOCs and action will extract domain part out of URLs. Only MD5 and SHA-256 hashes are supported. IP address entities are treated as IOCs.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
||Specify a comma-separated list of devices for which you want to retrieve processes related to entities.||None||



#### Search Events
Search events in Crowdstrike. Note: Action is running as async, please adjust script timeout value in Google SecOps IDE for action, as needed.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
||Repository that should be searched.||None||
||Query that needs to be executed in Crowdstrike. Note: don't provide "head" as part of the query. Action will provide it automatically based on the value provided in the "Max Results To Return" parameter.||None||
||Time frame for the results. If "Custom" is selected, you also need to provide "Start Time".||None||
||Start time for the results. This parameter is mandatory, if "Custom" is selected for the "Time Frame" parameter. Format: ISO 8601.||None||
||End time for the results. Format: ISO 8601. If nothing is provided and "Custom" is selected for the "Time Frame" parameter then this parameter will use current time.||None||
||How many results to return for the query. Action will append "head" to the provided query. Default: 50. Maximum: 1000.||None||



#### List Host Vulnerabilities
List vulnerabilities found on the host in Crowdstrike Falcon. Supported entities: IP Address and Hostname. Note: requires Falcon Spotlight license and permissions. 
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
||Specify the ID of the customer for which you want to execute the action.||None||
||Specify the comma-separated list of severities for vulnerabilities.If nothing is provided, action will ingest all related vulnerabilities. Possible values: Critical, High, Medium, Low, Unknown.||None||
||If enabled, action will create an insight per entity containing statistical information about related vulnerabilities.||None||
||Specify how many vulnerabilities to return per host. If nothing is provided action will process all of the related vulnerabilities.||None||



#### Submit URL
Submit urls to a sandbox in Crowdstrike. Note: This action requires a Falcon Sandbox license.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
||Specify the URLs that need to be submitted.||None||
||Specify the sandbox environment for the analysis.||None||
||Specify the network environment for the analysis.||None||
||If enabled, the action checks if the file was already submitted previously and returns an available report. Note: during the validation “Network Environment” and “Sandbox Environment” are not taken into consideration.||None||



#### Submit File
Submit files to a sandbox in Crowdstrike. Note: This action requires a Falcon Sandbox license. For the list of supported file formats, refer to the documentation portal.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
||Specify the file paths to the files that need to be submitted. Refer to the documentation portal for a list of the supported file formats.||None||
||Specify the sandbox environment for the analysis.||None||
||Specify the network environment for the analysis.||None||
||Specify the password that would need to be used, when working with archive files.||None||
||Specify the password that would need to be used, when working with Adobe or Office files. Maximum: 32 characters.||None||
||If enabled, the action checks if the file was already submitted previously and returns the available report. Note: during the validation “Network Environment” and “Sandbox Environment” are not taken into consideration.||None||
||Specify the comment for the submission.||None||
||If enabled, the file is only shown to users within your customer account.||None||



#### Update Detection
Deprecated. Update detection in Crowdstrike Falcon.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
||Specify the ID of the detection that needs to be updated.||None||
||Specify the new status for the detection.||None||
||Specify the email address of the Crowdstrike Falcon user, who needs to be assigned to this detection||None||



#### Update IOC Information
Update information about custom IOCs in Crowdstrike Falcon. Supported entities: Hostname, URL, IP address and Hash. Note: Hostname entities are treated as domain IOCs and action will extract domain part out of URLs. Only MD5 and SHA-256 hashes are supported.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
||Specify a new description for custom IOCs.||None||
||Specify the source for custom IOCs.||None||
||Specify the amount of days till expiration.||None||
||If enabled, IOCs that have been identifed, will send a notification. In other case, no action will be taken||None||



#### Get Alert Details
Get details of an alert in Crowdstrike.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
||Specify the ID of the alert.||None||



#### Update Identity Protection Detection
Update an identity protection detection in Crowdstrike. Note: this action requires an Identity Protection license.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
||Specify the ID of the detection that needs to be updated.||None||
||Specify the status for the detection.||None||
||Specify the name of the analyst to whom the detection needs to be assigned. If "Unassign" is provided, action will remove assignment from the detection. Note: API will accept any value that is provided, even if the underlying user doesn't exist.||None||



#### Upload IOCs
Add custom IOCs in Crowdstrike Falcon. Supported entities: Hostname, URL, IP address and Hash. Note: Hostname entities are treated as domain IOCs and action will extract domain part out of URLs. Only MD5 and SHA-256 hashes are supported.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
||Specify a comment with more context related to IOC.||None||
||Specify the name of the host group.||None||
||Specify the action for the uploaded IOCs. Note: "Block" action can only be applied to hashes. Action will always apply "Detect" policy to all other IOC types.||None||
||The number of days before the IOC expires.||None||
||Specify a comma-separated list of the platforms related to the IOC. Possible values: Windows, Linux, Mac.||None||
||Specify the severity for the IOC.||None||



#### Update Incident
Deprecated. Update incident in Crowdstrike.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
||Specify the ID of the customer for which you want to execute the action.||None||
||Specify the ID of the incident that needs to be updated.||None||
||Specify the status for the incident.||None||
||Specify the name or email of the analyst to whom the incident needs to be assigned. If "Unassign" is provided, action will remove assignment from the incident. Note: for name you need to provide first and last name of the analyst in the following format "{first name} {last name}"||None||



#### List Uploaded IOCs
List available custom IOCs in CrowdStrike Falcon.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
||Specify a comma-separated list of IOC types that should be returned. If nothing is provided, action will return IOCs from all types. Possible values: ipv4,ipv6,md5,sha256,domain.||None||
||Specify the value filter logic. If "Equal" is selected, action will try to find the exact match among IOCs and if "Contains" is selected, action will try to find IOCs that contain that substring.||None||
||Specify the string that should be searched among IOCs.||None||
||Specify how many IOCs to return. Default: 50. Maximum: 500.||None||



#### List Hosts
List available hosts in Crowdstrike Falcon.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
||Specify the ID of the customer for which you want to execute the action.||None||
||Specify what logic should be used, when searching for hosts.||None||
||Specify the value that should be used to filter hosts.||None||
||Specify how many hosts to return. Default: 50. Maximum: 1000.||None||



#### Execute Command
Execute commands on the hosts in Crowdstrike Falcon. Supported entities: IP Address and Hostname.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
||Specify the ID of the customer for which you want to execute the action.||None||
||Specify what command to execute on the hosts.||None||
||If enabled, action will execute commands with the admin level permissions. This is necessary for certain commands like "put".||None||
||Comma-separated list of hostnames on which you want to execute the action. Note: action will run the action on both entities + this parameter values.||None||
||If enabled, commands targeting offline hosts are queued and executed once the host reconnects to the network.||None||









## Connectors
#### Crowdstrike - Alerts Connector
Pull alerts from Crowdstrike. Dynamic List works with the "display_name" parameter. Note: To fetch identity protection detections use "Identity Protection Detections Connector".

|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
||Describes the name of the field where the environment name is stored. If the environment field isn't found, the environment is the default environment.||None||
||A regex pattern to run on the value found in the "Environment Field Name" field. Default is .* to catch all and return the value unchanged. Used to allow the user to manipulate the environment field through regex logic. If the regex pattern is null or empty, or the environment value is null, the final environment result is the default environment.||None|.*|
||API root of the Crowdstrike instance.||None|https://api.crowdstrike.com|
||Client ID  of the Crowdstrike account.||None||
||Client Secret of the Crowdstrike account.||None||
||Lowest severity score of the identity protection detections to fetch. If nothing is provided, the connector will ingest detections with all severities. Maximum is 100. Note: action also supports the following values: Informational, Low, Medium, High, Critical.||None||
||Number of hours before the first connector iteration to retrieve alerts from. This parameter applies to the initial connector iteration after you enable the connector for the first time, or used as a fallback value in cases where connector's last run timestamp expires.||None|1|
||How many alerts to process per one connector iteration. Default: 10.||None|10|
||If enabled, connector will also fetch alerts that are labeled as "hidden" by Crowdstrike.||None|true|
||Fallback severity for the SecOps alert that should be applied to the Crowdstrike alerts, which are missing severity information. Possible values: Informational, Low, Medium, High, Critical. If nothing is provided, connector will use "Informational" severity.||None|Informational|
||If enabled, the dynamic list will be used as a blocklist.||None|false|
||If enabled, verify the SSL certificate for the connection to the Crowdstrike server is valid.||None|false|
||If enabled, connector will ignore the overflow mechanism.||None|false|
||The address of the proxy server to use.||None||
||The proxy username to authenticate with.||None||
||The proxy password to authenticate with.||None||
||When provided, connector will add a new key called "custom_case_name" to the Google Secops Event. It can used to have a customer case name. Please refer to the documentation portal for more details. You can provide placeholders in the following format: [name of the field]. Example: Phishing - [event_mailbox]. Note: connector will use first Google Secops Event for placeholders. Only keys that have string value will be handled.||None||
||If provided, connector will use this value for Google Secops Alert Name. Please refer to the documentation portal for more details. You can provide placeholders in the following format: [name of the field]. Example: Phishing - [event_mailbox]. Note: connector will use first Google Secops Event for placeholders. Only keys that have string value will be handled. If nothing is provided or user provides an invalid template, connector will use the default alert name.||None||
||The customer ID of the tenant in which to execute the integration. For use in multi-tenant (MSSP) environments.||None||


#### Crowdstrike - Detections Connector
Deprecated. Pull detections from Crowdstrike. Whitelist works with filters that are supported by the API of Crowdstrike. For the details, please refer to the documentation portal.

|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
||Describes the name of the field where the environment name is stored. If the environment field isn't found, the environment is the default environment.||None||
||A regex pattern to run on the value found in the "Environment Field Name" field. Default is .* to catch all and return the value unchanged. Used to allow the user to manipulate the environment field via regex logic. If the regex pattern is null or empty, or the environment value is null, the final environment result is the default environment.||None|.*|
||API root of the Crowdstrike instance.||None|https://api.crowdstrike.com|
||Client ID  of the Crowdstrike account.||None||
||Client Secret of the Crowdstrike account.||None||
||Lowest severity score of the detections to fetch. If nothing is provided, the connector won't apply this filter. Maximum is 100. Note: action also supports the following values: Low, Medium, High, Critical.||None|50|
||Lowest confidence score of the detections to fetch. If nothing is provided, the connector won't apply this filter. Maximum is 100.||None|0|
||Number of hours before the first connector iteration to retrieve detections from. This parameter applies to the initial connector iteration after you enable the connector for the first time, or used as a fallback value in cases where connector's last run timestamp expires.||None|1|
||How many detections to process per one connector iteration. Default: 10.||None|10|
||The number of hours that connector will use for padding. Maximum: 6.||None|1|
||If enabled, connector will ignore the overflow mechanism.||None|false|
||If enabled, verify the SSL certificate for the connection to the Crowdstrike server is valid.||None|false|
||The address of the proxy server to use.||None||
||The proxy username to authenticate with.||None||
||The proxy password to authenticate with.||None||
||When provided, connector will add a new key called "custom_case_name" to the Google Secops Event. It can used to have a customer case name. Please refer to the documentation portal for more details. You can provide placeholders in the following format: [name of the field]. Example: Phishing - [event_mailbox]. Note: connector will use first Google Secops Event for placeholders. Only keys that have string value will be handled.||None||
||If provided, connector will use this value for Google Secops Alert Name. Please refer to the documentation portal for more details. You can provide placeholders in the following format: [name of the field]. Example: Phishing - [event_mailbox]. Note: connector will use first Google Secops Event for placeholders. Only keys that have string value will be handled. If nothing is provided or user provides an invalid template, connector will use the default alert name.||None||
||The customer ID of the tenant in which to execute the integration. For use in multi-tenant (MSSP) environments.||None||


#### Crowdstrike - Identity Protection Detections Connector
Pull Identity Protection detections from Crowdstrike. Note: this connector requires an Identity Protection license. Dynamic List works with the “display_name” parameter.

|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
||Describes the name of the field where the environment name is stored. If the environment field isn't found, the environment is the default environment.||None||
||A regex pattern to run on the value found in the "Environment Field Name" field. Default is .* to catch all and return the value unchanged. Used to allow the user to manipulate the environment field through regex logic. If the regex pattern is null or empty, or the environment value is null, the final environment result is the default environment.||None|.*|
||API root of the Crowdstrike instance.||None|https://api.crowdstrike.com|
||Client ID  of the Crowdstrike account.||None||
||Client Secret of the Crowdstrike account.||None||
||Lowest severity score of the identity protection detections to fetch. If nothing is provided, the connector will ingest detections with all severities. Maximum is 100. Note: action also supports the following values: Informational, Low, Medium, High, Critical.||None||
||Number of hours before the first connector iteration to retrieve detections from. This parameter applies to the initial connector iteration after you enable the connector for the first time, or used as a fallback value in cases where connector's last run timestamp expires.||None|1|
||How many identity protection detections to process per one connector iteration. Default: 10.||None|10|
||If enabled, the dynamic list will be used as a blocklist.||None|true|
||If enabled, connector will ignore the overflow mechanism.||None|false|
||If enabled, verify the SSL certificate for the connection to the Crowdstrike server is valid.||None|false|
||The address of the proxy server to use.||None||
||The proxy username to authenticate with.||None||
||The proxy password to authenticate with.||None||
||When provided, connector will add a new key called "custom_case_name" to the Google Secops Event. It can used to have a customer case name. Please refer to the documentation portal for more details. You can provide placeholders in the following format: [name of the field]. Example: Phishing - [event_mailbox]. Note: connector will use first Google Secops Event for placeholders. Only keys that have string value will be handled.||None||
||If provided, connector will use this value for Google Secops Alert Name. Please refer to the documentation portal for more details. You can provide placeholders in the following format: [name of the field]. Example: Phishing - [event_mailbox]. Note: connector will use first Google Secops Event for placeholders. Only keys that have string value will be handled. If nothing is provided or user provides an invalid template, connector will use the default alert name.||None||
||The customer ID of the tenant in which to execute the integration. For use in multi-tenant (MSSP) environments.||None||


#### Crowdstrike - Incidents Connector
Deprecated. Pull incident and related behaviors from Crowdstrike. Dynamic List works with the “incident_type” parameter.

|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
||API root of the Crowdstrike instance.||None|https://api.crowdstrike.com|
||Client ID  of the Crowdstrike account.||None||
||Client Secret of the Crowdstrike account.||None||
||Number of hours before the first connector iteration to retrieve incidents from. This parameter applies to the initial connector iteration after you enable the connector for the first time, or used as a fallback value in cases where connector's last run timestamp expires. Default: 1||None|1|
||Describes the name of the field where the environment name is stored. If the environment field isn't found, the environment is the default environment.||None||
||A regex pattern to run on the value found in the "Environment Field Name" field. Default is .* to catch all and return the value unchanged. Used to allow the user to manipulate the environment field via regex logic. If the regex pattern is null or empty, or the environment value is null, the final environment result is the default environment.||None|.*|
||Lowest severity score of the incidents to fetch. If nothing is provided, the connector will ingest incidents with all severities. Maximum is 100. Note: action also supports the following values: Low, Medium, High, Critical. In the Crowdstrike UI the same value is presented as divided by 10.||None||
||How many incidents to process per one connector iteration. Default: 10. Max: 100.||None|10|
||If enabled, the dynamic list will be used as a blocklist.||None|false|
||If enabled, connector will ignore the overflow mechanism.||None|false|
||If enabled, verify the SSL certificate for the connection to the Crowdstrike server is valid.||None|false|
||The address of the proxy server to use.||None||
||The proxy username to authenticate with.||None||
||The proxy password to authenticate with.||None||
||The customer ID of the tenant in which to execute the integration. For use in multi-tenant (MSSP) environments.||None||


#### Crowdstrike Falcon Streaming Events Connector
Crowdstrike Falcon Streaming Events Connector

|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
||Describes the name of the field where the environment name is stored. If environment field isn't found, environment is ""||None||
||A regex pattern to run on the value found in the "Environment Field Name" field.||None||
||API root of the Crowdstrike instance||None|https://api.crowdstrike.com|
||Client ID for Crowdstrike API||None||
||Client Secret for Crowdstrike API||None||
||Specify a comma-separated list of event types. Examples of the event types: DetectionSummaryEvent, IncidentSummaryEvent, UserActivityAuditEvent, RemoteResponseSessionStartEvent, RemoteResponseSessionEndEvent, EppDetectionSummaryEvent. For more information visit documentation portal.||None|DetectionSummaryEvent, IncidentSummaryEvent, UserActivityAuditEvent, RemoteResponseSessionStartEvent, RemoteResponseSessionEndEvent, EppDetectionSummaryEvent|
||Max events to process per connector run.||None|100|
||Number of days before the first connector iteration to retrieve events from. This parameter applies to the initial connector iteration after you enable the connector for the first time, or used as a fallback value in cases where connector's last run timestamp expires.||None|3|
||Specify the events that should be ingested based on the events severity (detections events). The value ranges from 0-5. If other event types besides detections are ingested by the connector, connector sets a severity for them as -1 and this filter is not applied to those types of events||None|0|
||If provided, connector will use this value for Siemplify Alert Name. Please refer to the documentation portal for more details. You can provide placeholders in the following format: [name of the field]. Example: Phishing - [event_mailbox]. Note: connector will use first Siemplify Event for placeholders. Only keys that have string value will be handled. If nothing is provided or user provides an invalid template, connector will use the default alert name.||None||
||	If provided, the connector will use this value for Siemplify Rule Generator. Please refer to the documentation portal for more details. You can provide placeholders in the following format: [name of the field]. Example: Phishing - [event_mailbox]. Note: connector will use the first Siemplify event for placeholders. Only keys that have string value will be handled. If nothing is provided or the user provides an invalid template, the connector will use the default rule generator.||None||
||Proxy server address.||None||
||Proxy username.||None||
||Proxy password.||None||
||If enabled, connector will ignore the overflow mechanism.||None|false|
||Indicate whether to use SSL in the session or not||None|false|
||The customer ID of the tenant in which to execute the integration. For use in multi-tenant (MSSP) environments.||None||




