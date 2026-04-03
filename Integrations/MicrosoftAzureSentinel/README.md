
# MicrosoftAzureSentinel

Microsoft Azure Sentinel is a scalable, cloud-native, security information event management (SIEM) and security orchestration automated response (SOAR) solution. Azure Sentinel delivers intelligent security analytics and threat intelligence across the enterprise, providing a single solution for alert detection, threat visibility, proactive hunting, and threat response.

Python Version - V3_11
#### Parameters
|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Azure Subscription ID|None|True|String||
|Azure Active Directory ID|None|True|String||
|Api Root|None|True|String||
|OAUTH2 Login Endpoint Url|None|True|String||
|Azure Resource Group|None|True|String||
|Azure Sentinel Workspace Name|None|True|String||
|Client ID|None|True|String||
|Client Secret|None|True|Password||
|Verify SSL|None|False|Boolean||


#### Dependencies
| |
|-|
|google_auth_httplib2-0.3.0-py3-none-any.whl|
|pycparser-3.0-py3-none-any.whl|
|google_api_python_client-2.188.0-py3-none-any.whl|
|requests_toolbelt-1.0.0-py2.py3-none-any.whl|
|EnvironmentCommon-1.0.1-py2.py3-none-any.whl|
|googleapis_common_protos-1.73.0-py3-none-any.whl|
|types_python_dateutil-2.9.0.20241003-py3-none-any.whl|
|isodate-0.7.2-py3-none-any.whl|
|TIPCommon-2.3.3-py3-none-any.whl|
|python_dateutil-2.9.0.post0-py2.py3-none-any.whl|
|urllib3-2.6.3-py3-none-any.whl|
|proto_plus-1.27.1-py3-none-any.whl|
|pyasn1_modules-0.4.2-py3-none-any.whl|
|arrow-1.3.0-py3-none-any.whl|
|sniffio-1.3.1-py3-none-any.whl|
|requests-2.32.5-py3-none-any.whl|
|h11-0.16.0-py3-none-any.whl|
|pyparsing-3.3.2-py3-none-any.whl|
|pycryptodome-3.23.0-cp37-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl|
|cffi-2.0.0-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.whl|
|google_api_core-2.30.0-py3-none-any.whl|
|protobuf-6.33.5-cp39-abi3-manylinux2014_x86_64.whl|
|rsa-4.9.1-py3-none-any.whl|
|google_auth-2.47.0-py3-none-any.whl|
|certifi-2026.2.25-py3-none-any.whl|
|idna-3.11-py3-none-any.whl|
|charset_normalizer-3.4.5-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl|
|pyopenssl-25.3.0-py3-none-any.whl|
|pyasn1-0.6.2-py3-none-any.whl|
|cryptography-46.0.4-cp311-abi3-manylinux_2_34_x86_64.whl|
|typing_extensions-4.15.0-py3-none-any.whl|
|cryptography-46.0.5-cp311-abi3-manylinux_2_34_x86_64.whl|
|httpx-0.28.1-py3-none-any.whl|
|anyio-4.12.1-py3-none-any.whl|
|cachetools-6.2.4-py3-none-any.whl|
|six-1.16.0-py2.py3-none-any.whl|
|uritemplate-4.2.0-py3-none-any.whl|
|pytz-2024.2-py2.py3-none-any.whl|
|httpcore-1.0.9-py3-none-any.whl|
|httplib2-0.31.2-py3-none-any.whl|


## Actions
#### Add Comment to Incident
Add a comment to Azure Sentinel Incident.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Incident Number|Specify Incident number to add comment to.|True|None||
|Comment to Add|Specify comment to add to Incident|True|None||



#### Get Incident Statistic
Get Azure Sentinel Incident Statistics
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Time Frame|Time frame in hours for which to fetch Incidents|False|None||



#### List Incidents
List Microsoft Azure Sentinel Incidents based on the provided search criteria.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Time Frame|Time frame in hours for which to fetch Incidents|False|None||
|Status|Statuses of the incidents to look for. Comma-separated string|False|None||
|Severity|Severities of the incidents to look for. Comma-separated string.|False|None||
|How Many Incidents to Fetch|How many incidents to fetch|False|None||



#### Update Incident Details
Update Incident Details. Please consider moving to the v2 version of the action, as it is implemented as a SOAR async action and provides more consistent results.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Incident Case Number|Specify Azure Sentinel incident number to update.|True|None||
|Title|Specify new title for the Azure Sentinel incident.|False|None||
|Status|Specify new status for the Azure Sentinel incident.|False|None||
|Severity|Specify new severity for the Azure Sentinel incident.|False|None||
|Description|Specify new description for the Azure Sentinel incident.|False|None||
|Assigned To|Specify the user to assign the incident to.|False|None||
|Closed Reason|If status of the incident is set to Closed, provide a Closed Reason for the incident.|False|None||
|Closing Comment|Optional closing comment to provide for the closed Azure Sentinel Incident.|False|None||
|Number of retries|Specify the number of retry attempts the action should make if the incident update was unsuccessful.|False|None||
|Retry Every|Specify what time period action should wait between incident update retries.|False|None||



#### Update Alert Rule
Update Azure Sentinel Scheduled Alert Rule
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Alert Rule ID|Alert Rule ID|True|None||
|Enable Alert Rule|Enable or disable new alert rule|False|None||
|Name|Display name of the new alert rule|False|None||
|Severity|Severity of the new alert rule|False|None||
|Query|Query of the new alert rule|False|None||
|Frequency|How frequently to run the query, use the following format: PT + number + (M, H), where M - minutes, H - hours. Use P + number + D to specify a number of days. Can be combined as P1DT1H1M - 1 day, 1 hour and 1 minute. Minimum is 5 minutes, maximum is 14 days.|False|None||
|Period of Lookup Data|Time of the last lookup data, use the following format: PT + number + (M, H), where M - minutes, H - hours. Use P + number + D to specify a number of days. Can be combined as P1DT1H1M - 1 day, 1 hour and 1 minute. Minimum is 5 minutes, maximum is 14 days.|False|None||
|Trigger Operator|Trigger operator for this alert rule.Possible values are: GreaterThan, LessThan, Equal, NotEqual|False|None||
|Trigger Threshold|Trigger threshold for this alert rule|False|None||
|Enable Suppression|Whether you want to stop running query after alert is generated|False|None||
|Suppression Duration|How long you want to stop running query after alert is generated, use the following format: PT + number + (M, H), where M - minutes, H - hours. Use P + number + D to specify a number of days. Can be combined as P1DT1H1M - 1 day, 1 hour and 1 minute. Minimum is 5 minutes, maximum is 14 days.|False|None||
|Description|Description of the new alert rule|False|None||
|Tactics|Tactics of the new alert rule. Comma-separated values.|False|None||



#### Update Incident Details v2
Update Incident Details v2. Action is a Chronicle SOAR async action and can be configured for a retry for a longer period of time.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Incident Case Number|Specify Azure Sentinel incident number to update.|True|None||
|Title|Specify new title for the Azure Sentinel incident.|False|None||
|Status|Specify new status for the Azure Sentinel incident.|False|None||
|Severity|Specify new severity for the Azure Sentinel incident.|False|None||
|Description|Specify new description for the Azure Sentinel incident.|False|None||
|Assigned To|Specify the user to assign the incident to.|False|None||
|Closed Reason|If status of the incident is set to Closed, provide a Closed Reason for the incident.|False|None||
|Closing Comment|Optional closing comment to provide for the closed Azure Sentinel Incident.|False|None||
|Number of retries|Specify the number of retry attempts the action should make if the incident update was unsuccessful.|False|None||



#### Create Alert Rule
Create Azure Sentinel Scheduled Alert Rule
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Enable Alert Rule|Enable or disable new alert rule|False|None||
|Name|Display name of the new alert rule|True|None||
|Severity|Severity of the new alert rule|True|None||
|Query|Query of the new alert rule|True|None||
|Frequency|How frequently to run the query, use the following format: PT + number + (M, H), where M - minutes, H - hours. Use P + number + D to specify a number of days. Can be combined as P1DT1H1M - 1 day, 1 hour and 1 minute. Minimum is 5 minutes, maximum is 14 days.|True|None||
|Period of Lookup Data|Time of the last lookup data, use the following format: PT + number + (M, H), where M - minutes, H - hours. Use P + number + D to specify a number of days. Can be combined as P1DT1H1M - 1 day, 1 hour and 1 minute. Minimum is 5 minutes, maximum is 14 days.|True|None||
|Trigger Operator|Trigger operator for this alert rule.Possible values are: GreaterThan, LessThan, Equal, NotEqual|True|None||
|Trigger Threshold|Trigger threshold for this alert rule|True|None||
|Enable Suppression|Whether you want to stop running query after alert is generated|False|None||
|Suppression Duration|How long you want to stop running query after alert is generated, use the following format: PT + number + (M, H), where M - minutes, H - hours. Use P + number + D to specify a number of days. Can be combined as P1DT1H1M - 1 day, 1 hour and 1 minute. Minimum is 5 minutes, maximum is 14 days.|True|None||
|Description|Description of the new alert rule|False|None||
|Tactics|Tactics of the new alert rule. Comma-separated values.|False|None||



#### Get Custom Hunting Rule Details
Get Details of the Azure Sentinel Custom Hunting Rule
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Hunting Rule ID|Hunting Rule ID|True|None||



#### Create Custom Hunting Rule
Create Azure Sentinel Custom Hunting Rule
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Display Name|Display name of the new custom hunting rule|True|None||
|Query|Query of the new custom hunting rule|True|None||
|Description|Description of the new custom hunting rule|False|None||
|Tactics|Tactics of the new custom hunting rule. Comma-separated values.|False|None||



#### Delete Alert Rule
Delete Azure Sentinel Scheduled Alert Rule
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Alert Rule ID|Alert Rule ID|True|None||



#### List Custom Hunting Rules
List Custom Hunting Rules available in Sentinel
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Hunting Rule Names to Return|Names for the hunting rules action should return. Comma-separated string|False|None||
|Fetch Specific Hunting Rule Tactics|What hunting rule tactics action should return. Comma-separated string|False|None||
|Max rules to return|How many scheduled alert rules the action should return, for example, 50.|False|None||



#### Delete Custom Hunting Rule
Delete Azure Sentinel Custom Hunting Rule
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Hunting Rule ID|Hunting Rule ID|True|None||



#### Update Incident Labels v2
Update Incident Labels v2. Action is a Chronicle SOAR async action and can be configured for a retry for a longer period of time.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Incident Case Number|Specify Azure Sentinel incident number to update with new labels.|True|None||
|Labels|Specify new labels that should be appended to the Incident. Parameter accepts multiple values as a comma-separated string.|True|None||
|Number of retries|Specify the number of retry attempts the action should make if the incident update was unsuccessful.|False|None||



#### Run Custom Hunting Rule Query
Run Custom Hunting Rule Query
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Hunting Rule ID|Hunting Rule ID|True|None||
|Timeout|Timeout value for the Azure Sentinel hunting rule API call|False|None||



#### List Alert Rules
Get Azure Sentinel Scheduled Rules list
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Alert Rule Severity|Severities of the alert rules to look for. Comma-separated string|False|None||
|Fetch Specific Alert Rule Types|What alert rule types action should return. Comma-separated string|False|None||
|Fetch Specific Alert Rule Tactics|What alert rule tactics action should return. Comma-separated string|False|None||
|Fetch only Enabled Alert Rules|If action should return only enabled alert rules|False|None||
|Max rules to return|How many scheduled alert rules the action should return, for example, 50.|False|None||



#### Get Alert Rule Details
Get Details of the Azure Sentinel Scheduled Alert Rule
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Alert Rule ID|Alert Rule ID|True|None||



#### Ping
Test connectivity to Microsoft Azure Sentinel
Timeout - 600 Seconds



#### Run KQL Query
Run Azure Sentinel KQL Query based on the provided action input parameters.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|KQL Query|A KQL Query to execute in Azure Sentinel. For example, to get security alerts available in Sentinel, query will be "SecurityAlert". Use other action input parameters (time span, limit) to filter the query results. For the examples of KQL queries consider Sentinel "Logs" Web page|True|None||
|Time Span|Time span to look for, use the following format: PT + number + (M, H), where M - minutes, H - hours. Use P + number + D to specify a number of days. Can be combined as P1DT1H1M - 1 day, 1 hour and 1 minute.|False|None||
|Query Timeout|Timeout value for the Azure Sentinel hunting rule API call. Note that Siemplify action python process timeout should be adjusted accordingly for this parameter, to not timeout action sooner than specified value because of the python process timeout.|False|None||
|Record Limit|How many records should be fetched. Optional parameter, if set, adds a "| limit x" to the kql query where x is the value set for the record limit. Can be removed if "limit" is already set in kql query or not needed.|False|None||



#### Update Incident Labels
Update Incident Labels. Please consider moving to the v2 version of the action, as it is implemented as a SOAR async action and provides more consistent results.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Incident Case Number|Specify Azure Sentinel incident number to update with new labels.|True|None||
|Labels|Specify new labels that should be appended to the Incident. Parameter accepts multiple values as a comma-separated string.|True|None||
|Number of retries|Specify the number of retry attempts the action should make if the incident update was unsuccessful.|False|None||
|Retry Every|Specify what time period in seconds action should wait between incident update retries.|False|None||



#### Update Custom Hunting Rule
Update Azure Sentinel Custom Hunting Rule
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Hunting Rule ID|Hunting Rule ID|True|None||
|Display Name|Display name of the new custom hunting rule|False|None||
|Query|Query of the new custom hunting rule|False|None||
|Description|Description of the new custom hunting rule|False|None||
|Tactics|Tactics of the new custom hunting rule. Comma-separated values.|False|None||






## Jobs

#### Sync Incidents
Deprecated. This job synchronizes Google SecOps Alerts and Microsoft Sentinel Incidents. It ensures that comments, status, and tags are kept in sync between the two systems. For the job to identify the correct information, the Google SecOps case must have the “Microsoft Sentinel Incident” tag. If the alert didn’t originate from “Microsoft Azure Sentinel Incident Connector v2”,  you will need to add an “Incident_ID” context value to the case for the job to be able to find the correct information.

|Name|IsMandatory|Type|DefaultValue|
|----|-----------|----|------------|
|Environment Name|True|None|Default Environment|
|Azure Active Directory ID|True|None||
|OAUTH2 Login Endpoint Url|True|None|https://login.microsoftonline.com|
|API Root|True|None|https://graph.microsoft.com|
|Client ID|True|None||
|Client Secret|True|None||
|Max Hours Backwards|False|None|24|
|Verify SSL|False|None|true|

#### Sync Incidents V2
Use the Sync Incidents V2 job to synchronize Google SecOps alerts with Microsoft Sentinel incidents. This job ensures that comments, statuses, and tags are synchronized bi-directionally between both systems. Note: Assignee and severity synchronization occurs exclusively from Microsoft Sentinel to Google SecOps. For the job to identify the correct information, the Google SecOps case must have the Microsoft Sentinel Incident tag. This job only works on alerts from the Microsoft Azure Sentinel Incident Connector v2.

|Name|IsMandatory|Type|DefaultValue|
|----|-----------|----|------------|
|Environment Name|True|None|Default Environment|
|Azure Subscription ID|True|None||
|Azure Active Directory ID|True|None||
|OAUTH2 Login Endpoint Url|True|None|https://login.microsoftonline.com|
|Management API Root|True|None|https://management.azure.com|
|Azure Resource Group|True|None||
|Azure Sentinel Workspace Name|True|None||
|Client ID|True|None||
|Client Secret|True|None||
|Max Hours Backwards|False|None|24|
|Sync Assignee|False|None|false|
|Verify SSL|False|None|true|



## Connectors
#### Microsoft Sentinel Incident Tracking Connector
Connector works with Microsoft Azure Sentinel incidents and fetches updates to the Sentinel incidents as the new SecOps alerts. Connector's Dynamic List can be used to specify the incidents names that needs to be fetched. It is recommended to configure SecOps Alerts grouping based on SourceGroupIdentifier for this connector. See connector documentation for more information.

|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Environment Field Name|Describes the name of the field where the environment name is stored. If environment field isn't found, environment is "".|False|None||
|Environment Regex Pattern|A regex pattern to run on the value found in the "Environment Field Name" field. Default is .* to catch all and return value unchanged. Used to allow the user to manipulate the environment field via regex logic. If regex pattern is null or empty, or the environment value is null, the final environment result is "".|False|None|.*|
|Azure Subscription ID|Microsoft Azure Subscription ID, can be viewed in Azure Portal > Subscriptions > <Your Subscription> > Subscription ID. |True|None||
|Entra ID Directory ID|Azure Entra ID Tenant ID, can be viewed in Active Directory > App Registration > <Application you configured for your integration> > Directory (tenant) ID.|True|None||
|Api Root|Management.azure.com Api root url to use with integration.|True|None|https://management.azure.com|
|OAUTH2 Login Endpoint Url|Specify the url, that connector should use for OAUTH2 Login.|True|None|https://login.microsoftonline.com|
|Azure Resource Group|Name of Azure Resource Group where Azure Sentinel is located.|True|None||
|Azure Sentinel Workspace Name|Name of the Azure Sentinel workspace to work with, can be viewed in Azure portal > Azure Sentinel > Azure Sentinel Workspaces.|True|None||
|Client ID|Client (Application) ID that was added for the app registration in Azure Active Directory for this integration.|True|None||
|Client Secret|Secret that was entered for Azure AD app registration.|True|None||
|Verify SSL|Verify SSL certificates for HTTPS requests to Microsoft Azure.|False|None|true|
|Max Hours Backwards|Number of hours before the first connector iteration to retrieve incidents from. This parameter applies to the initial connector iteration after you enable the connector for the first time, or used as a fallback value in cases where connector's last run timestamp expires.|True|None|24|
|Incident Statuses to Fetch|Specify the statuses of the incidents that should be fetched by the SecOps server. Parameter can take multiple values as a comma separated string.|True|None|New,  Active, Closed|
|Incident Severities to Fetch|Specify the severities of the incidents that should be fetched by the SecOps server. Parameter can take multiple values as a comma separated string.|True|None|Informational, Low, Medium, High|
|Max Incidents per Cycle|How many incidents should be processed during one connector run.|True|None|10|
|Wait For Scheduled/NRT Alert Object|If enabled, the connector will wait until a Scheduled/NRT alert object will be available.|False|None|false|
|Use the same approach with event creation for all alert types?|By default connector uses a different approach with Scheduled Alert or NRT types of alerts - it tries to fetch events that caused the alert by running the query specified in alert details. Specify whether to change this behavior and use the same approach for the scheduled and NRT alerts as for other alert types.|False|None|false|
|Incidents Tags To Ingest|Specify a comma separated list of tags Sentinel incident should have to be ingested. Incidents that will not have tags from this list will be ignored. Example of how Sentinel tags can be provided: tag1, tag2|False|None||
|Use dynamic list as a blocklist|If enabled, dynamic list will be used as a blocklist.|False|None|false|
|Backlog Expiration Timer|Time frame in minutes for connector to keep incidents in backlog for.|True|None|60|
|StartTimeFallback|Specify a comma separated list of incident or alert attributes that should be used as a fallback for the "Start Time" alert field in descending order. Additionally, new "SecOps_Start_Time" attribute will be added to created events. First attribute will have the highest priority, next if its not present or empty in the event - fallback to the next value from the list and so on. If none of the fallback fields are found, connector will use createdTimeUTC, and if that's also non existent - alert ingestion time to SecOps.|True|None|properties_firstActivityTimeGenerated,properties_startTimeUtc,properties_createdTimeUtc,properties_firstAlertTimeGenerated|
|EndTimeFallback|Specify a comma separated list of incident or alert attributes that should be used as a fallback for the "End Time" alert field in descending order. Additionally, new "SecOps_End_Time" attribute will be added to created events. First attribute will have the highest priority, next if its not present or empty in the event - fallback to the next value from the list and so on. If none of the fallback fields are found, connector will use createdTimeUTC, and if that's also non existent - alert ingestion time to SecOps.|True|None|properties_lastActivityTimeGenerated,properties_endTimeUtc,properties_createdTimeUtc,properties_lastAlertTimeGenerated|
|Enable Fallback Logic Debug?|Specify if connector should add to the created events a "debug" fields that will contain the values it used for fallback.|False|None|false|
|VendorFieldFallback|Specify a comma separated list of incident attributes that should be used as a fallback for the "DeviceVendor" field in descending order. First attribute will have the highest priority, next if its not present or empty in the event - fallback to the next value from the list and so on.|True|None|vendorName|
|ProductFieldFallback|Specify a comma separated list of incident or alert attributes that should be used as a fallback for the "Product Field Name" parameter and "DeviceProduct" field in descending order. First attribute will have the highest priority, next if its not present or empty in the event - fallback to the next value from the list and so on.|True|None|ProductName|
|EventFieldFallback|Specify a comma separated list of alert attributes that should be used as a fallback for the "Event Field Name" parameter in descending order. First attribute will have the highest priority, next if its not present or empty in the event - fallback to the next value from the list and so on.|True|None|kind|
|Max Backlog Incidents per cycle|How many incidents  connector should try to fetch from the backlog during one connector run.|True|None|10|
|Disable Overflow|If enabled, the connector will disable the overflow mechanism.|False|None|false|
|Total number of Scheduled Alerts Events Limit to Ingest|Specify the total number of events the connector should ingest for a Microsoft Sentinel incident that is based on a Scheduled or NRT alert. Connector ‘counts’ events in all corresponding SecOps alerts created for the Microsoft Sentinel Incident and no new events will be ingested once this limit is reached.|False|None|100|
|Create Chronicle SOAR Alerts for Sentinel incidents that do not have entities?|If enabled, connector will create SecOps alerts from Microsoft Sentinel incidents that dont have entities. Otherwise, such incidents will be skipped for all Sentinel incidents types except Sentinel Scheduled and NRT alerts.|False|None|false|
|Incidents Padding Period (minutes)|If specified, to get incidents returned not in chronological order, connector will fetch Sentinel incidents from this value backwards in time.|False|None|60|
|Alert Name Template|If specified, connector will use this value from the Microsoft Azure Sentinel API response for incident data for Chronicle SOAR Alert Name. You can provide placeholders in the following format: [name of the field]. Example: Sentinel incident - [title]. Note: the maximum length for the field is 256 characters. If nothing is provided or user provides an invalid template, connector will use the default alert name.|False|None||
|Rule Generator Template|If specified, connector will use this value from the Microsoft Azure Sentinel API response for incident data for Chronicle SOAR Rule Generator. You can provide placeholders in the following format: [name of the field]. Example: Sentinel incident - [severity]. Note: the maximum length for the field is 256 characters. If nothing is provided or user provides an invalid template, connector will use the default rule generator value.|False|None||
|How many hours to track ingested incident for updates|Specify how long connector should track already ingested Sentinel incident for updates - either addition of new events or entities and incident details.|True|None|24|
|Proxy Server Address|Proxy server to use for connection.|False|None||
|Proxy Username|Proxy server username.|False|None||
|Proxy Password|Proxy server password.|False|None||
|Create extra events for all entities|If enabled, when creating entities from the Sentinel API, connector will create extra SecOps events for all Sentinel incident's entities, not only Account, Mailbox, Host or Ip.|False|None|false|


#### Microsoft Azure Sentinel Incident Connector v2
Connector works with Microsoft Azure Sentinel incidents. Connector's Dynamic List can be used to specify the incidents names that needs to be fetched. See connector documentation for more information.

|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Disable Overflow|If enabled, the connector will disable the overflow mechanism.|False|None|false|
|Enable Fallback Logic Debug?|Specify if connector should add to the created events a “debug“ fields that will contain the values it used for fallback.|False|None|false|
|Environment Field Name|Describes the name of the field where the environment name is stored. If environment field isn't found, environment is "".|False|None||
|Scheduled Alerts Events Limit to Ingest|Specify the maximum number of events the connector should ingest per a single Azure Sentinel Scheduled or NRT Alert.|False|None|100|
|Environment Regex Pattern|A regex pattern to run on the value found in the "Environment Field Name" field. Default is .* to catch all and return value unchanged. Used to allow the user to manipulate the environment field via regex logic. If regex pattern is null or empty, or the environment value is null, the final environment result is "".|False|None|.*|
|Azure Subscription ID|Microsoft Azure Subscription ID, can be viewed in Azure Portal > Subscriptions > <Your Subscription> > Subscription ID. |True|None||
|Azure Active Directory ID|Azure Active Directory Tenant ID, can be viewed in Active Directory > App Registration > <Application you configured for your integration> > Directory (tenant) ID.|True|None||
|API Root|The API Root of Microsoft Azure Sentinel REST API root.|True|None|https://management.azure.com|
|OAUTH2 Login Endpoint Url|Specify the url, that connector should use for OAUTH2 Login.|True|None|https://login.microsoftonline.com|
|Azure Resource Group|Name of Azure Resource Group where Azure Sentinel is located.|True|None||
|Azure Sentinel Workspace Name|Name of the Azure Sentinel workspace to work with, can be viewed in Azure portal > Azure Sentinel > Azure Sentinel Workspaces.|True|None||
|Client ID|Client (Application) ID that was added for the app registration in Azure Active Directory for this integration.|True|None||
|Client Secret|Secret that was entered for Azure AD app registration|True|None||
|Verify SSL|Verify SSL certificates for HTTPS requests to Microsoft Azure.|False|None|false|
|Max New Incidents Per Cycle|How many incidents should be processed during one connector run|True|None|10|
|Max Backlog Incidents per cycle|How many incidents  connector should try to fetch from the backlog during one connector run.|True|None|10|
|Offset Time In Hours|Number of hours before the first connector iteration to retrieve incidents alerts. This parameter applies to the initial connector iteration after you enable the connector for the first time, or used as a fallback value in cases where connector's last run timestamp expires. Default value: 24 hours.|True|None|24|
|Incident Statuses to Fetch|Specify the statuses of the incidents that should be fetched by the Chronicle SOAR server. Parameter can take multiple values as a comma separated string.|True|None|New, Closed|
|Incident Severities to Fetch|Specify the severities of the incidents that should be fetched by the Chronicle SOAR server. Parameter can take multiple values as a comma separated string.|True|None|Informational, Low, Medium, High|
|Use the same approach with event creation for all alert types?|By default connector uses a different approach with Scheduled Alert or NRT types of alerts - it tries to fetch events that caused the alert by running the query specified in alert details. Specify whether to change this behavior and use the same approach for the scheduled and NRT alerts as for other alert types.|False|None|false|
|Use dynamic list as a blocklist|If enabled, dynamic list will be used as a blocklist.|False|None|false|
|Backlog Expiration Timer|Time frame in minutes for connector to keep incidents in backlog for.|True|None|60|
|EventFieldFallback|Specify a comma separated list of alert attributes that should be used as a fallback for the "Event Field Name" parameter in descending order. First attribute will have the highest priority, next if its not present or empty in the event - fallback to the next value from the list and so on.|True|None|kind|
|ProductFieldFallback|Specify a comma separated list of incident or alert attributes that should be used as a fallback for the "Product Field Name" parameter and "DeviceProduct" field in descending order. First attribute will have the highest priority, next if its not present or empty in the event - fallback to the next value from the list and so on.|True|None|ProductName,properties_providerName|
|VendorFieldFallback|Specify a comma separated list of incident attributes that should be used as a fallback for the "DeviceVendor" field in descending order. First attribute will have the highest priority, next if its not present or empty in the event - fallback to the next value from the list and so on.|True|None|vendorName|
|StartTimeFallback|Specify a comma separated list of incident or alert attributes that should be used as a fallback for the “Start Time” alert field in descending order. Additionally, new “Siemplify_Start_Time“ attribute will be added to created events. First attribute will have the highest priority, next if its not present or empty in the event - fallback to the next value from the list and so on. If none of the fallback fields are found, connector will use createdTimeUTC, and if that's also non existent - alert ingestion time to Chronicle SOAR.|True|None|properties_firstActivityTimeGenerated,properties_startTimeUtc,properties_createdTimeUtc,properties_firstAlertTimeGenerated|
|EndTimeFallback|Specify a comma separated list of incident or alert attributes that should be used as a fallback for the “End Time” alert field in descending order. Additionally, new “Siemplify_End_Time“ attribute will be added to created events. First attribute will have the highest priority, next if its not present or empty in the event - fallback to the next value from the list and so on. If none of the fallback fields are found, connector will use createdTimeUTC, and if that's also non existent - alert ingestion time to Chronicle SOAR.|True|None|properties_lastActivityTimeGenerated,properties_endTimeUtc,properties_createdTimeUtc,properties_lastAlertTimeGenerated|
|Incidents Tags To Ingest|Specify a comma separated list of tags Sentinel incident should have to be ingested. Incidents that will not have tags from this list will be ignored. Example of how Sentinel tags can be provided: tag1, tag2|False|None||
|Create Chronicle SOAR Alerts for Sentinel incidents that do not have entities?|If enabled, connector will create Chronicle SOAR alerts from Microsoft Sentinel incidents that dont have entities. Otherwise, such incidents will be skipped for all Sentinel incidents types except Sentinel Scheduled and NRT alerts.|False|None|false|
|Incident's Alerts Limit to Ingest|Specify the maximum number of  alerts the connector should ingest per a single Azure Sentinel incident.|False|None|10|
|Proxy Server Address|Proxy server to use for connection.|False|None||
|Proxy Username|Proxy server username|False|None||
|Proxy Password|Proxy server password|False|None||
|Incidents Padding Period (minutes)|If specified, to get incidents returned not in chronological order, connector will fetch Sentinel incidents from this value backwards in time.|False|None|60|
|Alert Name Template|If specified, connector will use this value from the Microsoft Azure Sentinel API response for incident data for Chronicle SOAR Alert Name. You can provide placeholders in the following format: [name of the field]. Example: Sentinel incident - [title]. Note: the maximum length for the field is 256 characters. If nothing is provided or user provides an invalid template, connector will use the default alert name.|False|None||
|Rule Generator Template|If specified, connector will use this value from the Microsoft Azure Sentinel API response for incident data for Chronicle SOAR Rule Generator. You can provide placeholders in the following format: [name of the field]. Example: Sentinel incident - [severity]. Note: the maximum length for the field is 256 characters. If nothing is provided or user provides an invalid template, connector will use the default rule generator value.|False|None||
|Create extra events for all entities|If enabled, when creating entities from the Sentinel API, connector will create extra SecOps events for all Sentinel incident's entities, not only Account, Mailbox, Host or Ip.|False|None|false|
|Azure API Timeout In Seconds|If specified, the value will be applied as the maximum waiting time in seconds for any request made to Azure API. Defaults to 60.|False|None|60|
|Wait For Scheduled/NRT Alert Object|If enabled, the connector will wait until a Scheduled/NRT alert object will be available.|False|None|false|


#### Microsoft Azure Sentinel Incident Connector
DEPRECATED! Fetches Incidents from Azure Sentinel.

|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Environment Field Name|Describes the name of the field where the environment name is stored.|False|None||
|Environment Regex Pattern|If defined - the connector will implement the specific RegEx pattern on the data from "environment field" to extract specific string. For example - extract domain from sender's address: "(?<=@)(\S+$)"|False|None||
|API Root|The API Root of Microsoft Azure Sentinel REST API root.|True|None|https://management.azure.com|
|OAUTH2 Login Endpoint Url|Specify the url, that connector should use for OAUTH2 Login.|True|None|https://login.microsoftonline.com|
|Client ID|Client (Application) ID that was added for the app registration in Azure Active Directory for this integration.|True|None||
|Client Secret|Secret that was entered for Azure AD app registration|True|None||
|Azure Active Directory ID|Azure Active Directory Tenant ID, can be viewed in Active Directory > App Registration > <Application you configured for your integration> > Directory (tenant) ID.|True|None||
|Azure Sentinel Workspace Name|Name of the Azure Sentinel workspace to work with, can be viewed in Azure portal > Azure Sentinel > Azure Sentinel Workspaces.|True|None||
|Azure Subscription ID|Microsoft Azure Subscription ID, can be viewed in Azure Portal > Subscriptions > <Your Subscription> > Subscription ID. |True|None||
|Azure Resource Group|Name of Azure Resource Group where Azure Sentinel is located.|True|None||
|Verify SSL|Verify SSL certificates for HTTPS requests to Microsoft Azure.|False|None|false|
|Max Incidents per Cycle|How many incidents should be processed during one connector run|False|None|10|
|Offset Time In Hours|Number of hours before the first connector iteration to retrieve alerts from. This parameter applies to the initial connector iteration after you enable the connector for the first time, or used as a fallback value in cases where connector's last run timestamp expires. Default value: 24 hours.|False|None|24|
|Incident Statuses to Fetch|Specify the statuses of the incidents that should be fetched by the Siemplify server. Comma-separated string.|True|None|Draft, New, InProgress, Closed|
|Incident Severities to Fetch|Specify the severities of the incidents that should be fetched by the Siemplify server. Comma-separated string.|True|None|Informational, Low, Medium, High, Critical|
|Proxy Server Address|Proxy server to use for connection.|False|None||
|Proxy Server Username|Proxy server username|False|None||
|Proxy Server Password|Proxy server password|False|None||




