# Google Chronicle - Chronicle Alerts Connector
Pull information about Rule based alerts from Google Chronicle. Note: dynamic list is used for filtering purposes. For all of the details please visit the documentation portal.


Integration: GoogleChronicle

Integration Version: 87.0

Device Product Field: alert_type

Event Name Field: event_type
### Parameters
|Name|Description|Is Mandatory|Value|
|----|-----------|------------|-----|
|Script Timeout (Seconds)|Timeout limit for the python process running the current script.|True|180|
|Environment Field Name|Describes the name of the field where the environment name is stored. If the environment field isn't found, the environment is the default environment.|False||
|Environment Regex Pattern|A regex pattern to run on the value found in the "Environment Field Name" field. Default is .* to catch all and return the value unchanged. Used to allow the user to manipulate the environment field via regex logic. If the regex pattern is null or empty, or the environment value is null, the final environment result is the default environment.|False|.*|
|API Root|API root of the Chronicle instance.|True|https://backstory.googleapis.com|
|User's Service Account|Service Account that is used for authentication. If not provided, the default Service Account of the SecOps Instance will be used to authenticate.|False||
|Workload Identity Email|The client email address of your workload identity. You can configure either this parameter or the User's Service Account parameter. To impersonate service accounts with the workload identity email address, grant the Service Account Token Creator role to your service account. If both this and User's Service Account not provided, the default Service Account of the SecOps Instance will be used to authenticate.|False||
|Max Hours Backwards|Number of hours before the first connector iteration to retrieve alerts from. This parameter applies to the initial connector iteration after you enable the connector for the first time, or used as a fallback value in cases where connector's last run timestamp expires. Maximum: 167 hours.|False|1|
|Max Alerts To Fetch|How many alerts per type to process per one connector iteration. Default: 100.|False|100|
|Fallback Severity|Specify the fallback severity for the detection. This parameter is going to be used, if Chronicle detection doesn't include any information related to the severity. Possible values: Critical, High, Medium, Low, Info.|True|Medium|
|Verify SSL|If enabled, verify the SSL certificate for the connection to the Google Chronicle server is valid.|False|true|
|Proxy Server Address|The address of the proxy server to use.|False||
| Proxy Username| The proxy username to authenticate with.|False||
| Proxy Password| The proxy password to authenticate with.|False||
|Disable Overflow|If enabled, the connector will ignore the overflow mechanism.|False|false|
|Validate Dynamic List Entries|If enabled, the connector will fail if any filter configured in the Dynamic List is invalid. If disabled, invalid filters will be ignored completely and warnings will be logged.|False|false|

