
# AzureMonitor

Azure Monitor is a comprehensive monitoring solution for collecting, analyzing, and responding to monitoring data from your cloud and on-premises environments.

Python Version - 3
#### Parameters
|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Login API Root|The login API root of the Azure Monitor service.|True|String|https://login.microsoftonline.com|
|API Root|The API root of the Azure Monitor service.|True|String|https://api.loganalytics.io|
|Tenant ID|The Azure Monitor account tenant ID.|True|String||
|Client ID|The Azure Monitor account Client ID.|True|String||
|Client Secret|The Azure Monitor account Client Secret.|True|Password|*****|
|Workspace ID|The Azure Monitor account Workspace ID.|False|String||
|Verify SSL|If selected, the integration validates the SSL certificate when connecting to the Azure Monitor server. Enabled by default.|False|Boolean|true|


#### Dependencies
| |
|-|
|proto_plus-1.28.3-py3-none-any.whl|
|google_auth_httplib2-0.4.1-py3-none-any.whl|
|cffi-2.1.1-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.whl|
|google_api_core-2.30.3-py3-none-any.whl|
|pycparser-3.0-py3-none-any.whl|
|idna-3.19-py3-none-any.whl|
|python_dateutil-2.9.0.post0-py2.py3-none-any.whl|
|googleapis_common_protos-1.75.1-py3-none-any.whl|
|pyasn1-0.6.4-py3-none-any.whl|
|pyasn1_modules-0.4.2-py3-none-any.whl|
|httplib2-0.32.0-py3-none-any.whl|
|cryptography-50.0.0-cp311-abi3-manylinux2014_x86_64.manylinux_2_17_x86_64.whl|
|requests-2.32.5-py3-none-any.whl|
|h11-0.16.0-py3-none-any.whl|
|pyparsing-3.3.2-py3-none-any.whl|
|typing_extensions-4.16.0-py3-none-any.whl|
|pycryptodome-3.23.0-cp37-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl|
|protobuf-7.35.1-py3-none-any.whl|
|google_api_python_client-2.198.0-py3-none-any.whl|
|TIPCommon-2.2.12-py2.py3-none-any.whl|
|anyio-4.14.2-py3-none-any.whl|
|google_auth-2.56.3-py3-none-any.whl|
|certifi-2026.7.22-py3-none-any.whl|
|httpx-0.28.1-py3-none-any.whl|
|EnvironmentCommon-1.0.2-py2.py3-none-any.whl|
|charset_normalizer-3.5.1-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl|
|six-1.17.0-py2.py3-none-any.whl|
|uritemplate-4.2.0-py3-none-any.whl|
|urllib3-2.7.0-py3-none-any.whl|
|httpcore-1.0.9-py3-none-any.whl|


## Actions
#### Search Logs
Use the Search Logs action to search logs based on the provided query in Azure Monitor.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Workspace ID|ID of the workspace that needs to be searched. If nothing is provided, action will take the Workspace ID provided in the integration configuration.|False|String||
|Query|Query that needs to be executed.|True|String||
|Time Frame|Time frame for the query. If "Custom" is selected, you also need to provide "Start Time".|False|List|Last Hour|
|Start Time|Start time for the query. This parameter is mandatory, if "Custom" is selected for the "Time Frame" parameter. Format: ISO 8601.|False|String||
|End Time|End time for the query. Format: ISO 8601. If nothing is provided and "Custom" is selected for the "Time Frame" parameter then this parameter will use current time.|False|String||
|Max Results To Return|How many results should be returned from the search. Maximum: 1000.|True|String|100|



##### JSON Results
```json
[{"TimeGenerated": "2025-10-29T11:50:45.3033407Z", "OperationName": "Update Documents"}, {"TimeGenerated": "2025-10-29T11:50:47.0376269Z", "OperationName": "Update Incidents"}]
```



#### Ping
Use the Ping action to test the connectivity to Azure Monitor.
Timeout - 600 Seconds









