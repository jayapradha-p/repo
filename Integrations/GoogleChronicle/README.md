
# GoogleChronicle

Google SecOps enables you to examine the aggregated security information for your enterprise going back for months or longer. Use Google SecOps to search across all of the domains accessed from within your enterprise. To enable the Google API client to communicate with the Backstory API you will need Google Developer Service Account Credential, https://developers.google.com/identity/protocols/OAuth2#serviceaccount.

Python Version - V3_11
#### Parameters
|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|UI Root|UI root of the Chronicle instance. It will be used to create a link that points back to Chronicle across multiple actions.|True|String|https://{instance}.chronicle.security|
|API Root|API root of the Chronicle instance.|True|String|https://backstory.googleapis.com|
|User's Service Account|Service Account that is used for authentication. You can configure either this parameter or the Workload Identity Email parameter. If both this and Workload Identity Email not provided, the default Service Account of the SecOps Instance will be used to authenticate.|False|Password|*****|
|Workload Identity Email|The client email address of your workload identity. You can configure either this parameter or the User's Service Account parameter. To impersonate service accounts with the workload identity email address, grant the Service Account Token Creator role to your service account. If both this and User's Service Account not provided, the default Service Account of the SecOps Instance will be used to authenticate.|False|Password|*****|
|Verify SSL|If enabled, verify the SSL certificate for the connection to the Google Chronicle server is valid.|False|Boolean|true|


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
#### List IOCs
List all of the IoCs discovered within your enterprise within the specified time range.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Start Time|Fetches IOC Domain from the specified time. Value should be in RFC 3339 format (e.g. 2018-11-05T12:00:00Z). If not supplied, the default is the UTC time corresponding to 3 days earlier than current time.|False|String||
|Max IoCs to Fetch|Specify the maximum number of IoCs to return. You can specify between 1 and 10,000. The default is 50.|False|String|50|



##### JSON Results
```json
[{"artifactIndicator": {"domain": "npatni-sysops"}, "sources": ["ACME-IOC-IP-DOMAIN"], "categories": ["C2"], "assetIndicators": [{"assetIpAddress": "172.30.202.229"}], "iocIngestTimestamp": "2024-12-10T13:52:38.780150Z", "firstSeenTimestamp": "2025-01-13T14:01:00Z", "lastSeenTimestamp": "2025-01-13T14:01:00Z", "filterProperties": {"stringProperties": {"TLD": {"values": [{"rawValue": "Invalid"}]}, "IOC CATEGORIES": {"values": [{"rawValue": "C2"}]}, "IOC FEED": {"values": [{"rawValue": "ACME-IOC-IP-DOMAIN"}]}}}, "logType": "UDM", "feedName": "ACME-IOC-IP-DOMAIN", "id": "Cg1ucGF0bmktc3lzb3BzEMgB", "fieldAndValue": {"value": "npatni-sysops", "valueType": "DOMAIN_NAME"}, "artifact": {"domainName": "npatni-sysops"}, "iocIngestTime": "2024-12-10T13:52:38.780150Z", "firstSeenTime": "2025-01-13T14:01:00Z", "lastSeenTime": "2025-01-13T14:01:00Z"}, {"artifactIndicator": {"destinationIpAddress": "35.246.203.0"}, "sources": ["ACME-IOC-IP-PORT-C2"], "categories": ["C2"], "assetIndicators": [{"assetIpAddress": "172.30.202.229"}], "iocIngestTimestamp": "2024-01-10T22:04:34.267566Z", "firstSeenTimestamp": "2025-01-13T14:00:00Z", "lastSeenTimestamp": "2025-01-13T14:00:00Z", "filterProperties": {"stringProperties": {"IOC CATEGORIES": {"values": [{"rawValue": "C2"}]}, "IOC FEED": {"values": [{"rawValue": "ACME-IOC-IP-PORT-C2"}]}}}, "logType": "CATCH_ALL", "feedName": "ACME-IOC-IP-PORT-C2", "id": "CgwzNS4yNDYuMjAzLjAQyQE", "fieldAndValue": {"value": "35.246.203.0", "valueType": "RESOLVED_IP_ADDRESS"}, "artifact": {"destinationIpAddress": "35.246.203.0"}, "iocIngestTime": "2024-01-10T22:04:34.267566Z", "firstSeenTime": "2025-01-13T14:00:00Z", "lastSeenTime": "2025-01-13T14:00:00Z"}, {"artifactIndicator": {"hashSha256": "bc866cfcdda37e24dc2634dc282c7a0e6f55209da17a8fa105b07414c0e7c527"}, "sources": ["ACME-IOC-FILE-HASH"], "categories": ["C2"], "assetIndicators": [{"namespace": "Yuriy", "assetIpAddress": "172.30.202.229"}, {"namespace": "Yuriy", "mac": "00:50:56:a2:b8:a0"}, {"namespace": "Yuriy", "hostname": "exlab2019-ad"}], "iocIngestTimestamp": "2025-01-10T13:52:38.780150Z", "firstSeenTimestamp": "2024-12-15T09:07:02Z", "lastSeenTimestamp": "2025-01-14T16:07:14Z", "filterProperties": {"stringProperties": {"IOC CATEGORIES": {"values": [{"rawValue": "C2"}]}, "IOC FEED": {"values": [{"rawValue": "ACME-IOC-FILE-HASH"}]}}}, "logType": "CATCH_ALL", "feedName": "ACME-IOC-FILE-HASH", "id": "CkBiYzg2NmNmY2RkYTM3ZTI0ZGMyNjM0ZGMyODJjN2EwZTZmNTUyMDlkYTE3YThmYTEwNWIwNzQxNGMwZTdjNTI3ELEC", "fieldAndValue": {"value": "bc866cfcdda37e24dc2634dc282c7a0e6f55209da17a8fa105b07414c0e7c527", "valueType": "HASH_SHA256"}, "artifact": {"hashSha256": "bc866cfcdda37e24dc2634dc282c7a0e6f55209da17a8fa105b07414c0e7c527"}, "iocIngestTime": "2025-01-10T13:52:38.780150Z", "firstSeenTime": "2024-12-15T09:07:02Z", "lastSeenTime": "2025-01-14T16:07:14Z"}]
```



#### Is Value In Reference List
Check, if provided values are found in reference lists in Google Chronicle.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Reference List Names|Specify a comma-separated list of display names of the reference list that needs to be searched.|True|String||
|Values|Specify a comma-separated list of values that need to be searched in reference lists.|True|String||
|Case Insensitive Search|If enabled, action will perform case insensitive matching.|False|Boolean|true|



##### JSON Results
```json
[{"Entity": "domain.com", "EntityResult": {"found_in": [], "not_found_in": "testList", "overall_status": "not found"}}]
```



#### Get Rule Details
Fetch information about a rule in Google Chronicle.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Rule ID|Specify the ID of the rule for which you want to fetch details.|True|String||



##### JSON Results
```json
{"name": "projects/xxxx/locations/us/instances/yyyy/rules/ru_7d66bc00-7164-4c56-bb6a-66f19524983c", "revisionId": "v_1733917896_973567000", "displayName": "Test_rule_SingleEvent", "text": "rule Test_rule_SingleEvent {\n  // This rule matches single events. Rules can also match multiple events within\n  // some time window. For details about how to write a multi-event rule, see\n  // https://cloud.google.com/chronicle/docs/detection/yara-l-2-0-overview#single-event_versus_multi-event\n\n  meta:\n    // Allows for storage of arbitrary key-value pairs of rule details - who\n    // wrote it, what it detects on, version control, etc.\n    // The \"author\" and \"severity\" fields are special, as they are used as\n    // columns on the rules dashboard. If you'd like to be able to sort based on\n    // these fields on the dashboard, make sure to add them here.\n    // Severity value, by convention, should be \"Low\", \"Medium\" or \"High\"\n    author = \"bhusingh\"\n    description = \"windowed single event example rule\"\n    //severity = \"Medium\"\n\n  events:\n    $e.metadata.event_type = \"USER_LOGIN\"\n    $e.principal.user.userid = $user\n\n  //outcome:\n    // For a multi-event rule an aggregation function is required\n    // e.g., risk_score = max(0)\n    // See https://cloud.google.com/chronicle/docs/detection/yara-l-2-0-overview#outcome_conditionals_example_rule\n    //$risk_score = 0\n  match:\n    $user over 1m\n\n  condition:\n    #e > 0\n}\n", "author": "bhusingh", "metadata": {"author": "bhusingh", "description": "windowed single event example rule", "severity": null}, "createTime": "2024-12-11T11:36:18.192127Z", "revisionCreateTime": "2024-12-11T11:51:36.973567Z", "compilationState": "SUCCEEDED", "type": "SINGLE_EVENT", "allowedRunFrequencies": ["LIVE", "HOURLY", "DAILY"], "etag": "CMj55boGEJjondAD", "ruleId": "ru_7d66bc00-7164-4c56-bb6a-66f19524983c", "versionId": "ru_7d66bc00-7164-4c56-bb6a-66f19524983c@v_1733917896_973567000", "ruleName": "Test_rule_SingleEvent", "ruleText": "rule Test_rule_SingleEvent {\n  // This rule matches single events. Rules can also match multiple events within\n  // some time window. For details about how to write a multi-event rule, see\n  // https://cloud.google.com/chronicle/docs/detection/yara-l-2-0-overview#single-event_versus_multi-event\n\n  meta:\n    // Allows for storage of arbitrary key-value pairs of rule details - who\n    // wrote it, what it detects on, version control, etc.\n    // The \"author\" and \"severity\" fields are special, as they are used as\n    // columns on the rules dashboard. If you'd like to be able to sort based on\n    // these fields on the dashboard, make sure to add them here.\n    // Severity value, by convention, should be \"Low\", \"Medium\" or \"High\"\n    author = \"bhusingh\"\n    description = \"windowed single event example rule\"\n    //severity = \"Medium\"\n\n  events:\n    $e.metadata.event_type = \"USER_LOGIN\"\n    $e.principal.user.userid = $user\n\n  //outcome:\n    // For a multi-event rule an aggregation function is required\n    // e.g., risk_score = max(0)\n    // See https://cloud.google.com/chronicle/docs/detection/yara-l-2-0-overview#outcome_conditionals_example_rule\n    //$risk_score = 0\n  match:\n    $user over 1m\n\n  condition:\n    #e > 0\n}\n", "ruleType": "SINGLE_EVENT", "versionCreateTime": "2024-12-11T11:51:36.973567Z"}
```



#### Add Entry To Watchlist
Use the Add Entry To Watchlist action to add a specified entity to an existing Risk Analytics Watchlist in Google SecOps. Note: This action requires Chronicle API authentication. Legacy Backstory API authentication is not supported.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Watchlist Name|The name of the Risk Analytics Watchlist to add the entry to.|True|String||
|Entry|The JSON object representing the entity to add to the Watchlist. The JSON structure requires the entity value, entity type, and an optional namespace.|True|String|[{"entity": "","type": "ASSET_IP_ADDRESS/MAC/HOSTNAME/PRODUCT_SPECIFIC_ID/USERNAME/EMAIL/EMPLOYEE_ID/WINDOWS_SID/PRODUCT_OBJECT_ID","namespace": "Optional"}]|



##### JSON Results
```json
[{"asset": {"hostname": "koko"}}, {"namespace": "Yuriy", "asset": {"hostname": "xyz"}}]
```



#### Get Reference Lists
Get available reference lists in Google Chronicle.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Filter Key|Specify the key that needs to be used to filter reference lists. Name option refers to a display name of the reference list.|False|List|Select One|
|Filter Logic|Specify what filter logic should be applied.|False|List|Equal|
|Filter Value|Specify what value should be used in the filter. If “Equal“ is selected, action will try to find the exact match among results and if “Contains“ is selected, action will try to find results that contain that substring. “Equal” works with “title” parameter, while “Contains” works with all values in response. If nothing is provided in this parameter, the filter will not be applied.|False|String||
|Expanded Details|If enabled, action will return detailed information about the reference lists.|False|Boolean|false|
|Max Reference Lists To Return|Specify how many reference lists to return. Default: 100.|False|String|100|



##### JSON Results
```json
[{"name": "projects/xxxx/locations/us/instances/yyyy/referenceLists/testList", "displayName": "testList", "revisionCreateTime": "2025-01-09T15:53:10.851775Z", "description": "Test reference list", "syntaxType": "REFERENCE_LIST_SYNTAX_TYPE_PLAIN_TEXT_STRING", "scopeInfo": {"referenceListScope": {}}, "createTime": "2025-01-09T15:53:10.851775Z"}]
```



#### Add Values To Reference List
Add values to a reference list in Google Chronicle.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Reference List Name|Specify the display name of the reference list that needs to be updated|True|String||
|Values|Specify a comma-separated list of values that need to be added to a reference list|True|String||



##### JSON Results
```json
{"name": "projects/xxxx/locations/us/instances/yyyy/referenceLists/testList", "displayName": "testList", "revisionCreateTime": "2025-01-16T09:15:21.795743Z", "description": "Test reference list", "entries": [{"value": "abc.co"}, {"value": "domain1.com"}], "syntaxType": "REFERENCE_LIST_SYNTAX_TYPE_PLAIN_TEXT_STRING", "scopeInfo": {"referenceListScope": {}}, "createTime": "2025-01-16T09:15:21.795743Z", "lines": ["abc.co", "domain1.com"]}
```



#### Execute UDM Query
Execute custom UDM query in Google Chronicle. Note: 120 action executions are allowed per hour. Aggregated queries are supported only via Chronicle API configuration of integration.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Query|Specify the query that needs to be executed in Chronicle.|True|String||
|Include Raw Log Data|If selected, the action retrieves the original raw log file associated with the UDM search results. Raw Log data is not available for aggregated searches. This option is only available when using Chronicle API authentication.|False|Boolean|false|
|Time Frame|Specify a time frame for the results. If "Alert Time Till Now" is selected, action will use start time of the alert as start time for the search and end time will be current time. If "30 Minutes Around Alert Time" is selected, action will search the alerts 30 minutes before the alert happened till the 30 minutes after the alert has happened.  Same idea applies to "1 Hour Around Alert Time" and "5 Minutes Around Alert Time". If "Custom" is selected, you also need to provide "Start Time".|False|List|Last Hour|
|Start Time|Specify the start time for the results. This parameter is mandatory, if "Custom" is selected for the "Time Frame" parameter. Format: ISO 8601. Note: The maximum time window (start time to end time) is 90 days.|False|String||
|End Time|Specify the end time for the results. Format: ISO 8601. If nothing is provided and "Custom" is selected for the "Time Frame" parameter then this parameter will use current time. Note: The maximum time window (start time to end time) is 90 days.|False|String||
|Max Results To Return|Specify how many results to return for the query. Default: 50. Maximum: 10000.|False|String|50|



##### JSON Results
```json
{"events":[{"name":"02c2c701c5bb7e7042701axxxxxxxxxx,4,16496990275xxxxx,EMAIL,","udm":{"metadata":{"eventTimestamp":"2022-04-11T17:43:47.586Z","eventType":"EMAIL_TRANSACTION","productName":"Chronicle Internal","ingestedTimestamp":"2022-04-11T15:50:21.912562Z","enrichmentState":"ENRICHED"},"principal":{"hostname":"test-pc","assetId":"CS:8973060bcf1d441a8cf10exxxxxxxxxx","user":{"userid":"test","userDisplayName":"test test","windowsSid":"S-1-5-21-2623356xxx-8883713xxx-9684409xxx-xxxxx","emailAddresses":["test@example.com"],"productObjectId":"test","attribute":{"labels":[{"key":"2FA Enabled","value":"false"}]},"groupIdentifiers":["Contractors"],"title":"IT Support Agent","department":["Cymbal Investments IT Contractors"]},"ip":["10.2.xx.xxx"],"mac":["b5:1c:8b:xx:xx:xx"],"location":{"city":"San Francisco","state":"California","countryOrRegion":"US"},"asset":{"hostname":"test-pc","assetId":"CS:8973060bcf1d441a8cf10exxxxxxxxxx","ip":["10.2.xx.xxx"],"mac":["b5:1c:8b:xx:xx:xx"]}},"securityResult":[{"action":["ALLOW"]}],"rawLogData": {"agent_id": "xxxxxx", "aggregate_id": "xxxxxx", "created_timestamp": "xxxxxx", "description": "xxxxxx", "display_name": "xxxxxx", "filename": "xxxxxx", "decodedString": "xxxxxx"},"network":{"email":{"from":"test@example.com","to":["test@example.com"],"subject":["I did not create this service account"]}}}},{"name":"02c2c701c5bb7e7042701axxxxxxxxxx,3,16496987245xxxxx,EMAIL,","udm":{"metadata":{"eventTimestamp":"2022-04-11T17:38:44.586Z","eventType":"EMAIL_TRANSACTION","productName":"Chronicle Internal","ingestedTimestamp":"2022-04-11T15:50:21.912562Z","enrichmentState":"ENRICHED"},"principal":{"hostname":"test-pc","assetId":"CS:8973060bcf1d441a8cf10exxxxxxxxxx","user":{"userid":"test","userDisplayName":"test test","windowsSid":"S-1-5-21-2623356xxx-8883713xxx-9684409xxx-xxxxx","emailAddresses":["test@example.com"],"productObjectId":"test","attribute":{"labels":[{"key":"2FA Enabled","value":"false"}]},"groupIdentifiers":["Contractors"],"title":"IT Support Agent","department":["Cymbal Investments IT Contractors"]},"ip":["10.2.xx.xxx"],"mac":["b5:1c:8b:xx:xx:xx"],"location":{"city":"San Francisco","state":"California","countryOrRegion":"US"},"asset":{"hostname":"test-pc","assetId":"CS:8973060bcf1d441a8cf10exxxxxxxxxx","ip":["10.2.xx.xxx"],"mac":["b5:1c:8b:xx:xx:xx"]}},"securityResult":[{"action":["ALLOW"]}],"rawLogData": {"agent_id": "xxxxxx", "aggregate_id": "xxxxxx", "created_timestamp": "xxxxxx", "description": "xxxxxx", "display_name": "xxxxxx", "filename": "xxxxxx", "decodedString": "xxxxxx"},"network":{"email":{"from":"test@example.com","to":["test@example.com"],"subject":["Did you create this service account"]}}}},{"target.file.vhash": {"values": [{"stringVal": "673961a71ba82e0556ef95cb2147e212"}]}, "event_type_array": {"values": [{"stringVal": "673961a71ba82e0556ef95cb2147e212"}]}, "avg_seconds": {"values": [{"doubleVal": 1755680893.3333333}]}}]}
```



#### Ask Gemini
Preview. Ask Gemini in Google SecOps. For this action to work, you have to check the Automatic Opt-in parameter. Note: this action only works with Chronicle API authentication. Backstory API is not supported
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Automatic Opt-in|If enabled, action will do an automatic opt-in for Gemini.|False|Boolean|true|
|Prompt|Specify the prompt that should be executed.|True|String||



##### JSON Results
```json
{"name": "projects/xxxxxx/locations/us/instances/xxxxxx/users/me/conversations/xxxxxx/messages/xxxxxx","input": {"body": "xxxxxx"},"responses": [{"blocks": [{"blockType": "HTML","htmlContent": {"privateDoNotAccessOrElseSafeHtmlWrappedValue": "<p>xxxxxx</p>\n<ul>\n<li>xxxxxx</li>\n<li>xxxxxx</li>\n<li>xxxxxx</li>\n<li>xxxxxx</li>\n<li>xxxxxx</li>\n<li>xxxxxx</li>\n</ul>\n<p>xxxxxx</p>\n"}}],"references": [{"blockType": "HTML","htmlContent": {"privateDoNotAccessOrElseSafeHtmlWrappedValue": "<ol>\n<li><a href=\"https://xxxxxx\" target=\"_blank\">xxxxxx</a></li>\n</ol>\n"}}],"groundings": ["xxxxxx","yyyyyy"]}],"createTime": "2025-05-16T11:31:36.660538Z"}
```



#### List Events
List events on the particular asset in the specified time frame. Supported entities: IP Address, Mac Address, Hostname. Note: action can only fetch 10000 events. Make sure to narrow down the timeframe for better results.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Event Types|Specify a comma-separated list of the event types that need to be returned. If nothing is provided, action will fetch all event types. Possible values: EVENTTYPE_UNSPECIFIED, PROCESS_UNCATEGORIZED, PROCESS_LAUNCH, PROCESS_INJECTION, PROCESS_PRIVILEGE_ESCALATION, PROCESS_TERMINATION, PROCESS_OPEN, PROCESS_MODULE_LOAD, REGISTRY_UNCATEGORIZED, REGISTRY_CREATION, REGISTRY_MODIFICATION, REGISTRY_DELETION, SETTING_UNCATEGORIZED, SETTING_CREATION, SETTING_MODIFICATION, SETTING_DELETION, MUTEX_UNCATEGORIZED, MUTEX_CREATION, FILE_UNCATEGORIZED, FILE_CREATION, FILE_DELETION, FILE_MODIFICATION, FILE_READ, FILE_COPY, FILE_OPEN, FILE_MOVE, FILE_SYNC, USER_UNCATEGORIZED, USER_LOGIN, USER_LOGOUT, USER_CREATION, USER_CHANGE_PASSWORD, USER_CHANGE_PERMISSIONS, USER_STATS, USER_BADGE_IN, USER_DELETION, USER_RESOURCE_CREATION, USER_RESOURCE_UPDATE_CONTENT, USER_RESOURCE_UPDATE_PERMISSIONS, USER_COMMUNICATION, USER_RESOURCE_ACCESS, USER_RESOURCE_DELETION, GROUP_UNCATEGORIZED, GROUP_CREATION, GROUP_DELETION, GROUP_MODIFICATION, EMAIL_UNCATEGORIZED, EMAIL_TRANSACTION, EMAIL_URL_CLICK, NETWORK_UNCATEGORIZED, NETWORK_FLOW, NETWORK_CONNECTION, NETWORK_FTP, NETWORK_DHCP, NETWORK_DNS, NETWORK_HTTP, NETWORK_SMTP, STATUS_UNCATEGORIZED, STATUS_HEARTBEAT, STATUS_STARTUP, STATUS_SHUTDOWN, STATUS_UPDATE, SCAN_UNCATEGORIZED, SCAN_FILE, SCAN_PROCESS_BEHAVIORS, SCAN_PROCESS, SCAN_HOST, SCAN_VULN_HOST, SCAN_VULN_NETWORK, SCAN_NETWORK, SCHEDULED_TASK_UNCATEGORIZED, SCHEDULED_TASK_CREATION, SCHEDULED_TASK_DELETION, SCHEDULED_TASK_ENABLE, SCHEDULED_TASK_DISABLE, SCHEDULED_TASK_MODIFICATION, SYSTEM_AUDIT_LOG_UNCATEGORIZED, SYSTEM_AUDIT_LOG_WIPE, SERVICE_UNSPECIFIED, SERVICE_CREATION, SERVICE_DELETION, SERVICE_START, SERVICE_STOP, SERVICE_MODIFICATION, GENERIC_EVENT, RESOURCE_CREATION, RESOURCE_DELETION, RESOURCE_PERMISSIONS_CHANGE, RESOURCE_READ, RESOURCE_WRITTEN, ANALYST_UPDATE_VERDICT, ANALYST_UPDATE_REPUTATION, ANALYST_UPDATE_SEVERITY_SCORE, ANALYST_UPDATE_STATUS, ANALYST_ADD_COMMENT|False|String||
|Time Frame|Specify a time frame for the results. If "Custom" is selected, you also need to provide "Start Time".|False|List|Custom|
|Start Time|Specify the start time for the results. This parameter is mandatory, if "Custom" is selected for the "Time Frame" parameter. Format: ISO 8601|False|String||
|End Time|Specify the end time for the results. Format: ISO 8601. If nothing is provided and "Custom" is selected for the "Time Frame" parameter then this parameter will use current time. Note: value "now" can also be used.|False|String||
|Reference Time|Specify the reference time for the event search. Format: YYYY-MM-DDThh:mmTZD. Note: if nothing is provided, action will use end time as reference time.|False|String||
|Output|Specify what should be the output for this action.|True|List|Events + Statistics|
|Max Events To Return|Specify how many events to process per entity type. Default: 100.|False|String|100|



##### JSON Results
```json
[{"Entity":"alan-centeno-pc","EntityResult":{"statistics":{"NETWORK_CONNECTION":10},"events":[{"metadata":{"eventTimestamp":"2020-09-28T17:20:00Z","eventType":"NETWORK_CONNECTION","productName":"Tanium Stream","productEventType":"NETWORK_DNS","ingestedTimestamp":"2020-09-28T16:28:11.615578Z"},"principal":{"hostname":"alan-centeno-pc","assetId":"TANIUM:alan-centeno-pc","process":{"pid":"1101","productSpecificProcessId":"TANIUM:32323"}},"target":{"hostname":"micrgsoft.com","user":{"userid":"alan"},"process":{"pid":"8172","file":{"md5":"a219fc7fcc93890a842183388f80369e","fullPath":"C:\\Program Files(x86)\\adobe\\acrobat reader dc\\reader\\acrord32.exe"},"commandLine":"\"C:\\Program Files(x86)\\adobe\\acrobat reader dc\\reader\\acrord32.exe\" ...","productSpecificProcessId":"TANIUM:82315"}}}],"uri":["https://demodev.backstory.chronicle.security/"]}}]
```



#### Remove Rows From Data Table
Remove rows from a data table in Google SecOps. Note: this action only works with Chronicle API authentication. Backstory API is not supported.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Data Table Name|Specify the display name of the data table that needs to be updated.|True|String||
|Rows|Specify a list of JSON objects that will be used to search rows in data tables. At least 1 valid column should be provided as part of payload. Action will search for all rows, where a specific column has that value and delete them.|True|String||



##### JSON Results
```json
[{"name": "projects/xxxxxx/locations/us/instances/xxxxxx/dataTables/data_table/dataTableRows/xxxxxx","values": {"columnName1": "asda","columnName2": "asdasd","columnName3": "zxczxc"},"createTime": "2025-05-14T12:52:51.908143Z","updateTime": "2025-0514T12:52:51.908143Z"}]
```



#### Enrich IP
Deprecated - Enrich IP entities using information from IOCs in Google Chronicle. Supported entities: IP address.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Create Insight|If enabled, action will create an insight containing information about the entities.|False|Boolean|true|
|Only Suspicious Insight|If enabled, action will only create an insight for entities that are marked as suspicious. Note: "Create Insight" parameter needs to be enabled.|False|Boolean|false|
|Lowest Suspicious Severity|Specify the lowest severity that should be associated with IP in order to mark it suspicious.|True|List|Medium|
|Mark Suspicious N/A Severity|If enabled, action will mark the entity as suspicious, if information about severity is not available.|False|Boolean|True|



##### JSON Results
```json
[{"Entity": "43.143.207.121", "EntityResult": {"sources": [{"category": "Indicator was published in publicly available sources", "firstActiveTime": "1970-01-01T00:00:01Z", "lastActiveTime": "9999-12-31T23:59:59Z", "addresses": [{"ipAddress": "K4/PeQ=="}], "rawSeverity": "low", "confidenceScore": {"strRawConfidenceScore": "67"}}], "feeds": [{"metadata": {"title": "Mandiant Open Source Intelligence", "description": "Open Source Intel IoC", "confidenceScoreBucket": {"rangeEnd": 100}}, "iocs": [{"categorization": "Indicator was published in publicly available sources", "activeTimerange": {"start": "1970-01-01T00:00:01Z", "end": "9999-12-31T23:59:59Z"}, "ipAndPorts": {"ipAddress": "K4/PeQ=="}, "confidenceScore": "67", "rawSeverity": "Low"}]}], "ioc_data_found": "false"}}]
```



#### Remove Values From Reference List
Remove values from a reference list in Google Chronicle.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Reference List Name|Specify the display name of the reference list that needs to be updated.|True|String||
|Values|Specify a comma-separated list of values that need to be removed from a reference list.|True|String||



##### JSON Results
```json
{"name": "projects/xxxx/locations/us/instances/yyyy/referenceLists/testList", "displayName": "testList", "revisionCreateTime": "2025-01-16T09:15:33.753071Z", "description": "Test reference list", "entries": [{"value": "domain1.com"}], "syntaxType": "REFERENCE_LIST_SYNTAX_TYPE_PLAIN_TEXT_STRING", "scopeInfo": {"referenceListScope": {}}, "createTime": "2025-01-16T09:15:33.753071Z", "lines": ["domain1.com"]}
```



#### Add Rows To Data Table
Add rows to a data table in Google SecOps. Note: this action only works with Chronicle API authentication. Backstory API is not supported.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Data Table Name|Specify the display name of the data table that needs to be updated.|True|String||
|Rows|Specify a list of JSON objects that contain information about the rows that need to be added.|True|String||



##### JSON Results
```json
[{"name": "xxxx", "values": "xxxx"}]
```



#### Enrich Entities
Enrich entities using information from Google SecOps. Supported entities: File Hash, IP Address, Domain, Hostname, URL (extracts domain part of URL), User, Email (User entity with email regex). Note: this action only works with Chronicle API authentication. Backstory API is not supported.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Namespace|Specify the namespace in which the entity is located. If nothing is provided, action will still put entities associated with a namespace in higher priority to be returned.|False|String||
|Time Frame|Specify a time frame for the results. Only the entities that have information in the provided timeframe will be returned. If “Custom” is selected, you also need to provide “Start Time”.|False|List|Last Month|
|Start Time|Specify the start time for the results. This parameter is mandatory, if “Custom” is selected for the “Time Frame” parameter. Format: ISO 8601.|False|String||
|End Time|Specify the end time for the results. Format: ISO 8601. If nothing is provided and “Custom” is selected for the “Time Frame” parameter then this parameter will use current time.|False|String||



##### JSON Results
```json
[{"Entity": "xxxx", "EntityResult": {"name": "xxxx", "metadata": {"entityType": "xxxx", "interval": {"startTime": "xxxx", "endTime": "xxxx"}}, "entity": {"namespace": "xxxx", "asset": "xxxx", "file": {"sha256": "xxxx", "md5": "xxxx", "sha1": "xxxx", "size": "xxxx", "fileType": "xxxx", "names": ["xxxx"], "firstSeenTime": "xxxx", "lastSeenTime": "xxxx", "lastAnalysisTime": "xxxx", "signatureInfo": {"sigcheck": {"verificationMessage": "xxxx", "verified": "xxxx", "signers": [{"name": "xxxx"}]}}, "firstSubmissionTime": "xxxx"}}, "metric": {"firstSeen": "xxxx", "lastSeen": "xxxx"}, "alertCounts": [{"rule": "xxxx", "count": "xxxx"}], "timeline": {"buckets": ["xxxx"], "bucketSize": "xxxx"}, "prevalenceResult": [{"prevalenceTime": "xxxx", "count": "xxxx"}], "fileMetadataAndProperties": "xxxx", "related_entities": [{"name": "xxxx", "metadata": {"entityType": "xxxx", "interval": {"startTime": "xxxx", "endTime": "xxxx"}}, "entity": {"namespace": "xxxx","asset": "xxxx"}, "metric": {"firstSeen": "xxxx", "lastSeen": "xxxx"}}]}}]
```



#### Is CIDR In Data Table
Check, if provided CIDR values are found in the data table in Google SecOps. Note: this action only works with Chronicle API authentication. Backstory API is not supported.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Data Table Name|The display name of the data table to search.|True|String||
|Column|A comma-separated list of columns to search within the data table. If no value is provided, the action searches all columns.|False|String||
|CIDR|The comma-separated list of CIDR values to search for in the data table.|True|String||
|Max Data Table Rows To Return|The number of data table rows to return for every matched value. Maximum: 1000.|True|String|1000|



##### JSON Results
```json
[{"Entity": "xxxx", "EntityResult": {"is_found": true, "matched_rows": [{"name": "xxxx", "values": "xxxx", "createTime": "xxxx", "updateTime": "xxxx"}]}}]
```



#### Ping
Test connectivity to the Google Chronicle with parameters provided at the integration configuration page on the Marketplace tab.
Timeout - 600 Seconds



#### Get Data Tables
Get available data tables in Google SecOps. Note: this action only works with Chronicle API authentication. Backstory API is not supported.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Filter Key|Specify the key that needs to be used to filter reference lists. Name option refers to a display name of the data table.|False|List|Select One|
|Filter Logic|Specify what filter logic should be applied.|False|List|Equal|
|Filter Value|Specify what value should be used in the filter. If “Equal“ is selected, action will try to find the exact match among results and if “Contains“ is selected, action will try to find results that contain that substring. “Equal” works with “title” parameter, while “Contains” works with all values in response. If nothing is provided in this parameter, the filter will not be applied.|False|String||
|Expanded Rows|If enabled, action will return data table rows as part of response.|False|Boolean|false|
|Max Data Tables To Return|Specify how many data tables to return. Maximum: 1000.|True|String|100|
|Max Data Table Rows To Return|Specify how many data table rows to return. Note: this parameter is only used if “Expanded Rows” is enabled. Maximum: 1000.|True|String|1000|



##### JSON Results
```json
[{"name": "projects/xxxxxx/locations/us/instances/xxxxxx/dataTables/xxxxxx","description":"test","displayName": "xxxxxx","createTime": "2025-05-14T12:52:50.064133Z","updateTime": "2025-05-14T13:13:48.631442Z","columnInfo": [{"originalColumn": "columnName1","columnType": "STRING"},{"columnIndex": 1,"originalColumn": "columnName2","columnType": "STRING"},{"columnIndex": 2,"originalColumn": "columnName3","columnType": "STRING"}],"dataTableUuid": "xxxxxx","approximateRowCount": "2","rows":[{"name":"projects/xxxxxx/locations/us/instances/xxxxxx/dataTables/data_table/dataTableRows/xxxxxx","values": {"columnName1": "asda","columnName2": "asdasd","columnName3": "zxczxc"},"createTime": "2025-05-14T12:52:51.908143Z","updateTime": "2025-05-14T12:52:51.908143Z"}]}]
```



#### Lookup Similar Alerts
Lookup similar alerts in Google Chronicle. Supported Chronicle alert types: RULE, EXTERNAL, IOC. Note: this action can only work with alerts that come from the "Chronicle Alerts Connector". Note: action can only fetch 10000 alerts. Make sure to narrow down the timeframe for better results.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Time Frame|Specify a time frame for the results. If "Alert Time Till Now" is selected, action will use start time of the alert as start time for the search and end time will be current time. If "30 Minutes Around Alert Time" is selected, action will search the alerts 30 minutes before the alert happened till the 30 minutes after the alert has happened.  Same idea applies to "1 Hour Around Alert Time" and "5 Minutes Around Alert Time".|False|List|Last Hour|
|IOCs / Assets|Specify a comma-separated list of IOCs or assets that you want to find in the alerts. Note: action will perform a different search for each item provided.|True|String||
|Similarity By|Specify what attributes need to be used, when the action is to search for similar alerts. If "Alert Name and Alert Type" is selected, action will try to find all of the alerts that have the same alert name and IOCs/Assets for the underlying alert type. If "Product" is selected, then action will try to find all of the alerts that originate from the same product and have the same IOCs/Assets, action will search among both "EXTERNAL" and "Rule" alerts. If "Only IOCs/Assets" is enabled, action will match the similarity only based upon the items provided in the parameter "IOCs/Assets", action will search among both "EXTERNAL" and "Rule" alerts.|False|List|Alert Name and Product|



##### JSON Results
```json
{"count":4,"distinct":[{"first_seen":"2021-12-01T20:47:02Z","last_seen":"2021-12-02T00:47:02Z","product_name":"Office 365","used_ioc_asset":"10.169.xxx.xxx","name":"Threat Model Positive Score:74","hostnames":"host-name","urls":"www.test.com","ips":"10.169.xxx.xxx","subjects":"Invoice for Goods","users":"test-user1, test-user2","email_addresses":"stanlee4@acme.com, tony@starkindustries.com","hashes":"xxxxxxxxxxxxxxxx","processes":"pr1, pr2","rule_urls":["www.rule-url.com"]},{"first_seen":"2021-12-01T20:47:02Z","last_seen":"2021-12-02T00:47:02Z","product_name":"Office 365","used_ioc_asset":"stanlee4@acme.com","name":"Threat Model Positive Score:74","hostnames":"host-name","urls":"www.test.com","ips":"10.169.xxx.xxx","subjects":"Invoice for Goods","users":"test-user1, test-user2","email_addresses":"stanlee4@acme.com, tony@starkindustries.com","hashes":"xxxxxxxxxxxxxxxx","processes":"pr1, pr2","rule_urls":["www.rule-url.com"]}],"processed_alerts":210,"run_time":0.640103,"external_url":"www.external-url.com"}
```



#### List Assets
List assets in Google Chronicle based on the related entities in the specified time frame. Supported entities: URL, IP Address, File hash. Only MD5, SHA-1 or SHA-256 hashes are supported.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Max Hours Backwards|Specify how many hours backwards to fetch the assets. Default: 1 hour.|False|String|1|
|Time Frame|Specify a time frame for the results. If "Custom" is selected, you also need to provide "Start Time". If the "Max Hours Backwards" parameter is provided then action will use the "Max Hours Backwards" parameter to provide a time filter. This is done for backwards compatibility.|False|List|Max Hours Backwards|
|Start Time|Specify the start time for the results. This parameter is mandatory, if "Custom" is selected for the "Time Frame" parameter. Format: ISO 8601|False|String||
|End Time|Specify the end time for the results. Format: ISO 8601. If nothing is provided and "Custom" is selected for the "Time Frame" parameter then this parameter will use current time.|False|String||
|Max Assets To Return|Specify how many assets to return in the response.|False|String|50|



##### JSON Results
```json
[{"Entity": "1.1.1.1", "EntityResult": {"assets": [{"asset": {"assetIpAddress": "1.1.1.1"}, "firstSeenArtifactInfo": {"artifactIndicator": {"destinationIpAddress": "1.1.1.1"}, "seenTime": "2020-10-03T00:22:00.944Z"}, "lastSeenArtifactInfo": {"artifactIndicator": {"destinationIpAddress": "1.1.1.1"}, "seenTime": "2020-10-04T08:27:17.971Z"}, "artifactIndicator": {"domain": "example.test"}, "sources": ["Mandiant Open Source Intelligence"], "categories": ["Indicator was published in publicly available sources"], "assetIndicators": [{"assetIpAddress": "172.xx.xxx.xxx"}], "iocIngestTimestamp": "2024-09-20T14:14:07.843Z", "firstSeenTimestamp": "2025-01-15T11:20:00Z", "lastSeenTimestamp": "2025-01-15T11:20:00Z", "filterProperties": {"stringProperties": {"TLD": {"values": [{"rawValue": ".test"}]}, "IOC FEED": {"values": [{"rawValue": "Mandiant Open Source Intelligence"}]}, "IOC CATEGORIES": {"values": [{"rawValue": "Indicator was published in publicly available sources"}]}, "IOC CONFIDENCE SCORE": {"values": [{"rawValue": "High"}]}, "IOC/ALERT SEVERITY": {"values": [{"rawValue": "Medium"}]}}}, "confidenceBucket": "High", "rawSeverity": "Medium", "logType": "OPEN_SOURCE_INTEL_IOC", "confidenceScore": 100, "globalCustomerId": "xxxxxxxxxx", "confidenceScoreBucket": {"rangeEnd": 100}, "categorization": "Indicator was published in publicly available sources", "domainAndPorts": {"domain": "example.test"}, "activeTimerange": {"startTime": "1970-01-01T00:00:01Z", "endTime": "9999-12-31T23:59:59Z"}, "feedName": "MANDIANT", "id": "ChBxxxxxxxxxx", "fieldAndValue": {"value": "example.test", "valueType": "DOMAIN_NAME"}}, {"asset": {"hostname": "test1"}, "firstSeenArtifactInfo": {"artifactIndicator": {"destinationIpAddress": "1.1.1.1"}, "seenTime": "2020-10-02T22:59:43.903Z"}, "lastSeenArtifactInfo": {"artifactIndicator": {"destinationIpAddress": "1.1.1.1"}, "seenTime": "2020-10-04T05:44:33.464Z"}, "artifactIndicator": {"domain": "example.test"}, "sources": ["Mandiant Active Breach Intelligence"], "categories": ["Indicator was published in publicly available sources"], "assetIndicators": [{"assetIpAddress": "172.xx.xxx.xxx"}], "iocIngestTimestamp": "2023-07-05T02:42:52.935Z", "firstSeenTimestamp": "2025-01-15T11:20:00Z", "lastSeenTimestamp": "2025-01-15T11:20:00Z", "filterProperties": {"stringProperties": {"IOC/ALERT SEVERITY": {"values": [{"rawValue": "Medium"}]}, "IOC CONFIDENCE SCORE": {"values": [{"rawValue": "High"}]}, "IOC FEED": {"values": [{"rawValue": "Mandiant Active Breach Intelligence"}]}, "IOC CATEGORIES": {"values": [{"rawValue": "Indicator was published in publicly available sources"}]}, "TLD": {"values": [{"rawValue": ".test"}]}}}, "confidenceBucket": "High", "rawSeverity": "Medium", "logType": "MANDIANT_ACTIVE_BREACH_IOC", "confidenceScore": 100, "globalCustomerId": "xxxxxxxxxx", "confidenceScoreBucket": {"rangeEnd": 100}, "categorization": "Indicator was published in publicly available sources", "domainAndPorts": {"domain": "example.test"}, "activeTimerange": {"startTime": "1970-01-01T00:00:01Z", "endTime": "9999-12-31T23:59:59Z"}, "feedName": "MANDIANT", "id": "ChBxxxxxxxxxx", "fieldAndValue": {"value": "example.test", "valueType": "DOMAIN_NAME"}}, {"asset": {"hostname": "test3"}, "firstSeenArtifactInfo": {"artifactIndicator": {"destinationIpAddress": "1.1.1.1"}, "seenTime": "2020-07-27T18:22:42.861Z"}, "lastSeenArtifactInfo": {"artifactIndicator": {"destinationIpAddress": "1.1.1.1"}, "seenTime": "2020-10-04T04:38:35.344Z"}, "artifactIndicator": {"domain": "example.test"}, "sources": ["Mandiant Active Breach Intelligence"], "categories": ["Indicator was published in publicly available sources"], "assetIndicators": [{"assetIpAddress": "172.xx.xxx.xxx"}], "iocIngestTimestamp": "2023-07-05T02:42:52.935Z", "firstSeenTimestamp": "2025-01-15T11:20:00Z", "lastSeenTimestamp": "2025-01-15T11:20:00Z", "filterProperties": {"stringProperties": {"IOC/ALERT SEVERITY": {"values": [{"rawValue": "Medium"}]}, "IOC CONFIDENCE SCORE": {"values": [{"rawValue": "High"}]}, "IOC FEED": {"values": [{"rawValue": "Mandiant Active Breach Intelligence"}]}, "IOC CATEGORIES": {"values": [{"rawValue": "Indicator was published in publicly available sources"}]}, "TLD": {"values": [{"rawValue": ".test"}]}}}, "confidenceBucket": "High", "rawSeverity": "Medium", "logType": "MANDIANT_ACTIVE_BREACH_IOC", "confidenceScore": 100, "globalCustomerId": "xxxxxxxxxx", "confidenceScoreBucket": {"rangeEnd": 100}, "categorization": "Indicator was published in publicly available sources", "domainAndPorts": {"domain": "example.test"}, "activeTimerange": {"startTime": "1970-01-01T00:00:01Z", "endTime": "9999-12-31T23:59:59Z"}, "feedName": "MANDIANT", "id": "ChBxxxxxxxxxx", "fieldAndValue": {"value": "example.test", "valueType": "DOMAIN_NAME"}}, {"asset": {"hostname": "exampledomain"}, "firstSeenArtifactInfo": {"artifactIndicator": {"destinationIpAddress": "1.1.1.1"}, "seenTime": "2019-12-04T13:46:34Z"}, "lastSeenArtifactInfo": {"artifactIndicator": {"destinationIpAddress": "1.1.1.1"}, "seenTime": "2020-10-04T08:27:17.971Z"}, "artifactIndicator": {"domain": "example.test"}, "sources": ["Mandiant Active Breach Intelligence"], "categories": ["Indicator was published in publicly available sources"], "assetIndicators": [{"assetIpAddress": "172.xx.xxx.xxx"}], "iocIngestTimestamp": "2023-07-05T02:42:52.935Z", "firstSeenTimestamp": "2025-01-15T11:20:00Z", "lastSeenTimestamp": "2025-01-15T11:20:00Z", "filterProperties": {"stringProperties": {"IOC/ALERT SEVERITY": {"values": [{"rawValue": "Medium"}]}, "IOC CONFIDENCE SCORE": {"values": [{"rawValue": "High"}]}, "IOC FEED": {"values": [{"rawValue": "Mandiant Active Breach Intelligence"}]}, "IOC CATEGORIES": {"values": [{"rawValue": "Indicator was published in publicly available sources"}]}, "TLD": {"values": [{"rawValue": ".test"}]}}}, "confidenceBucket": "High", "rawSeverity": "Medium", "logType": "MANDIANT_ACTIVE_BREACH_IOC", "confidenceScore": 100, "globalCustomerId": "xxxxxxxxxx", "confidenceScoreBucket": {"rangeEnd": 100}, "categorization": "Indicator was published in publicly available sources", "domainAndPorts": {"domain": "example.test"}, "activeTimerange": {"startTime": "1970-01-01T00:00:01Z", "endTime": "9999-12-31T23:59:59Z"}, "feedName": "MANDIANT", "id": "ChBxxxxxxxxxx", "fieldAndValue": {"value": "example.test", "valueType": "DOMAIN_NAME"}}], "uri": ["https://ironmountain.backstory.chronicle.security/domainResults?domain=www.google.com&selectedList=DomainViewDistinctAssets&whoIsTimestamp=2020-09-27T12%3A07%3A34.166830443Z"]}}]
```



#### Generate UDM Query
Preview. Use the Generate UDM Query action to construct complex UDM queries using natural language prompts in Google SecOps. Note: This action requires Chronicle API authentication. The legacy Backstory API authentication is not supported.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Prompt|The prompt that the system uses to generate the structured UDM query.|True|String||



##### JSON Results
```json
{"query": "ip = \"10.0.0.1\""}
```



#### Enrich Domain
Deprecated - Enrich domains using information from IOCs in Google Chronicle. Supported entities: Hostname, URL (action extracts domain part).
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Create Insight|If enabled, action will create an insight containing information about the entities.|False|Boolean|true|
|Only Suspicious Insight|If enabled, action will only create an insight for entities that are marked as suspicious. Note: "Create Insight" parameter needs to be enabled.|False|Boolean|false|
|Lowest Suspicious Severity|Specify the lowest severity that should be associated with domain in order to mark it suspicious.|True|List|Medium|
|Mark Suspicious N/A Severity|If enabled, action will mark the entity as suspicious, if information about severity is not available.|False|Boolean|True|



##### JSON Results
```json
[{"Entity": "facebooktoday.cc", "EntityResult": {"sources": [{"category": "Indicator was published in publicly available sources", "firstActiveTime": "1970-01-01T00:00:01Z", "lastActiveTime": "9999-12-31T23:59:59Z", "addresses": [{"domain": "facebooktoday.cc"}], "rawSeverity": "medium", "confidenceScore": {"strRawConfidenceScore": "100"}}, {"category": "Phishing", "firstActiveTime": null, "lastActiveTime": "2020-11-27T14:31:37Z", "addresses": [{"domain": "facebooktoday.cc"}, {"ipAddress": "ImaItA=="}], "rawSeverity": "high", "confidenceScore": {"strRawConfidenceScore": "high"}}, {"category": "Indicator was published in publicly available sources", "firstActiveTime": "1970-01-01T00:00:01Z", "lastActiveTime": "9999-12-31T23:59:59Z", "addresses": [{"domain": "facebooktoday.cc"}], "rawSeverity": "medium", "confidenceScore": {"strRawConfidenceScore": "100"}}], "feeds": [{"metadata": {"title": "Mandiant Open Source Intelligence", "description": "Open Source Intel IoC", "confidenceScoreBucket": {"rangeEnd": 100}}, "iocs": [{"domainAndPorts": {"domain": "facebooktoday.cc"}, "categorization": "Indicator was published in publicly available sources", "activeTimerange": {"start": "1970-01-01T00:00:01Z", "end": "9999-12-31T23:59:59Z"}, "confidenceScore": "100", "rawSeverity": "Medium"}]}, {"metadata": {"title": "ESET Threat Intelligence", "description": "ESET Threat Intelligence"}, "iocs": [{"domainAndPorts": {"domain": "facebooktoday.cc"}, "categorization": "Phishing", "activeTimerange": {"end": "2020-11-27T14:31:37Z"}, "ipAndPorts": {"ipAddress": "ImaItA=="}, "confidenceScore": "High", "rawSeverity": "High"}]}, {"metadata": {"title": "Mandiant Active Breach Intelligence", "description": "Mandiant Active Breach IoC", "confidenceScoreBucket": {"rangeEnd": 100}}, "iocs": [{"domainAndPorts": {"domain": "facebooktoday.cc"}, "categorization": "Indicator was published in publicly available sources", "activeTimerange": {"start": "1970-01-01T00:00:01Z", "end": "9999-12-31T23:59:59Z"}, "confidenceScore": "100", "rawSeverity": "Medium"}]}], "ioc_data_found": "false"}}]
```



#### Execute Retrohunt
Execute a rule retrohunt in Google Chronicle.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Rule ID|Specify the ID of the rule for which you want to run retrohunt.|True|String||
|Time Frame|Specify a time frame for the results. If “Alert Time Till Now” is selected, action will use start time of the alert as start time for the search and end time will be current time. If “30 Minutes Around Alert Time” is selected, action will search the alerts 30 minutes before the alert happened till the 30 minutes after the alert has happened.  Same idea applies to “1 Hour Around Alert Time” and “5 Minutes Around Alert Time”. If “Custom” is selected, you also need to provide “Start Time”.|False|List|Last Hour|
|Start Time|Specify the start time for the results. This parameter is mandatory, if “Custom” is selected for the “Time Frame” parameter. Format: ISO 8601.|False|String||
|End Time|Specify the end time for the results. Format: ISO 8601. If nothing is provided and “Custom” is selected for the “Time Frame” parameter then this parameter will use current time.|False|String||



##### JSON Results
```json
{"retrohuntId": "xxxxxxxxx-xxxxx-xxxxx-89e8-xxxxxxxxx", "ruleId": "xxxxxxxxx-xxf66d-xx4cec-xx-xxxxxxxxx", "versionId": "xxxxxxxxx-f66d-xx-b682-xxxxxxxxx@xxxxxxxxx", "eventStartTime": "2023-10-14T02:02:49.943Z", "eventEndTime": "2023-10-14T07:02:49.943Z", "retrohuntStartTime": "2023-10-16T12:28:09.042884Z", "state": "RUNNING", "name": "projects/365xxxxxxxxxx/locations/us/instances/df6xxxxxxxxxx/operations/oh_db3xxxxxxxxxx", "metadata": {"@type": "type.googleapis.com/google.cloud.chronicle.v1main.RetrohuntMetadata", "retrohunt": "projects/365xxxxxxxxxx/locations/us/instances/df6xxxxxxxxxx/rules/ru_a83xxxxxxxxxx@v_173xxxxxxxxxx/retrohunts/oh_db3xxxxxxxxxx", "executionInterval": {"startTime": "2025-01-09T13:30:10.098Z", "endTime": "2025-01-09T14:30:10.098Z"}}}
```



#### Get Detection Details
Fetch information about a detection in Google Chronicle.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Rule ID|Specify the ID of the rule, which is related to the detection.|True|String|[Alert.rule_id]|
|Detection ID|Specify the ID of the detection for which you want to fetch details.|True|String|[Alert.SiemID]|
|Include Raw Log Data|If selected, the action retrieves the original raw log file associated with the UDM search results. Note: This option is only available when using Chronicle API authentication.|False|Boolean|false|



##### JSON Results
```json
[{"type": "RULE_DETECTION", "detection": [{"ruleName": "dns_not_google", "urlBackToProduct": "https://unotest2.backstory-dev.chronicle.xxxx/alert?xxxx=xxxx-e380-xxxx-d29c-xxxx", "ruleId": "xxxx-f66d-xxxx-xxxx-xxxx", "ruleVersion": "xxxx-xxxx-xxxx-b682-xxxx@xxxx", "alertState": "ALERTING", "ruleType": "SINGLE_EVENT", "ruleLabels": [{"key": "priority", "value": "Medium"}, {"key": "severity", "value": "Medium"}], "riskScore": 40}], "createdTime": "2023-10-04T22:16:22.145254Z", "id": "xxxx-e380-xxxx-xxxx-xxxx", "timeWindow": {"startTime": "2023-10-04T21:18:44Z", "endTime": "2023-10-04T21:18:44Z"}, "collectionElements": [{"references": [{"event": {"metadata": {"productLogId": "xxxx-xxxx-xxxx45fc-xxxx-xxxx", "eventTimestamp": "2023-10-04T21:18:44Z", "eventType": "NETWORK_CONNECTION", "vendorName": "Palo Alto Networks", "productName": "NGFW", "productEventType": "Traffic - start", "ingestedTimestamp": "2023-10-04T21:31:03.790969Z", "id": "xxxx=", "logType": "UDM"}, "principal": {"hostname": "test3", "ip": ["x.x.0.x"], "port": 18985, "mac": ["00:00:00:0b:c9:11"], "asset": {"hostname": "test3", "ip": ["00.0.0.00"], "mac": ["00:00:00:0b:c9:11"]}}, "target": {"hostname": "youtube.com", "port": 4548, "asset": {"hostname": "youtube.com"}}, "securityResult": [{"action": ["ALLOW"]}], "network": {"sentBytes": "xxxxxxxxxxx", "receivedBytes": "xxxxxxxxxxx", "ipProtocol": "TCP", "sessionId": "xxxxxxxxxxx"}, "rawLogData":{"external_id": "xxxxxx","severity": "xxxxxx","matching_status": "xxxxxx","source": "xxxxxx","action": "xxxxxx","decodedString": "xxxxxx"}}}], "label": "e"}], "detectionTime": "2023-10-04T21:18:44Z"}]
```



#### Is Value In Data Table
Check, if provided values are found in the data table in Google SecOps. Note: this action only works with Chronicle API authentication. Backstory API is not supported.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Data Table Name|Specify the display name of the data table that needs to be updated.|True|String||
|Column|Specify a comma-separated list of columns that need to be searched within the data table. If nothing is provided, action will search within all columns.|False|String||
|Values|Specify a comma-separated list of values that need to be searched inside the data table.|True|String||
|Case Insensitive Search|If enabled, action will perform case insensitive matching.|False|Boolean|true|
|Max Data Table Rows To Return|Specify how many data table rows to return per value that was matched. Maximum: 1000.|True|String|1000|



##### JSON Results
```json
[{"Entity": "xxxx", "EntityResult": {"is_found": true, "matched_rows": [{"name": "xxxx", "values": "xxxx", "createTime": "xxxx", "updateTime": "xxxx"}]}}]
```






## Jobs

#### Google Chronicle Alerts Creator Job
This job will sync new SOAR alerts with Chronicle SIEM.
Note: This job is only supported from Chronicle SOAR version 6.2.30 and higher.

|Name|IsMandatory|Type|DefaultValue|
|----|-----------|----|------------|
|Environment|True|String|Default Environment|
|API Root|True|String|https://backstory.googleapis.com|
|User's Service Account|False|Password|*****|
|Workload Identity Email|False|Password|*****|
|Verify SSL|False|Boolean|true|

#### Google Chronicle Sync Job
This job will synchronize information about Chronicle SOAR Cases and Chronicle SOAR Alerts with Chronicle SIEM.
 Note: This job is only supported from Chronicle SOAR version 6.1.44 and higher.

|Name|IsMandatory|Type|DefaultValue|
|----|-----------|----|------------|
|Environment|True|String|Default Environment|
|API Root|True|String|https://backstory.googleapis.com|
|User's Service Account|False|Password|*****|
|Workload Identity Email|False|Password|*****|
|Max Hours Backwards|False|String|24|
|Verify SSL|False|Boolean|true|



## Connectors
#### Google Chronicle - Chronicle Alerts Connector
Pull information about Rule based alerts from Google Chronicle. Note: dynamic list is used for filtering purposes. For all of the details please visit the documentation portal.

|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Environment Field Name|Describes the name of the field where the environment name is stored. If the environment field isn't found, the environment is the default environment.|False|String||
|Environment Regex Pattern|A regex pattern to run on the value found in the "Environment Field Name" field. Default is .* to catch all and return the value unchanged. Used to allow the user to manipulate the environment field via regex logic. If the regex pattern is null or empty, or the environment value is null, the final environment result is the default environment.|False|String|.*|
|API Root|API root of the Chronicle instance.|True|String|https://backstory.googleapis.com|
|User's Service Account|Service Account that is used for authentication. If not provided, the default Service Account of the SecOps Instance will be used to authenticate.|False|Password|*****|
|Workload Identity Email|The client email address of your workload identity. You can configure either this parameter or the User's Service Account parameter. To impersonate service accounts with the workload identity email address, grant the Service Account Token Creator role to your service account. If both this and User's Service Account not provided, the default Service Account of the SecOps Instance will be used to authenticate.|False|Password|*****|
|Max Hours Backwards|Number of hours before the first connector iteration to retrieve alerts from. This parameter applies to the initial connector iteration after you enable the connector for the first time, or used as a fallback value in cases where connector's last run timestamp expires. Maximum: 167 hours.|False|Int|1|
|Max Alerts To Fetch|How many alerts per type to process per one connector iteration. Default: 100.|False|Int|100|
|Fallback Severity|Specify the fallback severity for the detection. This parameter is going to be used, if Chronicle detection doesn't include any information related to the severity. Possible values: Critical, High, Medium, Low, Info.|True|String|Medium|
|Verify SSL|If enabled, verify the SSL certificate for the connection to the Google Chronicle server is valid.|False|Boolean|true|
|Proxy Server Address|The address of the proxy server to use.|False|String||
| Proxy Username| The proxy username to authenticate with.|False|String||
| Proxy Password| The proxy password to authenticate with.|False|Password|*****|
|Disable Overflow|If enabled, the connector will ignore the overflow mechanism.|False|Boolean|false|
|Validate Dynamic List Entries|If enabled, the connector will fail if any filter configured in the Dynamic List is invalid. If disabled, invalid filters will be ignored completely and warnings will be logged.|False|Boolean|false|




