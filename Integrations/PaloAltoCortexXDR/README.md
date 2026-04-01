
# PaloAltoCortexXDR

Cortex XDR - XDR is the world’s first detection and response app that natively integrates network, endpoint and cloud data to stop sophisticated attacks.  Cortex XDR accurately detects threats with behavioral analytics and reveals the root cause to speed up investigations.

Python Version - V3_11


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
||ID of the incident that needs to be updated.||None||
||Comment for the incident.||None||



#### Add Hashes to Block List
The action will add files which do not exist in the allow or block lists to a block list. Note - only SH256 format  for file hashes is supported.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
||Provide additional comment that represents additional information regarding the action.||None||



#### Enrich Entities
Enrich Siemplify Host and IP entities based on the information from the Palo Alto Cortex XDR.
Timeout - 600 Seconds



#### Execute XQL Search
Use “Execute XQL Search” action to fetch information using XQL in Palo Alto XDR. Note: Action is running as async, please adjust script timeout value in Google SecOps IDE for action, as needed.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
||Query that needs to be executed in Palo Alto XDR. Note: don't provide "limit" as part of the query. Action will provide it automatically based on the value provided in the “Max Results To Return” parameter.||None||
||Time frame for the results. If “Custom” is selected, you also need to provide "Start Time".||None||
||Start time for the results. This parameter is mandatory, if “Custom” is selected for the "Time Frame" parameter. Format: ISO 8601.||None||
||End time for the results. Format: ISO 8601. If nothing is provided and "Custom" is selected for the "Time Frame" parameter then this parameter will use current time.||None||
||How many results to return for the query. Action will append "limit" to the provided query. Default: 50. Maximum: 1000.||None||



#### Get Endpoint Agent Report
Get the agent report for an endpoint.
Timeout - 600 Seconds



#### Get Incident Details
Use “Get Incident Details” action to fetch information about the incident in Palo Alto XDR.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
||ID of the incident that needs to be returned.||None||
||Lowest severity for the alert to be returned.||None||
||How many alerts to return for the query. Default: 50. Maximum: 1000.||None||



#### Isolate Endpoint
Isolate an endpoint.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
||A comma-separated list of agent IDs to isolate. This parameter works in conjunction with the provided entities.||None||



#### Scan Endpoint
Use the "Scan Endpoint" action to scan endpoints in Palo Alto XDR. Supported Entities: IP Address, Hostname. Note: This action executes asynchronously, requiring you to adjust the script timeout value in the Google SecOps IDE.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
||The ID of the incident to associate the scan activity with, allowing the results to appear in the incident timeline.||None||
||A comma-separated list of agent IDs to include in the scan. This parameter works in conjunction with the provided entities||None||



#### Ping
Test connectivity to Palo Alto Cortex XDR
Timeout - 600 Seconds



#### Query
Get data of a specific incident including alerts and key artifacts.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
||The ID of the incident for which you want to retrieve data.||None||



#### Unisolate Endpoint
Unisolate an endpoint.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
||A comma-separated list of agent IDs to unisolate. This parameter works in conjunction with the provided entities.||None||



#### Update an Incident
The ability to set a specific XDR incident as under investigation, assign to named users, etc.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
||The updated full name of the incident assignee.||None||
||Administrator-defined severity||None||
||Updated incident status||None||
||The ID of the incident to be updated.||None||



#### Resolve an Incident
The ability to close XDR incidents with a close reason.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
||The ID of the incident to be updated.||None||
||Updated incident status||None||
||Descriptive comment explaining the incident change.||None||






## Jobs

#### Sync Incidents
This job synchronizes Google SecOps Alerts and Palo Alto XDR Incidents. It ensures that comments and status are kept in sync between the two systems. For the job to identify the correct information, the Google SecOps case must have the "Palo Alto XDR Incident" tag. If the alert didn’t originate from "Palo Alto Cortex XDR Connector",  you will need to add an "Incident_ID" context value to the case for the job to be able to find the correct information.

|Name|IsMandatory|Type|DefaultValue|
|----|-----------|----|------------|
|||None|Default Environment|
|||None||
|||None||
|||None||
|||None|24|
|||None|{"Google SecOps Display Name": "XDR Username"}|
|||None|true|



## Connectors
#### Palo Alto Cortex XDR Connector
Pull incidents from Palo Alto XDR. Dynamic List works with the “source” parameter.

|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
||The API root of the Palo Alto XDR instance.||None|https://api-{fqdn}|
||The Palo Alto XDR API key.||None||
||The Palo Alto XDR API key ID.||None|3|
||If selected, the integration validates the SSL certificate when connecting to the Palo Alto XDR server.||None|true|
||The maximum number of incidents the connector processes for every iteration. Maximum: 100.||None|10|
||If selected, the connector uses the dynamic list as a blocklist.||None|false|
||If selected, the connector retrieves all historical artifacts associated with an alert during the initial ingestion. Enabling this option may increase the volume of data ingested during the first run.||None|true|
||If selected, the connector ignores the Google SecOps overflow mechanism.||None|true|
||The maximum number of days in the past to search for and retrieve incidents.||None|24|
||A comma-separated list of alert statuses for the connector to ingest. If no value is provided, the connector defaults to fetching alerts with the New and Under Investigation statuses.||None|New,Under Investigation|
||If selected, the connector separates the individual alerts within a single source incident, creating a distinct SOAR Alert for each one.||None|false|
||The lowest severity of the alerts to retrieve. If no value is provided, the connector ingests alerts with all severity levels. The Lowest Incident SmartScore To Fetch acts as a master filter. If an incident's score meets this threshold, all associated alerts will be processed, regardless of their individual severity filter settings.||None||
||The lowest severity of the incidents to retrieve. If no value is provided, the connector ingest incidents with all severities.||None||
||The lowest SmartScore (0 to 100) of the incidents to fetch. This filter operates independently of the severity filter. If no value is provided, the SmartScore filter is ignored.||None||
||The name of the field where the environment name is stored. If the environment field is missing, the connector uses the default value.||None||
||A regular expression pattern to run on the value found in the Environment Field Name field. This parameter lets you manipulate the environment field using the regular expression logic. Use the default value .* to retrieve the required raw Environment Field Name value. If the regular expression pattern is null or empty, or the environment value is null, the final environment result is the default environment.||None||
||The address of the proxy server to use.||None||
||The proxy username to authenticate with.||None||
||The proxy password to authenticate with.||None||




