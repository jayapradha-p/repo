# Crowdstrike - Detections Connector
Deprecated. Pull detections from Crowdstrike. Whitelist works with filters that are supported by the API of Crowdstrike. For the details, please refer to the documentation portal.


Integration: CrowdStrikeFalcon

Integration Version: 82.0

Device Product Field: Product Name

Event Name Field: behaviors_technique
### Parameters
|Name|Description|Is Mandatory|Value|
|----|-----------|------------|-----|
|Script Timeout (Seconds)|Timeout limit for the python process running the current script.|True|180|
|Environment Field Name|Describes the name of the field where the environment name is stored. If the environment field isn't found, the environment is the default environment.|False||
|Environment Regex Pattern|A regex pattern to run on the value found in the "Environment Field Name" field. Default is .* to catch all and return the value unchanged. Used to allow the user to manipulate the environment field via regex logic. If the regex pattern is null or empty, or the environment value is null, the final environment result is the default environment.|False|.*|
|API Root|API root of the Crowdstrike instance.|True|https://api.crowdstrike.com|
|Client ID|Client ID  of the Crowdstrike account.|True|dsddssd|
|Client Secret|Client Secret of the Crowdstrike account.|True|*****|
|Lowest Severity Score To Fetch|Lowest severity score of the detections to fetch. If nothing is provided, the connector won't apply this filter. Maximum is 100. Note: action also supports the following values: Low, Medium, High, Critical.|False|50|
|Lowest Confidence Score To Fetch|Lowest confidence score of the detections to fetch. If nothing is provided, the connector won't apply this filter. Maximum is 100.|False|0|
|Max Hours Backwards|Number of hours before the first connector iteration to retrieve detections from. This parameter applies to the initial connector iteration after you enable the connector for the first time, or used as a fallback value in cases where connector's last run timestamp expires.|False|1|
|Max Detections To Fetch|How many detections to process per one connector iteration. Default: 10.|False|10|
|Padding Period|The number of hours that connector will use for padding. Maximum: 6.|False|1|
|Disable Overflow|If enabled, connector will ignore the overflow mechanism.|False|false|
|Verify SSL|If enabled, verify the SSL certificate for the connection to the Crowdstrike server is valid.|False|false|
|Proxy Server Address|The address of the proxy server to use.|False||
|Proxy Username|The proxy username to authenticate with.|False||
|Proxy Password|The proxy password to authenticate with.|False|*****|
|Case Name Template|When provided, connector will add a new key called "custom_case_name" to the Google Secops Event. It can used to have a customer case name. Please refer to the documentation portal for more details. You can provide placeholders in the following format: [name of the field]. Example: Phishing - [event_mailbox]. Note: connector will use first Google Secops Event for placeholders. Only keys that have string value will be handled.|False||
|Alert Name Template|If provided, connector will use this value for Google Secops Alert Name. Please refer to the documentation portal for more details. You can provide placeholders in the following format: [name of the field]. Example: Phishing - [event_mailbox]. Note: connector will use first Google Secops Event for placeholders. Only keys that have string value will be handled. If nothing is provided or user provides an invalid template, connector will use the default alert name.|False||
|Customer ID|The customer ID of the tenant in which to execute the integration. For use in multi-tenant (MSSP) environments.|False||

