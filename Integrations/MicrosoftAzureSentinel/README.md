
# MicrosoftAzureSentinel

Microsoft Azure Sentinel is a scalable, cloud-native, security information event management (SIEM) and security orchestration automated response (SOAR) solution. Azure Sentinel delivers intelligent security analytics and threat intelligence across the enterprise, providing a single solution for alert detection, threat visibility, proactive hunting, and threat response.

Python Version - V3_11


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
||Specify Incident number to add comment to.||None||
||Specify comment to add to Incident||None||



#### Get Incident Statistic
Get Azure Sentinel Incident Statistics
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
||Time frame in hours for which to fetch Incidents||None||



#### List Incidents
List Microsoft Azure Sentinel Incidents based on the provided search criteria.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
||Time frame in hours for which to fetch Incidents||None||
||Statuses of the incidents to look for. Comma-separated string||None||
||Severities of the incidents to look for. Comma-separated string.||None||
||How many incidents to fetch||None||



#### Update Incident Details
Update Incident Details. Please consider moving to the v2 version of the action, as it is implemented as a SOAR async action and provides more consistent results.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
||Specify Azure Sentinel incident number to update.||None||
||Specify new title for the Azure Sentinel incident.||None||
||Specify new status for the Azure Sentinel incident.||None||
||Specify new severity for the Azure Sentinel incident.||None||
||Specify new description for the Azure Sentinel incident.||None||
||Specify the user to assign the incident to.||None||
||If status of the incident is set to Closed, provide a Closed Reason for the incident.||None||
||Optional closing comment to provide for the closed Azure Sentinel Incident.||None||
||Specify the number of retry attempts the action should make if the incident update was unsuccessful.||None||
||Specify what time period action should wait between incident update retries.||None||



#### Update Alert Rule
Update Azure Sentinel Scheduled Alert Rule
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
||Alert Rule ID||None||
||Enable or disable new alert rule||None||
||Display name of the new alert rule||None||
||Severity of the new alert rule||None||
||Query of the new alert rule||None||
||How frequently to run the query, use the following format: PT + number + (M, H), where M - minutes, H - hours. Use P + number + D to specify a number of days. Can be combined as P1DT1H1M - 1 day, 1 hour and 1 minute. Minimum is 5 minutes, maximum is 14 days.||None||
||Time of the last lookup data, use the following format: PT + number + (M, H), where M - minutes, H - hours. Use P + number + D to specify a number of days. Can be combined as P1DT1H1M - 1 day, 1 hour and 1 minute. Minimum is 5 minutes, maximum is 14 days.||None||
||Trigger operator for this alert rule.Possible values are: GreaterThan, LessThan, Equal, NotEqual||None||
||Trigger threshold for this alert rule||None||
||Whether you want to stop running query after alert is generated||None||
||How long you want to stop running query after alert is generated, use the following format: PT + number + (M, H), where M - minutes, H - hours. Use P + number + D to specify a number of days. Can be combined as P1DT1H1M - 1 day, 1 hour and 1 minute. Minimum is 5 minutes, maximum is 14 days.||None||
||Description of the new alert rule||None||
||Tactics of the new alert rule. Comma-separated values.||None||



#### Update Incident Details v2
Update Incident Details v2. Action is a Chronicle SOAR async action and can be configured for a retry for a longer period of time.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
||Specify Azure Sentinel incident number to update.||None||
||Specify new title for the Azure Sentinel incident.||None||
||Specify new status for the Azure Sentinel incident.||None||
||Specify new severity for the Azure Sentinel incident.||None||
||Specify new description for the Azure Sentinel incident.||None||
||Specify the user to assign the incident to.||None||
||If status of the incident is set to Closed, provide a Closed Reason for the incident.||None||
||Optional closing comment to provide for the closed Azure Sentinel Incident.||None||
||Specify the number of retry attempts the action should make if the incident update was unsuccessful.||None||



#### Create Alert Rule
Create Azure Sentinel Scheduled Alert Rule
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
||Enable or disable new alert rule||None||
||Display name of the new alert rule||None||
||Severity of the new alert rule||None||
||Query of the new alert rule||None||
||How frequently to run the query, use the following format: PT + number + (M, H), where M - minutes, H - hours. Use P + number + D to specify a number of days. Can be combined as P1DT1H1M - 1 day, 1 hour and 1 minute. Minimum is 5 minutes, maximum is 14 days.||None||
||Time of the last lookup data, use the following format: PT + number + (M, H), where M - minutes, H - hours. Use P + number + D to specify a number of days. Can be combined as P1DT1H1M - 1 day, 1 hour and 1 minute. Minimum is 5 minutes, maximum is 14 days.||None||
||Trigger operator for this alert rule.Possible values are: GreaterThan, LessThan, Equal, NotEqual||None||
||Trigger threshold for this alert rule||None||
||Whether you want to stop running query after alert is generated||None||
||How long you want to stop running query after alert is generated, use the following format: PT + number + (M, H), where M - minutes, H - hours. Use P + number + D to specify a number of days. Can be combined as P1DT1H1M - 1 day, 1 hour and 1 minute. Minimum is 5 minutes, maximum is 14 days.||None||
||Description of the new alert rule||None||
||Tactics of the new alert rule. Comma-separated values.||None||



#### Get Custom Hunting Rule Details
Get Details of the Azure Sentinel Custom Hunting Rule
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
||Hunting Rule ID||None||



#### Create Custom Hunting Rule
Create Azure Sentinel Custom Hunting Rule
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
||Display name of the new custom hunting rule||None||
||Query of the new custom hunting rule||None||
||Description of the new custom hunting rule||None||
||Tactics of the new custom hunting rule. Comma-separated values.||None||



#### Delete Alert Rule
Delete Azure Sentinel Scheduled Alert Rule
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
||Alert Rule ID||None||



#### List Custom Hunting Rules
List Custom Hunting Rules available in Sentinel
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
||Names for the hunting rules action should return. Comma-separated string||None||
||What hunting rule tactics action should return. Comma-separated string||None||
||How many scheduled alert rules the action should return, for example, 50.||None||



#### Delete Custom Hunting Rule
Delete Azure Sentinel Custom Hunting Rule
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
||Hunting Rule ID||None||



#### Update Incident Labels v2
Update Incident Labels v2. Action is a Chronicle SOAR async action and can be configured for a retry for a longer period of time.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
||Specify Azure Sentinel incident number to update with new labels.||None||
||Specify new labels that should be appended to the Incident. Parameter accepts multiple values as a comma-separated string.||None||
||Specify the number of retry attempts the action should make if the incident update was unsuccessful.||None||



#### Run Custom Hunting Rule Query
Run Custom Hunting Rule Query
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
||Hunting Rule ID||None||
||Timeout value for the Azure Sentinel hunting rule API call||None||



#### List Alert Rules
Get Azure Sentinel Scheduled Rules list
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
||Severities of the alert rules to look for. Comma-separated string||None||
||What alert rule types action should return. Comma-separated string||None||
||What alert rule tactics action should return. Comma-separated string||None||
||If action should return only enabled alert rules||None||
||How many scheduled alert rules the action should return, for example, 50.||None||



#### Get Alert Rule Details
Get Details of the Azure Sentinel Scheduled Alert Rule
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
||Alert Rule ID||None||



#### Ping
Test connectivity to Microsoft Azure Sentinel
Timeout - 600 Seconds



#### Run KQL Query
Run Azure Sentinel KQL Query based on the provided action input parameters.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
||A KQL Query to execute in Azure Sentinel. For example, to get security alerts available in Sentinel, query will be "SecurityAlert". Use other action input parameters (time span, limit) to filter the query results. For the examples of KQL queries consider Sentinel "Logs" Web page||None||
||Time span to look for, use the following format: PT + number + (M, H), where M - minutes, H - hours. Use P + number + D to specify a number of days. Can be combined as P1DT1H1M - 1 day, 1 hour and 1 minute.||None||
||Timeout value for the Azure Sentinel hunting rule API call. Note that Siemplify action python process timeout should be adjusted accordingly for this parameter, to not timeout action sooner than specified value because of the python process timeout.||None||
||How many records should be fetched. Optional parameter, if set, adds a "| limit x" to the kql query where x is the value set for the record limit. Can be removed if "limit" is already set in kql query or not needed.||None||



#### Update Incident Labels
Update Incident Labels. Please consider moving to the v2 version of the action, as it is implemented as a SOAR async action and provides more consistent results.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
||Specify Azure Sentinel incident number to update with new labels.||None||
||Specify new labels that should be appended to the Incident. Parameter accepts multiple values as a comma-separated string.||None||
||Specify the number of retry attempts the action should make if the incident update was unsuccessful.||None||
||Specify what time period in seconds action should wait between incident update retries.||None||



#### Update Custom Hunting Rule
Update Azure Sentinel Custom Hunting Rule
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
||Hunting Rule ID||None||
||Display name of the new custom hunting rule||None||
||Query of the new custom hunting rule||None||
||Description of the new custom hunting rule||None||
||Tactics of the new custom hunting rule. Comma-separated values.||None||






## Jobs

#### Sync Incidents
Deprecated. This job synchronizes Google SecOps Alerts and Microsoft Sentinel Incidents. It ensures that comments, status, and tags are kept in sync between the two systems. For the job to identify the correct information, the Google SecOps case must have the “Microsoft Sentinel Incident” tag. If the alert didn’t originate from “Microsoft Azure Sentinel Incident Connector v2”,  you will need to add an “Incident_ID” context value to the case for the job to be able to find the correct information.

|Name|IsMandatory|Type|DefaultValue|
|----|-----------|----|------------|
|||None|Default Environment|
|||None||
|||None|https://login.microsoftonline.com|
|||None|https://graph.microsoft.com|
|||None||
|||None||
|||None|24|
|||None|true|

#### Sync Incidents V2
Use the Sync Incidents V2 job to synchronize Google SecOps alerts with Microsoft Sentinel incidents. This job ensures that comments, statuses, and tags are synchronized bi-directionally between both systems. Note: Assignee and severity synchronization occurs exclusively from Microsoft Sentinel to Google SecOps. For the job to identify the correct information, the Google SecOps case must have the Microsoft Sentinel Incident tag. This job only works on alerts from the Microsoft Azure Sentinel Incident Connector v2.

|Name|IsMandatory|Type|DefaultValue|
|----|-----------|----|------------|
|||None|Default Environment|
|||None||
|||None||
|||None|https://login.microsoftonline.com|
|||None|https://management.azure.com|
|||None||
|||None||
|||None||
|||None||
|||None|24|
|||None|false|
|||None|true|



## Connectors
#### Microsoft Sentinel Incident Tracking Connector
Connector works with Microsoft Azure Sentinel incidents and fetches updates to the Sentinel incidents as the new SecOps alerts. Connector's Dynamic List can be used to specify the incidents names that needs to be fetched. It is recommended to configure SecOps Alerts grouping based on SourceGroupIdentifier for this connector. See connector documentation for more information.

|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
||Describes the name of the field where the environment name is stored. If environment field isn't found, environment is "".||None||
||A regex pattern to run on the value found in the "Environment Field Name" field. Default is .* to catch all and return value unchanged. Used to allow the user to manipulate the environment field via regex logic. If regex pattern is null or empty, or the environment value is null, the final environment result is "".||None|.*|
||Microsoft Azure Subscription ID, can be viewed in Azure Portal > Subscriptions > <Your Subscription> > Subscription ID. ||None||
||Azure Entra ID Tenant ID, can be viewed in Active Directory > App Registration > <Application you configured for your integration> > Directory (tenant) ID.||None||
||Management.azure.com Api root url to use with integration.||None|https://management.azure.com|
||Specify the url, that connector should use for OAUTH2 Login.||None|https://login.microsoftonline.com|
||Name of Azure Resource Group where Azure Sentinel is located.||None||
||Name of the Azure Sentinel workspace to work with, can be viewed in Azure portal > Azure Sentinel > Azure Sentinel Workspaces.||None||
||Client (Application) ID that was added for the app registration in Azure Active Directory for this integration.||None||
||Secret that was entered for Azure AD app registration.||None||
||Verify SSL certificates for HTTPS requests to Microsoft Azure.||None|true|
||Number of hours before the first connector iteration to retrieve incidents from. This parameter applies to the initial connector iteration after you enable the connector for the first time, or used as a fallback value in cases where connector's last run timestamp expires.||None|24|
||Specify the statuses of the incidents that should be fetched by the SecOps server. Parameter can take multiple values as a comma separated string.||None|New,  Active, Closed|
||Specify the severities of the incidents that should be fetched by the SecOps server. Parameter can take multiple values as a comma separated string.||None|Informational, Low, Medium, High|
||How many incidents should be processed during one connector run.||None|10|
||If enabled, the connector will wait until a Scheduled/NRT alert object will be available.||None|false|
||By default connector uses a different approach with Scheduled Alert or NRT types of alerts - it tries to fetch events that caused the alert by running the query specified in alert details. Specify whether to change this behavior and use the same approach for the scheduled and NRT alerts as for other alert types.||None|false|
||Specify a comma separated list of tags Sentinel incident should have to be ingested. Incidents that will not have tags from this list will be ignored. Example of how Sentinel tags can be provided: tag1, tag2||None||
||If enabled, dynamic list will be used as a blocklist.||None|false|
||Time frame in minutes for connector to keep incidents in backlog for.||None|60|
||Specify a comma separated list of incident or alert attributes that should be used as a fallback for the "Start Time" alert field in descending order. Additionally, new "SecOps_Start_Time" attribute will be added to created events. First attribute will have the highest priority, next if its not present or empty in the event - fallback to the next value from the list and so on. If none of the fallback fields are found, connector will use createdTimeUTC, and if that's also non existent - alert ingestion time to SecOps.||None|properties_firstActivityTimeGenerated,properties_startTimeUtc,properties_createdTimeUtc,properties_firstAlertTimeGenerated|
||Specify a comma separated list of incident or alert attributes that should be used as a fallback for the "End Time" alert field in descending order. Additionally, new "SecOps_End_Time" attribute will be added to created events. First attribute will have the highest priority, next if its not present or empty in the event - fallback to the next value from the list and so on. If none of the fallback fields are found, connector will use createdTimeUTC, and if that's also non existent - alert ingestion time to SecOps.||None|properties_lastActivityTimeGenerated,properties_endTimeUtc,properties_createdTimeUtc,properties_lastAlertTimeGenerated|
||Specify if connector should add to the created events a "debug" fields that will contain the values it used for fallback.||None|false|
||Specify a comma separated list of incident attributes that should be used as a fallback for the "DeviceVendor" field in descending order. First attribute will have the highest priority, next if its not present or empty in the event - fallback to the next value from the list and so on.||None|vendorName|
||Specify a comma separated list of incident or alert attributes that should be used as a fallback for the "Product Field Name" parameter and "DeviceProduct" field in descending order. First attribute will have the highest priority, next if its not present or empty in the event - fallback to the next value from the list and so on.||None|ProductName|
||Specify a comma separated list of alert attributes that should be used as a fallback for the "Event Field Name" parameter in descending order. First attribute will have the highest priority, next if its not present or empty in the event - fallback to the next value from the list and so on.||None|kind|
||How many incidents  connector should try to fetch from the backlog during one connector run.||None|10|
||If enabled, the connector will disable the overflow mechanism.||None|false|
||Specify the total number of events the connector should ingest for a Microsoft Sentinel incident that is based on a Scheduled or NRT alert. Connector ‘counts’ events in all corresponding SecOps alerts created for the Microsoft Sentinel Incident and no new events will be ingested once this limit is reached.||None|100|
||If enabled, connector will create SecOps alerts from Microsoft Sentinel incidents that dont have entities. Otherwise, such incidents will be skipped for all Sentinel incidents types except Sentinel Scheduled and NRT alerts.||None|false|
||If specified, to get incidents returned not in chronological order, connector will fetch Sentinel incidents from this value backwards in time.||None|60|
||If specified, connector will use this value from the Microsoft Azure Sentinel API response for incident data for Chronicle SOAR Alert Name. You can provide placeholders in the following format: [name of the field]. Example: Sentinel incident - [title]. Note: the maximum length for the field is 256 characters. If nothing is provided or user provides an invalid template, connector will use the default alert name.||None||
||If specified, connector will use this value from the Microsoft Azure Sentinel API response for incident data for Chronicle SOAR Rule Generator. You can provide placeholders in the following format: [name of the field]. Example: Sentinel incident - [severity]. Note: the maximum length for the field is 256 characters. If nothing is provided or user provides an invalid template, connector will use the default rule generator value.||None||
||Specify how long connector should track already ingested Sentinel incident for updates - either addition of new events or entities and incident details.||None|24|
||Proxy server to use for connection.||None||
||Proxy server username.||None||
||Proxy server password.||None||
||If enabled, when creating entities from the Sentinel API, connector will create extra SecOps events for all Sentinel incident's entities, not only Account, Mailbox, Host or Ip.||None|false|


#### Microsoft Azure Sentinel Incident Connector v2
Connector works with Microsoft Azure Sentinel incidents. Connector's Dynamic List can be used to specify the incidents names that needs to be fetched. See connector documentation for more information.

|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
||If enabled, the connector will disable the overflow mechanism.||None|false|
||Specify if connector should add to the created events a “debug“ fields that will contain the values it used for fallback.||None|false|
||Describes the name of the field where the environment name is stored. If environment field isn't found, environment is "".||None||
||Specify the maximum number of events the connector should ingest per a single Azure Sentinel Scheduled or NRT Alert.||None|100|
||A regex pattern to run on the value found in the "Environment Field Name" field. Default is .* to catch all and return value unchanged. Used to allow the user to manipulate the environment field via regex logic. If regex pattern is null or empty, or the environment value is null, the final environment result is "".||None|.*|
||Microsoft Azure Subscription ID, can be viewed in Azure Portal > Subscriptions > <Your Subscription> > Subscription ID. ||None||
||Azure Active Directory Tenant ID, can be viewed in Active Directory > App Registration > <Application you configured for your integration> > Directory (tenant) ID.||None||
||The API Root of Microsoft Azure Sentinel REST API root.||None|https://management.azure.com|
||Specify the url, that connector should use for OAUTH2 Login.||None|https://login.microsoftonline.com|
||Name of Azure Resource Group where Azure Sentinel is located.||None||
||Name of the Azure Sentinel workspace to work with, can be viewed in Azure portal > Azure Sentinel > Azure Sentinel Workspaces.||None||
||Client (Application) ID that was added for the app registration in Azure Active Directory for this integration.||None||
||Secret that was entered for Azure AD app registration||None||
||Verify SSL certificates for HTTPS requests to Microsoft Azure.||None|false|
||How many incidents should be processed during one connector run||None|10|
||How many incidents  connector should try to fetch from the backlog during one connector run.||None|10|
||Number of hours before the first connector iteration to retrieve incidents alerts. This parameter applies to the initial connector iteration after you enable the connector for the first time, or used as a fallback value in cases where connector's last run timestamp expires. Default value: 24 hours.||None|24|
||Specify the statuses of the incidents that should be fetched by the Chronicle SOAR server. Parameter can take multiple values as a comma separated string.||None|New, Closed|
||Specify the severities of the incidents that should be fetched by the Chronicle SOAR server. Parameter can take multiple values as a comma separated string.||None|Informational, Low, Medium, High|
||By default connector uses a different approach with Scheduled Alert or NRT types of alerts - it tries to fetch events that caused the alert by running the query specified in alert details. Specify whether to change this behavior and use the same approach for the scheduled and NRT alerts as for other alert types.||None|false|
||If enabled, dynamic list will be used as a blocklist.||None|false|
||Time frame in minutes for connector to keep incidents in backlog for.||None|60|
||Specify a comma separated list of alert attributes that should be used as a fallback for the "Event Field Name" parameter in descending order. First attribute will have the highest priority, next if its not present or empty in the event - fallback to the next value from the list and so on.||None|kind|
||Specify a comma separated list of incident or alert attributes that should be used as a fallback for the "Product Field Name" parameter and "DeviceProduct" field in descending order. First attribute will have the highest priority, next if its not present or empty in the event - fallback to the next value from the list and so on.||None|ProductName,properties_providerName|
||Specify a comma separated list of incident attributes that should be used as a fallback for the "DeviceVendor" field in descending order. First attribute will have the highest priority, next if its not present or empty in the event - fallback to the next value from the list and so on.||None|vendorName|
||Specify a comma separated list of incident or alert attributes that should be used as a fallback for the “Start Time” alert field in descending order. Additionally, new “Siemplify_Start_Time“ attribute will be added to created events. First attribute will have the highest priority, next if its not present or empty in the event - fallback to the next value from the list and so on. If none of the fallback fields are found, connector will use createdTimeUTC, and if that's also non existent - alert ingestion time to Chronicle SOAR.||None|properties_firstActivityTimeGenerated,properties_startTimeUtc,properties_createdTimeUtc,properties_firstAlertTimeGenerated|
||Specify a comma separated list of incident or alert attributes that should be used as a fallback for the “End Time” alert field in descending order. Additionally, new “Siemplify_End_Time“ attribute will be added to created events. First attribute will have the highest priority, next if its not present or empty in the event - fallback to the next value from the list and so on. If none of the fallback fields are found, connector will use createdTimeUTC, and if that's also non existent - alert ingestion time to Chronicle SOAR.||None|properties_lastActivityTimeGenerated,properties_endTimeUtc,properties_createdTimeUtc,properties_lastAlertTimeGenerated|
||Specify a comma separated list of tags Sentinel incident should have to be ingested. Incidents that will not have tags from this list will be ignored. Example of how Sentinel tags can be provided: tag1, tag2||None||
||If enabled, connector will create Chronicle SOAR alerts from Microsoft Sentinel incidents that dont have entities. Otherwise, such incidents will be skipped for all Sentinel incidents types except Sentinel Scheduled and NRT alerts.||None|false|
||Specify the maximum number of  alerts the connector should ingest per a single Azure Sentinel incident.||None|10|
||Proxy server to use for connection.||None||
||Proxy server username||None||
||Proxy server password||None||
||If specified, to get incidents returned not in chronological order, connector will fetch Sentinel incidents from this value backwards in time.||None|60|
||If specified, connector will use this value from the Microsoft Azure Sentinel API response for incident data for Chronicle SOAR Alert Name. You can provide placeholders in the following format: [name of the field]. Example: Sentinel incident - [title]. Note: the maximum length for the field is 256 characters. If nothing is provided or user provides an invalid template, connector will use the default alert name.||None||
||If specified, connector will use this value from the Microsoft Azure Sentinel API response for incident data for Chronicle SOAR Rule Generator. You can provide placeholders in the following format: [name of the field]. Example: Sentinel incident - [severity]. Note: the maximum length for the field is 256 characters. If nothing is provided or user provides an invalid template, connector will use the default rule generator value.||None||
||If enabled, when creating entities from the Sentinel API, connector will create extra SecOps events for all Sentinel incident's entities, not only Account, Mailbox, Host or Ip.||None|false|
||If specified, the value will be applied as the maximum waiting time in seconds for any request made to Azure API. Defaults to 60.||None|60|
||If enabled, the connector will wait until a Scheduled/NRT alert object will be available.||None|false|


#### Microsoft Azure Sentinel Incident Connector
DEPRECATED! Fetches Incidents from Azure Sentinel.

|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
||Describes the name of the field where the environment name is stored.||None||
||If defined - the connector will implement the specific RegEx pattern on the data from "environment field" to extract specific string. For example - extract domain from sender's address: "(?<=@)(\S+$)"||None||
||The API Root of Microsoft Azure Sentinel REST API root.||None|https://management.azure.com|
||Specify the url, that connector should use for OAUTH2 Login.||None|https://login.microsoftonline.com|
||Client (Application) ID that was added for the app registration in Azure Active Directory for this integration.||None||
||Secret that was entered for Azure AD app registration||None||
||Azure Active Directory Tenant ID, can be viewed in Active Directory > App Registration > <Application you configured for your integration> > Directory (tenant) ID.||None||
||Name of the Azure Sentinel workspace to work with, can be viewed in Azure portal > Azure Sentinel > Azure Sentinel Workspaces.||None||
||Microsoft Azure Subscription ID, can be viewed in Azure Portal > Subscriptions > <Your Subscription> > Subscription ID. ||None||
||Name of Azure Resource Group where Azure Sentinel is located.||None||
||Verify SSL certificates for HTTPS requests to Microsoft Azure.||None|false|
||How many incidents should be processed during one connector run||None|10|
||Number of hours before the first connector iteration to retrieve alerts from. This parameter applies to the initial connector iteration after you enable the connector for the first time, or used as a fallback value in cases where connector's last run timestamp expires. Default value: 24 hours.||None|24|
||Specify the statuses of the incidents that should be fetched by the Siemplify server. Comma-separated string.||None|Draft, New, InProgress, Closed|
||Specify the severities of the incidents that should be fetched by the Siemplify server. Comma-separated string.||None|Informational, Low, Medium, High, Critical|
||Proxy server to use for connection.||None||
||Proxy server username||None||
||Proxy server password||None||




