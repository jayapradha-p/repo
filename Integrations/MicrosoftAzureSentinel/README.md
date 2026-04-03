
# MicrosoftAzureSentinel

Microsoft Azure Sentinel is a scalable, cloud-native, security information event management (SIEM) and security orchestration automated response (SOAR) solution. Azure Sentinel delivers intelligent security analytics and threat intelligence across the enterprise, providing a single solution for alert detection, threat visibility, proactive hunting, and threat response.

Python Version - 3


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
||Specify Incident number to add comment to.||String||
||Specify comment to add to Incident||String||



##### JSON Results
```json
{"id":"/subscriptions/a052d33b-xxxx-4dc7-9e17-xxxxxxxxxxxx/resourceGroups/sentinel-check/providers/Microsoft.OperationalInsights/workspaces/sentinelwork01/providers/Microsoft.SecurityInsights/Incidents/00cfebdc-xxxx-463f-8355-xxxxxxxxxxxx/Comments/f0f31d1a-xxxx-4774-a21d-xxxxxxxxxxxx","name":"f0f31d1a-xxxx-4774-a21d-xxxxxxxxxxxx","etag":"\"7e000812-0000-0c00-0000-xxxxxxxxxxxx\"","type":"Microsoft.SecurityInsights/Incidents/Comments","properties":{"message":"Some message","createdTimeUtc":"2021-04-09T03:21:35.0894288Z","lastModifiedTimeUtc":"2021-04-09T03:21:35.0894288Z","author":{"objectId":"f6ce2f43-xxxx-4b30-9a4a-xxxxxxxxxxxx","email":null,"name":"Comment created from external application - log_analytics_rest_api_for_sentinel","userPrincipalName":null}}}
```



#### Get Incident Statistic
Get Azure Sentinel Incident Statistics
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
||Time frame in hours for which to fetch Incidents||String||



##### JSON Results
```json
{"ID":"/subscriptions/XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/XXXXXXXXXX/providers/Microsoft.XXXXXX","Name":"Cases","Kind":"CasesAggregation","Type":"Microsoft.SecurityInsights/Aggregations","Properties":{"Aggregation_By_Severity":{"Total_Critical_Severity":0,"Total_High_Severity":2,"Total_Medium_Severity":0,"Total_Low_Severity":0,"Total_Informational_Severity":0},"Aggregation_By_Status":{"Total_New_Status":2,"Total_In_Progress_Status":0,"Total_Resolved_Status":0,"Total_Dismissed_Status":0,"Total_True_Positive_Status":0,"Total_False_Positive_Status":0}}}
```



#### List Incidents
List Microsoft Azure Sentinel Incidents based on the provided search criteria.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
||Time frame in hours for which to fetch Incidents||String|3|
||Statuses of the incidents to look for. Comma-separated string||String|New, Active, Closed|
||Severities of the incidents to look for. Comma-separated string.||String|Informational, Low, Medium, High|
||How many incidents to fetch||String|200|



##### JSON Results
```json
[{"id":"/subscriptions/XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/resourceGroups/sentinel-check/providers/Microsoft.OperationalInsights/workspaces/XXXXXXXXXXXXXXX/providers/Microsoft.SecurityInsights/Incidents/XXXXXXXXXXXXXXXXXXXXXXXXXXXX","name":"XXXXXXXXXXXXXXXXXXXXXXXXXXXX","etag":"XXXXXXXXXXXXXXXXXXXXXXXXXXXXX","type":"Microsoft.SecurityInsights/Incidents","properties":{"title":"X","description":"Activity policyXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX","severity":"Low","status":"New","owner":{"objectId":null,"email":null,"assignedTo":null,"userPrincipalName":null},"labels":[],"firstActivityTimeUtc":"2021-04-13T07:42:54.366Z","lastActivityTimeUtc":"2021-04-13T07:42:54.366Z","lastModifiedTimeUtc":"2021-04-13T07:43:02.870674Z","createdTimeUtc":"2021-04-13T07:43:02.870674Z","incidentNumber":10684490,"additionalData":{"alertsCount":1,"bookmarksCount":0,"commentsCount":0,"alertProductNames":["Microsoft Cloud App Security"],"tactics":[]},"relatedAnalyticRuleIds":["/subscriptions/XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/resourceGroups/sentinel-check/providers/Microsoft.OperationalInsights/workspaces/XXXXXXXXXXXXXXX/providers/Microsoft.SecurityInsights/alertRules/XXXXXXXXXXXXXXXXXXXXX","/subscriptions/XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/resourceGroups/sentinel-check/providers/Microsoft.OperationalInsights/workspaces/XXXXXXXXXXXXXXX/providers/Microsoft.SecurityInsights/alertRules/XXXXXXXXXXXXXXXXXXXXX","/subscriptions/XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/resourceGroups/sentinel-check/providers/Microsoft.OperationalInsights/workspaces/XXXXXXXXXXXXXXX/providers/Microsoft.SecurityInsights/alertRules/XXXXXXXXXXXXXXXXXXXXX","/subscriptions/XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/resourceGroups/sentinel-check/providers/Microsoft.OperationalInsights/workspaces/XXXXXXXXXXXXXXX/providers/Microsoft.SecurityInsights/alertRules/XXXXXXXXXXXXXXXXXXXXX","/subscriptions/XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/resourceGroups/sentinel-check/providers/Microsoft.OperationalInsights/workspaces/XXXXXXXXXXXXXXX/providers/Microsoft.SecurityInsights/alertRules/XXXXXXXXXXXXXXXXXXXXX"],"incidentUrl":"https://portal.azure.com/#asset/Microsoft_Azure_Security_Insights/Incident/subscriptions/XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/resourceGroups/sentinel-check/providers/Microsoft.OperationalInsights/workspaces/XXXXXXXXXXXXXXX/providers/Microsoft.SecurityInsights/Incidents/XXXXXXXXXXXXXXXXXXXXXXXXXXXX","providerName":"Azure Sentinel","providerIncidentId":"XXXXXXX"}},{"id":"/subscriptions/XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/resourceGroups/sentinel-check/providers/Microsoft.OperationalInsights/workspaces/XXXXXXXXXXXXXXX/providers/Microsoft.SecurityInsights/Incidents/XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX","name":"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX","etag":"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX","type":"Microsoft.SecurityInsights/Incidents","properties":{"title":"X","description":"Activity policyXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX","severity":"Low","status":"New","owner":{"objectId":null,"email":null,"assignedTo":null,"userPrincipalName":null},"labels":[],"firstActivityTimeUtc":"2021-04-13T07:33:03.572Z","lastActivityTimeUtc":"2021-04-13T07:33:03.572Z","lastModifiedTimeUtc":"2021-04-13T07:33:33.0348454Z","createdTimeUtc":"2021-04-13T07:33:33.0348454Z","incidentNumber":10444889,"additionalData":{"alertsCount":1,"bookmarksCount":0,"commentsCount":0,"alertProductNames":["Microsoft Cloud App Security"],"tactics":[]},"relatedAnalyticRuleIds":["/subscriptions/XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/resourceGroups/sentinel-check/providers/Microsoft.OperationalInsights/workspaces/XXXXXXXXXXXXXXX/providers/Microsoft.SecurityInsights/alertRules/XXXXXXXXXXXXXXXXXXXXX","/subscriptions/XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/resourceGroups/sentinel-check/providers/Microsoft.OperationalInsights/workspaces/XXXXXXXXXXXXXXX/providers/Microsoft.SecurityInsights/alertRules/XXXXXXXXXXXXXXXXXXXXXXXXXXXXX","/subscriptions/XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/resourceGroups/sentinel-check/providers/Microsoft.OperationalInsights/workspaces/XXXXXXXXXXXXXXX/providers/Microsoft.SecurityInsights/alertRules/XXXXXXXXXXXXXXXXXXXXX","/subscriptions/XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/resourceGroups/sentinel-check/providers/Microsoft.OperationalInsights/workspaces/XXXXXXXXXXXXXXX/providers/Microsoft.SecurityInsights/alertRules/XXXXXXXXXXXXXXXXXXXXX","/subscriptions/XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/resourceGroups/sentinel-check/providers/Microsoft.OperationalInsights/workspaces/XXXXXXXXXXXXXXX/providers/Microsoft.SecurityInsights/alertRules/XXXXXXXXXXXXXXXXXXXXXX"],"incidentUrl":"https://portal.azure.com/#asset/Microsoft_Azure_Security_Insights/Incident/subscriptions/XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/resourceGroups/sentinel-check/providers/Microsoft.OperationalInsights/workspaces/XXXXXXXXXXXXXXX/providers/Microsoft.SecurityInsights/Incidents/XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX","providerName":"Azure Sentinel","providerIncidentId":"XXXXX"}}]
```



#### Update Incident Details
Update Incident Details. Please consider moving to the v2 version of the action, as it is implemented as a SOAR async action and provides more consistent results.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
||Specify Azure Sentinel incident number to update.||String||
||Specify new title for the Azure Sentinel incident.||String||
||Specify new status for the Azure Sentinel incident.||List|Not Updated|
||Specify new severity for the Azure Sentinel incident.||List|Not Updated|
||Specify new description for the Azure Sentinel incident.||String||
||Specify the user to assign the incident to.||String||
||If status of the incident is set to Closed, provide a Closed Reason for the incident.||List|Not Updated|
||Optional closing comment to provide for the closed Azure Sentinel Incident.||String||
||Specify the number of retry attempts the action should make if the incident update was unsuccessful.||String||
||Specify what time period action should wait between incident update retries.||String||



##### JSON Results
```json
{"id": "/subscriptions/a052d33b-b7c4-4dc7-9e17-xxxxx/resourceGroups/sentinel-check/providers/Microsoft.OperationalInsights/workspaces/sentinelwork01/providers/Microsoft.SecurityInsights/Incidents/2e0ce5a0-7563-43a1-86a4-xxxxx", "name": "2e0ce5a0-7563-43a1-86a4-xxxxx", "etag": "\"fb006b40-0000-0c00-0000-xxxxx\"", "type": "Microsoft.SecurityInsights/Incidents", "properties": {"title": "Test Name", "description": "", "severity": "Informational", "status": "Closed", "classification": "Undetermined", "classificationComment": "Hello Test", "owner": {"objectId": null, "email": null, "assignedTo": null, "userPrincipalName": null}, "labels": [], "firstActivityTimeUtc": "2021-04-09T05:47:55.4959374Z", "lastActivityTimeUtc": "2021-04-14T05:47:55.4959374Z", "lastModifiedTimeUtc": "2021-04-14T06:53:30.2380985Z", "createdTimeUtc": "2021-04-14T05:53:00.8171911Z", "incidentNumber": "106xxx", "additionalData": {"alertsCount": 1, "bookmarksCount": 0, "commentsCount": 0, "alertProductNames": ["Azure Sentinel"], "tactics": ["InitialAccess", "Execution"]}, "relatedAnalyticRuleIds": ["/subscriptions/a052d33b-b7c4-4dc7-9e17-xxxxx/resourceGroups/sentinel-check/providers/Microsoft.OperationalInsights/workspaces/sentinelwork01/providers/Microsoft.SecurityInsights/alertRules/545ee671-a997-4a5a-8763-xxxxx"], "incidentUrl": "https://portal.azure.com/#asset/Microsoft_Azure_Security_Insights/Incident/subscriptions/a052d33b-b7c4-4dc7-9e17-xxxxx/resourceGroups/sentinel-check/providers/Microsoft.OperationalInsights/workspaces/sentinelwork01/providers/Microsoft.SecurityInsights/Incidents/2e0ce5a0-7563-43a1-86a4-xxxxx", "providerName": "Azure Sentinel", "providerIncidentId": "106xxx"}}
```



#### Update Alert Rule
Update Azure Sentinel Scheduled Alert Rule
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
||Alert Rule ID||String||
||Enable or disable new alert rule||Boolean|true|
||Display name of the new alert rule||String||
||Severity of the new alert rule||List|Informational|
||Query of the new alert rule||String||
||How frequently to run the query, use the following format: PT + number + (M, H), where M - minutes, H - hours. Use P + number + D to specify a number of days. Can be combined as P1DT1H1M - 1 day, 1 hour and 1 minute. Minimum is 5 minutes, maximum is 14 days.||String||
||Time of the last lookup data, use the following format: PT + number + (M, H), where M - minutes, H - hours. Use P + number + D to specify a number of days. Can be combined as P1DT1H1M - 1 day, 1 hour and 1 minute. Minimum is 5 minutes, maximum is 14 days.||String||
||Trigger operator for this alert rule.Possible values are: GreaterThan, LessThan, Equal, NotEqual||List|GreaterThan|
||Trigger threshold for this alert rule||String||
||Whether you want to stop running query after alert is generated||Boolean|true|
||How long you want to stop running query after alert is generated, use the following format: PT + number + (M, H), where M - minutes, H - hours. Use P + number + D to specify a number of days. Can be combined as P1DT1H1M - 1 day, 1 hour and 1 minute. Minimum is 5 minutes, maximum is 14 days.||String||
||Description of the new alert rule||String||
||Tactics of the new alert rule. Comma-separated values.||String||



##### JSON Results
```json
{"Kind": "Scheduled", "Name": "31d38dc9-16fc-4464-8586-xxxx", "ID": "/subscriptions/a052d33b-b7c4-4dc7-9e17-xxxx/resourceGroups/sentinel-check/providers/Microsoft.OperationalInsights/workspaces/sentinelwork01/providers/Microsoft.SecurityInsights/alertRules/31d38dc9-16fc-4464-8586-xxxx", "ETag": "\"390028e7-0000-0d00-0000-xxxx\"", "Type": "Microsoft.SecurityInsights/alertRules", "Properties": {"Tactics": ["Discovery", "InitialAccess"], "Severity": "High", "Suppression_Enabled": false, "Query_Period": "5 days 0 hours 0 minutes 0 seconds", "Enabled": true, "Query_Frequency": "0 days 1 hour 0 minutes 0 seconds", "Alert_Rule_Template_Name": null, "Display_Name": "some name", "Description": "test", "Last_Modified_UTC": "2020-01-23T21:00:17.0860777Z", "Suppression_Duration": "0 days 5 hours 0 minutes 0 seconds", "Trigger": null, "Query": "SecurityEvent\r\n| where Activity startswith \"4625\"\r\n| summarize count() by IpAddress, Computer\r\n| where count_ >3\r\n| extend HostCustomEntity = Computer\r\n| extend IPCustomEntity = IpAddress"}}
```



#### Update Incident Details v2
Update Incident Details v2. Action is a Chronicle SOAR async action and can be configured for a retry for a longer period of time.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
||Specify Azure Sentinel incident number to update.||String||
||Specify new title for the Azure Sentinel incident.||String||
||Specify new status for the Azure Sentinel incident.||List|Not Updated|
||Specify new severity for the Azure Sentinel incident.||List|Not Updated|
||Specify new description for the Azure Sentinel incident.||String||
||Specify the user to assign the incident to.||String||
||If status of the incident is set to Closed, provide a Closed Reason for the incident.||List|Not Updated|
||Optional closing comment to provide for the closed Azure Sentinel Incident.||String||
||Specify the number of retry attempts the action should make if the incident update was unsuccessful.||String||



##### JSON Results
```json
{"id": "/subscriptions/a052d33b-b7c4-4dc7-9e17-xxxxx/resourceGroups/sentinel-check/providers/Microsoft.OperationalInsights/workspaces/sentinelwork01/providers/Microsoft.SecurityInsights/Incidents/2e0ce5a0-7563-43a1-86a4-xxxxx", "name": "2e0ce5a0-7563-43a1-86a4-xxxxx", "etag": "\"fb006b40-0000-0c00-0000-xxxxx\"", "type": "Microsoft.SecurityInsights/Incidents", "properties": {"title": "Test Name", "description": "", "severity": "Informational", "status": "Closed", "classification": "Undetermined", "classificationComment": "Hello Test", "owner": {"objectId": null, "email": null, "assignedTo": null, "userPrincipalName": null}, "labels": [], "firstActivityTimeUtc": "2021-04-09T05:47:55.4959374Z", "lastActivityTimeUtc": "2021-04-14T05:47:55.4959374Z", "lastModifiedTimeUtc": "2021-04-14T06:53:30.2380985Z", "createdTimeUtc": "2021-04-14T05:53:00.8171911Z", "incidentNumber": "106xxx", "additionalData": {"alertsCount": 1, "bookmarksCount": 0, "commentsCount": 0, "alertProductNames": ["Azure Sentinel"], "tactics": ["InitialAccess", "Execution"]}, "relatedAnalyticRuleIds": ["/subscriptions/a052d33b-b7c4-4dc7-9e17-xxxxx/resourceGroups/sentinel-check/providers/Microsoft.OperationalInsights/workspaces/sentinelwork01/providers/Microsoft.SecurityInsights/alertRules/545ee671-a997-4a5a-8763-xxxxx"], "incidentUrl": "https://portal.azure.com/#asset/Microsoft_Azure_Security_Insights/Incident/subscriptions/a052d33b-b7c4-4dc7-9e17-xxxxx/resourceGroups/sentinel-check/providers/Microsoft.OperationalInsights/workspaces/sentinelwork01/providers/Microsoft.SecurityInsights/Incidents/2e0ce5a0-7563-43a1-86a4-xxxxx", "providerName": "Azure Sentinel", "providerIncidentId": "106xxx"}}
```



#### Create Alert Rule
Create Azure Sentinel Scheduled Alert Rule
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
||Enable or disable new alert rule||Boolean|true|
||Display name of the new alert rule||String||
||Severity of the new alert rule||List|Informational|
||Query of the new alert rule||String||
||How frequently to run the query, use the following format: PT + number + (M, H), where M - minutes, H - hours. Use P + number + D to specify a number of days. Can be combined as P1DT1H1M - 1 day, 1 hour and 1 minute. Minimum is 5 minutes, maximum is 14 days.||String||
||Time of the last lookup data, use the following format: PT + number + (M, H), where M - minutes, H - hours. Use P + number + D to specify a number of days. Can be combined as P1DT1H1M - 1 day, 1 hour and 1 minute. Minimum is 5 minutes, maximum is 14 days.||String||
||Trigger operator for this alert rule.Possible values are: GreaterThan, LessThan, Equal, NotEqual||List|GreaterThan|
||Trigger threshold for this alert rule||String||
||Whether you want to stop running query after alert is generated||Boolean|true|
||How long you want to stop running query after alert is generated, use the following format: PT + number + (M, H), where M - minutes, H - hours. Use P + number + D to specify a number of days. Can be combined as P1DT1H1M - 1 day, 1 hour and 1 minute. Minimum is 5 minutes, maximum is 14 days.||String||
||Description of the new alert rule||String||
||Tactics of the new alert rule. Comma-separated values.||String||



##### JSON Results
```json
{"Kind": "Scheduled", "Name": "31d38dc9-16fc-4464-8586-41bbfa220766", "ID": "/subscriptions/a052d33b-b7c4-4dc7-9e17-5c89ea594669/resourceGroups/sentinel-check/providers/Microsoft.OperationalInsights/workspaces/sentinelwork01/providers/Microsoft.SecurityInsights/alertRules/31d38dc9-16fc-4464-8586-41bbfa220766", "ETag": "\"390028e7-0000-0d00-0000-5e2a09660000\"", "Type": "Microsoft.SecurityInsights/alertRules", "Properties": {"Tactics": ["Discovery", "InitialAccess"], "Severity": "High", "Suppression_Enabled": false, "Query_Period": "5 days 0 hours 0 minutes 0 seconds", "Enabled": true, "Query_Frequency": "0 days 1 hour 0 minutes 0 seconds", "Alert_Rule_Template_Name": null, "Display_Name": "some name", "Description": "dsadad", "Last_Modified_UTC": "2020-01-23T21:00:17.0860777Z", "Suppression_Duration": "0 days 5 hours 0 minutes 0 seconds", "Trigger": null, "Query": "SecurityEvent\r\n| where Activity startswith \"4625\"\r\n| summarize count() by IpAddress, Computer\r\n| where count_ >3\r\n| extend HostCustomEntity = Computer\r\n| extend IPCustomEntity = IpAddress"}}
```



#### Get Custom Hunting Rule Details
Get Details of the Azure Sentinel Custom Hunting Rule
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
||Hunting Rule ID||String||



##### JSON Results
```json
{"Properties": {"Category": "Hunting Queries", "Tactics": ["DefenseEvasion"], "Tags": [{"Name": "description", "Value": "123"}, {"Name": "tactics", "Value": "DefenseEvasion"}, {"Name": "createdBy", "Value": "yuriy.landovskyy@siemplifycyarx.onmicrosoft.com"}, {"Name": "createdTimeUtc", "Value": "12/02/2019 09:21:18"}], "Version": 2, "Display_Name": "Yura Query", "Query": "\r\nlet timeframe = 7d;\r\nAWSCloudTrail\r\n| where TimeGenerated >= ago(timeframe)\r\n| where  EventName in~ (\"AttachGroupPolicy\", \"AttachRolePolicy\", \"AttachUserPolicy\", \"CreatePolicy\",\r\n\"DeleteGroupPolicy\", \"DeletePolicy\", \"DeleteRolePolicy\", \"DeleteUserPolicy\", \"DetachGroupPolicy\",\r\n\"PutUserPolicy\", \"PutGroupPolicy\", \"CreatePolicyVersion\", \"DeletePolicyVersion\", \"DetachRolePolicy\", \"CreatePolicy\")\r\n| project TimeGenerated, EventName, EventTypeName, UserIdentityAccountId, UserIdentityPrincipalid, UserAgent, \r\nUserIdentityUserName, SessionMfaAuthenticated, SourceIpAddress, AWSRegion, EventSource, AdditionalEventData, ResponseElements\r\n| extend timestamp = TimeGenerated, IPCustomEntity = SourceIpAddress, AccountCustomEntity = UserIdentityAccountId\r\n"}, "ETag": "W/\"datetime'2019-12-08T09%3A34%3A10.176586Z'\"", "ID": "subscriptions/a052d33b-XXXX-XXXX-XXXX-5c89ea594669/resourceGroups/sentinel-check/providers/Microsoft.OperationalInsights/workspaces/sentinelwork01/savedSearches/XXXXXXXXXXXXXXXXXXXXXXXXXX", "Name": "XXXXXXXXXXXXXXXXXXXXXXXXXX"}
```



#### Create Custom Hunting Rule
Create Azure Sentinel Custom Hunting Rule
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
||Display name of the new custom hunting rule||String||
||Query of the new custom hunting rule||String||
||Description of the new custom hunting rule||String||
||Tactics of the new custom hunting rule. Comma-separated values.||String||



##### JSON Results
```json
{"Properties": {"Category": "Log Management O", "Tactics": ["CustomTactic", "NotCustomTactic"], "Tags": [{"Name": "description", "Value": "Some Desc"}, {"Name": "tactics", "Value": "CustomTactic"}, {"Name": "tactics", "Value": "NotCustomTactic"}], "Version": 2, "Display_Name": "Some Name", "Query": "let timeframe = 7d;AWSCloudTrail| where TimeGenerated >= ago(timeframe)| where  EventName in~ (\"AttachGroupPolicy\", \"AttachRolePolicy\", \"AttachUserPolicy\", \"CreatePolicy\",\"DeleteGroupPolicy\", \"DeletePolicy\", \"DeleteRolePolicy\", \"DeleteUserPolicy\", \"DetachGroupPolicy\",\"PutUserPolicy\", \"PutGroupPolicy\", \"CreatePolicyVersion\", \"DeletePolicyVersion\", \"DetachRolePolicy\", \"CreatePolicy\")| project TimeGenerated, EventName, EventTypeName, UserIdentityAccountId, UserIdentityPrincipalid, UserAgent, UserIdentityUserName, SessionMfaAuthenticated, SourceIpAddress, AWSRegion, EventSource, AdditionalEventData, ResponseElements| extend timestamp = TimeGenerated, IPCustomEntity = SourceIpAddress, AccountCustomEntity = UserIdentityAccountId"}, "ETag": "W/\"datetime'2020-01-23T21%3A13%3A18.968169Z'\"", "ID": "subscriptions/a052d33b-b5c4-4dc7-9e17-5c89ea594669/resourceGroups/sentinel-check/providers/Microsoft.OperationalInsights/workspaces/sentinelwork01/savedSearches/a5a24268-XXXX-XXXX-XXXX-4ab6c9b7ad5b", "Name": "a052d33b-b5c4-XXXX-XXXX-5c89ea594669"}
```



#### Delete Alert Rule
Delete Azure Sentinel Scheduled Alert Rule
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
||Alert Rule ID||String||



#### List Custom Hunting Rules
List Custom Hunting Rules available in Sentinel
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
||Names for the hunting rules action should return. Comma-separated string||String||
||What hunting rule tactics action should return. Comma-separated string||String||
||How many scheduled alert rules the action should return, for example, 50.||String||



##### JSON Results
```json
[{"Properties": {"Category": "General Exploration", "Tactics": ["Execution"], "Tags": [{"Name": "description", "Value": "456"}, {"Name": "tactics", "Value": "DefenseEvasion"}], "Version": 2, "Display_Name": "All Computers with their most recent data", "Query": "search not(ObjectName == \"Advisor Metrics\" or ObjectName == \"ManagedSpace\") | summarize AggregatedValue = max(TimeGenerated) by Computer | limit 500000 | sort by Computer asc\r\n// Oql: NOT(ObjectName=\"Advisor Metrics\" OR ObjectName=ManagedSpace) | measure max(TimeGenerated) by Computer | top 500000 | Sort Computer // Args: {OQ: True; WorkspaceId: 00000000-0000-0000-0000-000000000000} // Settings: {PTT: True; SortI: True; SortF: True} // Version: 0.1.122"}, "ETag": null, "ID": "subscriptions/a052d33b-b7c4-4dc7-9e17-5c89ea594669/resourceGroups/sentinel-check/providers/Microsoft.OperationalInsights/workspaces/XXXXXX/savedSearches/LogManagement(XXXXXX)_General|AlphabeticallySortedComputers", "Name": "LogManagement(XXXXXX)_General|AlphabeticallySortedComputers"}, {"Properties": {"Category": "General Exploration", "Tactics": [], "Tags": null, "Version": 2, "Display_Name": "Stale Computers (data older than 24 hours)", "Query": "search not(ObjectName == \"Advisor Metrics\" or ObjectName == \"ManagedSpace\") | summarize lastdata = max(TimeGenerated) by Computer | limit 500000 | where lastdata < ago(24h)\r\n// Oql: NOT(ObjectName=\"Advisor Metrics\" OR ObjectName=ManagedSpace) | measure max(TimeGenerated) as lastdata by Computer | top 500000 | where lastdata < NOW-24HOURS // Args: {OQ: True; WorkspaceId: 00000000-0000-0000-0000-000000000000} // Settings: {PTT: True; SortI: True; SortF: True} // Version: 0.1.122"}, "ETag": null, "ID": "subscriptions/a052d33b-b7c4-4dc7-9e17-5c89ea594669/resourceGroups/sentinel-check/providers/Microsoft.OperationalInsights/workspaces/XXXXXX/savedSearches/LogManagement(XXXXXX)_General|StaleComputers", "Name": "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"}]
```



#### Delete Custom Hunting Rule
Delete Azure Sentinel Custom Hunting Rule
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
||Hunting Rule ID||String||



#### Update Incident Labels v2
Update Incident Labels v2. Action is a Chronicle SOAR async action and can be configured for a retry for a longer period of time.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
||Specify Azure Sentinel incident number to update with new labels.||String||
||Specify new labels that should be appended to the Incident. Parameter accepts multiple values as a comma-separated string.||String||
||Specify the number of retry attempts the action should make if the incident update was unsuccessful.||String||



##### JSON Results
```json
{"id": "/subscriptions/a052d33b-b7c4-4dc7-9e17-xxxxx/resourceGroups/sentinel-check/providers/Microsoft.OperationalInsights/workspaces/sentinelwork01/providers/Microsoft.SecurityInsights/Incidents/2e0ce5a0-7563-43a1-86a4-xxxxx", "name": "2e0ce5a0-7563-43a1-86a4-xxxxx", "etag": "\"fb006b40-0000-0c00-0000-xxxxx\"", "type": "Microsoft.SecurityInsights/Incidents", "properties": {"title": "Test Name", "description": "", "severity": "Informational", "status": "Closed", "classification": "Undetermined", "classificationComment": "Hello Test", "owner": {"objectId": null, "email": null, "assignedTo": null, "userPrincipalName": null}, "labels": [], "firstActivityTimeUtc": "2021-04-09T05:47:55.4959374Z", "lastActivityTimeUtc": "2021-04-14T05:47:55.4959374Z", "lastModifiedTimeUtc": "2021-04-14T06:53:30.2380985Z", "createdTimeUtc": "2021-04-14T05:53:00.8171911Z", "incidentNumber": "106xxx", "additionalData": {"alertsCount": 1, "bookmarksCount": 0, "commentsCount": 0, "alertProductNames": ["Azure Sentinel"], "tactics": ["InitialAccess", "Execution"]}, "relatedAnalyticRuleIds": ["/subscriptions/a052d33b-b7c4-4dc7-9e17-xxxxx/resourceGroups/sentinel-check/providers/Microsoft.OperationalInsights/workspaces/sentinelwork01/providers/Microsoft.SecurityInsights/alertRules/545ee671-a997-4a5a-8763-xxxxx"], "incidentUrl": "https://portal.azure.com/#asset/Microsoft_Azure_Security_Insights/Incident/subscriptions/a052d33b-b7c4-4dc7-9e17-xxxxx/resourceGroups/sentinel-check/providers/Microsoft.OperationalInsights/workspaces/sentinelwork01/providers/Microsoft.SecurityInsights/Incidents/2e0ce5a0-7563-43a1-86a4-xxxxx", "providerName": "Azure Sentinel", "providerIncidentId": "106xxx"}}
```



#### Run Custom Hunting Rule Query
Run Custom Hunting Rule Query
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
||Hunting Rule ID||String||
||Timeout value for the Azure Sentinel hunting rule API call||String||



##### JSON Results
```json
[{"Avg7Day": 327, "EventID": 455625, "Account": "host.local\\some.user", "StartTimeUtc": "2020-01-08T13:57:26.75Z", "LogonTypeName": "3 - Network", "timestamp": "2020-01-08T13:57:26.75Z", "CountLast7day": 2292, "EndTimeUtc": "2020-01-08T17:38:05.337Z", "CountToday": 1554, "SubStatus": "0xc0000071", "Computer": "XXXXXXXXXXX.XXX", "AccountType": "User", "HostCustomEntity": "XXXXXXXXXXX.XXX", "WorkstationName": "XXXXXX", "IpAddress": "127.0.0.1", "AccountCustomEntity": "host.local\\some.user"}]
```



#### List Alert Rules
Get Azure Sentinel Scheduled Rules list
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
||Severities of the alert rules to look for. Comma-separated string||String||
||What alert rule types action should return. Comma-separated string||String||
||What alert rule tactics action should return. Comma-separated string||String||
||If action should return only enabled alert rules||Boolean|false|
||How many scheduled alert rules the action should return, for example, 50.||String||



##### JSON Results
```json
[{"ID": "/subscriptions/a052d33b-b7c4-4dc7-9e17-xxxx/resourceGroups/sentinel-check/providers/Microsoft.OperationalInsights/workspaces/sentinelwork01/providers/Microsoft.SecurityInsights/alertRules/d7e959da-20fb-4257-8744-xxxx", "ETag": "\"ef00b54e-0000-0c00-0000-5fa8eddd0000\"", "Name": "d7e959da-20fb-4257-8744-xxxx", "Kind": "Scheduled", "Type": "Microsoft.SecurityInsights/alertRules", "Properties": {"Alert_Rule_Template_Name": null, "Description": "", "Display_Name": "Multiple failed login attempts from the same IP", "Enabled": false, "Last_Modified_UTC": "2020-11-09T07:21:01.7747459Z", "Query": "SecurityEvent\r\n| where Activity startswith \"4625\"\r\n| summarize count() by IpAddress, Computer\r\n| where count_ >3\r\n| extend HostCustomEntity = Computer\r\n| extend IPCustomEntity = IpAddress", "Query_Frequency": "0 days 1 hour 0 minutes 0 seconds", "Query_Period": "5 days 0 hours 0 minutes 0 seconds", "Severity": "High", "Suppression_Duration": "0 days 5 hours 0 minutes 0 seconds", "Suppression_Enabled": false, "Tactics": ["InitialAccess", "Execution", "Persistence", "PrivilegeEscalation", "DefenseEvasion", "CredentialAccess", "Discovery", "LateralMovement", "Collection", "Exfiltration", "CommandAndControl", "Impact"], "Trigger": null}}]
```



#### Get Alert Rule Details
Get Details of the Azure Sentinel Scheduled Alert Rule
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
||Alert Rule ID||String||



##### JSON Results
```json
{"Kind": "MLBehaviorAnalytics", "Name": "872ddb07-0415-4e57-b519-xxxx", "ID": "/subscriptions/a052d33b-b7c4-4dc7-9e17-xxxx/resourceGroups/Sentinel-Check/providers/Microsoft.OperationalInsights/workspaces/sentinelWork01/providers/Microsoft.SecurityInsights/alertRules/872ddb07-0415-4e57-b519-xxxx", "ETag": "\"62003e11-0000-0d00-0000-xxxx\"", "Type": "Microsoft.SecurityInsights/alertRules", "Properties": {"Tactics": ["InitialAccess"], "Severity": "Medium", "Suppression_Enabled": null, "Query_Period": null, "Enabled": true, "Query_Frequency": null, "Alert_Rule_Template_Name": "fa118b98-de46-4e94-87f9-xxxx", "Display_Name": "(Preview) Anomalous SSH Login Detection", "Description": "This detection uses machine learning (ML) to identify anomalous Secure Shell (SSH) login activity, based on syslog data. Scenarios include:\n\n* Impossible travel \u2013 when two successful login events occur from two locations that are impossible to reach within the timeframe of the two login events.\n* Unexpected location \u2013 the location from where a successful login event occurred is suspicious. For example, the location has not been seen recently.\n\nAllow two weeks after this alert is enabled for Azure Sentinel to build a profile of normal activity for your environment.\n\nThis detection requires a specific configuration of the data source. [Learn more](https://aka.ms/SentinelAnomalousSSHLoginDetection)", "Last_Modified_UTC": "2020-01-04T04:23:03.5607962Z", "Suppression_Duration": null, "Trigger": null, "Query": null}}
```



#### Ping
Test connectivity to Microsoft Azure Sentinel
Timeout - 600 Seconds



#### Run KQL Query
Run Azure Sentinel KQL Query based on the provided action input parameters.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
||A KQL Query to execute in Azure Sentinel. For example, to get security alerts available in Sentinel, query will be "SecurityAlert". Use other action input parameters (time span, limit) to filter the query results. For the examples of KQL queries consider Sentinel "Logs" Web page||String||
||Time span to look for, use the following format: PT + number + (M, H), where M - minutes, H - hours. Use P + number + D to specify a number of days. Can be combined as P1DT1H1M - 1 day, 1 hour and 1 minute.||String||
||Timeout value for the Azure Sentinel hunting rule API call. Note that Siemplify action python process timeout should be adjusted accordingly for this parameter, to not timeout action sooner than specified value because of the python process timeout.||String||
||How many records should be fetched. Optional parameter, if set, adds a "| limit x" to the kql query where x is the value set for the record limit. Can be removed if "limit" is already set in kql query or not needed.||String||



##### JSON Results
```json
[{"Avg7Day": 327, "EventID": 4625, "Account": "host.local\\some.user", "StartTimeUtc": "2020-01-08T13:57:26.75Z", "LogonTypeName": "3 - Network", "timestamp": "2020-01-08T13:57:26.75Z", "CountLast7day": 2292, "EndTimeUtc": "2020-01-08T17:38:05.337Z", "CountToday": 1554, "SubStatus": "0xc0000071", "Computer": "us-dc-v01001.host.local", "AccountType": "User", "HostCustomEntity": "us-dc-v01001.host.local", "WorkstationName": "US-DC-V01001", "IpAddress": "127.0.0.1", "AccountCustomEntity": "host.local\\some.user"}]
```



#### Update Incident Labels
Update Incident Labels. Please consider moving to the v2 version of the action, as it is implemented as a SOAR async action and provides more consistent results.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
||Specify Azure Sentinel incident number to update with new labels.||String||
||Specify new labels that should be appended to the Incident. Parameter accepts multiple values as a comma-separated string.||String||
||Specify the number of retry attempts the action should make if the incident update was unsuccessful.||String||
||Specify what time period in seconds action should wait between incident update retries.||String||



##### JSON Results
```json
{"id": "/subscriptions/a052d33b-b7c4-4dc7-9e17-xxxxx/resourceGroups/sentinel-check/providers/Microsoft.OperationalInsights/workspaces/sentinelwork01/providers/Microsoft.SecurityInsights/Incidents/2e0ce5a0-7563-43a1-86a4-xxxxx", "name": "2e0ce5a0-7563-43a1-86a4-xxxxx", "etag": "\"fb006b40-0000-0c00-0000-xxxxx\"", "type": "Microsoft.SecurityInsights/Incidents", "properties": {"title": "Test Name", "description": "", "severity": "Informational", "status": "Closed", "classification": "Undetermined", "classificationComment": "Hello Test", "owner": {"objectId": null, "email": null, "assignedTo": null, "userPrincipalName": null}, "labels": [], "firstActivityTimeUtc": "2021-04-09T05:47:55.4959374Z", "lastActivityTimeUtc": "2021-04-14T05:47:55.4959374Z", "lastModifiedTimeUtc": "2021-04-14T06:53:30.2380985Z", "createdTimeUtc": "2021-04-14T05:53:00.8171911Z", "incidentNumber": "106xxx", "additionalData": {"alertsCount": 1, "bookmarksCount": 0, "commentsCount": 0, "alertProductNames": ["Azure Sentinel"], "tactics": ["InitialAccess", "Execution"]}, "relatedAnalyticRuleIds": ["/subscriptions/a052d33b-b7c4-4dc7-9e17-xxxxx/resourceGroups/sentinel-check/providers/Microsoft.OperationalInsights/workspaces/sentinelwork01/providers/Microsoft.SecurityInsights/alertRules/545ee671-a997-4a5a-8763-xxxxx"], "incidentUrl": "https://portal.azure.com/#asset/Microsoft_Azure_Security_Insights/Incident/subscriptions/a052d33b-b7c4-4dc7-9e17-xxxxx/resourceGroups/sentinel-check/providers/Microsoft.OperationalInsights/workspaces/sentinelwork01/providers/Microsoft.SecurityInsights/Incidents/2e0ce5a0-7563-43a1-86a4-xxxxx", "providerName": "Azure Sentinel", "providerIncidentId": "106xxx"}}
```



#### Update Custom Hunting Rule
Update Azure Sentinel Custom Hunting Rule
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
||Hunting Rule ID||String|None|
||Display name of the new custom hunting rule||String|None|
||Query of the new custom hunting rule||String|None|
||Description of the new custom hunting rule||String|None|
||Tactics of the new custom hunting rule. Comma-separated values.||String|None|



##### JSON Results
```json
{"Properties": {"Category": "Log Management O", "Tactics": ["NewCustomTactic", "NewNotCustomTactic"], "Tags": [{"Name": "description", "Value": "New Description"}, {"Name": "tactics", "Value": "NewCustomTactic"}, {"Name": "tactics", "Value": "NewNotCustomTactic"}], "Version": 2, "Display_Name": "New Display Name", "Query": "let timeframe = 7d;AWSCloudTrail| where TimeGenerated >= ago(timeframe)| where  EventName in~ (\"AttachGroupPolicy\", \"AttachRolePolicy\", \"AttachUserPolicy\", \"CreatePolicy\",\"DeleteGroupPolicy\", \"DeletePolicy\", \"DeleteRolePolicy\", \"DeleteUserPolicy\", \"DetachGroupPolicy\",\"PutUserPolicy\", \"PutGroupPolicy\", \"CreatePolicyVersion\", \"DeletePolicyVersion\", \"DetachRolePolicy\", \"CreatePolicy\")| project TimeGenerated, EventName, EventTypeName, UserIdentityAccountId, UserIdentityPrincipalid, UserAgent, UserIdentityUserName, SessionMfaAuthenticated, SourceIpAddress, AWSRegion, EventSource, AdditionalEventData, ResponseElements| extend timestamp = TimeGenerated, IPCustomEntity = SourceIpAddress, AccountCustomEntity = UserIdentityAccountId"}, "ETag": "W/\"datetime'2020-01-23T21%3A14%3A33.2335395Z'\"", "ID": "subscriptions/a052d33b-b7c4-4dc7-9e17-5c89ea594669/resourceGroups/sentinel-check/providers/Microsoft.OperationalInsights/workspaces/sentinelwork01/savedSearches/a5a24268-XXXX-XXXX-XXXX-4ab6c9b7ad5b", "Name": "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"}
```






## Jobs

#### Sync Incidents
Deprecated. This job synchronizes Google SecOps Alerts and Microsoft Sentinel Incidents. It ensures that comments, status, and tags are kept in sync between the two systems. For the job to identify the correct information, the Google SecOps case must have the “Microsoft Sentinel Incident” tag. If the alert didn’t originate from “Microsoft Azure Sentinel Incident Connector v2”,  you will need to add an “Incident_ID” context value to the case for the job to be able to find the correct information.

|Name|IsMandatory|Type|DefaultValue|
|----|-----------|----|------------|
|||String|Default Environment|
|||String||
|||String|https://login.microsoftonline.com|
|||String|https://graph.microsoft.com|
|||String||
|||Password|*****|
|||Integer|24|
|||Boolean|true|

#### Sync Incidents V2
Use the Sync Incidents V2 job to synchronize Google SecOps alerts with Microsoft Sentinel incidents. This job ensures that comments, statuses, and tags are synchronized bi-directionally between both systems. Note: Assignee and severity synchronization occurs exclusively from Microsoft Sentinel to Google SecOps. For the job to identify the correct information, the Google SecOps case must have the Microsoft Sentinel Incident tag. This job only works on alerts from the Microsoft Azure Sentinel Incident Connector v2.

|Name|IsMandatory|Type|DefaultValue|
|----|-----------|----|------------|
|||String|Default Environment|
|||String||
|||String||
|||String|https://login.microsoftonline.com|
|||String|https://management.azure.com|
|||String||
|||String||
|||String||
|||Password|*****|
|||Integer|24|
|||Boolean|false|
|||Boolean|true|



## Connectors
#### Microsoft Sentinel Incident Tracking Connector
Connector works with Microsoft Azure Sentinel incidents and fetches updates to the Sentinel incidents as the new SecOps alerts. Connector's Dynamic List can be used to specify the incidents names that needs to be fetched. It is recommended to configure SecOps Alerts grouping based on SourceGroupIdentifier for this connector. See connector documentation for more information.

|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
||Describes the name of the field where the product name is stored.||String|product_type|
||Describes the name of the field where the event name is stored.||String|event_type|
||Timeout limit for the python process running the current script.||Integer|480|
||Describes the name of the field where the environment name is stored. If environment field isn't found, environment is "".||String||
||A regex pattern to run on the value found in the "Environment Field Name" field. Default is .* to catch all and return value unchanged. Used to allow the user to manipulate the environment field via regex logic. If regex pattern is null or empty, or the environment value is null, the final environment result is "".||String|.*|
||Microsoft Azure Subscription ID, can be viewed in Azure Portal > Subscriptions > <Your Subscription> > Subscription ID. ||String||
||Azure Entra ID Tenant ID, can be viewed in Active Directory > App Registration > <Application you configured for your integration> > Directory (tenant) ID.||String||
||Management.azure.com Api root url to use with integration.||String|https://management.azure.com|
||Specify the url, that connector should use for OAUTH2 Login.||String|https://login.microsoftonline.com|
||Name of Azure Resource Group where Azure Sentinel is located.||String||
||Name of the Azure Sentinel workspace to work with, can be viewed in Azure portal > Azure Sentinel > Azure Sentinel Workspaces.||String||
||Client (Application) ID that was added for the app registration in Azure Active Directory for this integration.||String||
||Secret that was entered for Azure AD app registration.||Password|*****|
||Verify SSL certificates for HTTPS requests to Microsoft Azure.||Boolean|true|
||Number of hours before the first connector iteration to retrieve incidents from. This parameter applies to the initial connector iteration after you enable the connector for the first time, or used as a fallback value in cases where connector's last run timestamp expires.||Integer|24|
||Specify the statuses of the incidents that should be fetched by the SecOps server. Parameter can take multiple values as a comma separated string.||String|New,  Active, Closed|
||Specify the severities of the incidents that should be fetched by the SecOps server. Parameter can take multiple values as a comma separated string.||String|Informational, Low, Medium, High|
||How many incidents should be processed during one connector run.||Integer|10|
||If enabled, the connector will wait until a Scheduled/NRT alert object will be available.||Boolean|false|
||By default connector uses a different approach with Scheduled Alert or NRT types of alerts - it tries to fetch events that caused the alert by running the query specified in alert details. Specify whether to change this behavior and use the same approach for the scheduled and NRT alerts as for other alert types.||Boolean|false|
||Specify a comma separated list of tags Sentinel incident should have to be ingested. Incidents that will not have tags from this list will be ignored. Example of how Sentinel tags can be provided: tag1, tag2||String||
||If enabled, dynamic list will be used as a blocklist.||Boolean|false|
||Time frame in minutes for connector to keep incidents in backlog for.||Integer|60|
||Specify a comma separated list of incident or alert attributes that should be used as a fallback for the "Start Time" alert field in descending order. Additionally, new "SecOps_Start_Time" attribute will be added to created events. First attribute will have the highest priority, next if its not present or empty in the event - fallback to the next value from the list and so on. If none of the fallback fields are found, connector will use createdTimeUTC, and if that's also non existent - alert ingestion time to SecOps.||String|properties_firstActivityTimeGenerated,properties_startTimeUtc,properties_createdTimeUtc,properties_firstAlertTimeGenerated|
||Specify a comma separated list of incident or alert attributes that should be used as a fallback for the "End Time" alert field in descending order. Additionally, new "SecOps_End_Time" attribute will be added to created events. First attribute will have the highest priority, next if its not present or empty in the event - fallback to the next value from the list and so on. If none of the fallback fields are found, connector will use createdTimeUTC, and if that's also non existent - alert ingestion time to SecOps.||String|properties_lastActivityTimeGenerated,properties_endTimeUtc,properties_createdTimeUtc,properties_lastAlertTimeGenerated|
||Specify if connector should add to the created events a "debug" fields that will contain the values it used for fallback.||Boolean|false|
||Specify a comma separated list of incident attributes that should be used as a fallback for the "DeviceVendor" field in descending order. First attribute will have the highest priority, next if its not present or empty in the event - fallback to the next value from the list and so on.||String|vendorName|
||Specify a comma separated list of incident or alert attributes that should be used as a fallback for the "Product Field Name" parameter and "DeviceProduct" field in descending order. First attribute will have the highest priority, next if its not present or empty in the event - fallback to the next value from the list and so on.||String|ProductName|
||Specify a comma separated list of alert attributes that should be used as a fallback for the "Event Field Name" parameter in descending order. First attribute will have the highest priority, next if its not present or empty in the event - fallback to the next value from the list and so on.||String|kind|
||How many incidents  connector should try to fetch from the backlog during one connector run.||Integer|10|
||If enabled, the connector will disable the overflow mechanism.||Boolean|false|
||Specify the total number of events the connector should ingest for a Microsoft Sentinel incident that is based on a Scheduled or NRT alert. Connector ‘counts’ events in all corresponding SecOps alerts created for the Microsoft Sentinel Incident and no new events will be ingested once this limit is reached.||Integer|100|
||If enabled, connector will create SecOps alerts from Microsoft Sentinel incidents that dont have entities. Otherwise, such incidents will be skipped for all Sentinel incidents types except Sentinel Scheduled and NRT alerts.||Boolean|false|
||If specified, to get incidents returned not in chronological order, connector will fetch Sentinel incidents from this value backwards in time.||Integer|60|
||If specified, connector will use this value from the Microsoft Azure Sentinel API response for incident data for Chronicle SOAR Alert Name. You can provide placeholders in the following format: [name of the field]. Example: Sentinel incident - [title]. Note: the maximum length for the field is 256 characters. If nothing is provided or user provides an invalid template, connector will use the default alert name.||String||
||If specified, connector will use this value from the Microsoft Azure Sentinel API response for incident data for Chronicle SOAR Rule Generator. You can provide placeholders in the following format: [name of the field]. Example: Sentinel incident - [severity]. Note: the maximum length for the field is 256 characters. If nothing is provided or user provides an invalid template, connector will use the default rule generator value.||String||
||Specify how long connector should track already ingested Sentinel incident for updates - either addition of new events or entities and incident details.||Integer|24|
||Proxy server to use for connection.||String||
||Proxy server username.||String||
||Proxy server password.||Password|*****|
||If enabled, when creating entities from the Sentinel API, connector will create extra SecOps events for all Sentinel incident's entities, not only Account, Mailbox, Host or Ip.||Boolean|false|


#### Microsoft Azure Sentinel Incident Connector v2
Connector works with Microsoft Azure Sentinel incidents. Connector's Dynamic List can be used to specify the incidents names that needs to be fetched. See connector documentation for more information.

|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
||If enabled, the connector will disable the overflow mechanism.||Boolean|false|
||Specify if connector should add to the created events a “debug“ fields that will contain the values it used for fallback.||Boolean|false|
||Describes the name of the field where the product name is stored.||String|product_type|
||Describes the name of the field where the event name is stored.||String|event_type|
||The timeout limit (in seconds) for the python process running current script||Integer|480|
||Describes the name of the field where the environment name is stored. If environment field isn't found, environment is "".||String||
||Specify the maximum number of events the connector should ingest per a single Azure Sentinel Scheduled or NRT Alert.||Integer|100|
||A regex pattern to run on the value found in the "Environment Field Name" field. Default is .* to catch all and return value unchanged. Used to allow the user to manipulate the environment field via regex logic. If regex pattern is null or empty, or the environment value is null, the final environment result is "".||String|.*|
||Microsoft Azure Subscription ID, can be viewed in Azure Portal > Subscriptions > <Your Subscription> > Subscription ID. ||String||
||Azure Active Directory Tenant ID, can be viewed in Active Directory > App Registration > <Application you configured for your integration> > Directory (tenant) ID.||String||
||The API Root of Microsoft Azure Sentinel REST API root.||String|https://management.azure.com|
||Specify the url, that connector should use for OAUTH2 Login.||String|https://login.microsoftonline.com|
||Name of Azure Resource Group where Azure Sentinel is located.||String||
||Name of the Azure Sentinel workspace to work with, can be viewed in Azure portal > Azure Sentinel > Azure Sentinel Workspaces.||String||
||Client (Application) ID that was added for the app registration in Azure Active Directory for this integration.||String||
||Secret that was entered for Azure AD app registration||Password|*****|
||Verify SSL certificates for HTTPS requests to Microsoft Azure.||Boolean|false|
||How many incidents should be processed during one connector run||Integer|10|
||How many incidents  connector should try to fetch from the backlog during one connector run.||Integer|10|
||Number of hours before the first connector iteration to retrieve incidents alerts. This parameter applies to the initial connector iteration after you enable the connector for the first time, or used as a fallback value in cases where connector's last run timestamp expires. Default value: 24 hours.||Integer|24|
||Specify the statuses of the incidents that should be fetched by the Chronicle SOAR server. Parameter can take multiple values as a comma separated string.||String|New, Closed|
||Specify the severities of the incidents that should be fetched by the Chronicle SOAR server. Parameter can take multiple values as a comma separated string.||String|Informational, Low, Medium, High|
||By default connector uses a different approach with Scheduled Alert or NRT types of alerts - it tries to fetch events that caused the alert by running the query specified in alert details. Specify whether to change this behavior and use the same approach for the scheduled and NRT alerts as for other alert types.||Boolean|false|
||If enabled, dynamic list will be used as a blocklist.||Boolean|false|
||Time frame in minutes for connector to keep incidents in backlog for.||Integer|60|
||Specify a comma separated list of alert attributes that should be used as a fallback for the "Event Field Name" parameter in descending order. First attribute will have the highest priority, next if its not present or empty in the event - fallback to the next value from the list and so on.||String|kind|
||Specify a comma separated list of incident or alert attributes that should be used as a fallback for the "Product Field Name" parameter and "DeviceProduct" field in descending order. First attribute will have the highest priority, next if its not present or empty in the event - fallback to the next value from the list and so on.||String|ProductName,properties_providerName|
||Specify a comma separated list of incident attributes that should be used as a fallback for the "DeviceVendor" field in descending order. First attribute will have the highest priority, next if its not present or empty in the event - fallback to the next value from the list and so on.||String|vendorName|
||Specify a comma separated list of incident or alert attributes that should be used as a fallback for the “Start Time” alert field in descending order. Additionally, new “Siemplify_Start_Time“ attribute will be added to created events. First attribute will have the highest priority, next if its not present or empty in the event - fallback to the next value from the list and so on. If none of the fallback fields are found, connector will use createdTimeUTC, and if that's also non existent - alert ingestion time to Chronicle SOAR.||String|properties_firstActivityTimeGenerated,properties_startTimeUtc,properties_createdTimeUtc,properties_firstAlertTimeGenerated|
||Specify a comma separated list of incident or alert attributes that should be used as a fallback for the “End Time” alert field in descending order. Additionally, new “Siemplify_End_Time“ attribute will be added to created events. First attribute will have the highest priority, next if its not present or empty in the event - fallback to the next value from the list and so on. If none of the fallback fields are found, connector will use createdTimeUTC, and if that's also non existent - alert ingestion time to Chronicle SOAR.||String|properties_lastActivityTimeGenerated,properties_endTimeUtc,properties_createdTimeUtc,properties_lastAlertTimeGenerated|
||Specify a comma separated list of tags Sentinel incident should have to be ingested. Incidents that will not have tags from this list will be ignored. Example of how Sentinel tags can be provided: tag1, tag2||String||
||If enabled, connector will create Chronicle SOAR alerts from Microsoft Sentinel incidents that dont have entities. Otherwise, such incidents will be skipped for all Sentinel incidents types except Sentinel Scheduled and NRT alerts.||Boolean|false|
||Specify the maximum number of  alerts the connector should ingest per a single Azure Sentinel incident.||Integer|10|
||Proxy server to use for connection.||String||
||Proxy server username||String||
||Proxy server password||Password|*****|
||If specified, to get incidents returned not in chronological order, connector will fetch Sentinel incidents from this value backwards in time.||Integer|60|
||If specified, connector will use this value from the Microsoft Azure Sentinel API response for incident data for Chronicle SOAR Alert Name. You can provide placeholders in the following format: [name of the field]. Example: Sentinel incident - [title]. Note: the maximum length for the field is 256 characters. If nothing is provided or user provides an invalid template, connector will use the default alert name.||String||
||If specified, connector will use this value from the Microsoft Azure Sentinel API response for incident data for Chronicle SOAR Rule Generator. You can provide placeholders in the following format: [name of the field]. Example: Sentinel incident - [severity]. Note: the maximum length for the field is 256 characters. If nothing is provided or user provides an invalid template, connector will use the default rule generator value.||String||
||If enabled, when creating entities from the Sentinel API, connector will create extra SecOps events for all Sentinel incident's entities, not only Account, Mailbox, Host or Ip.||Boolean|false|
||If specified, the value will be applied as the maximum waiting time in seconds for any request made to Azure API. Defaults to 60.||Integer|60|
||If enabled, the connector will wait until a Scheduled/NRT alert object will be available.||Boolean|false|


#### Microsoft Azure Sentinel Incident Connector
DEPRECATED! Fetches Incidents from Azure Sentinel.

|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
||The field name used to determine the device product||String|ProductName|
||The field name used to determine the event name (sub-type)||String|AlertName|
||The timeout limit (in seconds) for the python process running current script||String|180|
||Describes the name of the field where the environment name is stored.||String||
||If defined - the connector will implement the specific RegEx pattern on the data from "environment field" to extract specific string. For example - extract domain from sender's address: "(?<=@)(\S+$)"||Integer||
||The API Root of Microsoft Azure Sentinel REST API root.||String|https://management.azure.com|
||Specify the url, that connector should use for OAUTH2 Login.||String|https://login.microsoftonline.com|
||Client (Application) ID that was added for the app registration in Azure Active Directory for this integration.||String||
||Secret that was entered for Azure AD app registration||Password|*****|
||Azure Active Directory Tenant ID, can be viewed in Active Directory > App Registration > <Application you configured for your integration> > Directory (tenant) ID.||String||
||Name of the Azure Sentinel workspace to work with, can be viewed in Azure portal > Azure Sentinel > Azure Sentinel Workspaces.||String||
||Microsoft Azure Subscription ID, can be viewed in Azure Portal > Subscriptions > <Your Subscription> > Subscription ID. ||String||
||Name of Azure Resource Group where Azure Sentinel is located.||String||
||Verify SSL certificates for HTTPS requests to Microsoft Azure.||Boolean|false|
||How many incidents should be processed during one connector run||Integer|10|
||Number of hours before the first connector iteration to retrieve alerts from. This parameter applies to the initial connector iteration after you enable the connector for the first time, or used as a fallback value in cases where connector's last run timestamp expires. Default value: 24 hours.||Integer|24|
||Specify the statuses of the incidents that should be fetched by the Siemplify server. Comma-separated string.||String|Draft, New, InProgress, Closed|
||Specify the severities of the incidents that should be fetched by the Siemplify server. Comma-separated string.||String|Informational, Low, Medium, High, Critical|
||Proxy server to use for connection.||IP||
||Proxy server username||String||
||Proxy server password||Password|*****|




