
# GoogleSecOpsAiAgents

This integration provides first-party AI agents for Google Chronicle. It allows users to leverage Google's advanced AI capabilities for security operations and threat intelligence within the Chronicle platform.

Python Version - V3_11
#### Parameters
|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Verify SSL|If enabled, verify the SSL certificate for the connection.|False|Boolean|true|


#### Dependencies
| |
|-|
|google_auth_httplib2-0.3.0-py3-none-any.whl|
|pycparser-3.0-py3-none-any.whl|
|google_api_python_client-2.188.0-py3-none-any.whl|
|requests_toolbelt-1.0.0-py2.py3-none-any.whl|
|certifi-2026.1.4-py3-none-any.whl|
|urllib3-2.6.3-py3-none-any.whl|
|proto_plus-1.27.1-py3-none-any.whl|
|pyasn1_modules-0.4.2-py3-none-any.whl|
|requests-2.32.5-py3-none-any.whl|
|h11-0.16.0-py3-none-any.whl|
|pyparsing-3.3.2-py3-none-any.whl|
|google_api_core-2.29.0-py3-none-any.whl|
|pycryptodome-3.23.0-cp37-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl|
|cffi-2.0.0-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.whl|
|protobuf-6.33.5-cp39-abi3-manylinux2014_x86_64.whl|
|charset_normalizer-3.4.4-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl|
|TIPCommon-2.3.1-py3-none-any.whl|
|rsa-4.9.1-py3-none-any.whl|
|google_auth-2.47.0-py3-none-any.whl|
|idna-3.11-py3-none-any.whl|
|pyopenssl-25.3.0-py3-none-any.whl|
|pyasn1-0.6.2-py3-none-any.whl|
|typing_extensions-4.15.0-py3-none-any.whl|
|cryptography-46.0.5-cp311-abi3-manylinux_2_34_x86_64.whl|
|httpx-0.28.1-py3-none-any.whl|
|anyio-4.12.1-py3-none-any.whl|
|EnvironmentCommon-1.0.2-py2.py3-none-any.whl|
|uritemplate-4.2.0-py3-none-any.whl|
|httpcore-1.0.9-py3-none-any.whl|
|httplib2-0.31.2-py3-none-any.whl|
|googleapis_common_protos-1.72.0-py3-none-any.whl|


## Actions
#### Ping
Use the Ping action to test the connectivity to Google Chronicle.
Timeout - 600 Seconds



#### Triage and Investigation Agent
Performs triage and investigation of Google SIEM alerts.
Timeout - 1200 Seconds



##### JSON Results
```json
{"confidence": "High Confidence", "verdict": "True Positive","agent_raw_data":{"name":"projects/123456789/locations/us/instances/00000000-0000-0000-0000-000000000000/investigations/11111111-1111-1111-1111-111111111111","verdict":"FALSE_POSITIVE","summary":"A security alert from SourceVendor detected a process making an outgoing connection to a destination IP. The investigation analyzed the process tree and command line arguments and determined the activity was benign/malicious.","status":"STATUS_COMPLETED_SUCCESS","timeRange":{"startTime":"2024-01-01T12:00:00.000000Z","endTime":"2024-01-01T12:05:00.000000Z"},"notebook":"projects/123456789/locations/us/instances/00000000-0000-0000-0000-000000000000/notebooks/22222222-2222-2222-2222-222222222222","confidence":"HIGH_CONFIDENCE","nextSteps":[{"title":"Search for network connection events from this hostname.","type":"SEARCHABLE"},{"title":"Search for process execution events on this hostname.","type":"SEARCHABLE"},{"title":"Manually verify the purpose of the triggered rule.","type":"MANUAL"}],"publishTime":"2024-01-01T12:05:00.000000Z","updateTime":"2024-01-01T12:05:00.000000Z","investigationSteps":[{"name":"projects/123456789/locations/us/instances/00000000-0000-0000-0000-000000000000/investigations/11111111-1111-1111-1111-111111111111/investigationSteps/1","analysisSummary":"Analysis of automated query results.","description":"No events were found for this query.","executionInterval":{"startTime":"2024-01-01T12:00:01.000Z","endTime":"2024-01-01T12:00:02.000Z"},"sourceMetadata":{"sourceType":"SOURCE_TYPE_SEARCH","query":{"queryCode":"generic_query_string","timeRange":{"startTime":"2024-01-01T12:00:00.000Z","endTime":"2024-01-01T12:05:00.000Z"},"operation":"projects/123456789/locations/us/instances/00000000-0000-0000-0000-000000000000/operations/"}}},{"name":"projects/123456789/locations/us/instances/00000000-0000-0000-0000-000000000000/investigations/11111111-1111-1111-1111-111111111111/investigationSteps/2","analysisSummary":"Analyzed Process Tree","description":"The process tree shows a specific process accessing a network resource.\n* **Network Communication:** The process is accessing a destination IP directly.","executionInterval":{"startTime":"2024-01-01T12:00:02.000Z","endTime":"2024-01-01T12:00:05.000Z"},"sourceMetadata":{"sourceType":"SOURCE_TYPE_PROCESS_TREE","processTree":{"processTree":"* C:\\path\\to\\process_name.exe (command line: \"/path/to/process_name.exe\" -argument, PID: 1234)\n  2024-01-01T12:00:00Z: NETWORK_UNCATEGORIZED\n"}}}],"alerts":{"ids":["alert_id_12345"]}}}
```









