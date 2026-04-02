
# GoogleChronicle

Google SecOps enables you to examine the aggregated security information for your enterprise going back for months or longer. Use Google SecOps to search across all of the domains accessed from within your enterprise. To enable the Google API client to communicate with the Backstory API you will need Google Developer Service Account Credential, https://developers.google.com/identity/protocols/OAuth2#serviceaccount.

Python Version - V3_11


#### Dependencies
| |
|-|
|anyio-4.8.0-py3-none-any.whl|
|pyparsing-3.2.1-py3-none-any.whl|
|proto_plus-1.26.0-py3-none-any.whl|
|pycryptodome-3.21.0-cp36-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl|
|google_api_core-2.24.1-py3-none-any.whl|
|certifi-2025.1.31-py3-none-any.whl|
|requests_file-2.1.0-py2.py3-none-any.whl|
|google_auth-2.38.0-py2.py3-none-any.whl|
|cachetools-5.5.1-py3-none-any.whl|
|sniffio-1.3.1-py3-none-any.whl|
|googleapis_common_protos-1.67.0-py2.py3-none-any.whl|
|urllib3-2.3.0-py3-none-any.whl|
|typing_extensions-4.12.2-py3-none-any.whl|
|charset_normalizer-3.4.1-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl|
|pyasn1-0.6.1-py3-none-any.whl|
|httplib2-0.22.0-py3-none-any.whl|
|google_auth_httplib2-0.2.0-py2.py3-none-any.whl|
|google_api_python_client-2.161.0-py2.py3-none-any.whl|
|tldextract-5.1.3-py3-none-any.whl|
|regex-2024.11.6-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl|
|idna-3.10-py3-none-any.whl|
|rsa-4.9-py3-none-any.whl|
|filelock-3.16.1-py3-none-any.whl|
|requests-2.32.3-py3-none-any.whl|
|httpcore-1.0.7-py3-none-any.whl|
|httpx-0.28.1-py3-none-any.whl|
|EnvironmentCommon-1.0.2-py2.py3-none-any.whl|
|uritemplate-4.1.1-py2.py3-none-any.whl|
|TIPCommon-2.2.10-py2.py3-none-any.whl|
|protobuf-5.29.3-cp38-abi3-manylinux2014_x86_64.whl|
|h11-0.14.0-py3-none-any.whl|
|pyasn1_modules-0.4.1-py3-none-any.whl|


## Actions
#### Execute UDM Query
Execute custom UDM query in Google Chronicle. Note: 120 action executions are allowed per hour. Aggregated queries are supported only via Chronicle API configuration of integration.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
||Specify the query that needs to be executed in Chronicle.|True|None||
||If selected, the action retrieves the original raw log file associated with the UDM search results. Raw Log data is not available for aggregated searches. This option is only available when using Chronicle API authentication.|False|None||
||Specify a time frame for the results. If "Alert Time Till Now" is selected, action will use start time of the alert as start time for the search and end time will be current time. If "30 Minutes Around Alert Time" is selected, action will search the alerts 30 minutes before the alert happened till the 30 minutes after the alert has happened.  Same idea applies to "1 Hour Around Alert Time" and "5 Minutes Around Alert Time". If "Custom" is selected, you also need to provide "Start Time".|False|None||
||Specify the start time for the results. This parameter is mandatory, if "Custom" is selected for the "Time Frame" parameter. Format: ISO 8601. Note: The maximum time window (start time to end time) is 90 days.|False|None||
||Specify the end time for the results. Format: ISO 8601. If nothing is provided and "Custom" is selected for the "Time Frame" parameter then this parameter will use current time. Note: The maximum time window (start time to end time) is 90 days.|False|None||
||Specify how many results to return for the query. Default: 50. Maximum: 10000.|False|None||



#### Generate UDM Query
Preview. Use the Generate UDM Query action to construct complex UDM queries using natural language prompts in Google SecOps. Note: This action requires Chronicle API authentication. The legacy Backstory API authentication is not supported.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
||The prompt that the system uses to generate the structured UDM query.|True|None||



#### Get Rule Details
Fetch information about a rule in Google Chronicle.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
||Specify the ID of the rule for which you want to fetch details.|True|None||



#### Add Values To Reference List
Add values to a reference list in Google Chronicle.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
||Specify the display name of the reference list that needs to be updated|True|None||
||Specify a comma-separated list of values that need to be added to a reference list|True|None||



#### Enrich Domain
Deprecated - Enrich domains using information from IOCs in Google Chronicle. Supported entities: Hostname, URL (action extracts domain part).
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
||If enabled, action will create an insight containing information about the entities.|False|None||
||If enabled, action will only create an insight for entities that are marked as suspicious. Note: "Create Insight" parameter needs to be enabled.|False|None||
||Specify the lowest severity that should be associated with domain in order to mark it suspicious.|True|None||
||If enabled, action will mark the entity as suspicious, if information about severity is not available.|False|None||



#### Remove Rows From Data Table
Remove rows from a data table in Google SecOps. Note: this action only works with Chronicle API authentication. Backstory API is not supported.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
||Specify the display name of the data table that needs to be updated.|True|None||
||Specify a list of JSON objects that will be used to search rows in data tables. At least 1 valid column should be provided as part of payload. Action will search for all rows, where a specific column has that value and delete them.|True|None||



#### Add Entry To Watchlist
Use the Add Entry To Watchlist action to add a specified entity to an existing Risk Analytics Watchlist in Google SecOps. Note: This action requires Chronicle API authentication. Legacy Backstory API authentication is not supported.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
||The name of the Risk Analytics Watchlist to add the entry to.|True|None||
||The JSON object representing the entity to add to the Watchlist. The JSON structure requires the entity value, entity type, and an optional namespace.|True|None||



#### Get Data Tables
Get available data tables in Google SecOps. Note: this action only works with Chronicle API authentication. Backstory API is not supported.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
||Specify the key that needs to be used to filter reference lists. Name option refers to a display name of the data table.|False|None||
||Specify what filter logic should be applied.|False|None||
||Specify what value should be used in the filter. If “Equal“ is selected, action will try to find the exact match among results and if “Contains“ is selected, action will try to find results that contain that substring. “Equal” works with “title” parameter, while “Contains” works with all values in response. If nothing is provided in this parameter, the filter will not be applied.|False|None||
||If enabled, action will return data table rows as part of response.|False|None||
||Specify how many data tables to return. Maximum: 1000.|True|None||
||Specify how many data table rows to return. Note: this parameter is only used if “Expanded Rows” is enabled. Maximum: 1000.|True|None||



#### Get Reference Lists
Get available reference lists in Google Chronicle.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
||Specify the key that needs to be used to filter reference lists. Name option refers to a display name of the reference list.|False|None||
||Specify what filter logic should be applied.|False|None||
||Specify what value should be used in the filter. If “Equal“ is selected, action will try to find the exact match among results and if “Contains“ is selected, action will try to find results that contain that substring. “Equal” works with “title” parameter, while “Contains” works with all values in response. If nothing is provided in this parameter, the filter will not be applied.|False|None||
||If enabled, action will return detailed information about the reference lists.|False|None||
||Specify how many reference lists to return. Default: 100.|False|None||



#### Ask Gemini
Preview. Ask Gemini in Google SecOps. For this action to work, you have to check the Automatic Opt-in parameter. Note: this action only works with Chronicle API authentication. Backstory API is not supported
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
||If enabled, action will do an automatic opt-in for Gemini.|False|None||
||Specify the prompt that should be executed.|True|None||



#### Get Detection Details
Fetch information about a detection in Google Chronicle.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
||Specify the ID of the rule, which is related to the detection.|True|None||
||Specify the ID of the detection for which you want to fetch details.|True|None||
||If selected, the action retrieves the original raw log file associated with the UDM search results. Note: This option is only available when using Chronicle API authentication.|False|None||



#### Is Value In Data Table
Check, if provided values are found in the data table in Google SecOps. Note: this action only works with Chronicle API authentication. Backstory API is not supported.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
||Specify the display name of the data table that needs to be updated.|True|None||
||Specify a comma-separated list of columns that need to be searched within the data table. If nothing is provided, action will search within all columns.|False|None||
||Specify a comma-separated list of values that need to be searched inside the data table.|True|None||
||If enabled, action will perform case insensitive matching.|False|None||
||Specify how many data table rows to return per value that was matched. Maximum: 1000.|True|None||



#### List Events
List events on the particular asset in the specified time frame. Supported entities: IP Address, Mac Address, Hostname. Note: action can only fetch 10000 events. Make sure to narrow down the timeframe for better results.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
||Specify a comma-separated list of the event types that need to be returned. If nothing is provided, action will fetch all event types. Possible values: EVENTTYPE_UNSPECIFIED, PROCESS_UNCATEGORIZED, PROCESS_LAUNCH, PROCESS_INJECTION, PROCESS_PRIVILEGE_ESCALATION, PROCESS_TERMINATION, PROCESS_OPEN, PROCESS_MODULE_LOAD, REGISTRY_UNCATEGORIZED, REGISTRY_CREATION, REGISTRY_MODIFICATION, REGISTRY_DELETION, SETTING_UNCATEGORIZED, SETTING_CREATION, SETTING_MODIFICATION, SETTING_DELETION, MUTEX_UNCATEGORIZED, MUTEX_CREATION, FILE_UNCATEGORIZED, FILE_CREATION, FILE_DELETION, FILE_MODIFICATION, FILE_READ, FILE_COPY, FILE_OPEN, FILE_MOVE, FILE_SYNC, USER_UNCATEGORIZED, USER_LOGIN, USER_LOGOUT, USER_CREATION, USER_CHANGE_PASSWORD, USER_CHANGE_PERMISSIONS, USER_STATS, USER_BADGE_IN, USER_DELETION, USER_RESOURCE_CREATION, USER_RESOURCE_UPDATE_CONTENT, USER_RESOURCE_UPDATE_PERMISSIONS, USER_COMMUNICATION, USER_RESOURCE_ACCESS, USER_RESOURCE_DELETION, GROUP_UNCATEGORIZED, GROUP_CREATION, GROUP_DELETION, GROUP_MODIFICATION, EMAIL_UNCATEGORIZED, EMAIL_TRANSACTION, EMAIL_URL_CLICK, NETWORK_UNCATEGORIZED, NETWORK_FLOW, NETWORK_CONNECTION, NETWORK_FTP, NETWORK_DHCP, NETWORK_DNS, NETWORK_HTTP, NETWORK_SMTP, STATUS_UNCATEGORIZED, STATUS_HEARTBEAT, STATUS_STARTUP, STATUS_SHUTDOWN, STATUS_UPDATE, SCAN_UNCATEGORIZED, SCAN_FILE, SCAN_PROCESS_BEHAVIORS, SCAN_PROCESS, SCAN_HOST, SCAN_VULN_HOST, SCAN_VULN_NETWORK, SCAN_NETWORK, SCHEDULED_TASK_UNCATEGORIZED, SCHEDULED_TASK_CREATION, SCHEDULED_TASK_DELETION, SCHEDULED_TASK_ENABLE, SCHEDULED_TASK_DISABLE, SCHEDULED_TASK_MODIFICATION, SYSTEM_AUDIT_LOG_UNCATEGORIZED, SYSTEM_AUDIT_LOG_WIPE, SERVICE_UNSPECIFIED, SERVICE_CREATION, SERVICE_DELETION, SERVICE_START, SERVICE_STOP, SERVICE_MODIFICATION, GENERIC_EVENT, RESOURCE_CREATION, RESOURCE_DELETION, RESOURCE_PERMISSIONS_CHANGE, RESOURCE_READ, RESOURCE_WRITTEN, ANALYST_UPDATE_VERDICT, ANALYST_UPDATE_REPUTATION, ANALYST_UPDATE_SEVERITY_SCORE, ANALYST_UPDATE_STATUS, ANALYST_ADD_COMMENT|False|None||
||Specify a time frame for the results. If "Custom" is selected, you also need to provide "Start Time".|False|None||
||Specify the start time for the results. This parameter is mandatory, if "Custom" is selected for the "Time Frame" parameter. Format: ISO 8601|False|None||
||Specify the end time for the results. Format: ISO 8601. If nothing is provided and "Custom" is selected for the "Time Frame" parameter then this parameter will use current time. Note: value "now" can also be used.|False|None||
||Specify the reference time for the event search. Format: YYYY-MM-DDThh:mmTZD. Note: if nothing is provided, action will use end time as reference time.|False|None||
||Specify what should be the output for this action.|True|None||
||Specify how many events to process per entity type. Default: 100.|False|None||



#### Is Value In Reference List
Check, if provided values are found in reference lists in Google Chronicle.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
||Specify a comma-separated list of display names of the reference list that needs to be searched.|True|None||
||Specify a comma-separated list of values that need to be searched in reference lists.|True|None||
||If enabled, action will perform case insensitive matching.|False|None||



#### List IOCs
List all of the IoCs discovered within your enterprise within the specified time range.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
||Fetches IOC Domain from the specified time. Value should be in RFC 3339 format (e.g. 2018-11-05T12:00:00Z). If not supplied, the default is the UTC time corresponding to 3 days earlier than current time.|False|None||
||Specify the maximum number of IoCs to return. You can specify between 1 and 10,000. The default is 50.|False|None||



#### Lookup Similar Alerts
Lookup similar alerts in Google Chronicle. Supported Chronicle alert types: RULE, EXTERNAL, IOC. Note: this action can only work with alerts that come from the "Chronicle Alerts Connector". Note: action can only fetch 10000 alerts. Make sure to narrow down the timeframe for better results.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
||Specify a time frame for the results. If "Alert Time Till Now" is selected, action will use start time of the alert as start time for the search and end time will be current time. If "30 Minutes Around Alert Time" is selected, action will search the alerts 30 minutes before the alert happened till the 30 minutes after the alert has happened.  Same idea applies to "1 Hour Around Alert Time" and "5 Minutes Around Alert Time".|False|None||
||Specify a comma-separated list of IOCs or assets that you want to find in the alerts. Note: action will perform a different search for each item provided.|True|None||
||Specify what attributes need to be used, when the action is to search for similar alerts. If "Alert Name and Alert Type" is selected, action will try to find all of the alerts that have the same alert name and IOCs/Assets for the underlying alert type. If "Product" is selected, then action will try to find all of the alerts that originate from the same product and have the same IOCs/Assets, action will search among both "EXTERNAL" and "Rule" alerts. If "Only IOCs/Assets" is enabled, action will match the similarity only based upon the items provided in the parameter "IOCs/Assets", action will search among both "EXTERNAL" and "Rule" alerts.|False|None||



#### Execute Retrohunt
Execute a rule retrohunt in Google Chronicle.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
||Specify the ID of the rule for which you want to run retrohunt.|True|None||
||Specify a time frame for the results. If “Alert Time Till Now” is selected, action will use start time of the alert as start time for the search and end time will be current time. If “30 Minutes Around Alert Time” is selected, action will search the alerts 30 minutes before the alert happened till the 30 minutes after the alert has happened.  Same idea applies to “1 Hour Around Alert Time” and “5 Minutes Around Alert Time”. If “Custom” is selected, you also need to provide “Start Time”.|False|None||
||Specify the start time for the results. This parameter is mandatory, if “Custom” is selected for the “Time Frame” parameter. Format: ISO 8601.|False|None||
||Specify the end time for the results. Format: ISO 8601. If nothing is provided and “Custom” is selected for the “Time Frame” parameter then this parameter will use current time.|False|None||



#### Ping
Test connectivity to the Google Chronicle with parameters provided at the integration configuration page on the Marketplace tab.
Timeout - 600 Seconds



#### Remove Values From Reference List
Remove values from a reference list in Google Chronicle.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
||Specify the display name of the reference list that needs to be updated.|True|None||
||Specify a comma-separated list of values that need to be removed from a reference list.|True|None||



#### Enrich IP
Deprecated - Enrich IP entities using information from IOCs in Google Chronicle. Supported entities: IP address.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
||If enabled, action will create an insight containing information about the entities.|False|None||
||If enabled, action will only create an insight for entities that are marked as suspicious. Note: "Create Insight" parameter needs to be enabled.|False|None||
||Specify the lowest severity that should be associated with IP in order to mark it suspicious.|True|None||
||If enabled, action will mark the entity as suspicious, if information about severity is not available.|False|None||



#### Enrich Entities
Enrich entities using information from Google SecOps. Supported entities: File Hash, IP Address, Domain, Hostname, URL (extracts domain part of URL), User, Email (User entity with email regex). Note: this action only works with Chronicle API authentication. Backstory API is not supported.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
||Specify the namespace in which the entity is located. If nothing is provided, action will still put entities associated with a namespace in higher priority to be returned.|False|None||
||Specify a time frame for the results. Only the entities that have information in the provided timeframe will be returned. If “Custom” is selected, you also need to provide “Start Time”.|False|None||
||Specify the start time for the results. This parameter is mandatory, if “Custom” is selected for the “Time Frame” parameter. Format: ISO 8601.|False|None||
||Specify the end time for the results. Format: ISO 8601. If nothing is provided and “Custom” is selected for the “Time Frame” parameter then this parameter will use current time.|False|None||



#### Add Rows To Data Table
Add rows to a data table in Google SecOps. Note: this action only works with Chronicle API authentication. Backstory API is not supported.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
||Specify the display name of the data table that needs to be updated.|True|None||
||Specify a list of JSON objects that contain information about the rows that need to be added.|True|None||



#### List Assets
List assets in Google Chronicle based on the related entities in the specified time frame. Supported entities: URL, IP Address, File hash. Only MD5, SHA-1 or SHA-256 hashes are supported.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
||Specify how many hours backwards to fetch the assets. Default: 1 hour.|False|None||
||Specify a time frame for the results. If "Custom" is selected, you also need to provide "Start Time". If the "Max Hours Backwards" parameter is provided then action will use the "Max Hours Backwards" parameter to provide a time filter. This is done for backwards compatibility.|False|None||
||Specify the start time for the results. This parameter is mandatory, if "Custom" is selected for the "Time Frame" parameter. Format: ISO 8601|False|None||
||Specify the end time for the results. Format: ISO 8601. If nothing is provided and "Custom" is selected for the "Time Frame" parameter then this parameter will use current time.|False|None||
||Specify how many assets to return in the response.|False|None||






## Jobs

#### Google Chronicle Alerts Creator Job
This job will sync new SOAR alerts with Chronicle SIEM.
Note: This job is only supported from Chronicle SOAR version 6.2.30 and higher.

|Name|IsMandatory|Type|DefaultValue|
|----|-----------|----|------------|
|||None|Default Environment|
|||None|https://backstory.googleapis.com|
|||None||
|||None||
|||None|true|

#### Google Chronicle Sync Job
This job will synchronize information about Chronicle SOAR Cases and Chronicle SOAR Alerts with Chronicle SIEM.
 Note: This job is only supported from Chronicle SOAR version 6.1.44 and higher.

|Name|IsMandatory|Type|DefaultValue|
|----|-----------|----|------------|
|||None|Default Environment|
|||None|https://backstory.googleapis.com|
|||None||
|||None||
|||None|24|
|||None|true|



## Connectors
#### Google Chronicle - Chronicle Alerts Connector
Pull information about Rule based alerts from Google Chronicle. Note: dynamic list is used for filtering purposes. For all of the details please visit the documentation portal.

|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
||Describes the name of the field where the environment name is stored. If the environment field isn't found, the environment is the default environment.||None||
||A regex pattern to run on the value found in the "Environment Field Name" field. Default is .* to catch all and return the value unchanged. Used to allow the user to manipulate the environment field via regex logic. If the regex pattern is null or empty, or the environment value is null, the final environment result is the default environment.||None|.*|
||API root of the Chronicle instance.||None|https://backstory.googleapis.com|
||Service Account that is used for authentication. If not provided, the default Service Account of the SecOps Instance will be used to authenticate.||None||
||The client email address of your workload identity. You can configure either this parameter or the User's Service Account parameter. To impersonate service accounts with the workload identity email address, grant the Service Account Token Creator role to your service account. If both this and User's Service Account not provided, the default Service Account of the SecOps Instance will be used to authenticate.||None||
||Number of hours before the first connector iteration to retrieve alerts from. This parameter applies to the initial connector iteration after you enable the connector for the first time, or used as a fallback value in cases where connector's last run timestamp expires. Maximum: 167 hours.||None|1|
||How many alerts per type to process per one connector iteration. Default: 100.||None|100|
||Specify the fallback severity for the detection. This parameter is going to be used, if Chronicle detection doesn't include any information related to the severity. Possible values: Critical, High, Medium, Low, Info.||None|Medium|
||If enabled, verify the SSL certificate for the connection to the Google Chronicle server is valid.||None|true|
||The address of the proxy server to use.||None||
|| The proxy username to authenticate with.||None||
|| The proxy password to authenticate with.||None||
||If enabled, the connector will ignore the overflow mechanism.||None|false|




