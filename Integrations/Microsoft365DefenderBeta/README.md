
# Microsoft365DefenderBeta

Microsoft 365 Defender is a unified pre- and post-breach enterprise defense suite that natively coordinates detection, prevention, investigation, and response across endpoints, identities, email, and applications to provide integrated protection against sophisticated attacks.

Python Version - 3
#### Parameters
|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Login API Root|None|True|String|https://login.microsoftonline.com|
|Graph API Root|None|True|String|https://graph.microsoft.com|
|API Root|None|True|String|https://api.security.microsoft.com|
|Tenant ID|None|True|String||
|Client ID|None|True|String||
|Client Secret|None|True|Password|*****|
|Verify SSL|None|False|Boolean|True|


#### Dependencies
| |
|-|
|PyJWT-2.9.0-py3-none-any.whl|
|protobuf-6.33.6-cp39-abi3-manylinux2014_x86_64.whl|
|TIPCommon-2.3.4-py3-none-any.whl|
|google_auth_httplib2-0.3.0-py3-none-any.whl|
|pycparser-3.0-py3-none-any.whl|
|google_api_python_client-2.188.0-py3-none-any.whl|
|requests_toolbelt-1.0.0-py2.py3-none-any.whl|
|EnvironmentCommon-1.0.1-py2.py3-none-any.whl|
|googleapis_common_protos-1.73.0-py3-none-any.whl|
|urllib3-2.6.3-py3-none-any.whl|
|proto_plus-1.27.1-py3-none-any.whl|
|charset_normalizer-3.4.6-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl|
|pyasn1_modules-0.4.2-py3-none-any.whl|
|chardet-5.2.0-py3-none-any.whl|
|sniffio-1.3.1-py3-none-any.whl|
|requests-2.32.5-py3-none-any.whl|
|h11-0.16.0-py3-none-any.whl|
|pyparsing-3.3.2-py3-none-any.whl|
|pycryptodome-3.23.0-cp37-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl|
|cffi-2.0.0-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.whl|
|google_api_core-2.30.0-py3-none-any.whl|
|pyasn1-0.6.3-py3-none-any.whl|
|rsa-4.9.1-py3-none-any.whl|
|google_auth-2.47.0-py3-none-any.whl|
|certifi-2026.2.25-py3-none-any.whl|
|idna-3.11-py3-none-any.whl|
|pyopenssl-25.3.0-py3-none-any.whl|
|typing_extensions-4.15.0-py3-none-any.whl|
|cryptography-46.0.5-cp311-abi3-manylinux_2_34_x86_64.whl|
|httpx-0.28.1-py3-none-any.whl|
|anyio-4.12.1-py3-none-any.whl|
|cachetools-6.2.4-py3-none-any.whl|
|uritemplate-4.2.0-py3-none-any.whl|
|httpcore-1.0.9-py3-none-any.whl|
|httplib2-0.31.2-py3-none-any.whl|


## Actions
#### Execute Entity Query
Execute a hunting query based on entities in Microsoft 365 Defender. Note: this action prepares a where filter based on entities. Please refer to the documentation for more details. Supported entities: IP, Host, User, Hash, URL.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Hostname Entity Key|Specify what key should be used with Hostname entities. Please refer to the action documentation for details.|False|String||
|File Hash Entity Key|Specify what key should be used with File Hash entities. Please refer to the action documentation for details.|False|String||
|User Entity Key|Specify what key should be used with User entities. Please refer to the action documentation for details.|False|String||
|URL Entity Key|Specify what key should be used with URL entities. Please refer to the action documentation for details.|False|String||
|Email Address Entity Key|Specify what key should be used with Email Address (User entity with email regex) entities. Please refer to the action documentation for details.|False|String||
|Stop If Not Enough Entities|If enabled, action will not start execution, unless all of the entity types are available for the specified “.. Entity Keys”. Example: if “IP Entity Key” and “File Hash Entity Key” are specified, but in the scope there are no file hashes then if this parameter is enabled, action will not execute the query.|False|Boolean|true|
|Cross Entity Operator|Specify what should be the logical operator used between different entity types.|True|List|OR|
|Table Names|Specify what tables should be queried.|True|String||
|Time Frame|Specify a time frame for the results. If "Custom" is selected, you also need to provide "Start Time".|False|List|Last Hour|
|Start Time|Specify the start time for the results. This parameter is mandatory, if "Custom" is selected for the "Time Frame" parameter. Format: ISO 8601|False|String||
|End Time|Specify the end time for the results. Format: ISO 8601. If nothing is provided and "Custom" is selected for the "Time Frame" parameter then this parameter will use current time.|False|String||
|Fields To Return|Specify what fields to return.|False|String||
|Sort Field|Specify what parameter should be used for sorting.|False|String|Timestamp|
|Sort Order|Specify the order of sorting.|False|List|ASC|
|Max Results To Return|Specify how many results to return. Default: 50.|False|String|50|
|IP Entity Key|Specify what key should be used with IP entities. Please refer to the action documentation for details.|False|String||



##### JSON Results
```json
[{"Timestamp":"2021-04-29T10:04:27.9049321Z","AlertId":"","ServiceSource":"","EntityType":"","EvidenceRole":"","EvidenceDirection":"","FileName":"","FolderPath":"","SHA1":"","SHA256":"","FileSize":null,"ThreatFamily":"","RemoteIP":"","RemoteUrl":"","AccountName":"","AccountDomain":"","AccountSid":"","AccountObjectId":"","AccountUpn":"","DeviceId":"4404d21581b65a3dbxxxxxxxxxxxxxxxxxxxxxxxxxxx","DeviceName":"desktop-xxxxxx","LocalIP":"","NetworkMessageId":"","EmailSubject":"","ApplicationId":null,"Application":"","OAuthApplicationId":"","ProcessCommandLine":"","AdditionalFields":"{\"IsLocalLogon\":true}","RegistryKey":"","RegistryValueName":"","RegistryValueData":"","Title":"","Category":"","Severity":"","DetectionSource":"","AttackTechniques":"","ClientVersion":"","PublicIP":"","OSArchitecture":"","OSPlatform":"","OSBuild":null,"IsAzureADJoined":null,"AadDeviceId":"","LoggedOnUsers":"","RegistryDeviceTag":"","OSVersion":"","MachineGroup":"","ReportId":2826,"OnboardingStatus":"","DeviceCategory":"","DeviceType":"","DeviceSubType":"","Model":"","Vendor":"","OSDistribution":"","OSVersionInfo":"","MergedDeviceIds":"","MergedToDeviceId":"","DeviceObjectId":"","NetworkAdapterName":"","MacAddress":"","NetworkAdapterType":"","NetworkAdapterStatus":"","TunnelType":"","ConnectedNetworks":"","DnsAddresses":"","IPv4Dhcp":"","IPv6Dhcp":"","DefaultGateways":"","IPAddresses":"","NetworkAdapterVendor":"","ActionType":"LogonFailed","LogonType":"Network","Protocol":"Kerberos","FailureReason":"","IsLocalAdmin":null,"LogonId":null,"RemoteDeviceName":"","RemoteIPType":"","RemotePort":null,"InitiatingProcessAccountDomain":"nt authority","InitiatingProcessAccountName":"system","InitiatingProcessAccountSid":"S-1-5-18","InitiatingProcessAccountUpn":"","InitiatingProcessAccountObjectId":"","InitiatingProcessIntegrityLevel":"","InitiatingProcessTokenElevation":"None","InitiatingProcessSHA1":"75c5a97f521f760e32a4a9639axxxxxxxxxxxxxx","InitiatingProcessSHA256":"","InitiatingProcessMD5":"9520a99e77d6196d0d0xxxxxxxxxxxxx","InitiatingProcessFileName":"svchost.exe","InitiatingProcessFileSize":null,"InitiatingProcessVersionInfoCompanyName":"","InitiatingProcessVersionInfoProductName":"","InitiatingProcessVersionInfoProductVersion":"","InitiatingProcessVersionInfoInternalFileName":"","InitiatingProcessVersionInfoOriginalFileName":"","InitiatingProcessVersionInfoFileDescription":"","InitiatingProcessId":3020,"InitiatingProcessCommandLine":"svchost.exe -k netsvcs -p -s Winmgmt","InitiatingProcessCreationTime":"2021-04-29T09:59:11.8716716Z","InitiatingProcessFolderPath":"C:\\Windows\\System32","InitiatingProcessParentId":728,"InitiatingProcessParentFileName":"\\Device\\HarddiskVolume4\\Windows\\System32\\services.exe","InitiatingProcessParentCreationTime":"2021-04-29T09:59:09.9224656Z","AppGuardContainerId":""}]
```



#### Execute Query
Execute hunting query in Microsoft 365 Defender.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Table Names|Specify what tables should be queried.|True|String||
|Query|Specify the query that needs to be executed. Use this parameter to provide |where clauses. Note: you don’t need to provide time filter, limiting and sorting.|False|String||
|Time Frame|Specify a time frame for the results. If "Custom" is selected, you also need to provide "Start Time".|False|List|Last Hour|
|Start Time|Specify the start time for the results. This parameter is mandatory, if "Custom" is selected for the "Time Frame" parameter. Format: ISO 8601|False|String||
|End Time|Specify the end time for the results. Format: ISO 8601. If nothing is provided and "Custom" is selected for the "Time Frame" parameter then this parameter will use current time.|False|String||
|Fields To Return|Specify what fields to return.|False|String||
|Sort Field|Specify what parameter should be used for sorting.|False|String|Timestamp|
|Sort Order|Specify the order of sorting.|False|List|ASC|
|Max Results To Return|Specify how many results to return. Default: 50.|False|String|50|



##### JSON Results
```json
[{"Timestamp":"2021-04-12T07:25:00Z","AlertId":"fa7a318954-6c4c-eaab-xxx-xxxxxxxxxx","Title":"CC_Sensitive information","Category":"InitialAccess","Severity":"Medium","ServiceSource":"Microsoft Defender for Office 365","DetectionSource":"Microsoft Defender for Office 365","AttackTechniques":""}]
```



#### Ping
Test connectivity to the Microsoft 365 Defender with parameters provided at the integration configuration page on the Marketplace tab.
Timeout - 600 Seconds



#### Update Incident
Update incident in Microsoft 365 Defender.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Incident ID|Specify the id of the incident that needs to be updated.|True|String||
|Status|Specify what status to set for the incident.|False|List|Select One|
|Classification|Specify what classification to set for the incident..|False|List|Select One|
|Determination|Specify what determination to set for the incident. Note: determination can only be set, when classification is true positive.|False|List|Select One|
|Assign To|Specify to whom to assign this incident.|False|String||



#### Add Comment To Incident
Add comment to incident in Microsoft 365 Defender.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Incident ID|Specify the id of the incident that needs to be updated.|True|String||
|Comment|Specify the comment that needs to be added to the incident.|True|String||



#### Execute Custom Query
Execute a custom hunting query in Microsoft 365 Defender.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Query|Specify the query that needs to be executed. Use this parameter to provide |where clauses. Note: Note: you don't need to provide a limiting ("top" keyword).|True|String||
|Max Results To Return|Specify how many results to return. Default: 50.|False|String|50|



##### JSON Results
```json
[{"Timestamp":"2021-04-12T07:25:00Z","AlertId":"fa7a318954-6c4c-eaab-xxx-xxxxxxxxxx","Title":"CC_Sensitive information","Category":"InitialAccess","Severity":"Medium","ServiceSource":"Microsoft Defender for Office 365","DetectionSource":"Microsoft Defender for Office 365","AttackTechniques":""}]
```






## Jobs

#### Sync Alerts
This job synchronizes Google SecOps Alerts and Microsoft Defender XDR Alerts. It ensures that comments and status are synchronized bi-directionally between both systems. Note: Assignee synchronization occurs exclusively from Microsoft Defender to Google SecOps. For the job to identify the correct information, the Google SecOps case must have the "Microsoft Defender XDR Alert" tag. If the alert didn’t originate from "Microsoft 365 Defender - Incidents Connector",  you will need to add an "Alert_ID" context value to the alert for the job to be able to find the correct information.

|Name|IsMandatory|Type|DefaultValue|
|----|-----------|----|------------|
|Environment Name|True|String|Default Environment|
|Login API Root|True|String|https://login.microsoftonline.com|
|Graph API Root|True|String|https://graph.microsoft.com|
|API Root|True|String|https://api.security.microsoft.com|
|Tenant ID|True|String||
|Client ID|True|String||
|Client Secret|True|Password|*****|
|Max Hours Backwards|True|Integer|24|
|Sync Assignee|False|Boolean|false|
|Verify SSL|False|Boolean|true|



## Connectors
#### Microsoft365DefenderBeta-Microsoft 365 Defender - Incidents Connector
Pull information about incidents and related alerts from Microsoft 365 Defender. Note: whitelist works with an incident name.

|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Environment Field Name|Describes the name of the field where the environment name is stored. If the environment field isn't found, the environment is the default environment.|False|String||
|Environment Regex Pattern|A regex pattern to run on the value found in the "Environment Field Name" field. Default is .* to catch all and return the value unchanged. Used to allow the user to manipulate the environment field via regex logic. If the regex pattern is null or empty, or the environment value is null, the final environment result is the default environment.|False|String|.*|
|Login API Root|Login API root of the Microsoft 365 Defender instance.|True|String|https://login.microsoftonline.com|
|Graph API Root|API root of the Microsoft Graph service.|True|String|https://graph.microsoft.com|
|API Root|API root of the Microsoft 365 Defender service.|True|String|https://api.security.microsoft.com|
|Tenant ID|Microsoft 365 Defender account tenant ID.|True|String||
|Client ID|Microsoft 365 Defender account client ID.|True|String||
|Client Secret|Microsoft 365 Defender account client secret.|True|Password|*****|
|Verify SSL|If enabled, verify the SSL certificate for the connection to the Microsoft 365 Defender server is valid.|False|Boolean|true|
|Lowest Severity To Fetch|Lowest severity that will be used to fetch incidents. Possible values: Informational, Low, Medium, High.|False|String||
|Max Hours Backwards|Number of hours before the first connector iteration to retrieve incidents from. This parameter applies to the initial connector iteration after you enable the connector for the first time, or used as a fallback value in cases where connector's last run timestamp expires.|False|Integer|1|
|Max Incidents To Fetch|How many incidents  to process per one connector iteration. Maximum is 20.|False|Integer|10|
|Dynamic List Field|Field that can be used in the dynamic list for filtering. Possible values: Incident Name, Alert Name. If nothing is provided, connector will work with the incident name.|False|String|Incident Name|
|Incident Status Filter|A comma-separated list of incident statuses that need to be ingested. If nothing is provided, the connector will ingest incidents with status “Active” and “In Progress”. Possible values:Active, In Progress, Resolved, Redirected.Note: it’s not recommended to ingest redirected incidents, because in most situations they will be empty.|False|String|Active, In Progress|
|Alert Detection Source Filter|A comma-separated list of detection sources of alerts that need to be ingested. Note: this is a case sensitive parameter. Example of the values:antivirus, microsoftDefenderForEndpoint|False|String||
|Alert Service Source Filter|A comma-separated list of service sources of alerts that need to be ingested. Note: this is a case sensitive parameter. Example of the values:antivirus, microsoftDefenderForEndpoint|False|String||
|Use whitelist as a blacklist|If enabled, whitelist will be used as a blacklist.|False|Boolean|false|
|Disable Overflow|If enabled, connector will ignore the overflow mechanism.|False|Boolean|true|
|Lowest Alert Severity To Fetch|Lowest severity that will be used to fetch alerts. Possible values: Informational, Low, Medium, High.|False|String||
|Disable Alert Tracking|If enabled, the connector will stop tracking updates associated with alerts.|False|Boolean|false|
|Proxy Server Address|The address of the proxy server to use.|False|String||
|Proxy Username|The proxy username to authenticate with.|False|String||
|Proxy Password|The proxy password to authenticate with.|False|Password|*****|




