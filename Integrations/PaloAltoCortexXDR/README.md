
# PaloAltoCortexXDR

Cortex XDR - XDR is the world’s first detection and response app that natively integrates network, endpoint and cloud data to stop sophisticated attacks.  Cortex XDR accurately detects threats with behavioral analytics and reveals the root cause to speed up investigations.

Python Version - V3_11
#### Parameters
|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Api Root|None|True|None||
|Api Key|None|True|None||
|Api Key ID|None|True|None||
|Verify SSL|None|False|None||


#### Dependencies
| |
|-|
|google_auth_httplib2-0.2.1-py3-none-any.whl|
|protobuf-6.33.2-cp39-abi3-manylinux2014_x86_64.whl|
|cachetools-6.2.2-py3-none-any.whl|
|urllib3-2.6.0-py3-none-any.whl|
|pytz-2024.1-py2.py3-none-any.whl|
|google_api_core-2.28.1-py3-none-any.whl|
|types_python_dateutil-2.9.0.20240316-py3-none-any.whl|
|TIPCommon-2.2.22-py2.py3-none-any.whl|
|anyio-4.12.0-py3-none-any.whl|
|requests_toolbelt-1.0.0-py2.py3-none-any.whl|
|python_dateutil-2.9.0.post0-py2.py3-none-any.whl|
|pycparser-2.23-py3-none-any.whl|
|pyasn1_modules-0.4.2-py3-none-any.whl|
|arrow-1.3.0-py3-none-any.whl|
|chardet-5.2.0-py3-none-any.whl|
|certifi-2025.11.12-py3-none-any.whl|
|google_auth-2.43.0-py2.py3-none-any.whl|
|sniffio-1.3.1-py3-none-any.whl|
|google_api_python_client-2.187.0-py3-none-any.whl|
|requests-2.32.5-py3-none-any.whl|
|cryptography-46.0.3-cp311-abi3-manylinux_2_34_x86_64.whl|
|h11-0.16.0-py3-none-any.whl|
|pyasn1-0.6.1-py3-none-any.whl|
|pycryptodome-3.23.0-cp37-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl|
|python2_secrets-1.0.5-py2.py3-none-any.whl|
|cffi-2.0.0-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.whl|
|charset_normalizer-3.4.4-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl|
|rsa-4.9.1-py3-none-any.whl|
|proto_plus-1.26.1-py3-none-any.whl|
|idna-3.11-py3-none-any.whl|
|pyopenssl-25.3.0-py3-none-any.whl|
|typing_extensions-4.15.0-py3-none-any.whl|
|httplib2-0.31.0-py3-none-any.whl|
|pyparsing-3.2.5-py3-none-any.whl|
|httpx-0.28.1-py3-none-any.whl|
|six-1.16.0-py2.py3-none-any.whl|
|EnvironmentCommon-1.0.2-py2.py3-none-any.whl|
|uritemplate-4.2.0-py3-none-any.whl|
|httpcore-1.0.9-py3-none-any.whl|
|googleapis_common_protos-1.72.0-py3-none-any.whl|


## Actions
#### Add Comment To Incident
Add a comment to an incident in Palo Alto Cortex XDR.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Incident ID|ID of the incident that needs to be updated.|True|None||
|Comment|Comment for the incident.|True|None||



#### Add Hashes to Block List
The action will add files which do not exist in the allow or block lists to a block list. Note - only SH256 format  for file hashes is supported.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Comment|Provide additional comment that represents additional information regarding the action.|False|None||



#### Enrich Entities
Enrich Siemplify Host and IP entities based on the information from the Palo Alto Cortex XDR.
Timeout - 600 Seconds



#### Execute XQL Search
Use “Execute XQL Search” action to fetch information using XQL in Palo Alto XDR. Note: Action is running as async, please adjust script timeout value in Google SecOps IDE for action, as needed.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Query|Query that needs to be executed in Palo Alto XDR. Note: don't provide "limit" as part of the query. Action will provide it automatically based on the value provided in the “Max Results To Return” parameter.|True|None||
|Time Frame|Time frame for the results. If “Custom” is selected, you also need to provide "Start Time".|False|None||
|Start Time|Start time for the results. This parameter is mandatory, if “Custom” is selected for the "Time Frame" parameter. Format: ISO 8601.|False|None||
|End Time|End time for the results. Format: ISO 8601. If nothing is provided and "Custom" is selected for the "Time Frame" parameter then this parameter will use current time.|False|None||
|Max Results To Return|How many results to return for the query. Action will append "limit" to the provided query. Default: 50. Maximum: 1000.|False|None||



#### Get Endpoint Agent Report
Get the agent report for an endpoint.
Timeout - 600 Seconds



#### Get Incident Details
Use “Get Incident Details” action to fetch information about the incident in Palo Alto XDR.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Incident ID|ID of the incident that needs to be returned.|True|None||
|Lowest Alert Severity|Lowest severity for the alert to be returned.|False|None||
|Max Alerts To Return|How many alerts to return for the query. Default: 50. Maximum: 1000.|False|None||



#### Isolate Endpoint
Isolate an endpoint.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Agent ID|A comma-separated list of agent IDs to isolate. This parameter works in conjunction with the provided entities.|False|None||



#### Scan Endpoint
Use the "Scan Endpoint" action to scan endpoints in Palo Alto XDR. Supported Entities: IP Address, Hostname. Note: This action executes asynchronously, requiring you to adjust the script timeout value in the Google SecOps IDE.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Incident ID|The ID of the incident to associate the scan activity with, allowing the results to appear in the incident timeline.|False|None||
|Agent ID|A comma-separated list of agent IDs to include in the scan. This parameter works in conjunction with the provided entities|False|None||



#### Ping
Test connectivity to Palo Alto Cortex XDR
Timeout - 600 Seconds



#### Query
Get data of a specific incident including alerts and key artifacts.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Incident ID|The ID of the incident for which you want to retrieve data.|True|None||



#### Unisolate Endpoint
Unisolate an endpoint.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Agent ID|A comma-separated list of agent IDs to unisolate. This parameter works in conjunction with the provided entities.|False|None||



#### Update an Incident
The ability to set a specific XDR incident as under investigation, assign to named users, etc.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Assigned User Name|The updated full name of the incident assignee.|False|None||
|Severity|Administrator-defined severity|False|None||
|Status|Updated incident status|False|None||
|Incident ID|The ID of the incident to be updated.|True|None||



#### Resolve an Incident
The ability to close XDR incidents with a close reason.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Incident ID|The ID of the incident to be updated.|True|None||
|Status|Updated incident status|True|None||
|Resolve Comment|Descriptive comment explaining the incident change.|False|None||






## Jobs

#### Sync Incidents
This job synchronizes Google SecOps Alerts and Palo Alto XDR Incidents. It ensures that comments and status are kept in sync between the two systems. For the job to identify the correct information, the Google SecOps case must have the "Palo Alto XDR Incident" tag. If the alert didn’t originate from "Palo Alto Cortex XDR Connector",  you will need to add an "Incident_ID" context value to the case for the job to be able to find the correct information.

|Name|IsMandatory|Type|DefaultValue|
|----|-----------|----|------------|
|Environment Name|True|None|Default Environment|
|Api Root|False|None||
|Api Key|True|None||
|Api Key ID|True|None||
|Max Hours Backwards|True|None|24|
|User Mapping JSON|False|None|{"Google SecOps Display Name": "XDR Username"}|
|Verify SSL|False|None|true|



## Connectors
#### Palo Alto Cortex XDR Connector
Pull incidents from Palo Alto XDR. Dynamic List works with the “source” parameter.

|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Api Root|The API root of the Palo Alto XDR instance.|True|None|https://api-{fqdn}|
|Api Key|The Palo Alto XDR API key.|True|None||
|Api Key ID|The Palo Alto XDR API key ID.|True|None|3|
|Verify SSL|If selected, the integration validates the SSL certificate when connecting to the Palo Alto XDR server.|False|None|true|
|Alerts Count Limit|The maximum number of incidents the connector processes for every iteration. Maximum: 100.|False|None|10|
|Use dynamic list as a blocklist|If selected, the connector uses the dynamic list as a blocklist.|False|None|false|
|Include Historical Artifacts|If selected, the connector retrieves all historical artifacts associated with an alert during the initial ingestion. Enabling this option may increase the volume of data ingested during the first run.|False|None|true|
|Disable Overflow|If selected, the connector ignores the Google SecOps overflow mechanism.|False|None|true|
|Max Days Backwards|The maximum number of days in the past to search for and retrieve incidents.|True|None|24|
|Status Filter|A comma-separated list of alert statuses for the connector to ingest. If no value is provided, the connector defaults to fetching alerts with the New and Under Investigation statuses.|False|None|New,Under Investigation|
|Split Incident Alerts|If selected, the connector separates the individual alerts within a single source incident, creating a distinct SOAR Alert for each one.|False|None|false|
|Lowest Alert Severity To Fetch|The lowest severity of the alerts to retrieve. If no value is provided, the connector ingests alerts with all severity levels. The Lowest Incident SmartScore To Fetch acts as a master filter. If an incident's score meets this threshold, all associated alerts will be processed, regardless of their individual severity filter settings.|False|None||
|Lowest Incident Severity To Fetch|The lowest severity of the incidents to retrieve. If no value is provided, the connector ingest incidents with all severities.|False|None||
|Lowest Incident SmartScore To Fetch|The lowest SmartScore (0 to 100) of the incidents to fetch. This filter operates independently of the severity filter. If no value is provided, the SmartScore filter is ignored.|False|None||
|Environment Field Name|The name of the field where the environment name is stored. If the environment field is missing, the connector uses the default value.|False|None||
|Environment Regex Pattern|A regular expression pattern to run on the value found in the Environment Field Name field. This parameter lets you manipulate the environment field using the regular expression logic. Use the default value .* to retrieve the required raw Environment Field Name value. If the regular expression pattern is null or empty, or the environment value is null, the final environment result is the default environment.|False|None||
|Proxy Server Address|The address of the proxy server to use.|False|None||
|Proxy Username|The proxy username to authenticate with.|False|None||
|Proxy Password|The proxy password to authenticate with.|False|None||




