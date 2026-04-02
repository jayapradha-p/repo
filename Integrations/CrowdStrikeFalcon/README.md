
# CrowdStrikeFalcon

CrowdStrike Falcon is the leader in next-generation endpoint protection, threat intelligence and incident response through cloud-based endpoint protection.

Python Version - V3_11
#### Parameters
|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|API Root|None|False|None||
|Client API ID|None|True|None||
|Client API Secret|None|True|None||
|Verify SSL|None|False|None||
|Customer ID|The customer ID of the tenant in which to execute the integration. For use in multi-tenant (MSSP) environments.|False|None||


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






## Connectors
#### Crowdstrike - Alerts Connector
Pull alerts from Crowdstrike. Dynamic List works with the "display_name" parameter. Note: To fetch identity protection detections use "Identity Protection Detections Connector".

|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Environment Field Name|Describes the name of the field where the environment name is stored. If the environment field isn't found, the environment is the default environment.|False|None||
|Environment Regex Pattern|A regex pattern to run on the value found in the "Environment Field Name" field. Default is .* to catch all and return the value unchanged. Used to allow the user to manipulate the environment field through regex logic. If the regex pattern is null or empty, or the environment value is null, the final environment result is the default environment.|False|None|.*|
|API Root|API root of the Crowdstrike instance.|True|None|https://api.crowdstrike.com|
|Client ID|Client ID  of the Crowdstrike account.|True|None||
|Client Secret|Client Secret of the Crowdstrike account.|True|None||
|Lowest Severity Score To Fetch|Lowest severity score of the identity protection detections to fetch. If nothing is provided, the connector will ingest detections with all severities. Maximum is 100. Note: action also supports the following values: Informational, Low, Medium, High, Critical.|False|None||
|Max Hours Backwards|Number of hours before the first connector iteration to retrieve alerts from. This parameter applies to the initial connector iteration after you enable the connector for the first time, or used as a fallback value in cases where connector's last run timestamp expires.|True|None|1|
|Max Alerts To Fetch|How many alerts to process per one connector iteration. Default: 10.|True|None|10|
|Include Hidden Alerts|If enabled, connector will also fetch alerts that are labeled as "hidden" by Crowdstrike.|False|None|true|
|Fallback Severity|Fallback severity for the SecOps alert that should be applied to the Crowdstrike alerts, which are missing severity information. Possible values: Informational, Low, Medium, High, Critical. If nothing is provided, connector will use "Informational" severity.|False|None|Informational|
|Use dynamic list as a blocklist|If enabled, the dynamic list will be used as a blocklist.|False|None|false|
|Verify SSL|If enabled, verify the SSL certificate for the connection to the Crowdstrike server is valid.|False|None|false|
|Disable Overflow|If enabled, connector will ignore the overflow mechanism.|False|None|false|
|Proxy Server Address|The address of the proxy server to use.|False|None||
|Proxy Username|The proxy username to authenticate with.|False|None||
|Proxy Password|The proxy password to authenticate with.|False|None||
|Case Name Template|When provided, connector will add a new key called "custom_case_name" to the Google Secops Event. It can used to have a customer case name. Please refer to the documentation portal for more details. You can provide placeholders in the following format: [name of the field]. Example: Phishing - [event_mailbox]. Note: connector will use first Google Secops Event for placeholders. Only keys that have string value will be handled.|False|None||
|Alert Name Template|If provided, connector will use this value for Google Secops Alert Name. Please refer to the documentation portal for more details. You can provide placeholders in the following format: [name of the field]. Example: Phishing - [event_mailbox]. Note: connector will use first Google Secops Event for placeholders. Only keys that have string value will be handled. If nothing is provided or user provides an invalid template, connector will use the default alert name.|False|None||
|Customer ID|The customer ID of the tenant in which to execute the integration. For use in multi-tenant (MSSP) environments.|False|None||


#### Crowdstrike - Detections Connector
Deprecated. Pull detections from Crowdstrike. Whitelist works with filters that are supported by the API of Crowdstrike. For the details, please refer to the documentation portal.

|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Environment Field Name|Describes the name of the field where the environment name is stored. If the environment field isn't found, the environment is the default environment.|False|None||
|Environment Regex Pattern|A regex pattern to run on the value found in the "Environment Field Name" field. Default is .* to catch all and return the value unchanged. Used to allow the user to manipulate the environment field via regex logic. If the regex pattern is null or empty, or the environment value is null, the final environment result is the default environment.|False|None|.*|
|API Root|API root of the Crowdstrike instance.|True|None|https://api.crowdstrike.com|
|Client ID|Client ID  of the Crowdstrike account.|True|None||
|Client Secret|Client Secret of the Crowdstrike account.|True|None||
|Lowest Severity Score To Fetch|Lowest severity score of the detections to fetch. If nothing is provided, the connector won't apply this filter. Maximum is 100. Note: action also supports the following values: Low, Medium, High, Critical.|False|None|50|
|Lowest Confidence Score To Fetch|Lowest confidence score of the detections to fetch. If nothing is provided, the connector won't apply this filter. Maximum is 100.|False|None|0|
|Max Hours Backwards|Number of hours before the first connector iteration to retrieve detections from. This parameter applies to the initial connector iteration after you enable the connector for the first time, or used as a fallback value in cases where connector's last run timestamp expires.|False|None|1|
|Max Detections To Fetch|How many detections to process per one connector iteration. Default: 10.|False|None|10|
|Padding Period|The number of hours that connector will use for padding. Maximum: 6.|False|None|1|
|Disable Overflow|If enabled, connector will ignore the overflow mechanism.|False|None|false|
|Verify SSL|If enabled, verify the SSL certificate for the connection to the Crowdstrike server is valid.|False|None|false|
|Proxy Server Address|The address of the proxy server to use.|False|None||
|Proxy Username|The proxy username to authenticate with.|False|None||
|Proxy Password|The proxy password to authenticate with.|False|None||
|Case Name Template|When provided, connector will add a new key called "custom_case_name" to the Google Secops Event. It can used to have a customer case name. Please refer to the documentation portal for more details. You can provide placeholders in the following format: [name of the field]. Example: Phishing - [event_mailbox]. Note: connector will use first Google Secops Event for placeholders. Only keys that have string value will be handled.|False|None||
|Alert Name Template|If provided, connector will use this value for Google Secops Alert Name. Please refer to the documentation portal for more details. You can provide placeholders in the following format: [name of the field]. Example: Phishing - [event_mailbox]. Note: connector will use first Google Secops Event for placeholders. Only keys that have string value will be handled. If nothing is provided or user provides an invalid template, connector will use the default alert name.|False|None||
|Customer ID|The customer ID of the tenant in which to execute the integration. For use in multi-tenant (MSSP) environments.|False|None||


#### Crowdstrike - Identity Protection Detections Connector
Pull Identity Protection detections from Crowdstrike. Note: this connector requires an Identity Protection license. Dynamic List works with the “display_name” parameter.

|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Environment Field Name|Describes the name of the field where the environment name is stored. If the environment field isn't found, the environment is the default environment.|False|None||
|Environment Regex Pattern|A regex pattern to run on the value found in the "Environment Field Name" field. Default is .* to catch all and return the value unchanged. Used to allow the user to manipulate the environment field through regex logic. If the regex pattern is null or empty, or the environment value is null, the final environment result is the default environment.|False|None|.*|
|API Root|API root of the Crowdstrike instance.|True|None|https://api.crowdstrike.com|
|Client ID|Client ID  of the Crowdstrike account.|True|None||
|Client Secret|Client Secret of the Crowdstrike account.|True|None||
|Lowest Severity Score To Fetch|Lowest severity score of the identity protection detections to fetch. If nothing is provided, the connector will ingest detections with all severities. Maximum is 100. Note: action also supports the following values: Informational, Low, Medium, High, Critical.|False|None||
|Max Hours Backwards|Number of hours before the first connector iteration to retrieve detections from. This parameter applies to the initial connector iteration after you enable the connector for the first time, or used as a fallback value in cases where connector's last run timestamp expires.|False|None|1|
|Max Detections To Fetch|How many identity protection detections to process per one connector iteration. Default: 10.|False|None|10|
|Use dynamic list as a blocklist|If enabled, the dynamic list will be used as a blocklist.|False|None|true|
|Disable Overflow|If enabled, connector will ignore the overflow mechanism.|False|None|false|
|Verify SSL|If enabled, verify the SSL certificate for the connection to the Crowdstrike server is valid.|False|None|false|
|Proxy Server Address|The address of the proxy server to use.|False|None||
|Proxy Username|The proxy username to authenticate with.|False|None||
|Proxy Password|The proxy password to authenticate with.|False|None||
|Case Name Template|When provided, connector will add a new key called "custom_case_name" to the Google Secops Event. It can used to have a customer case name. Please refer to the documentation portal for more details. You can provide placeholders in the following format: [name of the field]. Example: Phishing - [event_mailbox]. Note: connector will use first Google Secops Event for placeholders. Only keys that have string value will be handled.|False|None||
|Alert Name Template|If provided, connector will use this value for Google Secops Alert Name. Please refer to the documentation portal for more details. You can provide placeholders in the following format: [name of the field]. Example: Phishing - [event_mailbox]. Note: connector will use first Google Secops Event for placeholders. Only keys that have string value will be handled. If nothing is provided or user provides an invalid template, connector will use the default alert name.|False|None||
|Customer ID|The customer ID of the tenant in which to execute the integration. For use in multi-tenant (MSSP) environments.|False|None||


#### Crowdstrike - Incidents Connector
Deprecated. Pull incident and related behaviors from Crowdstrike. Dynamic List works with the “incident_type” parameter.

|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|API Root|API root of the Crowdstrike instance.|True|None|https://api.crowdstrike.com|
|Client ID|Client ID  of the Crowdstrike account.|True|None||
|Client Secret|Client Secret of the Crowdstrike account.|True|None||
|Max Hours Backwards|Number of hours before the first connector iteration to retrieve incidents from. This parameter applies to the initial connector iteration after you enable the connector for the first time, or used as a fallback value in cases where connector's last run timestamp expires. Default: 1|False|None|1|
|Environment Field Name|Describes the name of the field where the environment name is stored. If the environment field isn't found, the environment is the default environment.|False|None||
|Environment Regex Pattern|A regex pattern to run on the value found in the "Environment Field Name" field. Default is .* to catch all and return the value unchanged. Used to allow the user to manipulate the environment field via regex logic. If the regex pattern is null or empty, or the environment value is null, the final environment result is the default environment.|False|None|.*|
|Lowest Severity Score To Fetch|Lowest severity score of the incidents to fetch. If nothing is provided, the connector will ingest incidents with all severities. Maximum is 100. Note: action also supports the following values: Low, Medium, High, Critical. In the Crowdstrike UI the same value is presented as divided by 10.|False|None||
|Max Incidents To Fetch|How many incidents to process per one connector iteration. Default: 10. Max: 100.|False|None|10|
|Use dynamic list as a blocklist|If enabled, the dynamic list will be used as a blocklist.|False|None|false|
|Disable Overflow|If enabled, connector will ignore the overflow mechanism.|False|None|false|
|Verify SSL|If enabled, verify the SSL certificate for the connection to the Crowdstrike server is valid.|False|None|false|
|Proxy Server Address|The address of the proxy server to use.|False|None||
|Proxy Username|The proxy username to authenticate with.|False|None||
|Proxy Password|The proxy password to authenticate with.|False|None||
|Customer ID|The customer ID of the tenant in which to execute the integration. For use in multi-tenant (MSSP) environments.|False|None||


#### Crowdstrike Falcon Streaming Events Connector
Crowdstrike Falcon Streaming Events Connector

|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Environment Field Name|Describes the name of the field where the environment name is stored. If environment field isn't found, environment is ""|False|None||
|Environment Regex Pattern|A regex pattern to run on the value found in the "Environment Field Name" field.|False|None||
|API Root|API root of the Crowdstrike instance|False|None|https://api.crowdstrike.com|
|Client ID|Client ID for Crowdstrike API|True|None||
|Client Secret|Client Secret for Crowdstrike API|True|None||
|Event types|Specify a comma-separated list of event types. Examples of the event types: DetectionSummaryEvent, IncidentSummaryEvent, UserActivityAuditEvent, RemoteResponseSessionStartEvent, RemoteResponseSessionEndEvent, EppDetectionSummaryEvent. For more information visit documentation portal.|False|None|DetectionSummaryEvent, IncidentSummaryEvent, UserActivityAuditEvent, RemoteResponseSessionStartEvent, RemoteResponseSessionEndEvent, EppDetectionSummaryEvent|
|Max Events per Cycle|Max events to process per connector run.|True|None|100|
|Max Day Backwards|Number of days before the first connector iteration to retrieve events from. This parameter applies to the initial connector iteration after you enable the connector for the first time, or used as a fallback value in cases where connector's last run timestamp expires.|False|None|3|
|Min Severity|Specify the events that should be ingested based on the events severity (detections events). The value ranges from 0-5. If other event types besides detections are ingested by the connector, connector sets a severity for them as -1 and this filter is not applied to those types of events|False|None|0|
|Alert Name Template|If provided, connector will use this value for Siemplify Alert Name. Please refer to the documentation portal for more details. You can provide placeholders in the following format: [name of the field]. Example: Phishing - [event_mailbox]. Note: connector will use first Siemplify Event for placeholders. Only keys that have string value will be handled. If nothing is provided or user provides an invalid template, connector will use the default alert name.|False|None||
|Rule Generator Template|	If provided, the connector will use this value for Siemplify Rule Generator. Please refer to the documentation portal for more details. You can provide placeholders in the following format: [name of the field]. Example: Phishing - [event_mailbox]. Note: connector will use the first Siemplify event for placeholders. Only keys that have string value will be handled. If nothing is provided or the user provides an invalid template, the connector will use the default rule generator.|False|None||
|Proxy Server Address|Proxy server address.|False|None||
|Proxy Username|Proxy username.|False|None||
|Proxy Password|Proxy password.|False|None||
|Disable Overflow|If enabled, connector will ignore the overflow mechanism.|False|None|false|
|Verify SSL|Indicate whether to use SSL in the session or not|False|None|false|
|Customer ID|The customer ID of the tenant in which to execute the integration. For use in multi-tenant (MSSP) environments.|False|None||




