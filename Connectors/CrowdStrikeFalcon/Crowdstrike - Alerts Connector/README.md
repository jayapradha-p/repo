# Crowdstrike - Alerts Connector
Pull alerts from Crowdstrike. Dynamic List works with the "display_name" parameter. Note: To fetch identity protection detections use "Identity Protection Detections Connector".


Integration: CrowdStrikeFalcon

Integration Version: 82.0

Device Product Field: Product Name

Event Name Field: type
### Parameters
|Name|Description|Is Mandatory|Value|
|----|-----------|------------|-----|
|Environment Field Name|Describes the name of the field where the environment name is stored. If the environment field isn't found, the environment is the default environment.|False||
|Environment Regex Pattern|A regex pattern to run on the value found in the "Environment Field Name" field. Default is .* to catch all and return the value unchanged. Used to allow the user to manipulate the environment field through regex logic. If the regex pattern is null or empty, or the environment value is null, the final environment result is the default environment.|False|.*|
|Script Timeout (Seconds)|Timeout limit for the python process running the current script.|True|180|
|API Root|API root of the Crowdstrike instance.|True|https://api.crowdstrike.com|
|Client ID|Client ID  of the Crowdstrike account.|True|assss|
|Client Secret|Client Secret of the Crowdstrike account.|True|*****|
|Lowest Severity Score To Fetch|Lowest severity score of the identity protection detections to fetch. If nothing is provided, the connector will ingest detections with all severities. Maximum is 100. Note: action also supports the following values: Informational, Low, Medium, High, Critical.|False||
|Max Hours Backwards|Number of hours before the first connector iteration to retrieve alerts from. This parameter applies to the initial connector iteration after you enable the connector for the first time, or used as a fallback value in cases where connector's last run timestamp expires.|True|1|
|Max Alerts To Fetch|How many alerts to process per one connector iteration. Default: 10.|True|10|
|Include Hidden Alerts|If enabled, connector will also fetch alerts that are labeled as "hidden" by Crowdstrike.|False|true|
|Fallback Severity|Fallback severity for the SecOps alert that should be applied to the Crowdstrike alerts, which are missing severity information. Possible values: Informational, Low, Medium, High, Critical. If nothing is provided, connector will use "Informational" severity.|False|Informational|
|Use dynamic list as a blocklist|If enabled, the dynamic list will be used as a blocklist.|False|false|
|Verify SSL|If enabled, verify the SSL certificate for the connection to the Crowdstrike server is valid.|False|false|
|Disable Overflow|If enabled, connector will ignore the overflow mechanism.|False|false|
|Proxy Server Address|The address of the proxy server to use.|False||
|Proxy Username|The proxy username to authenticate with.|False||
|Proxy Password|The proxy password to authenticate with.|False|*****|
|Case Name Template|When provided, connector will add a new key called "custom_case_name" to the Google Secops Event. It can used to have a customer case name. Please refer to the documentation portal for more details. You can provide placeholders in the following format: [name of the field]. Example: Phishing - [event_mailbox]. Note: connector will use first Google Secops Event for placeholders. Only keys that have string value will be handled.|False||
|Alert Name Template|If provided, connector will use this value for Google Secops Alert Name. Please refer to the documentation portal for more details. You can provide placeholders in the following format: [name of the field]. Example: Phishing - [event_mailbox]. Note: connector will use first Google Secops Event for placeholders. Only keys that have string value will be handled. If nothing is provided or user provides an invalid template, connector will use the default alert name.|False||
|Customer ID|The customer ID of the tenant in which to execute the integration. For use in multi-tenant (MSSP) environments.|False||

