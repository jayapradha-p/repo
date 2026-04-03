<p align="center"><img src="./Resources/CrowdStrikeFalcon.svg" 
     alt="CrowdStrikeFalcon" width="200"/></p>

# CrowdStrikeFalcon

CrowdStrike Falcon is the leader in next-generation endpoint protection, threat intelligence and incident response through cloud-based endpoint protection.

Python Version - 3
#### Parameters
|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|API Root|||None|https://api.crowdstrike.com|
|Client API ID||True|None||
|Client API Secret||True|None|None|
|Verify SSL|||None|False|
|Customer ID|||None||


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


## Actions
#### Download File
Download files from the hosts in Crowdstrike Falcon. Supported entities: File Name, IP Address and Hostname. Note: action requires both File Name and IP Address/Hostname entity to be in the scope of the Siemplify alert. The downloaded file will be in password-protected zip. Password is "infected".
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Customer ID|Specify the ID of the customer for which you want to execute the action.||String||
|Download Folder Path|Specify the path to the folder, where you want to store the threat file.|True|String||
|Overwrite|If enabled, action will overwrite the file with the same name.||Boolean|false|



##### JSON Results
```json
{"absolute_paths":["/opt/file_1","opt_file_2"]}
```



#### Add Alert Comment
Add a comment to alert in Crowdstrike. 
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Alert ID|Specify the ID of the alert that needs to be updated.|True|String||
|Comment|Specify the comment for the alert.|True|String||



#### Add Identity Protection Detection Comment
Add a comment to identity protection detection in Crowdstrike.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Detection ID|Specify the ID of the detection that needs to be updated.|True|String||
|Comment|Specify the comment for the detection.|True|String||



#### Add Incident Comment
Deprecated. Add comment to incident in Crowdstrike.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Incident ID|Specify the ID of the incident that needs to be updated.|True|String||
|Comment|Specify the comment for the incident.|True|String||



##### JSON Results
```json
[{"incident_id": "inc:466a00b13a5e4a9a9x.ac1a5e:x.x.x.", "incident_type": 1, "cid": "27fe4e476ca3490b6b2b6650e5a74", "host_ids": ["466a00b13a5e4a9a93ce2aca5eac1a5e"], "hosts": [{"device_id": "466a00b13a5e4a9a93ce2aca5eac1a5e", "cid": "27fe4e476ca34dd90b8476b2b6650e5a74", "agent_load_flags": "0", "agent_local_time": "2023-09-25T15:41:40.130Z", "agent_version": "7.01.17312.0", "bios_manufacturer": "VMware, Inc.", "bios_version": "VMW71.00V.17369862.B64.2012240522", "config_id_base": "65994753", "config_id_build": "17312", "config_id_platform": "3", "external_ip": "35.246.203.0", "hostname": "EX16-AD01", "first_seen": "2023-01-20T00:40:31Z", "last_seen": "2023-10-06T07:19:50Z", "local_ip": "172.30.3.162", "mac_address": "00-50-56-a2-94-8d", "machine_domain": "exlab.local", "major_version": "10", "minor_version": "0", "os_version": "Windows Server 2016", "ou": ["Domain Controllers"], "platform_id": "0", "platform_name": "Windows", "product_type": "2", "product_type_desc": "Domain Controller", "site_name": "Default-First-Site-Name", "status": "contained", "system_manufacturer": "VMware, Inc.", "system_product_name": "VMware7,1", "groups": ["9489d65c343244169627dcbc"], "modified_timestamp": "2023-10-06T07:19:58Z"}], "created": "2023-10-06T07:20:51Z", "start": "2023-10-06T07:19:21Z", "end": "2023-10-06T07:30:27Z", "state": "closed", "assigned_to": "67494-b86d-4a55-9e52-7492449400a1", "assigned_to_name": "Yuriy Landovskyy", "status": 30, "tactics": ["Persistence", "Defense Evasion", "Command and Control", "Credential Access", "Malware", "Privilege Escalation"], "techniques": ["Create Account", "Masquerading", "Ingress Tool Transfer", "OS Credential Dumping", "Malicious File", "Image File Execution Options Injection", "Bypass User Account Control", "Accessibility Features", "Registry Run Keys / Startup Folder"], "objectives": ["Keep Access", "Contact Controlled Systems", "Gain Access", "Falcon Detection Method"], "modified_timestamp": "2023-10-20T08:34:07.078440797Z", "users": ["EX16-AD01$", "administrator"], "fine_score": 100}]
```



#### Close Detection
Deprecated. Close a Crowdstrike Falcon detection. Note: Action "Update Detection" is the best practice for this use case.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Detection ID|Specify the id of the detection that needs to be closed.|True|String||
|Hide Detection|If enabled, action will hide the detection in the UI.||Boolean|true|



#### Add Comment to Detection
Deprecated. Add a comment to the detection in Crowdstrike Falcon.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Detection ID|Specify the id of the detection to which you want to add a comment.|True|String||
|Comment|Specify the comment that needs to be added to the detection.|True|String||



#### Delete IOC
Delete custom IOCs in Crowdstrike Falcon. Supported entities: Hostname, URL, IP address and Hash. Note: Hostname entities are treated as domain IOCs and action will extract domain part out of URLs. Only MD5 and SHA-256 hashes are supported.
Timeout - 600 Seconds



#### Contain Endpoint
Contain endpoint in Crowdstrike Falcon. Supported entities: Hostname and IP address.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Customer ID|Specify the ID of the customer for which you want to execute the action.||String||
|Fail If Timeout|If enabled, action will be failed, if not all of the endpoints were contained.||Boolean|true|



##### JSON Results
```json
{"Entity":"XXX.XXX.XXX","EntityResult":{"device_id":"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX","cid":"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX","agent_load_flags":"1","agent_local_time":"2021-05-26T11:54:38.105Z","agent_version":"X.XXX.XXX.0","bios_manufacturer":"Phoenix Technologies LTD","bios_version":"6.00","build_number":"XXXX","config_id_base":"XXXX","config_id_build":"XXXX","config_id_platform":"3","cpu_signature":"XXXXX","external_ip":"XXX.XXX.XXX.XXX","mac_address":"XX-XX-XX-XX-XX-XX","hostname":"XXXXXXXXXXXX","first_seen":"2021-01-12T16:01:43Z","last_seen":"2021-05-26T12:46:53Z","local_ip":"XXX.XXX.X.XX","major_version":"10","minor_version":"0","os_version":"Windows 10","platform_id":"0","platform_name":"Windows","policies":[{"policy_type":"prevention","policy_id":"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX","applied":true,"settings_hash":"71932dc2","assigned_date":"2021-02-05T10:17:18.181166503Z","applied_date":"2021-02-05T10:17:29.147610493Z","rule_groups":[]}],"reduced_functionality_mode":"no","device_policies":{"prevention":{"policy_type":"prevention","policy_id":"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX","applied":true,"settings_hash":"71932dc2","assigned_date":"2021-02-05T10:17:18.181166503Z","applied_date":"2021-02-05T10:17:29.147610493Z","rule_groups":[]},"sensor_update":{"policy_type":"sensor-update","policy_id":"XXXXXXXXXXXXXXXXXXXXXXXXXXX","applied":true,"settings_hash":"tagged|1;101","assigned_date":"2021-05-20T13:21:15.793890625Z","applied_date":"2021-05-20T13:23:10.339303233Z","uninstall_protection":"ENABLED"},"device_control":{"policy_type":"device-control","policy_id":"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX","applied":true,"assigned_date":"2021-01-12T16:05:30.418267934Z","applied_date":"2021-01-12T16:07:29.124988572Z"},"global_config":{"policy_type":"globalconfig","policy_id":"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX","applied":true,"settings_hash":"f61a5761","assigned_date":"2021-05-26T08:56:57.749380428Z","applied_date":"2021-05-26T08:57:09.08333925Z"},"remote_response":{"policy_type":"remote-response","policy_id":"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX","applied":true,"settings_hash":"XXXXXXX","assigned_date":"2021-01-12T16:05:30.418259588Z","applied_date":"2021-01-12T16:05:41.768614744Z"},"firewall":{"policy_type":"firewall","policy_id":"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX","applied":true,"assigned_date":"2021-01-12T16:05:30.41820681Z","applied_date":"2021-01-12T16:07:35.656641903Z","rule_set_id":"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"}},"groups":[],"group_hash":"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX","product_type":"1","product_type_desc":"Workstation","provision_status":"Provisioned","serial_number":"VMware-XX XX XX XX XX XX XX XX-XX XX XX XX XX XX XX XX","service_pack_major":"0","service_pack_minor":"0","pointer_size":"8","status":"contained","system_manufacturer":"VMware, Inc.","system_product_name":"VMware Virtual Platform","tags":[],"modified_timestamp":"2021-05-26T12:46:59Z","slow_changing_modified_timestamp":"2021-05-26T08:54:51Z","meta":{"version":"XXXXX"}}}
```



#### Get Hosts by IOC
DEPRECATED. List hosts related to the IOCs in Crowdstrike Falcon. Supported entities: Hostname, URL, IP address and Hash. Note: Hostname entities are treated as domain IOCs and action will extract domain part out of URLs. Only MD5 and SHA-256 hashes are supported.
Timeout - 600 Seconds



##### JSON Results
```json
{"hash": [{"modified_timestamp": "2019-01-17T13: 44: 57Z", "major_version": "10", "site_name": "Default-First-Site-Name", "platform_id": "0", "config_id_platform": "3", "system_manufacturer": "DellInc.", "meta": {"version": "49622"}, "first_seen": "2018-04-22T13: 06: 53Z", "service_pack_minor": "0", "product_type_desc": "Workstation", "build_number": "14393", "hostname": "name", "config_id_build": "8104", "minor_version": "0", "os_version": "Windows10", "provision_status": "Provisioned", "mac_address": "64-00-6a-2a-43-3f", "bios_version": "1.2.1", "agent_load_flags": "1", "status": "normal", "bios_manufacturer": "DellInc.", "machine_domain": "domain name", "device_policies": {"sensor_update": {"applied": true, "applied_date": "2018-12-11T23: 09: 18.071417837Z", "settings_hash": "65994753|3|2|automatic", "policy_type": "sensor-update", "assigned_date": "2018-12-11T23: 08: 38.16990705Z", "policy_id": "gdfgdghdhdhf53535"}}, "agent_local_time": "2019-01-14T19: 41: 09.738Z", "slow_changing_modified_timestamp": "2019-01-14T17: 44: 40Z", "service_pack_major": "0", "device_id": "2653595a063e4566519ef4fc813fcc56", "system_product_name": "OptiPlex7040", "product_type": "1", "local_ip": "1.1.1.1", "external_ip": "1.1.1.1", "cid": "27fe4e476ca3490b8476b2b6650e5a74", "platform_name": "Windows", "config_id_base": "65994753", "policies": [{"applied": true, "applied_date": "2019-01-02T22: 45: 21.315392338Z", "settings_hash": "18db1203", "policy_type": "prevention", "assigned_date": "2019-01-02T22: 45: 11.214774996Z", "policy_id": "7efdf97d7805402186b61151e8abd745"}], "last_seen": "2019-01-17T13: 44: 46Z", "pointer_size": "8", "agent_version": "4.18.8104.0"}]}
```



#### On-Demand Scan
Scan the endpoint on demand in Crowdstrike. Note: only Windows hosts are supported. Supported entities: IP Address, Hostname. Note: Action is running as async, please adjust script timeout value in Chronicle SecOps IDE for action, as needed.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Customer ID|Specify the ID of the customer for which you want to execute the action.||String||
|File Paths To Scan|Comma-separated list of paths to scan.|True|String||
|File Paths To Exclude From Scan|Comma-separated list of paths to exclude from scanning.||String||
|Host Group Name|Comma-separated list of host group names to initiate scanning for. Note: Separate scanning process is created for each host group.||String||
|Scan Description|Description for the scan. If no value is provided, the action sets the description to the following: "Scan initialized by Chronicle SecOps."||String||
|CPU Priority|The amount of CPU to  use for the underlying host during scanning.||List|Up to 25% CPU utilization|
|Sensor Anti-malware Detection Level|Specify the sensor anti-malware detection level. Note: Detection level must be equal to or higher than the Prevention level.||List|Moderate|
|Sensor Anti-malware Prevention Level|Specify the sensor anti-malware prevention level. Note: Detection level must be equal to or higher than the Prevention level.||List|Moderate|
|Cloud Anti-malware Detection Level|Specify the cloud anti-malware detection level. Note: Detection level must be equal to or higher than the Prevention level.||List|Moderate|
|Cloud Anti-malware Prevention Level|Specify the cloud anti-malware prevention level. Note: Detection level must be equal to or higher than the Prevention level.||List|Moderate|
|Quarantine Hosts|If enabled, underlying hosts are quarantined as part of scanning.||Boolean|false|
|Create Endpoint Notification|If enabled, the scanning process creates an endpoint notification.||Boolean|true|
|Max Scan Duration|Number of hours for a scan to run. If no value is provided, the scan runs continuously.||String|1|
|Hostname|Comma-separated list of hostnames on which you want to execute the action. Note: action will run the action on both entities + this parameter values.||String||



##### JSON Results
```json
[{"Entity": "ADCXXX", "EntityResult": [{"id": "10eaa473dbc94a348f1ee5e1d2b77xxx", "cid": "27fe4e476ca3490b8476b2b6650e5xxx", "profile_id": "9c78189ede704ced8f76b455dca20xxx", "description": "Scan initialized by Chronicle SecOps.", "file_paths": ["C:\\Windows"], "initiated_from": "falcon_adhoc", "cpu_priority": 2, "preemption_priority": 1, "metadata": [{"host_id": "86db81f390394cb080417a1ffb7d4xxx", "host_name": "ADCXXX", "host_scan_id": "308f4ac6bbf73643afc84e15df4ddxxx", "scan_host_metadata_id": "ec2ce10dd1f24b819140c79474b87xxx", "filecount": {"scanned": 17046, "malicious": 0, "quarantined": 0, "skipped": 134081, "traversed": 207957}, "status": "completed", "started_on": "2024-06-24T06:37:50.289634769Z", "completed_on": "2024-06-24T06:42:13.349949529Z", "last_updated": "2024-06-24T06:42:13.811079826Z"}], "filecount": {"scanned": 17046, "malicious": 0, "quarantined": 0, "skipped": 134081, "traversed": 207957}, "targeted_host_count": 1, "completed_host_count": 1, "status": "completed", "hosts": ["86db81f390394cb080417a1ffb7d4xxx"], "endpoint_notification": "true", "pause_duration": 2, "max_duration": 1, "max_file_size": 60, "sensor_ml_level_detection": 2, "sensor_ml_level_prevention": 2, "cloud_ml_level_detection": 2, "cloud_ml_level_prevention": 2, "policy_setting": [26439818674573, 26439818674574, 26439818675074, 26405458936702, 26405458936703, 26405458936707, 26439818675124, 26439818675125, 26439818675157, 26439818675158, 26439818675182, 26439818675183, 26439818675190, 26439818675191, 26439818675196, 26439818675197, 26439818675204, 26439818675205, 26405458936760, 26405458936761, 26405458936793, 26405458936794, 26405458936818, 26405458936819, 26405458936825, 26405458936826, 26405458936832, 26405458936833, 26405458936840, 26405458936841, 26456998543793, 26456998544045, 26456998543652, 26456998543653, 26456998543656, 26456998543654, 26456998543950, 26456998543963], "scan_started_on": "2024-06-24T06:37:50.289Z", "scan_completed_on": "2024-06-24T06:42:13.349Z", "created_on": "2024-06-24T06:37:47.044033931Z", "created_by": "38c5488700bd4741a75ba6a965843xxx", "last_updated": "2024-06-24T06:42:25.383373465Z"}]}]
```



#### Update Alert
Update an alert in Crowdstrike.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Alert ID|Specify the ID of the alert that needs to be updated.|True|String||
|Status|Specify the status for the alert.||List|Select One|
|Verdict|Specify the verdict for the alert.||List|Select One|
|Assign To|Specify the name of the analyst to whom the alert needs to be assigned. If "Unassign" is provided, action will remove assignment from the alert. Note: API will accept any value that is provided, even if the underlying user doesn’t exist.||String||



##### JSON Results
```json
[{"agent_id":"abcd","aggregate_id":"abcd","assigned_to_name":"anurags","cid":"xyz1234","cloud_indicator":"false","cmdline":"bashcrowdstrike_test_high","composite_id":":abcd","confidence":100,"context_timestamp":"2024-07-30T07:35:01.531Z","control_graph_id":"ctg:abcd","crawled_timestamp":"2024-07-30T07:40:06.744441898Z","created_timestamp":"2024-07-30T07:36:04.72770105Z","data_domains":["Endpoint"],"description":"Ahighleveldetectionwastriggeredonthisprocessfortestingpurposes.","device":{"agent_load_flags":"0","agent_local_time":"2024-01-04T23:40:57.736Z","agent_version":"7.06.16108.0","bios_manufacturer":"PhoenixTechnologiesLTD","bios_version":"6.00","cid":"abcd123","config_id_base":"65994753","config_id_build":"16108","config_id_platform":"8","device_id":"xyz","external_ip":"0.0.0.0","first_seen":"2023-06-14T10:50:40Z","groups":["9876"],"hostname":"abcd-sysops","last_seen":"2024-07-30T07:34:13Z","local_ip":"0.0.0.0","mac_address":"00-00-00-x0-00-00","major_version":"3","minor_version":"10","modified_timestamp":"2024-07-30T07:34:18Z","os_version":"CentOS7.9","ou":null,"platform_id":"3","platform_name":"Linux","pod_labels":null,"product_type_desc":"Server","status":"normal","system_manufacturer":"VMware,Inc.","system_product_name":"VMwareVirtualPlatform"},"display_name":"TestTriggerHigh","email_sent":true,"falcon_host_link":"https://falcon.crowdstrike.com/activity-v2/detections/27fe4e476ca3490b8476b2b6650e5a74:ind:2a1c5ef609ac479ba77f8ca5879c82fc:312465436839417-10304-1406208272?_cid=g03000sdn2nuopjvhx5iffjmntogcedi","filename":"bash","filepath":"/usr/bin/bash","global_prevalence":"common","grandparent_details":{"cmdline":"/usr/sbin/crond-n","filename":"crond","filepath":"/usr/sbin/crond","local_process_id":"17602","md5":"123lmnpo","process_graph_id":"pid:abcd","process_id":"00000000","sha256":"aabbccdd1234","timestamp":"2024-01-04T23:40:57.178Z","user_graph_id":"uid:00000000:abcd","user_name":"root"},"id":"abcd1234","indicator_id":"ind:00000abcd","ioc_context":[],"ioc_values":[],"local_prevalence":"unique","local_process_id":"9606","md5":"xyz0987","name":"DemoHighPattern","objective":"FalconDetectionMethod","parent_details":{"cmdline":"/bin/sh-c./alert.sh","filename":"bash","filepath":"/usr/bin/bash","local_process_id":"9604","md5":"xyz1234","process_graph_id":"pid:2a1c5ef609ac479ba77f8ca5879c82fc:312465432584345","process_id":"312465432584345","sha256":"00f8cbc5b3a6640af5ac18d01bc5a666f6f583b1379b9491e0bcc28ba78c92e9","timestamp":"2024-07-30T07:35:17Z","user_graph_id":"uid:2a1c5ef609ac479ba77f8ca5879c82fc:0","user_name":"root"},"parent_process_id":"000000","pattern_disposition":0,"pattern_disposition_description":"Detection,standarddetection.","pattern_disposition_details":{"blocking_unsupported_or_disabled":false,"bootup_safeguard_enabled":false,"containment_file_system":false,"critical_process_disabled":false,"detect":false,"fs_operation_blocked":false,"handle_operation_downgraded":false,"inddet_mask":false,"indicator":false,"kill_action_failed":false,"kill_parent":false,"kill_process":false,"kill_subprocess":false,"mfa_required":false,"operation_blocked":false,"policy_disabled":false,"prevention_provisioning_enabled":false,"process_blocked":false,"quarantine_file":false,"quarantine_machine":false,"registry_operation_blocked":false,"response_action_already_applied":false,"response_action_failed":false,"response_action_triggered":false,"rooting":false,"sensor_only":false,"suspend_parent":false,"suspend_process":false},"pattern_id":00000,"platform":"Linux","poly_id":"abcd==","process_end_time":"1722324901","process_id":"0000000","process_start_time":"1722324901","product":"epp","scenario":"suspicious_activity","seconds_to_resolved":168,"seconds_to_triaged":0,"severity":70,"severity_name":"High","sha1":"0000000000000000000000000000000000000000","sha256":"000000000000000","show_in_ui":true,"source_products":["FalconInsight"],"source_vendors":["CrowdStrike"],"status":"new","tactic":"FalconOverwatch","tactic_id":"CSTA0006","tags":["true_positive"],"technique":"MaliciousActivity","technique_id":"CST0002","template_instance_id":"1359","timestamp":"2024-07-30T07:35:02.101Z","tree_id":"2965447926650","tree_root":"312465436839417","triggering_process_graph_id":"pid:2a1c5ef609ac479ba77f8ca5879c82fc:312465436839417","type":"ldt","updated_timestamp":"2024-07-30T08:27:57.39990427Z","user_name":"root"}]
```



#### Get Host Information
Retrieve information about the hostname from Crowdstrike Falcon. Supported entities: Hostname, IP Address.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Customer ID|Specify the ID of the customer for which you want to execute the action.||String||
|Create Insight|If enabled, action will create insights containing information regarding entities.||Boolean|true|



##### JSON Results
```json
[{"EntityResult":[{"modified_timestamp":"2019-01-17T13: 44: 57Z","major_version":"10","site_name":"Default-First-Site-Name","platform_id":"0","config_id_platform":"3","system_manufacturer":"DellInc.","meta":{"version":"1111"},"first_seen":"2018-04-22T13: 06: 53Z","service_pack_minor":"0","product_type_desc":"Workstation","build_number":"111","hostname":"name","config_id_build":"8104","minor_version":"0","os_version":"Windows10","provision_status":"Provisioned","mac_address":"64-00-6a-2a-43-3f","bios_version":"1.2.1","agent_load_flags":"1","status":"normal","bios_manufacturer":"DellInc.","machine_domain":"Domain name","agent_local_time":"2019-01-14T19: 41: 09.738Z","slow_changing_modified_timestamp":"2019-01-14T17: 44: 40Z","service_pack_major":"0","device_id":"2653595a063e4566519ef4fc813xxxx","system_product_name":"OptiPlex7040","product_type":"1","local_ip":"1.1.x.x","external_ip":"1.1.x.x","cid":"27fe4e476ca3490b8476b2b66xxxx","platform_name":"Windows","config_id_base":"65994753","last_seen":"2019-01-17T13: 44: 46Z","pointer_size":"8","agent_version":"4.18.8104.0","recent_logins":[{"user_name":"test","login_time":"2022-08-10T07:36:38Z"},{"user_name":"test","login_time":"2022-08-10T07:36:35Z"}],"online_status":"offline"}],"Entity":"1.1.x.x"}]
```



#### Lift Contained Endpoint
Lift endpoint containment in Crowdstrike Falcon. Supported entities: Hostname and IP address.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Customer ID|Specify the ID of the customer for which you want to execute the action.||String||
|Fail If Timeout|If enabled, action will be failed, if containment was not lifted on all endpoints.||Boolean|true|



##### JSON Results
```json
{"Entity":"XXX.XXX.XXX","EntityResult":{"device_id":"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX","cid":"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX","agent_load_flags":"1","agent_local_time":"2021-05-26T11:54:38.105Z","agent_version":"X.XXX.XXX.0","bios_manufacturer":"Phoenix Technologies LTD","bios_version":"6.00","build_number":"XXXX","config_id_base":"XXXX","config_id_build":"XXXX","config_id_platform":"3","cpu_signature":"XXXXX","external_ip":"XXX.XXX.XXX.XXX","mac_address":"XX-XX-XX-XX-XX-XX","hostname":"XXXXXXXXXXXX","first_seen":"2021-01-12T16:01:43Z","last_seen":"2021-05-26T12:46:53Z","local_ip":"XXX.XXX.X.XX","major_version":"10","minor_version":"0","os_version":"Windows 10","platform_id":"0","platform_name":"Windows","policies":[{"policy_type":"prevention","policy_id":"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX","applied":true,"settings_hash":"71932dc2","assigned_date":"2021-02-05T10:17:18.181166503Z","applied_date":"2021-02-05T10:17:29.147610493Z","rule_groups":[]}],"reduced_functionality_mode":"no","device_policies":{"prevention":{"policy_type":"prevention","policy_id":"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX","applied":true,"settings_hash":"71932dc2","assigned_date":"2021-02-05T10:17:18.181166503Z","applied_date":"2021-02-05T10:17:29.147610493Z","rule_groups":[]},"sensor_update":{"policy_type":"sensor-update","policy_id":"XXXXXXXXXXXXXXXXXXXXXXXXXXX","applied":true,"settings_hash":"tagged|1;101","assigned_date":"2021-05-20T13:21:15.793890625Z","applied_date":"2021-05-20T13:23:10.339303233Z","uninstall_protection":"ENABLED"},"device_control":{"policy_type":"device-control","policy_id":"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX","applied":true,"assigned_date":"2021-01-12T16:05:30.418267934Z","applied_date":"2021-01-12T16:07:29.124988572Z"},"global_config":{"policy_type":"globalconfig","policy_id":"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX","applied":true,"settings_hash":"f61a5761","assigned_date":"2021-05-26T08:56:57.749380428Z","applied_date":"2021-05-26T08:57:09.08333925Z"},"remote_response":{"policy_type":"remote-response","policy_id":"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX","applied":true,"settings_hash":"XXXXXXX","assigned_date":"2021-01-12T16:05:30.418259588Z","applied_date":"2021-01-12T16:05:41.768614744Z"},"firewall":{"policy_type":"firewall","policy_id":"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX","applied":true,"assigned_date":"2021-01-12T16:05:30.41820681Z","applied_date":"2021-01-12T16:07:35.656641903Z","rule_set_id":"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"}},"groups":[],"group_hash":"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX","product_type":"1","product_type_desc":"Workstation","provision_status":"Provisioned","serial_number":"VMware-XX XX XX XX XX XX XX XX-XX XX XX XX XX XX XX XX","service_pack_major":"0","service_pack_minor":"0","pointer_size":"8","status":"normal","system_manufacturer":"VMware, Inc.","system_product_name":"VMware Virtual Platform","tags":[],"modified_timestamp":"2021-05-26T12:46:59Z","slow_changing_modified_timestamp":"2021-05-26T08:54:51Z","meta":{"version":"XXXXX"}}}
```



#### Hide Hosts
Use the Hide Hosts action to hide one or more hosts from the CrowdStrike Falcon console. Supported entities: IP Address, Hostname.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Hostname|A comma-separated list of hostnames to hide in CrowdStrike Falcon. The action processes both the input values provided in this parameter and the Hostname and IP Address entities attached to the case.||String||
|Customer ID|The unique CrowdStrike Customer ID (CID) used to target a specific tenant. This parameter is required in Falcon Flight Control or multi-tenant environments to perform the action on a specific child CID.||String||



##### JSON Results
```json
[{"Entity":"XXX.XXX.XXX","EntityResult":{"device_id":"a1b2c3d4e5f67890a1b2c3d4e5f6xxxx","cid":"0987654321fedcba0987654321fexxxx","agent_load_flags":"16","agent_local_time":"2026-03-01T10:00:00.000Z","agent_version":"8.1.20501.0","bios_manufacturer":"Dell Inc.","bios_version":"1.15.0","build_number":"19xxx","config_id_base":"7599xxxx","config_id_build":"20xxx","config_id_platform":"3","cpu_signature":"456xxx","cpu_vendor":"0","external_ip":"xxx.xxx.xxx.xxx","mac_address":"00-1A-2B-3C-XX-XX","hostname":"FINANCE-PC-xx","host_hidden_status":"visible","filesystem_containment_status":"normal","first_seen":"2025-11-15T08:30:00Z","last_seen":"2026-03-01T09:55:10Z","local_ip":"192.168.1.xxx","machine_domain":"example.corp","major_version":"10","minor_version":"0","os_version":"Windows 11","os_build":"22xxx","platform_id":"0","platform_name":"Windows"}}]
```



#### Ping
Test Connectivity
Timeout - 600 Seconds



#### Run Script
Execute a powershell script on the endpoints in Crowdstrike. Supported entities: IP Address, Hostname. Note: Action is running as async, please adjust script timeout value in Google SecOps IDE for the action, as needed.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Customer ID|Specify the ID of the customer for which you want to execute the action.||String||
|Script Name|The name of the script file that needs to be executed. Note: either “Script Name” or “Raw Script” should be provided. If both “Script Name” and “Raw Script” are provided, then “Raw Script” will have the priority.||String||
|Raw Script|Raw powershell script payload that needs to be executed on the endpoints. Note: either “Script Name” or “Raw Script” should be provided. If both “Script Name” and “Raw Script” are provided, then “Raw Script” will have the priority.||String||
|Hostname|Comma-separated list of hostnames on which you want to execute the action. Note: action will run the action on both entities + this parameter values.||String||
|Queue Offline|If enabled, commands targeting offline hosts are queued and executed once the host reconnects to the network.||Boolean|false|



##### JSON Results
```json
{"Entity":"XXX.XXX.XXX","EntityResult":{"session_id":"2a066818-XXXX-XXXX-XXXX-c295ed7295b3","task_id":"84846f59-XXXX-XXXX-XXXX-12af4af88a8b","complete":true,"stdout":"","stderr":"","base_command":"get"}}
```



#### Get Event Offset
Action will retrieve the event offset that is used by the Event Streaming Connector. Note: action starts processing events from 30 days ago.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Max Events To Process|Specify how many events the action needs to process starting from the offset from 30 days ago.|True|String|10000|



##### JSON Results
```json
{"offset":100000,"timestamp":1627634506826}
```



#### Get Process Name By IOC
DEPRECATED. Retrieve processes related to the IOCs and provided devices in Crowdstrike Falcon. Supported entities: Hostname, URL, IP address and Hash. Note: Hostname entities are treated as domain IOCs and action will extract domain part out of URLs. Only MD5 and SHA-256 hashes are supported. IP address entities are treated as IOCs.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Devices Names|Specify a comma-separated list of devices for which you want to retrieve processes related to entities.|True|String||



##### JSON Results
```json
{"EntityResult": [{"device_id":"74089e3XXXXa4271ab14abXXXXXd18eb","command_line":"\\C:\\\\TMP\\\\mim.exe\\","process_id":"74089e3XXXXa4271ab14abXXXXXd18eb:400084000045","process_id_local":"400084000045","file_name":"\\\\Device\\\\HarddiskVolume2\\\\TMP\\\\mim.exe","start_timestamp":"2021-05-21T06:05:10Z","start_timestamp_raw":"132660507103371800","stop_timestamp":"2021-05-21T06:05:26Z","stop_timestamp_raw":"132660507260335807"},{"device_id":"74089e3XXXXa4271ab14abXXXXXd18eb","command_line":"C:\\\\TMP\\\\mim.exe\\","process_id":"74089e3XXXXa4271ab14abXXXXXd18eb:000029753080","process_id_local":"000029753080","file_name":"\\\\Device\\\\HarddiskVolume2\\\\TMP\\\\mim.exe","start_timestamp":"2021-05-21T06:07:15Z","start_timestamp_raw":"132660508352040249","stop_timestamp":"2021-05-21T06:07:21Z","stop_timestamp_raw":"132660508418773254"},{"device_id":"74089e3XXXXa4271ab14abXXXXXd18eb","command_line":"\\C:\\\\TMP\\\\mim.exe\\","process_id":"74089e3XXXXa4271ab14abXXXXXd18eb:000021388856","process_id_local":"000021388856","file_name":"\\\\Device\\\\HarddiskVolume2\\\\TMP\\\\mim.exe","start_timestamp":"2021-05-21T05:53:03Z","start_timestamp_raw":"132660499835265266","stop_timestamp":"2021-05-21T05:53:25Z","stop_timestamp_raw":"132660500056273239"},{"device_id":"74089e3XXXXa4271ab14abXXXXXd18eb","command_line":"\\C:\\\\TMP\\\\mim.exe\\","process_id":"74089e3XXXXa4271ab14abXXXXXd18eb:0000310768731","process_id_local":"000010768731","file_name":"\\\\Device\\\\HarddiskVolume2\\\\TMP\\\\mim.exe","start_timestamp":"2021-05-21T05:47:59Z","start_timestamp_raw":"132660496793281001","stop_timestamp":"2021-05-21T05:48:00Z","stop_timestamp_raw":"132660496807679553"}], "Entity": "f8f1c210a8c863efc0f6b8ac3553030a14a702ce8cf573cb5e9cd58f70c7c622"}
```



#### Search Events
Search events in Crowdstrike. Note: Action is running as async, please adjust script timeout value in Google SecOps IDE for action, as needed.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Repository|Repository that should be searched.|True|List|All|
|Query|Query that needs to be executed in Crowdstrike. Note: don't provide "head" as part of the query. Action will provide it automatically based on the value provided in the "Max Results To Return" parameter.|True|String||
|Time Frame|Time frame for the results. If "Custom" is selected, you also need to provide "Start Time".||List|Last Hour|
|Start Time|Start time for the results. This parameter is mandatory, if "Custom" is selected for the "Time Frame" parameter. Format: ISO 8601.||String||
|End Time|End time for the results. Format: ISO 8601. If nothing is provided and "Custom" is selected for the "Time Frame" parameter then this parameter will use current time.||String||
|Max Results To Return|How many results to return for the query. Action will append "head" to the provided query. Default: 50. Maximum: 1000.||String|50|



##### JSON Results
```json
{"events": [{"eid": "118", "AuditKeyValues[8].Key": "elapsed_time", "AuditKeyValues[12].ValueString": "201", "UserIp": "1.1.1.1", "AuditKeyValues[14].ValueString": "test", "AuditKeyValues[3].ValueString": "application/x-www-form-urlencoded", "@timezone": "Z", "Message": "", "@rawstring": "{}", "AuditKeyValues[9].ValueString": "[application/json]", "AuditKeyValues[0].Key": "received_time", "Attributes.request_content_type": "application/x-www-form-urlencoded", "@timestamp": 1745319167000, "@ingesttimestamp": "1745319168954", "Attributes.request_accept": "*/*", "AuditKeyValues[9].Key": "produces", "Attributes.elapsed_microseconds": "97465", "Attributes.received_time": "2025-04-22T10:52:47.020550693Z", "ServiceName": "api_request", "#type": "falcon-raw-data", "Attributes.request_uri_length": "13", "Attributes.status_code": "201", "timestamp": "2025-04-22T10:52:47Z", "AuditKeyValues[7].Key": "request_path", "CustomerIdString": "test", "Attributes.trace_id": "test", "AuditKeyValues[14].Key": "trace_id", "AuditKeyValues[6].ValueString": "test", "AgentIdString": "", "Attributes.produces": "[application/json]", "Attributes.request_method": "POST", "Attributes.user_ip": "1.1.1.1", "AuditKeyValues[4].Key": "user_agent", "#repo": "detections", "Attributes.cid": "test", "EventType": "Event_ExternalApiEvent", "#repo.cid": "test", "#event_simpleName": "Event_AuthActivityAuditEvent", "SourceIp": "1.1.1.1", "AuditKeyValues[8].ValueString": "97.465879ms", "@sourcetype": "xdr/xdr-base-parsers:falcon-raw-data", "Attributes.elapsed_time": "97.465879ms", "AuditKeyValues[13].Key": "elapsed_microseconds", "AuditKeyValues[2].Key": "consumes", "AuditKeyValues[7].ValueString": "/oauth2/token", "cid": "test", "AuditKeyValues[5].ValueString": "1.1.1.1", "AuditKeyValues[15].Key": "request_accept", "Source": "api_request", "Attributes.request_path": "/oauth2/token", "AuditKeyValues[11].Key": "request_uri_length", "AuditKeyValues[4].ValueString": "python-requests/2.28.2", "Attributes.APIClientID": "test", "AuditKeyValues[13].ValueString": "97465", "AuditKeyValues[6].Key": "APIClientID", "AuditKeyValues[15].ValueString": "*/*", "OperationName": "logged", "UTCTimestamp": "1745319167", "Attributes.consumes": "[application/x-www-form-urlencoded text/html]", "@source": "PlatformEvents", "UserId": "", "AuditKeyValues[12].Key": "status_code", "Nonce": "1", "@timestamp.nanos": "0", "AuditKeyValues[10].Key": "request_method", "Success": "true", "ExternalApiType": "Event_AuthActivityAuditEvent", "AuditKeyValues[1].Key": "cid", "AuditKeyValues[10].ValueString": "POST", "AuditKeyValues[2].ValueString": "[application/x-www-form-urlencoded text/html]", "AuditKeyValues[11].ValueString": "13", "AuditKeyValues[3].Key": "request_content_type", "AuditKeyValues[0].ValueString": "2025-04-22T10:52:47.020550693Z", "Attributes.user_agent": "python-requests/2.28.2", "AuditKeyValues[5].Key": "user_ip", "AuditKeyValues[1].ValueString": "test", "@id": "test"},{"timestamp": "1744958227655", "ImageSubsystem": "2", "RawProcessId": "2276", "ParentProcessId": "123434", "@sourcetype": "xdr/xdr-base-parsers:falcon-raw-data", "@timezone": "Z", "Tags": "test", "ParentBaseFileName": "services.exe", "Entitlements": "15", "@id": "test", "LocalAddressIP4": "1.1.1.1", "@ingesttimestamp": "1744958230195", "aip": "1.1.1.1", "@timestamp": 1744958227655, "LocalIP": "1.1.1.1", "name": "ProcessRollup2V19", "UserName": "test", "#type": "falcon-raw-data", "SessionId": "0", "SourceThreadId": "294601313697", "aid": "test", "ProcessParameterFlags": "8193", "ProcessStartTime": "1744958226.246", "SHA1HashData": "test", "ConfigStateHash": "734988097", "WindowFlags": "128", "ImageFileName": "test", "UserSid": "S-1-5-18", "#repo": "base_sensor", "EffectiveTransmissionClass": "3", "EventOrigin": "1", "ProcessSxsFlags": "64", "ComputerName": "test", "#repo.cid": "test", "FilePath": "test", "#event_simpleName": "ProcessRollup2", "ParentAuthenticationId": "999", "event_platform": "Win", "ProcessEndTime": "", "id": "test", "cid": "test", "SourceProcessId": "25780621399", "SignInfoFlags": "9175042", "Agent IP": "1.1.1.1", "FileName": "svchost.exe", "Tactic": "Execution", "TargetProcessId": "39296068781", "CommandLine": "test", "TokenType": "2", "ProcessCreateFlags": "525324", "@source": "PlatformEvents", "AuthenticodeHashData": "test", "SHA256HashData": "test", "MD5HashData": "test", "AuthenticationId": "999", "@timestamp.nanos": "0", "IntegrityLevel": "16384", "ConfigBuild": "122345", "Technique": "System Services", "@rawstring": "raw_string"}]}
```



#### List Host Vulnerabilities
List vulnerabilities found on the host in Crowdstrike Falcon. Supported entities: IP Address and Hostname. Note: requires Falcon Spotlight license and permissions. 
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Customer ID|Specify the ID of the customer for which you want to execute the action.||String||
|Severity Filter|Specify the comma-separated list of severities for vulnerabilities.If nothing is provided, action will ingest all related vulnerabilities. Possible values: Critical, High, Medium, Low, Unknown.||String||
|Create Insight|If enabled, action will create an insight per entity containing statistical information about related vulnerabilities.||Boolean|true|
|Max Vulnerabilities To Return|Specify how many vulnerabilities to return per host. If nothing is provided action will process all of the related vulnerabilities.||String|100|



##### JSON Results
```json
{"Entity":"XXX.XXX.XXX","EntityResult": {"statistics":{"total":123,"severity":{"critical":1,"high":1,"medium":1,"low":1,"unknown":1},"status":{"open":1,"reopened":1},"total_available_remediations":1},"details":[{"id":"74089e36ac3XXXXXab14abc076ed18eb_fff6dXXXXXX7352babdf7c7d240749e7","cid":"27fe4e476cXXXXXX8476b2b6650e5a74","aid":"74089e36acXXXXXXab14abc076ed18eb","created_timestamp":"2021-05-12T22:45:47Z","updated_timestamp":"2021-05-12T22:45:47Z","status":"open","cve":{"id":"CVE-2021-28476","base_score":9.9,"severity":"CRITICAL","exploit_status":0},"app":{"product_name_version":"Windows Windows 10"},"apps":[{"product_name_version":"Windows Windows 10","sub_status":"open","remediation":{"ids":["acc34cd461023ffXXXXX420fa8839365"]}}],"host_info":{"hostname":"CROWDSTRIKE-H01","local_ip":"172.30.202.33","machine_domain":"","os_version":"Windows 10","ou":"","site_name":"","system_manufacturer":"VMware, Inc.","groups":[],"tags":[],"platform":"Windows"},"remediation":[{"id":"acc34cd461023ffXXXXX420fa8839365","reference":"KB5003169","title":"Update Microsoft Windows 10 1909","action":"Install patch for Microsoft Windows 10 1909 x64 (Workstation): Security Update KB5003169","link":"https://catalog.update.microsoft.com/v7/site/Search.aspx?q=KB5003169"}]}]}}
```



#### Submit URL
Submit urls to a sandbox in Crowdstrike. Note: This action requires a Falcon Sandbox license.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|URLs|Specify the URLs that need to be submitted.|True|String||
|Sandbox Environment|Specify the sandbox environment for the analysis.||List|Windows 10, 64-bit|
|Network Environment|Specify the network environment for the analysis.||List|Default|
|Check Duplicate|If enabled, the action checks if the file was already submitted previously and returns an available report. Note: during the validation “Network Environment” and “Sandbox Environment” are not taken into consideration.||Boolean|true|



##### JSON Results
```json
[{"Entity": "https://www.google.com", "EntityResult": [{"id": "27fe4e476ca3490b8476b2b6650e5a74_aa14936582d941fda1441fcc47a65d86", "cid": "27fe4e476ca3490b8476b2b6650e5a74", "created_timestamp": "2023-04-28T12:01:51Z", "origin": "apigateway", "sandbox": [{"sha256": "15fea7cc23194aea10dce58cff8fff050c81e1be0d16e4da542f4fedd5a421c3", "environment_id": 160, "environment_description": "Windows 10 64 bit", "submit_url": "hxxps://www.google.com", "submission_type": "page_url", "verdict": "no specific threat", "incidents": [{"name": "Network Behavior", "details": ["Contacts 3 domains and 3 hosts"]}], "sample_flags": ["Network Traffic", "Extracted Files"], "network_settings": "default"}], "verdict": "no specific threat", "ioc_report_strict_csv_artifact_id": "6fb809c85f671f754f9af8ef345e1db2c432ed8a4638197a187f5b23c6c0388e", "ioc_report_broad_csv_artifact_id": "4149f8276272bc8f0cbf485aff5969d24dcdca62b28bf90432186e2db7e82e24", "ioc_report_strict_json_artifact_id": "d3b00b1fb18996afe15960c30ce226052f7d6901bd43a180764bfd020ca119da", "ioc_report_broad_json_artifact_id": "6d3bef8ddf0513bf009ffa36d0fb169627c73eddca9404dbe9ea75fb6ad454e5", "ioc_report_strict_stix_artifact_id": "5b05d9fe2b7d0baa7cc005fca234c8eebd3b8ae899776ec7be882cedfcbbb0b3", "ioc_report_broad_stix_artifact_id": "45b4cdd9a4316a91f764c09b14f9cbde04ffc87e0730e2df86c8d4c57a0a77ec", "ioc_report_strict_maec_artifact_id": "3f5a7636feaf55492ae2cb8315d821fc1a89a5ebc108056a1905fb66019f35a2", "ioc_report_broad_maec_artifact_id": "7e8db3819b3a4a0bbb62b545cf14b18d090934eeed160d04007bbcb00f3290cc"}]}]
```



#### Submit File
Submit files to a sandbox in Crowdstrike. Note: This action requires a Falcon Sandbox license. For the list of supported file formats, refer to the documentation portal.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|File Paths|Specify the file paths to the files that need to be submitted. Refer to the documentation portal for a list of the supported file formats.|True|String||
|Sandbox Environment|Specify the sandbox environment for the analysis.||List|Windows 10, 64-bit|
|Network Environment|Specify the network environment for the analysis.||List|Default|
|Archive Password|Specify the password that would need to be used, when working with archive files.||Password|*****|
|Document Password|Specify the password that would need to be used, when working with Adobe or Office files. Maximum: 32 characters.||Password|*****|
|Check Duplicate|If enabled, the action checks if the file was already submitted previously and returns the available report. Note: during the validation “Network Environment” and “Sandbox Environment” are not taken into consideration.||Boolean|true|
|Comment|Specify the comment for the submission.||String||
|Confidential Submission|If enabled, the file is only shown to users within your customer account.||Boolean|false|



##### JSON Results
```json
[{"Entity": "/test1.pdf", "EntityResult": [{"id": "27fe4e476ca3490b8476b2b6650e5a74_8b43a4c9d5ea4306af4e827b6901cd60", "cid": "27fe4e476ca3490b8476b2b6650e5a74", "created_timestamp": "2023-04-28T14:00:00Z", "origin": "apigateway", "sandbox": [{"sha256": "8decc8571946d4cd70a024949e033a2a2a54377fe9f1c1b944c20f9ee11a9e51", "environment_id": 160, "environment_description": "Windows 10 64 bit", "submit_name": "test1.pdf", "submission_type": "file", "verdict": "no specific threat", "file_type": "PDF document, version 1.3", "sample_flags": ["Extracted Files"], "network_settings": "default"}], "verdict": "whitelisted", "ioc_report_strict_csv_artifact_id": "ded2c6801f51b43ba4b6de371188960239e84d227a16f065b6b96404854f27d4", "ioc_report_broad_csv_artifact_id": "ded2c6801f51b43ba4b6de371188960239e84d227a16f065b6b96404854f27d4", "ioc_report_strict_json_artifact_id": "9a659092e0dc2ea6b57254eed04af5012267fb2c8990b277492fe172dfa86bf2", "ioc_report_broad_json_artifact_id": "9a659092e0dc2ea6b57254eed04af5012267fb2c8990b277492fe172dfa86bf2", "ioc_report_strict_stix_artifact_id": "fa98bc61b6e62837dbff2a7c34e0e3cee3e90ff277bed059b634d806bcdad726", "ioc_report_broad_stix_artifact_id": "fa98bc61b6e62837dbff2a7c34e0e3cee3e90ff277bed059b634d806bcdad726", "ioc_report_strict_maec_artifact_id": "cf12de7c8249dd80dc9e9591d964b13aa18b9b4a292a4ec3c9f58e7b1ff1d50d", "ioc_report_broad_maec_artifact_id": "cf12de7c8249dd80dc9e9591d964b13aa18b9b4a292a4ec3c9f58e7b1ff1d50d"}]}]
```



#### Update Detection
Deprecated. Update detection in Crowdstrike Falcon.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Detection ID|Specify the ID of the detection that needs to be updated.|True|String||
|Status|Specify the new status for the detection.|True|List||
|Assign Detection to|Specify the email address of the Crowdstrike Falcon user, who needs to be assigned to this detection||String||



#### Update IOC Information
Update information about custom IOCs in Crowdstrike Falcon. Supported entities: Hostname, URL, IP address and Hash. Note: Hostname entities are treated as domain IOCs and action will extract domain part out of URLs. Only MD5 and SHA-256 hashes are supported.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Description|Specify a new description for custom IOCs.||Content||
|Source|Specify the source for custom IOCs.||Content||
|Expiration days|Specify the amount of days till expiration.||String||
|Detect policy|If enabled, IOCs that have been identifed, will send a notification. In other case, no action will be taken||Boolean||



##### JSON Results
```json
[{"Entity":"69630e4574ec6798239b09xxxxxxxxxx","EntityResult":{"id":"1cbca683ca9575609567419287aa92fba40f3ffee8badf6738f2c1xxxxxxxxxx","type":"md5","value":"69630e4574ec6798239b09xxxxxxxxxx","source":"test","action":"no_action","severity":"","description":"test","platforms":["windows","mac","linux"],"tags":["a7829d13-1d10-4126-9970-60xxxxxxxxxx"],"expiration":"2021-10-19T13:04:22Z","expired":false,"deleted":false,"applied_globally":true,"from_parent":false,"created_on":"2019-04-29T07:15:48Z","created_by":"","modified_on":"2021-10-14T13:04:23.666091115Z","modified_by":"7fff03c3227242a0bae84bxxxxxxxxxx"}},{"Entity":"908b64b1971a979c7e3e8ce4621945cba84854cb98d76367b791a6xxxxxxxxxx","EntityResult":{"id":"6b2987ace3c0f5dbfa5414fa13e7302bc61cca5a5db6cde8e1d135xxxxxxxxxx","type":"sha256","value":"908b64b1971a979c7e3e8ce4621945cba84854cb98d76367b791a6xxxxxxxxxx","source":"test","action":"detect","severity":"medium","description":"test","metadata":{"company_name":"Microsoft Corporation","original_filename":"PowerShell.EXE","file_version":"10.0.18362.1 (WinBuild.160101.0800)","file_description":"Windows PowerShell","product_name":"Microsoft® Windows® Operating System","product_version":"10.0.18362.1","signed":false,"av_hits":0},"platforms":["windows","mac","linux"],"tags":["f09f1a25-e6d0-4709-a105-05xxxxxxxxxx"],"expiration":"2021-10-19T13:04:26Z","expired":false,"deleted":false,"applied_globally":true,"from_parent":false,"created_on":"2021-02-15T11:36:58Z","created_by":"","modified_on":"2021-10-14T13:04:28.074605009Z","modified_by":"7fff03c3227242a0bae84bxxxxxxxxxx"}}]
```



#### Get Alert Details
Get details of an alert in Crowdstrike.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Alert ID|Specify the ID of the alert.|True|String||



##### JSON Results
```json
{"agent_id":"cc","aggregate_id":"cc","cid":"27fe4e476ca3490b8476b2b6650e5a74","cloud_indicator":"false","cmdline":"bashcrowdstrike_test_low","composite_id":"cc","confidence":100,"context_timestamp":"2025-09-19T06:39:01.295Z","control_graph_id":"ccc","crawled_timestamp":"2025-09-19T07:39:03.206707502Z","created_timestamp":"2025-09-19T06:40:03.130645734Z","data_domains":["Endpoint"],"description":"Alowleveldetectionwastriggeredonthisprocessfortestingpurposes.","device":{"agent_load_flags":"0","agent_local_time":"2025-09-09T15:37:16.410Z","agent_version":"7.28.18108.0","bios_manufacturer":"ssLTD","bios_version":"6.00","cid":"cc","config_id_base":"65994767","config_id_build":"18108","config_id_platform":"8","device_id":"cc","external_ip":"34.159.51.108","first_seen":"2023-06-14T10:50:40Z","groups":["cc"],"hostinfo":{"domain":""},"hostname":"npatni-sysops","last_seen":"2025-09-19T07:37:26Z","local_ip":"172.30.3.72","mac_address":"00-50-56-b6-34-86","machine_domain":"","major_version":"3","minor_version":"10","modified_timestamp":"2025-09-19T07:37:35Z","os_version":"CentOS7.9","ou":null,"platform_id":"3","platform_name":"Linux","product_type_desc":"Server","status":"normal","system_manufacturer":"VMware,Inc.","system_product_name":"VMwareVirtualPlatform"},"display_name":"TestTriggerLow","email_sent":true,"falcon_host_link":"https://abc.com","filename":"bash","filepath":"/usr/bin/bash","global_prevalence":"common","grandparent_details":{"cmdline":"/usr/sbin/crond-n","filename":"crond","filepath":"/usr/sbin/crond","local_process_id":"836","md5":"cc","process_graph_id":"cc","process_id":"cc","sha256":"cc","timestamp":"1601-01-01T00:00:00.000Z","user_graph_id":"ui0","user_name":"root"},"id":"icc","indicator_id":"cc","ioc_context":[],"local_prevalence":"unique","local_process_id":"16948","md5":"cc","mitre_attack":[{"pattern_id":10306,"tactic_id":"cc","technique_id":"cc","tactic":"cc","technique":"MaliciousActivity"}],"name":"DemoLowPattern","objective":"FalconDetectionMethod","parent_details":{"cmdline":"/bin/sh-c./alert.sh","filename":"bash","filepath":"/usr/bin/bash","local_process_id":"16943","md5":"xx","process_graph_id":"cc","process_id":"cc","sha256":"cc","timestamp":"2025-09-19T06:39:47Z","user_graph_id":"cc","user_name":"root"},"parent_process_id":"cc","pattern_disposition":0,"pattern_disposition_description":"ccc","pattern_disposition_details":{"blocking_unsupported_or_disabled":false,"bootup_safeguard_enabled":false,"containment_file_system":false,"critical_process_disabled":false,"detect":false,"fs_operation_blocked":false,"handle_operation_downgraded":false,"inddet_mask":false,"indicator":false,"kill_action_failed":false,"kill_parent":false,"kill_process":false,"kill_subprocess":false,"mfa_required":false,"operation_blocked":false,"policy_disabled":false,"prevention_provisioning_enabled":false,"process_blocked":false,"quarantine_file":false,"quarantine_machine":false,"registry_operation_blocked":false,"response_action_already_applied":false,"response_action_failed":false,"response_action_triggered":false,"rooting":false,"sensor_only":false,"suspend_parent":false,"suspend_process":false},"pattern_id":10306,"platform":"Linux","poly_id":"ccc","priority_explanation":["[MOD]Theseverityofthedetection"],"priority_value":40,"process_end_time":"1758263941","process_id":"cc","process_start_time":"1758263941","product":"epp","scenario":"suspicious_activity","seconds_to_resolved":0,"seconds_to_triaged":0,"severity":30,"severity_name":"Low","sha1":"cc","sha256":"xx","show_in_ui":true,"source_products":["FalconInsight"],"source_vendors":["CrowdStrike"],"status":"new","tactic":"cc","tactic_id":"CSTA0006","technique":"MaliciousActivity","technique_id":"CST0002","template_instance_id":"1357","timestamp":"2025-09-19T06:39:01.842Z","tree_id":"cc","tree_root":"","triggering_process_graph_id":"ccc","type":"ldt","updated_timestamp":"2025-09-19T07:39:03.206700216Z","user_name":"root"}
```



#### Update Identity Protection Detection
Update an identity protection detection in Crowdstrike. Note: this action requires an Identity Protection license.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Detection ID|Specify the ID of the detection that needs to be updated.|True|String||
|Status|Specify the status for the detection.||List|Select One|
|Assign To|Specify the name of the analyst to whom the detection needs to be assigned. If "Unassign" is provided, action will remove assignment from the detection. Note: API will accept any value that is provided, even if the underlying user doesn't exist.||String||



##### JSON Results
```json
{"added_privileges":["DomainAdminsRole"],"aggregate_id":"aggind:27fe4e476ca3490b8476b2xxxxx:xxxxxxxx-xxxx-xxxx-xxxx-4ED8DB047549","cid":"27fxxxxxxxxxxxxxxxxxxxxxa74","composite_id":"27fe4e4xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-4ED8DB047549","confidence":20,"context_timestamp":"2022-11-15T12:58:15.629Z","crawl_edge_ids":{"Sensor":["N6KIxxxxxxxxxCA4lr/"]},"crawl_vertex_ids":{"Sensor":["ind:27fe4e47xxxxxxxxxxxxxxxxxxxxxxxxxxxx4ED8DB047549"]},"crawled_timestamp":"2022-11-15T13:58:17.251061883Z","created_timestamp":"2022-11-15T12:59:17.239585706Z","description":"A user received new privileges","display_name":"Privilege escalation (user)","end_time":"2022-11-15T12:58:15.629Z","falcon_host_link":"https://falcon.crowdstrike.com/identity-protection/detections/nd:27fe4e476caxxxxxxxxxxxxxxxxxxxxxxxxxxxxED8DB047549","id":"ind:27fe4e476caxxxxxxxxxxxxxxxxxxxxxxxxxxxxED8DB047549","name":"IdpEntityPrivilegeEscalationUser","objective":"Gain Access","pattern_id":51113,"previous_privileges":"0","privileges":"8321","product":"idp","scenario":"privilege_escalation","severity":2,"show_in_ui":true,"source_account_domain":"test","source_account_name":"Mailbox438","source_account_object_sid":"S-1-5-21-3479765008-4256118348-3151044947-3595","start_time":"2022-11-15T12:58:15.629Z","status":"new","tactic":"Privilege Escalation","tactic_id":"TA0xxx","tags":["red_team"],"technique":"Valid Accounts","technique_id":"Txxx8","timestamp":"2022-11-15T12:58:17.239Z","type":"idp-user-endpoint-app-info","updated_timestamp":"2023-03-03T10:24:48.744735285Z"}
```



#### Upload IOCs
Add custom IOCs in Crowdstrike Falcon. Supported entities: Hostname, URL, IP address and Hash. Note: Hostname entities are treated as domain IOCs and action will extract domain part out of URLs. Only MD5 and SHA-256 hashes are supported.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Comment|Specify a comment with more context related to IOC.||String||
|Host Group Name|Specify the name of the host group.||String||
|Action|Specify the action for the uploaded IOCs. Note: "Block" action can only be applied to hashes. Action will always apply "Detect" policy to all other IOC types.||List|Detect|
|Days To Expire|The number of days before the IOC expires.||String||
|Platform|Specify a comma-separated list of the platforms related to the IOC. Possible values: Windows, Linux, Mac.|True|String|Windows,Linux,Mac|
|Severity|Specify the severity for the IOC.|True|List|Medium|



#### Update Incident
Deprecated. Update incident in Crowdstrike.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Customer ID|Specify the ID of the customer for which you want to execute the action.||String||
|Incident ID|Specify the ID of the incident that needs to be updated.|True|String||
|Status|Specify the status for the incident.||List||
|Assign to|Specify the name or email of the analyst to whom the incident needs to be assigned. If "Unassign" is provided, action will remove assignment from the incident. Note: for name you need to provide first and last name of the analyst in the following format "{first name} {last name}"||String||



##### JSON Results
```json
[{"incident_id": "inc:466a00b13a5e4a9a9x.ac1a5e:x.x.x.", "incident_type": 1, "cid": "27fe4e476ca3490b6b2b6650e5a74", "host_ids": ["466a00b13a5e4a9a93ce2aca5eac1a5e"], "hosts": [{"device_id": "466a00b13a5e4a9a93ce2aca5eac1a5e", "cid": "27fe4e476ca34dd90b8476b2b6650e5a74", "agent_load_flags": "0", "agent_local_time": "2023-09-25T15:41:40.130Z", "agent_version": "7.01.17312.0", "bios_manufacturer": "VMware, Inc.", "bios_version": "VMW71.00V.17369862.B64.2012240522", "config_id_base": "65994753", "config_id_build": "17312", "config_id_platform": "3", "external_ip": "35.246.203.0", "hostname": "EX16-AD01", "first_seen": "2023-01-20T00:40:31Z", "last_seen": "2023-10-06T07:19:50Z", "local_ip": "172.30.3.162", "mac_address": "00-50-56-a2-94-8d", "machine_domain": "exlab.local", "major_version": "10", "minor_version": "0", "os_version": "Windows Server 2016", "ou": ["Domain Controllers"], "platform_id": "0", "platform_name": "Windows", "product_type": "2", "product_type_desc": "Domain Controller", "site_name": "Default-First-Site-Name", "status": "contained", "system_manufacturer": "VMware, Inc.", "system_product_name": "VMware7,1", "groups": ["9489d65c343244169627dcbc"], "modified_timestamp": "2023-10-06T07:19:58Z"}], "created": "2023-10-06T07:20:51Z", "start": "2023-10-06T07:19:21Z", "end": "2023-10-06T07:30:27Z", "state": "closed", "assigned_to": "67494-b86d-4a55-9e52-7492449400a1", "assigned_to_name": "Yuriy Landovskyy", "status": 30, "tactics": ["Persistence", "Defense Evasion", "Command and Control", "Credential Access", "Malware", "Privilege Escalation"], "techniques": ["Create Account", "Masquerading", "Ingress Tool Transfer", "OS Credential Dumping", "Malicious File", "Image File Execution Options Injection", "Bypass User Account Control", "Accessibility Features", "Registry Run Keys / Startup Folder"], "objectives": ["Keep Access", "Contact Controlled Systems", "Gain Access", "Falcon Detection Method"], "modified_timestamp": "2023-10-20T08:34:07.078440797Z", "users": ["EX16-AD01$", "administrator"], "fine_score": 100}]
```



#### List Uploaded IOCs
List available custom IOCs in CrowdStrike Falcon.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|IOC Type Filter|Specify a comma-separated list of IOC types that should be returned. If nothing is provided, action will return IOCs from all types. Possible values: ipv4,ipv6,md5,sha256,domain.||String|ipv4,ipv6,md5,sha256,domain|
|Value Filter Logic|Specify the value filter logic. If "Equal" is selected, action will try to find the exact match among IOCs and if "Contains" is selected, action will try to find IOCs that contain that substring.||List|Equal|
|Value Filter String|Specify the string that should be searched among IOCs.||String||
|Max IOCs To Return|Specify how many IOCs to return. Default: 50. Maximum: 500.||String|50|



##### JSON Results
```json
[{"id":"6b2987ace3c0f5dbfa5414fa13e7302bc61cca5a5db6cde8e1d135xxxxxxxxxx","type":"sha256","value":"908b64b1971a979c7e3e8ce4621945cba84854cb98d76367b791a6xxxxxxxxxx","source":"testSource","action":"detect","severity":"medium","description":"test description update","metadata":{"company_name":"Microsoft Corporation","original_filename":"PowerShell.EXE","file_version":"10.0.18362.1 (WinBuild.160101.0800)","file_description":"Windows PowerShell","product_name":"Microsoft® Windows® Operating System","product_version":"10.0.18362.1","signed":false,"av_hits":0},"platforms":["windows","mac","linux"],"tags":["f09f1a25-e6d0-4709-a105-05xxxxxxxxxx"],"expiration":"2022-05-01T12:00:00Z","expired":false,"deleted":false,"applied_globally":true,"from_parent":false,"created_on":"2021-02-15T11:36:58Z","created_by":"","modified_on":"2021-10-13T09:42:13.466234223Z","modified_by":"7fff03c3227242a0bae84bxxxxxxxxxx"},{"id":"fbe8c2739f3c6df95e62e0ae54569974437b2d9306eaf6740134ccxxxxxxxxxx","type":"sha256","value":"8a86c4eecf12446ff273afc03e1b3a09a911d0b7981db1af58cb45xxxxxxxxxx","action":"no_action","severity":"","metadata":{"signed":false,"av_hits":-1},"platforms":["windows"],"tags":["Hashes 22.Nov.20 15:29 (Windows)"],"expired":false,"deleted":false,"applied_globally":true,"from_parent":false,"created_on":"2021-04-22T03:54:09.235120463Z","created_by":"internal@crowdstrike.com","modified_on":"2021-04-22T03:54:09.235120463Z","modified_by":"internal@crowdstrike.com"}]
```



#### List Hosts
List available hosts in Crowdstrike Falcon.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Customer ID|Specify the ID of the customer for which you want to execute the action.||String||
|Filter Logic|Specify what logic should be used, when searching for hosts.||List|Equal|
|Filter Value|Specify the value that should be used to filter hosts.||String||
|Max Hosts To Return|Specify how many hosts to return. Default: 50. Maximum: 1000.||String|50|



##### JSON Results
```json
[{"modified_timestamp":"2019-05-15T15:03:12Z","platform_id":"0","config_id_platform":"3","system_manufacturer":"Microsoft Corporation","meta":{"version":"XXXX"},"first_seen":"2019-04-29T07:39:45Z","service_pack_minor":"0","product_type_desc":"Server","build_number":"XXXX","hostname":"Gnrl-Elis","config_id_build":"XXXX","minor_version":"3","os_version":"Windows Server XXXXX","provision_status":"Provisioned","mac_address":"XXXXXXXXX","bios_version":"XXXXX ","agent_load_flags":"0","status":"normal","bios_manufacturer":"American Megatrends Inc.","device_policies":{"sensor_update":{"applied":true,"applied_date":"2019-05-02T22:05:09.577000651Z","settings_hash":"XXXXXXXXXXXXXXXXXXXXX","policy_type":"sensor-update","assigned_date":"2019-05-02T22:03:36.804382667Z","policy_id":"XXXXXXXXXXXXXXXXXXXXXXXX"},"remote_response":{"applied":true,"applied_date":"2019-04-29T07:40:04.469808388Z","settings_hash":"XXXXXXXX","policy_type":"remote-response","assigned_date":"2019-04-29T07:39:55.218642441Z","policy_id":"XXXXXXXXXXXXXXXXXXXXXXXXXXXXX"},"device_control":{"applied":true,"applied_date":"2019-04-29T07:40:06.834362608Z","assigned_date":"2019-04-29T07:39:55.214337999Z","policy_type":"device-control","policy_id":"XXXXXXXXXXXXXXXXXXXXXX"},"prevention":{"applied":true,"applied_date":"2019-04-29T07:40:06.876850888Z","settings_hash":"XXXXXXXXXXXXXXXXXXXXXX","policy_type":"prevention","assigned_date":"2019-04-29T07:39:55.218651583Z","policy_id":"XXXXXXXXXXXXXXXXXXXXXXXXXX"},"global_config":{"applied":true,"applied_date":"2019-04-29T07:45:18.94807838Z","settings_hash":"XXXXXXXXXXXXXXXXXXXXXXXXX","policy_type":"globalconfig","assigned_date":"2019-04-29T07:45:08.165941325Z","policy_id":"XXXXXXXXXXXXXXXXXXXXXXX"}},"cid":"XXXXXXXXXXXXXXXXXXXXXXXXXXXXx","agent_local_time":"2019-05-02T22:05:00.015Z","slow_changing_modified_timestamp":"2019-05-02T22:05:09Z","service_pack_major":"0","device_id":"XXXXXXXXXXXXXXXXXXXXXXXXXXX","system_product_name":"Virtual Machine","product_type":"3","local_ip":"1.1.1.1","external_ip":"1.1.1.1","major_version":"6","platform_name":"Windows","config_id_base":"XXXXXXXXXXXXXXXXXXX","policies":[{"applied":true,"applied_date":"2019-04-29T07:40:06.876850888Z","settings_hash":"XXXXXXXXXXXXXXXXXXXXXX","policy_type":"prevention","assigned_date":"2019-04-29T07:39:55.218651583Z","policy_id":"XXXXXXXXXXXXXXXXXXXXXXXXXX"}],"agent_version":"4.26.XXXX.0","pointer_size":"8","last_seen":"2019-05-15T15:01:23Z"},{"modified_timestamp":"2019-05-13T07:24:36Z","site_name":"Default-First-Site-Name","config_id_platform":"3","system_manufacturer":"Dell Inc.","meta":{"version":"XXXXXX"},"first_seen":"2018-04-17T11:02:20Z","platform_name":"Windows","service_pack_minor":"0","product_type_desc":"Workstation","build_number":"XXXXXXXXXX","hostname":"XXXXXXXXXXX","config_id_build":"XXXX","minor_version":"0","os_version":"Windows 10","provision_status":"Provisioned","mac_address":"XXXXXXXXXXXXXXXXX","bios_version":"1.6.5","agent_load_flags":"0","status":"normal","bios_manufacturer":"Dell Inc.","machine_domain":"SIEMPLIFY.LOCAL","device_policies":{"sensor_update":{"applied":true,"applied_date":"2019-05-05T12:52:23.121596885Z","settings_hash":"XXXXXXXXXXXXXXXXXXXXX","policy_type":"sensor-update","assigned_date":"2019-05-05T12:51:37.544605747Z","policy_id":"XXXXXXXXXXXXXXXXXXXXXXXX"},"remote_response":{"applied":true,"applied_date":"2019-02-10T07:57:59.064362539Z","settings_hash":"XXXXXXXX","policy_type":"remote-response","assigned_date":"2019-02-10T07:57:50.610924385Z","policy_id":"XXXXXXXXXXXXXXXXXXXXXXXXXXXXX"},"device_control":{"applied":true,"applied_date":"2019-03-25T15:01:28.51681072Z","assigned_date":"2019-03-25T15:00:22.442519168Z","policy_type":"device-control","policy_id":"XXXXXXXXXXXXXXXXXXXXXX"},"prevention":{"applied":true,"applied_date":"2019-04-04T06:54:06.909774295Z","settings_hash":"XXXXXXXXXXXXXXXXXXXXXX","policy_type":"prevention","assigned_date":"2019-04-04T06:53:57.135897343Z","policy_id":"XXXXXXXXXXXXXXXXXXXXXXXXXX"},"global_config":{"applied":true,"applied_date":"2019-02-10T07:57:53.70275875Z","settings_hash":"XXXXXXXXXXXXXXXXXXXXXXXXX","policy_type":"globalconfig","assigned_date":"2019-02-10T07:57:50.610917888Z","policy_id":"XXXXXXXXXXXXXXXXXXXXXXX"}},"cid":"XXXXXXXXXXXXXXXXXXXXXXXXXXXXx","agent_local_time":"2019-05-05T15:52:08.172Z","slow_changing_modified_timestamp":"2019-05-12T12:37:35Z","service_pack_major":"0","device_id":"XXXXXXXXXXXXXXXXXXXXX","system_product_name":"Latitude XXXX","product_type":"1","local_ip":"1.1.1.1","external_ip":"1.1.1.1","major_version":"10","platform_id":"0","config_id_base":"XXXXXXXXXXXXXXXXXXX","policies":[{"applied":true,"applied_date":"2019-04-04T06:54:06.909774295Z","settings_hash":"XXXXXXXXXXXXXXXXXXXXXX","policy_type":"prevention","assigned_date":"2019-04-04T06:53:57.135897343Z","policy_id":"XXXXXXXXXXXXXXXXXXXXXXXXXX"}],"agent_version":"4.26.XXXX.0","pointer_size":"8","last_seen":"2019-05-13T07:21:30Z"}]
```



#### Execute Command
Execute commands on the hosts in Crowdstrike Falcon. Supported entities: IP Address and Hostname.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Customer ID|Specify the ID of the customer for which you want to execute the action.||String||
|Command|Specify what command to execute on the hosts.|True|String||
|Admin Command|If enabled, action will execute commands with the admin level permissions. This is necessary for certain commands like "put".||Boolean|false|
|Hostname|Comma-separated list of hostnames on which you want to execute the action. Note: action will run the action on both entities + this parameter values.||String||
|Queue Offline|If enabled, commands targeting offline hosts are queued and executed once the host reconnects to the network.||Boolean|false|



##### JSON Results
```json
{"Entity":"XXX.XXX.XXX","EntityResult":{"session_id":"2a066818-XXXX-XXXX-XXXX-c295ed7295b3","task_id":"84846f59-XXXX-XXXX-XXXX-12af4af88a8b","complete":true,"stdout":"","stderr":"","base_command":"get"}}
```









## Connectors
#### Crowdstrike - Alerts Connector
Pull alerts from Crowdstrike. Dynamic List works with the "display_name" parameter. Note: To fetch identity protection detections use "Identity Protection Detections Connector".

|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|DeviceProductField|Enter the source field name in order to retrieve the Product Field name.|True|String|Product Name|
|EventClassId|Enter the source field name in order to retrieve the Event Field name.|True|String|type|
|Environment Field Name|Describes the name of the field where the environment name is stored. If the environment field isn't found, the environment is the default environment.||String||
|Environment Regex Pattern|A regex pattern to run on the value found in the "Environment Field Name" field. Default is .* to catch all and return the value unchanged. Used to allow the user to manipulate the environment field through regex logic. If the regex pattern is null or empty, or the environment value is null, the final environment result is the default environment.||String|.*|
|PythonProcessTimeout|Timeout limit for the python process running the current script.|True|Integer|180|
|API Root|API root of the Crowdstrike instance.|True|String|https://api.crowdstrike.com|
|Client ID|Client ID  of the Crowdstrike account.|True|String||
|Client Secret|Client Secret of the Crowdstrike account.|True|Password|*****|
|Lowest Severity Score To Fetch|Lowest severity score of the identity protection detections to fetch. If nothing is provided, the connector will ingest detections with all severities. Maximum is 100. Note: action also supports the following values: Informational, Low, Medium, High, Critical.||String||
|Max Hours Backwards|Number of hours before the first connector iteration to retrieve alerts from. This parameter applies to the initial connector iteration after you enable the connector for the first time, or used as a fallback value in cases where connector's last run timestamp expires.|True|Integer|1|
|Max Alerts To Fetch|How many alerts to process per one connector iteration. Default: 10.|True|Integer|10|
|Include Hidden Alerts|If enabled, connector will also fetch alerts that are labeled as "hidden" by Crowdstrike.||Boolean|true|
|Fallback Severity|Fallback severity for the SecOps alert that should be applied to the Crowdstrike alerts, which are missing severity information. Possible values: Informational, Low, Medium, High, Critical. If nothing is provided, connector will use "Informational" severity.||String|Informational|
|Use dynamic list as a blocklist|If enabled, the dynamic list will be used as a blocklist.||Boolean|false|
|Verify SSL|If enabled, verify the SSL certificate for the connection to the Crowdstrike server is valid.||Boolean|false|
|Disable Overflow|If enabled, connector will ignore the overflow mechanism.||Boolean|false|
|Proxy Server Address|The address of the proxy server to use.||String||
|Proxy Username|The proxy username to authenticate with.||String||
|Proxy Password|The proxy password to authenticate with.||Password|*****|
|Case Name Template|When provided, connector will add a new key called "custom_case_name" to the Google Secops Event. It can used to have a customer case name. Please refer to the documentation portal for more details. You can provide placeholders in the following format: [name of the field]. Example: Phishing - [event_mailbox]. Note: connector will use first Google Secops Event for placeholders. Only keys that have string value will be handled.||String||
|Alert Name Template|If provided, connector will use this value for Google Secops Alert Name. Please refer to the documentation portal for more details. You can provide placeholders in the following format: [name of the field]. Example: Phishing - [event_mailbox]. Note: connector will use first Google Secops Event for placeholders. Only keys that have string value will be handled. If nothing is provided or user provides an invalid template, connector will use the default alert name.||String||
|Customer ID|The customer ID of the tenant in which to execute the integration. For use in multi-tenant (MSSP) environments.||String||


#### Crowdstrike - Detections Connector
Deprecated. Pull detections from Crowdstrike. Whitelist works with filters that are supported by the API of Crowdstrike. For the details, please refer to the documentation portal.

|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|EventClassId|Enter the source field name in order to retrieve the Event Field name.|True|String|behaviors_technique|
|PythonProcessTimeout|Timeout limit for the python process running the current script.|True|Integer|180|
|DeviceProductField|Enter the source field name in order to retrieve the Product Field name.|True|String|Product Name|
|Environment Field Name|Describes the name of the field where the environment name is stored. If the environment field isn't found, the environment is the default environment.||String||
|Environment Regex Pattern|A regex pattern to run on the value found in the "Environment Field Name" field. Default is .* to catch all and return the value unchanged. Used to allow the user to manipulate the environment field via regex logic. If the regex pattern is null or empty, or the environment value is null, the final environment result is the default environment.||String|.*|
|API Root|API root of the Crowdstrike instance.|True|String|https://api.crowdstrike.com|
|Client ID|Client ID  of the Crowdstrike account.|True|String||
|Client Secret|Client Secret of the Crowdstrike account.|True|Password|*****|
|Lowest Severity Score To Fetch|Lowest severity score of the detections to fetch. If nothing is provided, the connector won't apply this filter. Maximum is 100. Note: action also supports the following values: Low, Medium, High, Critical.||String|50|
|Lowest Confidence Score To Fetch|Lowest confidence score of the detections to fetch. If nothing is provided, the connector won't apply this filter. Maximum is 100.||Integer|0|
|Max Hours Backwards|Number of hours before the first connector iteration to retrieve detections from. This parameter applies to the initial connector iteration after you enable the connector for the first time, or used as a fallback value in cases where connector's last run timestamp expires.||Integer|1|
|Max Detections To Fetch|How many detections to process per one connector iteration. Default: 10.||Integer|10|
|Padding Period|The number of hours that connector will use for padding. Maximum: 6.||Integer|1|
|Disable Overflow|If enabled, connector will ignore the overflow mechanism.||Boolean|false|
|Verify SSL|If enabled, verify the SSL certificate for the connection to the Crowdstrike server is valid.||Boolean|false|
|Proxy Server Address|The address of the proxy server to use.||String||
|Proxy Username|The proxy username to authenticate with.||String||
|Proxy Password|The proxy password to authenticate with.||Password|*****|
|Case Name Template|When provided, connector will add a new key called "custom_case_name" to the Google Secops Event. It can used to have a customer case name. Please refer to the documentation portal for more details. You can provide placeholders in the following format: [name of the field]. Example: Phishing - [event_mailbox]. Note: connector will use first Google Secops Event for placeholders. Only keys that have string value will be handled.||String||
|Alert Name Template|If provided, connector will use this value for Google Secops Alert Name. Please refer to the documentation portal for more details. You can provide placeholders in the following format: [name of the field]. Example: Phishing - [event_mailbox]. Note: connector will use first Google Secops Event for placeholders. Only keys that have string value will be handled. If nothing is provided or user provides an invalid template, connector will use the default alert name.||String||
|Customer ID|The customer ID of the tenant in which to execute the integration. For use in multi-tenant (MSSP) environments.||String||


#### Crowdstrike - Identity Protection Detections Connector
Pull Identity Protection detections from Crowdstrike. Note: this connector requires an Identity Protection license. Dynamic List works with the “display_name” parameter.

|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|DeviceProductField|Enter the source field name in order to retrieve the Product Field name.|True|String|Product Name|
|EventClassId|Enter the source field name in order to retrieve the Event Field name.|True|String|type|
|Environment Field Name|Describes the name of the field where the environment name is stored. If the environment field isn't found, the environment is the default environment.||String||
|Environment Regex Pattern|A regex pattern to run on the value found in the "Environment Field Name" field. Default is .* to catch all and return the value unchanged. Used to allow the user to manipulate the environment field through regex logic. If the regex pattern is null or empty, or the environment value is null, the final environment result is the default environment.||String|.*|
|PythonProcessTimeout|Timeout limit for the python process running the current script.|True|Integer|180|
|API Root|API root of the Crowdstrike instance.|True|String|https://api.crowdstrike.com|
|Client ID|Client ID  of the Crowdstrike account.|True|String||
|Client Secret|Client Secret of the Crowdstrike account.|True|Password|*****|
|Lowest Severity Score To Fetch|Lowest severity score of the identity protection detections to fetch. If nothing is provided, the connector will ingest detections with all severities. Maximum is 100. Note: action also supports the following values: Informational, Low, Medium, High, Critical.||String||
|Max Hours Backwards|Number of hours before the first connector iteration to retrieve detections from. This parameter applies to the initial connector iteration after you enable the connector for the first time, or used as a fallback value in cases where connector's last run timestamp expires.||Integer|1|
|Max Detections To Fetch|How many identity protection detections to process per one connector iteration. Default: 10.||Integer|10|
|Use dynamic list as a blocklist|If enabled, the dynamic list will be used as a blocklist.||Boolean|true|
|Disable Overflow|If enabled, connector will ignore the overflow mechanism.||Boolean|false|
|Verify SSL|If enabled, verify the SSL certificate for the connection to the Crowdstrike server is valid.||Boolean|false|
|Proxy Server Address|The address of the proxy server to use.||String||
|Proxy Username|The proxy username to authenticate with.||String||
|Proxy Password|The proxy password to authenticate with.||Password|*****|
|Case Name Template|When provided, connector will add a new key called "custom_case_name" to the Google Secops Event. It can used to have a customer case name. Please refer to the documentation portal for more details. You can provide placeholders in the following format: [name of the field]. Example: Phishing - [event_mailbox]. Note: connector will use first Google Secops Event for placeholders. Only keys that have string value will be handled.||String||
|Alert Name Template|If provided, connector will use this value for Google Secops Alert Name. Please refer to the documentation portal for more details. You can provide placeholders in the following format: [name of the field]. Example: Phishing - [event_mailbox]. Note: connector will use first Google Secops Event for placeholders. Only keys that have string value will be handled. If nothing is provided or user provides an invalid template, connector will use the default alert name.||String||
|Customer ID|The customer ID of the tenant in which to execute the integration. For use in multi-tenant (MSSP) environments.||String||


#### Crowdstrike - Incidents Connector
Deprecated. Pull incident and related behaviors from Crowdstrike. Dynamic List works with the “incident_type” parameter.

|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|DeviceProductField|Enter the source field name in order to retrieve the Product Field name.|True|String|Product Name|
|EventClassId|Enter the source field name in order to retrieve the Event Field name.|True|String|data_type|
|API Root|API root of the Crowdstrike instance.|True|String|https://api.crowdstrike.com|
|Client ID|Client ID  of the Crowdstrike account.|True|String||
|Client Secret|Client Secret of the Crowdstrike account.|True|Password|*****|
|Max Hours Backwards|Number of hours before the first connector iteration to retrieve incidents from. This parameter applies to the initial connector iteration after you enable the connector for the first time, or used as a fallback value in cases where connector's last run timestamp expires. Default: 1||String|1|
|Environment Field Name|Describes the name of the field where the environment name is stored. If the environment field isn't found, the environment is the default environment.||String||
|Environment Regex Pattern|A regex pattern to run on the value found in the "Environment Field Name" field. Default is .* to catch all and return the value unchanged. Used to allow the user to manipulate the environment field via regex logic. If the regex pattern is null or empty, or the environment value is null, the final environment result is the default environment.||String|.*|
|PythonProcessTimeout|Timeout limit for the python process running the current script. Default: 180|True|Integer|180|
|Lowest Severity Score To Fetch|Lowest severity score of the incidents to fetch. If nothing is provided, the connector will ingest incidents with all severities. Maximum is 100. Note: action also supports the following values: Low, Medium, High, Critical. In the Crowdstrike UI the same value is presented as divided by 10.||String||
|Max Incidents To Fetch|How many incidents to process per one connector iteration. Default: 10. Max: 100.||String|10|
|Use dynamic list as a blocklist|If enabled, the dynamic list will be used as a blocklist.||Boolean|false|
|Disable Overflow|If enabled, connector will ignore the overflow mechanism.||Boolean|false|
|Verify SSL|If enabled, verify the SSL certificate for the connection to the Crowdstrike server is valid.||Boolean|false|
|Proxy Server Address|The address of the proxy server to use.||String||
|Proxy Username|The proxy username to authenticate with.||String||
|Proxy Password|The proxy password to authenticate with.||Password|*****|
|Customer ID|The customer ID of the tenant in which to execute the integration. For use in multi-tenant (MSSP) environments.||String||


#### Crowdstrike Falcon Streaming Events Connector
Crowdstrike Falcon Streaming Events Connector

|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|DeviceProductField|Describes the name of the field where the product name is stored.|True|String|device_product|
|EventClassId|Describes the name of the field where the event name is stored.|True|String|Name|
|PythonProcessTimeout|The timeout limit (in seconds) for the python process running current script|True|Integer|600|
|Environment Field Name|Describes the name of the field where the environment name is stored. If environment field isn't found, environment is ""||String||
|Environment Regex Pattern|A regex pattern to run on the value found in the "Environment Field Name" field.||String||
|API Root|API root of the Crowdstrike instance||String|https://api.crowdstrike.com|
|Client ID|Client ID for Crowdstrike API|True|String||
|Client Secret|Client Secret for Crowdstrike API|True|Password|*****|
|Event types|Specify a comma-separated list of event types. Examples of the event types: DetectionSummaryEvent, IncidentSummaryEvent, UserActivityAuditEvent, RemoteResponseSessionStartEvent, RemoteResponseSessionEndEvent, EppDetectionSummaryEvent. For more information visit documentation portal.||String|DetectionSummaryEvent, IncidentSummaryEvent, UserActivityAuditEvent, RemoteResponseSessionStartEvent, RemoteResponseSessionEndEvent, EppDetectionSummaryEvent|
|Max Events per Cycle|Max events to process per connector run.|True|Integer|100|
|Max Day Backwards|Number of days before the first connector iteration to retrieve events from. This parameter applies to the initial connector iteration after you enable the connector for the first time, or used as a fallback value in cases where connector's last run timestamp expires.||Integer|3|
|Min Severity|Specify the events that should be ingested based on the events severity (detections events). The value ranges from 0-5. If other event types besides detections are ingested by the connector, connector sets a severity for them as -1 and this filter is not applied to those types of events||Integer|0|
|Alert Name Template|If provided, connector will use this value for Siemplify Alert Name. Please refer to the documentation portal for more details. You can provide placeholders in the following format: [name of the field]. Example: Phishing - [event_mailbox]. Note: connector will use first Siemplify Event for placeholders. Only keys that have string value will be handled. If nothing is provided or user provides an invalid template, connector will use the default alert name.||String||
|Rule Generator Template|	If provided, the connector will use this value for Siemplify Rule Generator. Please refer to the documentation portal for more details. You can provide placeholders in the following format: [name of the field]. Example: Phishing - [event_mailbox]. Note: connector will use the first Siemplify event for placeholders. Only keys that have string value will be handled. If nothing is provided or the user provides an invalid template, the connector will use the default rule generator.||String||
|Proxy Server Address|Proxy server address.||String||
|Proxy Username|Proxy username.||String||
|Proxy Password|Proxy password.||Password|*****|
|Disable Overflow|If enabled, connector will ignore the overflow mechanism.||Boolean|false|
|Verify SSL|Indicate whether to use SSL in the session or not||Boolean|false|
|Customer ID|The customer ID of the tenant in which to execute the integration. For use in multi-tenant (MSSP) environments.||String||




