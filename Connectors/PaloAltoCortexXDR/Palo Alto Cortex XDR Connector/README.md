# Palo Alto Cortex XDR Connector
Pull incidents from Palo Alto XDR. Dynamic List works with the “source” parameter.


Integration: PaloAltoCortexXDR

Integration Version: 30

Device Product Field: Product Name

Event Name Field: event_type
### Parameters
|Name|Description|Is Mandatory|Value|
|----|-----------|------------|-----|
|Api Root|The API root of the Palo Alto XDR instance.|True|https://api-gcptesting.xdr.us.paloaltonetworks.com|
|Api Key|The Palo Alto XDR API key.|True|*****|
|Api Key ID|The Palo Alto XDR API key ID.|True|56|
|Verify SSL|If selected, the integration validates the SSL certificate when connecting to the Palo Alto XDR server.|False|true|
|Alerts Count Limit|The maximum number of incidents the connector processes for every iteration. Maximum: 100.|False|10|
|Use dynamic list as a blocklist|If selected, the connector uses the dynamic list as a blocklist.|False|false|
|Include Historical Artifacts|If selected, the connector retrieves all historical artifacts associated with an alert during the initial ingestion. Enabling this option may increase the volume of data ingested during the first run.|False|true|
|Disable Overflow|If selected, the connector ignores the Google SecOps overflow mechanism.|False|true|
|Max Days Backwards|The maximum number of days in the past to search for and retrieve incidents.|True|24|
|Status Filter|A comma-separated list of alert statuses for the connector to ingest. If no value is provided, the connector defaults to fetching alerts with the New and Under Investigation statuses.|False|New,Under Investigation|
|Split Incident Alerts|If selected, the connector separates the individual alerts within a single source incident, creating a distinct SOAR Alert for each one.|False|false|
|Lowest Alert Severity To Fetch|The lowest severity of the alerts to retrieve. If no value is provided, the connector ingests alerts with all severity levels. The Lowest Incident SmartScore To Fetch acts as a master filter. If an incident's score meets this threshold, all associated alerts will be processed, regardless of their individual severity filter settings.|False||
|Lowest Incident Severity To Fetch|The lowest severity of the incidents to retrieve. If no value is provided, the connector ingest incidents with all severities.|False||
|Lowest Incident SmartScore To Fetch|The lowest SmartScore (0 to 100) of the incidents to fetch. This filter operates independently of the severity filter. If no value is provided, the SmartScore filter is ignored.|False||
|Environment Field Name|The name of the field where the environment name is stored. If the environment field is missing, the connector uses the default value.|False||
|Environment Regex Pattern|A regular expression pattern to run on the value found in the Environment Field Name field. This parameter lets you manipulate the environment field using the regular expression logic. Use the default value .* to retrieve the required raw Environment Field Name value. If the regular expression pattern is null or empty, or the environment value is null, the final environment result is the default environment.|False||
|Proxy Server Address|The address of the proxy server to use.|False||
|Proxy Username|The proxy username to authenticate with.|False||
|Proxy Password|The proxy password to authenticate with.|False|*****|
|Artifacts To Ignore|A comma-separated list of artifacts to exclude from Google SecOps event creation.|False||

