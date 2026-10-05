
# MicrosoftGraphMail

Microsoft 365 and Office 365 deliver the power of cloud productivity to businesses of all sizes, helping save time, money, and free up valued resources. The Microsoft 365 and Office 365 plans combine the familiar Microsoft Office desktop suite with cloud-based versions of Microsoft's next-generation communications and collaboration services (including Office for the web, Microsoft Exchange Online, Microsoft Teams, and Microsoft SharePoint Online) to help users be productive from virtually anywhere through the Internet. This integration uses Microsoft Graph Mail API to communicate with Microsoft 365 and Office 365 services.

Python Version - V3_11
#### Parameters
|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Azure AD Endpoint|The Microsoft Entra endpoint to connect to.|True|String|https://login.microsoftonline.com|
|Microsoft Graph Endpoint|The Microsoft Graph endpoint to connect to.|True|String|https://graph.microsoft.com|
|Client ID|The client (application) ID of the Microsoft Entra application to use in the integration.|True|String||
|Secret ID|The client secret value of the Microsoft Entra app to use in the integration.|True|Password|*****|
|Tenant|The Microsoft Entra ID (tenant ID) value.|True|String||
|Default Mailbox|The default mailbox to use in the integration.|True|String||
|Mail field source|If enabled, user's mailbox address will be fetched from the 'mail' attribute of user's details. Otherwise, user's mailbox address will be fetched from the 'userPrincipalName' field.|False|Boolean|false|
|Base64 Encoded Private Key|Specify a base64 encoded private key that will be used to decrypt the email.|False|Password|*****|
|Base64 Encoded Certificate|Specify a base64 encoded certificate that will be used to decrypt the email.|False|Password|*****|
|Base64 Encoded CA certificate|Specify a base64 encoded trusted CA certificate for signature verification.|False|Password|*****|
|Verify SSL|If selected, the integration verifies that the SSL certificate for the connection to the Microsoft Graph server is valid.|False|Boolean|true|


#### Dependencies
| |
|-|
|PyJWT-2.9.0-py3-none-any.whl|
|google_api_core-2.30.3-py3-none-any.whl|
|soupsieve-2.6-py3-none-any.whl|
|google_auth_httplib2-0.3.0-py3-none-any.whl|
|proto_plus-1.28.0-py3-none-any.whl|
|pycparser-3.0-py3-none-any.whl|
|google_api_python_client-2.188.0-py3-none-any.whl|
|pcodedmp-1.2.6-py2.py3-none-any.whl|
|protobuf-7.35.1-cp310-abi3-manylinux2014_x86_64.whl|
|requests_toolbelt-1.0.0-py2.py3-none-any.whl|
|easygui-0.98.3-py2.py3-none-any.whl|
|EnvironmentCommon-1.0.1-py2.py3-none-any.whl|
|exceptiongroup-1.2.2-py3-none-any.whl|
|oletools-0.60.2-py2.py3-none-any.whl|
|python_dateutil-2.9.0.post0-py2.py3-none-any.whl|
|setuptools-80.9.0-py3-none-any.whl|
|olefile-0.47-py2.py3-none-any.whl|
|oscrypto-1.3.0-py3-none-any.whl|
|lark-1.1.9-py3-none-any.whl|
|compressed_rtf-1.0.6.tar.gz|
|tzlocal-5.2-py3-none-any.whl|
|pyasn1_modules-0.4.2-py3-none-any.whl|
|httplib2-0.32.0-py3-none-any.whl|
|chardet-5.2.0-py3-none-any.whl|
|emaildata-0.3.4-py3-none-any.whl|
|sniffio-1.3.1-py3-none-any.whl|
|siemplify_html2text-2020.1.16-py3-none-any.whl|
|asn1crypto-1.5.1-py2.py3-none-any.whl|
|cryptography-46.0.7-cp311-abi3-manylinux_2_34_x86_64.whl|
|icalendar-6.0.1-py3-none-any.whl|
|RTFDE-0.1.2-py3-none-any.whl|
|extract_msg-0.52.0-py3-none-any.whl|
|requests-2.32.5-py3-none-any.whl|
|h11-0.16.0-py3-none-any.whl|
|pyparsing-3.3.2-py3-none-any.whl|
|typing_extensions-4.16.0-py3-none-any.whl|
|pycryptodome-3.23.0-cp37-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl|
|tzdata-2024.2-py2.py3-none-any.whl|
|cachetools-5.5.0-py3-none-any.whl|
|cffi-2.0.0-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.whl|
|python_smail-0.9.0-py3-none-any.whl|
|googleapis_common_protos-1.75.0-py3-none-any.whl|
|colorclass-2.2.2-py2.py3-none-any.whl|
|pyasn1-0.6.3-py3-none-any.whl|
|rsa-4.9.1-py3-none-any.whl|
|google_auth-2.47.0-py3-none-any.whl|
|msoffcrypto_tool-5.4.2-py3-none-any.whl|
|red-black-tree-mod-1.20.tar.gz|
|pyopenssl-25.3.0-py3-none-any.whl|
|ebcdic-1.1.1-py2.py3-none-any.whl|
|IMAPClient-3.0.1-py2.py3-none-any.whl|
|pyth3-0.7-py3-none-any.whl|
|beautifulsoup4-4.12.3-py3-none-any.whl|
|TIPCommon-2.4.3-py3-none-any.whl|
|httpx-0.28.1-py3-none-any.whl|
|six-1.16.0-py2.py3-none-any.whl|
|certifi-2026.6.17-py3-none-any.whl|
|uritemplate-4.2.0-py3-none-any.whl|
|anyio-4.14.1-py3-none-any.whl|
|urllib3-2.7.0-py3-none-any.whl|
|charset_normalizer-3.4.7-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl|
|pytz-2024.2-py2.py3-none-any.whl|
|idna-3.18-py3-none-any.whl|
|httpcore-1.0.9-py3-none-any.whl|


## Actions
#### Block Domain
Block specified email domains by adding them to a message rule in the given Mailbox. If the rule does not exist, it will be created.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Domains|Comma-separated list of sender domains to block (e.g., example.com). NOTE: Domains manually input in this field and domains dynamically extracted from entities work together and will both be added to the rule conditions.|False|String||
|Mailboxes|Mailboxes where the message rule will be added. Can be a comma-separated list of user principal names.|True|String|Default Mailbox|
|Rule Name|Name of the message rule to add these domains into. If the rule exists, it will be updated.|True|String|Google SecOps - Blocked Domains|
|Action|Action that should be taken for these domains. 'Move To Junk' will move them to Junk Email folder, 'Delete' will route them to Deleted Items. 'Select One' will preserve the existing action if the rule exists.|True|List|Select One|
|How many mailboxes to process in a single batch|Specify how many mailboxes action should process in a single batch. If nothing is provided, default value of 20 will be used.|False|String|20|



##### JSON Results
```json
[  
  {  
    "Entity": "example.com",  
    "EntityResult": {  
      "successful_mailboxes": [  
        "user@example.com"  
      ],  
      "failed_mailboxes": []  
    }  
  }  
]
```



#### Delete Email
Delete one or multiple emails from the mailbox based on provided search criteria. If permissions allow, action can move emails in mailboxes other than the one provided in the integration configuration. Action is async, please adjust action timeout in IDE accordingly. Action is not working on Chronicle entities.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Delete In Mailbox|By default, delete operation will be executed in the default mailbox specified in the integration configuration. If permissions allow, action can search in other mailboxes as well. Parameter accepts multiple values as a comma separated string.|True|String|Default Mailbox|
|Folder Name|Specify the mailbox folder to search in. '/' separator can be used to specify a subfolder to search in, example: Inbox/Subfolder|True|String|Inbox|
|Mail IDs|Specify the mail ids or internetMessageIds to search for. Parameter accepts multiple values as a comma separated string. If mail id or internet message id is provided, it takes priority for the search, subject and sender filters are ignored.|False|String||
|Subject Filter|Specify the subject of the email to search for. Filter works with “contains” logic.|False|String||
|Sender Filter|Specify the sender of the email to search for. Filter works with “equals” logic.|False|String||
|Time Frame (minutes)|Specify time frame in minutes to search emails for.|False|String||
|Only Unread|If enabled, action searches only for the unread emails.|False|Boolean||
|How many mailboxes to process in a single batch|Specify how many mailboxes action should process in a single batch (single connection to O365). If nothing is provided, default value of 25 will be used.|False|String||
|Limit the Amount of Information Returned in the JSON Result|If enabled, the amount of information returned by the action will be limited only to the key email fields.|False|Boolean|false|
|Disable the Action JSON Result|If enabled, action will not return JSON result.|False|Boolean|true|



##### JSON Results
```json
[{"@odata.context": "xx", "@odata.etag": "xxxx", "id": "xxxx", "createdDateTime": "2025-02-12T15:18:43Z", "lastModifiedDateTime": "2025-02-12T15:18:49Z", "changeKey": "xx+xx", "categories": [], "receivedDateTime": "2025-02-12T15:18:44Z", "sentDateTime": "2025-02-12T15:18:41Z", "hasAttachments": false, "internetMessageId": "xxx", "subject": "Re: Testing", "bodyPreview": "xxxx", "importance": "normal", "parentFolderId": "xxx", "conversationId": "xxx", "conversationIndex": "xxx", "isDeliveryReceiptRequested": false, "isReadReceiptRequested": false, "isRead": false, "isDraft": false, "webLink": "xxx", "inferenceClassification": "focused", "body": {"contentType": "html", "content": "xxxx"}, "sender": {"emailAddress": {"name": "Idris Elba", "address": "xxxx"}}, "from": {"emailAddress": {"name": "Idris Elba", "address": "xxx"}}, "toRecipients": [{"emailAddress": {"name": "xxxx", "address": "xxxx"}}], "ccRecipients": [], "bccRecipients": [], "replyTo": [], "flag": {"flagStatus": "notFlagged"}}]
```



#### Remove Block Sender
Remove specified email senders from a message rule in the given Mailbox. If the rule becomes empty, it will be deleted.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Senders|Comma-separated list of sender email addresses to remove.|False|String||
|Mailboxes|Mailboxes where the message rule exists. Can be a comma-separated list of user principal names.|True|String|Default Mailbox|
|Rule Name|Name of the message rule to remove these senders from.|True|String|Google SecOps - Blocked Senders|
|How many mailboxes to process in a single batch|Specify how many mailboxes action should process in a single batch. If nothing is provided, default value of 20 will be used.|False|String|20|



##### JSON Results
```json
[  
  {  
    "Entity": "sender1@example.com",  
    "EntityResult": {  
      "successful_mailboxes": [  
        "user@example.com"  
      ],  
      "failed_mailboxes": []  
    }  
  }  
]
```



#### Wait For Email From User
Wait for user's response based on an email sent via the "Send Mail" action. Action is async, please adjust action timeout in IDE accordingly. Action is not working on Chronicle entities.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Mail ID|Specify the id or internetMessageId of the email, which current action would be waiting for. If the message has been sent using Send Email action, please select SendEmail.JSONResult|id or Send Email.JsonResult|internetMessageId field as a placeholder. Search Emails action also can return ids for emails.|True|String||
|Mail Date|Send timestamp of the email, which current action would be waiting for. If message has been sent using Send Email action, please select SendEmail.JSONResult|sentDateTime or SendEmail.JSONResult|createdDateTime field as a placeholder.|False|String||
|Mail Recipients|Comma-separated list of recipient emails, response from which current action would be waiting for. If message has been sent using Send Email action, please select SendEmail.JSONResult|toRecipients field as a placeholder.|False|String||
|How long to wait for recipient reply (minutes)|How long in minutes to wait for the user's reply before marking it timed out.|False|String|10080|
|Wait for All Recipients to Reply?|If enabled, the action will wait for responses from all of the recipients until timeout, and not finish upon getting the first response.|False|Boolean|False|
|Wait Stage Exclude pattern|Define a regular expression to exclude specific replies from the wait stage. This applies to both the subject and body of the email. For example, use it to exclude automatic Out-of-Office emails from being treated as recipient replies, so the process waits for an actual user reply instead.|False|String||
|Folder to Check for Reply|Mailbox folder to search for incoming recipient replies. Supports nested subfolders using the '/' separator (for example, 'Inbox/Subfolder').|False|String|Inbox|
|Fetch Response Attachments|If enabled, if recipient replies with attachment - fetch recipient response and add it as attachment for the action result.|False|Boolean|False|
|Limit the Amount of Information Returned in the JSON Result|If enabled, the amount of information returned by the action will be limited only to the key email fields.|False|Boolean|true|
|Disable the Action JSON Result|If enabled, action will not return JSON result.|False|Boolean|false|



##### JSON Results
```json
{"Responses": [{"recipient": "recipient@example.com", "content": {"@odata.etag": "W/\"dummy_etag\"", "id": "dummy_id", "createdDateTime": "2024-01-01T12:00:00Z", "lastModifiedDateTime": "2024-01-01T12:00:01Z", "changeKey": "dummy_change_key", "categories": [], "receivedDateTime": "2024-01-01T12:00:00Z", "sentDateTime": "2024-01-01T12:00:00Z", "hasAttachments": false, "internetMessageId": "<dummy_message_id@example.com>", "subject": "Dummy Subject", "bodyPreview": "Dummy Body Preview", "importance": "normal", "parentFolderId": "dummy_folder_id", "conversationId": "dummy_conversation_id", "conversationIndex": "dummy_conversation_index", "isDeliveryReceiptRequested": false, "isReadReceiptRequested": false, "isRead": false, "isDraft": false, "webLink": "https://outlook.office365.com/owa/?ItemID=dummy_item_id&exvsurl=1&viewmodel=ReadMessageItem", "inferenceClassification": "focused", "internetMessageHeaders": [{"name": "Received", "value": "from dummy_server by dummy_server"}, {"name": "Authentication-Results", "value": "dummy_authentication_results"},  {"name": "From", "value": "\"Dummy Sender\" <dummy_sender@example.com>"}, {"name": "To", "value": "\"Dummy Recipient\" <dummy_recipient@example.com>"}, {"name": "Subject", "value": "Dummy Subject"}, {"name": "Thread-Topic", "value": "Dummy Thread Topic"}, {"name": "Thread-Index", "value": "dummy_thread_index"}, {"name": "Date", "value": "Mon, 01 Jan 2024 12:00:00 +0000"}, {"name": "Message-ID", "value": "<dummy_message_id@example.com>"}, {"name": "References", "value": "<dummy_reference_id@example.com>"}, {"name": "In-Reply-To", "value": "<dummy_in_reply_to_id@example.com>"}, {"name": "X-MS-Exchange-Organization-SCL", "value": "0"}, {"name": "X-MS-TNEF-Correlator", "value": "dummy_correlator"}, {"name": "MIME-Version", "value": "1.0"}], "body": {"contentType": "html", "content": "<html><body>Dummy Body</body></html>"}, "sender": {"emailAddress": {"name": "Dummy Sender", "address": "dummy_sender@example.com"}}, "from": {"emailAddress": {"name": "Dummy Sender", "address": "dummy_sender@example.com"}}, "toRecipients": [{"emailAddress": {"name": "Dummy Recipient", "address": "dummy_recipient@example.com"}}], "ccRecipients": [], "bccRecipients": [], "replyTo": [], "uniqueBody": {"contentType": "html", "content": "<html><body>Dummy Unique Body</body></html>"}, "flag": {"flagStatus": "notFlagged"}, "singleValueExtendedProperties": [{"id": "String 0x7d", "value": "Dummy Extended Property"}]}}]}
```



#### List Rules
List all message rules for a specific mailbox using Microsoft Graph API.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Mailboxes|Mailboxes to list rules for. Can be a comma-separated list of user principal names.|True|String|Default Mailbox|
|Rule Name|Filter by the display name of the rule.|False|String||
|Limit|Limit the number of rules to return per mailbox.|False|String|20|



##### JSON Results
```json
[  
  {  
    "Entity": "user@example.com",  
    "EntityResult": {  
      "mailbox": "user@example.com",  
      "rules": [  
        {  
          "id": "rule_1",  
          "displayName": "Google SecOps - Blocked Domains",  
          "isEnabled": true,  
          "sequence": 1,  
          "senders": [  
            "bad-domain.com"  
          ]  
        }  
      ]  
    }  
  }  
]
```



#### Download Attachments from Email
Download attachments from an email based on the provided criteria. Note: Action is not running on SecOps entities. Action is running asynchronously. Adjust the script timeout value in the SecOps IDE for action as needed. If the downloaded attachments contain "/" or "\" characters in their names, the characters will be replaced with the '_' character.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Search In Mailbox|By default, the action  attempts to search for an email in the default mailbox specified in the integration configuration. If permissions allow, the action can execute search in other mailboxes. This parameter accepts multiple values as a comma-separated string.|True|String|Default Mailbox|
|Folder Name|Specify the mailbox folder to search in. '/' separator can be used to specify a subfolder to search in, example: Inbox/Subfolder|False|String|Inbox|
|Download Destination|Destination to save the downloaded attachments to. By default, the action attempts to save the attachment to the Google Cloud storage bucket. Saving an attachment to the local file system is a fallback option.|True|List|GCP Bucket|
|Download Path|Path to download attachments to. When saving attachments to the Google Cloud bucket or a local file system, the action expects download path to be specified in the unix-like format, for example, “/tmp/test”.|True|String||
|Mail IDs|Specify the mail ids or internetMessageIds to search for. Parameter accepts multiple values as a comma separated string. If mail id or internet message id is provided, it takes priority for the search, subject and sender filters are ignored.|False|String||
|Subject Filter|Specify the subject of the email to search for. Filter works with "contains" logic.|False|String||
|Sender Filter|Specify the sender of the email to search for. Filter works with "equals" logic.|False|String||
|Download Attachments from EML|If checked, the action downloads attachments from attached EML files.|False|Boolean|False|
|Download Attachments to unique path?|If checked, the action downloads attachments to the unique path under the path value provided in the “Download Path” parameter to avoid overwiting of previously downloaded attachments.|False|Boolean|False|
|How many mailboxes to process in a single batch|Number of  mailboxes to process in a single batch (single connection to O365). If no value is provided, the default value of 25 mailboxes is used.|False|String|25|



##### JSON Results
```json
[{"attachment_name":"name1.png","downloaded_path":"file_path/name1.png"},{"attachment_name":"name2.png","downloaded_path":"file_path/name2.png"}]
```



#### Extract Data from Attached EML
Extract data from the email EML attachments and return it in the actions JSON result. The action supports .eml, .msg, .ics file formats. Note: Action is not running on SecOps entities.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Search In Mailbox|By default, the action attempts to search for an email in the default mailbox specified in the integration configuration. If permissions allow, the action can execute search in other mailboxes. This parameter accepts multiple values as a comma-separated string.|True|String|Default Mailbox|
|Folder Name|Specify the mailbox folder to search in. '/' separator can be used to specify a subfolder to search in, example: Inbox/Subfolder|False|String|Inbox|
|Mail IDs|Specify the mail ids or internetMessageIds to search for. This parameter accepts multiple values as a comma-separated string.|True|String||
|Regex Map JSON|JSON definition containing regular expressions to apply to the attached email file and produce additional key values in the action JSON result. Example of the JSON definition is as follows: {ips: \b\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}\b}|False|String|{}|



##### JSON Results
```json
[{"type":"EML","subject":"examplesubject","from":"example@mail.com","to":"example1@mail.com,example2@mail.com","date":"Thu,4Jul202412:11:29+0530","text":"Someexampleintext","html":"<p>Someexampleinhtml</p>","regex":{},"regex_from_text_part":{},"id":"abcd","name":"abc.eml"},{"type":"MSG","subject":"examplesubject","from":"example@mail.com","to":"example1@mail.com,example2@mail.com","date":"Thu,4Jul202412:11:29+0530","text":"Someexampleintext","html":"<p>Someexampleinhtml</p>","regex":{},"regex_from_text_part":{},"id":"abcd","name":"abc.msg"},{"type":"ICS","subject":"examplesubject","from":"example@mail.com","to":"example1@mail.com,example2@mail.com","date":"Thu,4Jul202412:11:29+0530","text":"Someexampleintext","html":"<p>Someexampleinhtml</p>","regex":{},"regex_from_text_part":{},"id":"abcd","name":"abc.ics"}]
```



#### Send Email HTML
Send email with the Google SecOps HTML template from a specific mailbox to an arbitrary list of recipients. If permissions allow, the action sends an email from a mailbox different than the one specified in the integration configuration. Note: Action is not running on Google SecOps entities.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|BCC|Arbitrary comma-separated list of email addresses to use in the BCC email field. Use the same format for the "Send to" field.|False|String||
|Attachments Paths|Specify the attachments to be added, parameter expects full paths to be provided, for example: /<work directory>/file1.pdf. Parameter accepts multiple values as a comma separated string.|False|String||
|Email HTML Template|The question you would like to ask, or describe the decision you would like the recipient to be able to respond to|True|EmailContent|Email HTML Template|
|Reply-To Recipients|Comma-separated list of recipients used in the Reply-To header. Note: The Reply-To header is added to force email replies to specific email addresses instead of the email sender address stated in the From field.|False|String||
|Attachment Location|Location where the attachments to be added are stored. By default, the action attempts to get the attachment from the Google Cloud storage bucket, another option is to fetch it from the local file system.|True|List|GCP Bucket|
|Send From|Optional email address to send an email from (if permissions allow it). By default, the email is sent from the default mailbox specified in the integration configuration.|True|String|Default Mailbox|
|Subject|Email subject.|True|String||
|Send to|Specify the arbitrary comma-separated list of email addresses for the email recipients,for example, user1@company.co, user2@company.co.|True|String||
|CC|Arbitrary comma-separated list of email addresses to use in the CC email field. Use the same format as for the "Send to" field.|False|String||



##### JSON Results
```json
{"createdDateTime": "2024-01-30T16:50:27Z", "lastModifiedDateTime": "2024-01-30T16:50:27Z", "changeKey": "xxxxx", "categories": [], "receivedDateTime": "2024-01-30T16:50:27Z", "sentDateTime": "2024-01-30T16:50:27Z", "hasAttachments": false, "internetMessageId": "<outlook.com>", "subject": "Testing", "bodyPreview": "bbcbcb", "importance": "normal", "parentFolderId": "xxxxx", "conversationId": "xxxxx", "conversationIndex": "xxxxxxx", "isDeliveryReceiptRequested": false, "isReadReceiptRequested": false, "isRead": true, "isDraft": false, "webLink": "https://example.com", "inferenceClassification": "focused", "body": {"contentType": "html", "content": "hdhdhd"}, "sender": {"emailAddress": {"name": "sdjsdjs", "address": "xxxxx"}}, "from": {"emailAddress": {"name": "jdsjdjs", "address": "xxxxxx"}}, "toRecipients": [{"emailAddress": {"name": "example@mail.com", "address": "xxxxxxx"}}], "ccRecipients": [], "bccRecipients": [], "replyTo": [], "uniqueBody": {"contentType": "html", "content": "ssfsf"}, "flag": {"flagStatus": "notFlagged"}, "id": "xxxxxxx"}
```



#### Mark Email as Not Junk
Mark an email as not junk for a specific mailbox. This action removes the sender from the list of blocked senders and moves the message to the Inbox folder. Note: This action uses the beta version of Microsoft Graph APIs and is not running on Google SecOps entities.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Search In Mailbox|A mailbox to search for an email in. By default, the action  attempts to search for the email in the default mailbox that you specified in the integration configuration. With correct permissions, the action can execute a search in other mailboxes. Parameter accepts multiple values as a comma separated string. |True|String|Default Mailbox|
|Folder Name|A mailbox folder to search in.|True|String|Junk Email|
|Mail IDs|Specify the mail ids or internetMessageIds to mark as not junk. Parameter accepts multiple values as a comma separated string.|True|String||



##### JSON Results
```json

```



#### Forward Email
Forward email including previous threads. If permissions allow, action can send an email from a mailbox different that is specified in the integration configuration. Note: Action is not running on Siemplify entities.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Send From|Specify the optional email address from which if permissions allow, email should be sent. By default, the email will be sent from the default mailbox specified in the integration configuration.|True|String|Default Mailbox|
|Mail ID|Specify the mail ids or internetMessageIds of the message that you want to forward.|True|String||
|Folder Name|Specify the mailbox folder to search in. '/' separator can be used to specify a subfolder to search in, example: Inbox/Subfolder|False|String|Inbox|
|Subject|Specify the mail subject part.|True|String||
|Send to|Specify the arbitrary comma separated list of email addresses for the email recipients. For example: user1@company.co, user2@company.co|True|String||
|CC|Specify the arbitrary comma separated list of email addresses to be put in the CC field of email. Format is the same as for the 'Send to' field.|False|String||
|BCC|Arbitrary comma separated list of email addresses to be put in the BCC field of email. Format is the same as for the 'Send to' field.|False|String||
|Attachments Paths|Specify the attachments to be added, parameter expects full paths to be provided, for example: /<work directory>/file1.pdf. Parameter accepts multiple values as a comma separated string.|False|String||
|Mail Content|Specify the email body part.|True|String||
|Attachment Location|Location where the attachments to be added are stored. By default, the action attempts to get the attachment from the Google Cloud storage bucket, another option is to fetch it from the local file system.|True|List|GCP Bucket|



##### JSON Results
```json
{"id": "xxxxx", "createdDateTime": "2024-02-02T09:49:53Z", "lastModifiedDateTime": "2024-02-02T09:51:19Z", "changeKey": "ieiohjdskj", "categories": [], "receivedDateTime": "2024-02-02T09:49:54Z", "sentDateTime": "2024-02-02T09:49:54Z", "hasAttachments": true, "internetMessageId": "<xyz>", "subject": "xxxx", "bodyPreview": "Mail Action body", "importance": "normal", "parentFolderId": "ddd==", "conversationId": "dagazz=", "conversationIndex": "daf+UJo/clVcxTQ==", "isDeliveryReceiptRequested": false, "isReadReceiptRequested": false, "isRead": true, "isDraft": false, "webLink": "https://www.example.com/about", "inferenceClassification": "focused", "body": {"contentType": "text", "content": "Send Mail Action body"}, "sender": {"emailAddress": {"name": "wdzd", "address": "sample@s.com"}}, "from": {"emailAddress": {"name": "safd", "address": "xxx"}}, "toRecipients": [{"emailAddress": {"name": "xx", "address": "aef"}}], "ccRecipients": [{"emailAddress": {"name": "as", "address": "kdaw"}}], "bccRecipients": [{"emailAddress": {"name": "xxsf", "address": "wf"}}], "replyTo": [], "uniqueBody": {"contentType": "html", "content": "Mail Action body"}, "flag": {"flagStatus": "notFlagged"}}
```



#### Block Sender
Block specified email senders by adding them to a message rule in the given Mailbox. If the rule does not exist, it will be created.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Senders|Comma-separated list of sender email addresses to block. NOTE: Senders manually input in this field and senders dynamically extracted from entities work together and will both be added to the rule conditions.|False|String||
|Mailboxes|Mailboxes where the message rule will be added. Can be a comma-separated list of user principal names.|True|String|Default Mailbox|
|Rule Name|Name of the message rule to add these senders into. If the rule exists, it will be updated.|True|String|Google SecOps - Blocked Senders|
|Action|Action that should be taken for these senders. 'Move To Junk' will move them to Junk Email folder, 'Delete' will route them to Deleted Items. 'Select One' will preserve the existing action if the rule exists.|True|List|Select One|
|How many mailboxes to process in a single batch|Specify how many mailboxes action should process in a single batch. If nothing is provided, default value of 20 will be used.|False|String|20|



##### JSON Results
```json
[  
  {  
    "Entity": "sender1@example.com",  
    "EntityResult": {  
      "successful_mailboxes": [  
        "user@example.com"  
      ],  
      "failed_mailboxes": []  
    }  
  }  
]
```



#### Delete Inbox Rules
Delete a specified inbox message rule for the given Mailboxes.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Mailboxes|Mailboxes where the message rule will be deleted from. Can be a comma-separated list of user principal UPNs.|True|String|Default Mailbox|
|Rule Name|The exact name of the inbox message rule to delete.|True|String||
|How many mailboxes to process in a single batch|Specify how many mailboxes the action should process in a single batch. If nothing is provided, a default value of 25 will be used.|False|String|25|



##### JSON Results
```json
{  
    "deleted_rule": [  
        "New test cases"  
    ],  
    "successful_mailboxes": [  
        "labops1@siemplifycyarx.onmicrosoft.com"  
    ],  
    "failed_mailboxes": [  
        "user2@example.com",  
        "user3@example.com"  
    ]  
}
```



#### Move Email To Folder
Move one or multiple emails from source email folder to another folder in the mailbox. If permissions allow, action can move emails in mailboxes other than the one provided in the integration configuration. Action is async, please adjust action timeout in IDE accordingly. Action is not working on Chronicle entities.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Subject Filter|Specify the subject of the email to search for. Filter works with "contains" logic.|False|String||
|Sender Filter|Specify the sender of the email to search for. Filter works with "equals" logic.|False|String||
|Time Frame (minutes)|Specify time frame in minutes to search emails for.|False|String||
|Only Unread|If enabled, action searches only for the unread emails.|False|Boolean|False|
|How many mailboxes to process in a single batch|Specify how many mailboxes action should process in a single batch (single connection to O365). If nothing is provided, default value of 25 will be used.|False|String||
|Limit the Amount of Information Returned in the JSON Result|If enabled, the amount of information returned by the action will be limited only to the key email fields.|False|Boolean|false|
|Disable the Action JSON Result|If enabled, action will not return JSON result.|False|Boolean|false|
|Move In Mailbox|By default, move operation will be executed in the default mailbox specified in the integration configuration. If permissions allow, action can search in other mailboxes as well. If permissions allow, action can search in other mailboxes as well. Parameter accepts multiple values as a comma separated string.|True|String|Default Mailbox|
|Source Folder Name|Specify the source folder name to move mail from. '/' separator can be used to specify a subfolder to search in, example: Inbox/Subfolder|True|String||
|Destination Folder Name|Specify the destination folder name to move mail to. '/' separator can be used to specify a subfolder to search in, example: Inbox/Subfolder|True|String||
|Mail IDs|Specify the mail ids or internetMessageIds to search for. Parameter accepts multiple values as a comma separated string. If mail id or internet message id is provided, it takes priority for the search, subject and sender filters are ignored.|False|String||



##### JSON Results
```json
[{"Mailbox": "example@mail.com", "Emails": [{"id": "xxxxx", "createdDateTime": "2024-02-05T10:03:14Z", "lastModifiedDateTime": "2024-02-05T16:30:11Z", "changeKey": "cxsdjjh", "categories": [], "receivedDateTime": "2024-02-05T10:03:15Z", "sentDateTime": "2024-02-05T10:03:12Z", "hasAttachments": true, "internetMessageId": "sdfhsjdfhjsdjfd", "subject": "Forwarding for the last time with attachment", "bodyPreview": "this is the mail content for testingxyzrxyzn________________________________xyzrxyznFrom: xyzxyzrxyznSent: Monday, February 5, 2024 7:48:16 AMxyzrxyznTo: example.com <example.com>xyzrxyznSubject: subjectxyzrxyznxyzrxyznmail", "importance": "normal", "parentFolderId": "id", "conversationId": "id", "conversationIndex": "hjaoihfehf", "isDeliveryReceiptRequested": false, "isReadReceiptRequested": false, "isRead": true, "isDraft": false, "webLink": "https://www.example.com/about", "inferenceClassification": "focused", "body": {"contentType": "html", "content": "xyz"}, "sender": {"emailAddress": {"name": "xyz", "address": "example@mail.com"}}, "from": {"emailAddress": {"name": "xyz", "address": "example@mail.com"}}, "toRecipients": [{"emailAddress": {"name": "xyz", "address": "example@mail.com"}}], "ccRecipients": [], "bccRecipients": [], "replyTo": [], "flag": {"flagStatus": "notFlagged"}}]}]
```



#### Save Email to the Case
Save email or email attachments to the Chronicle Case Wall. If permissions allow, action can save emails from mailboxes other than the one provided in the integration configuration. Action is not working on Chronicle entities.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Search In Mailbox|By default, action will try to search for email in the default mailbox specified in the integration configuration. If permissions allow, action can search in other mailboxes as well.|True|String|Default Mailbox|
|Folder Name|Specify the mailbox folder to search in. '/' separator can be used to specify a subfolder to search in, example: Inbox/Subfolder|False|String|Inbox|
|Mail ID|Specify the mail id or internetMessageId to save email and attachments to the case. If the message has been sent using Send Email action, please select SendEmail.JSONResult|id or Send Email.JsonResult|internetMessageId field as a placeholder. Search Emails action also can return ids for emails.|True|String||
|Save Only Email Attachments|If enabled, action will save only attachments of the specified email.|False|Boolean|False|
|Attachment To Save|If "Save Only Email Attachments" checkbox is enabled, action can save only specific attachments that are specified in this parameter. Parameter accepts multiple values as a comma-separated string.|False|String||
|Base64 Encode|If enabled, encode the email file to base64 encoding.|False|Boolean|false|
|Save Email to the Case Wall|If enabled, save the Email directly to the SecOps Case Wall.|False|Boolean|false|



##### JSON Results
```json
{"id": "xxxx-=", "createdDateTime": "2024-02-16T14:10:34Z", "eml_info":"xyzhd", "lastModifiedDateTime": "2024-02-16T14:10:41Z", "changeKey": "cxsdjjh", "categories": [], "receivedDateTime": "2024-02-16T14:10:35Z", "sentDateTime": "2024-02-16T14:09:36Z", "hasAttachments": true, "internetMessageId": "sdfhsjdfhjsdjfd", "subject": "all attachments", "bodyPreview": "all the attachments", "importance": "normal", "parentFolderId": "id", "conversationId": "id", "conversationIndex": "sfsdfds", "isDeliveryReceiptRequested": false, "isReadReceiptRequested": false, "isRead": true, "isDraft": false, "webLink": "https://outlook.office365.com/hgh", "inferenceClassification": "focused", "body": {"contentType": "html", "content": "<html><head>somehtml</head></html>"}, "sender": {"emailAddress": {"name": "yyyyy", "address": "yyyyy"}}, "from": {"emailAddress": {"name": "yyyyy", "address": "yyyyy"}}, "toRecipients": [{"emailAddress": {"name": "xxxx", "address": "xxxx"}}], "ccRecipients": [], "bccRecipients": [], "replyTo": [], "flag": {"flagStatus": "notFlagged"}}
```



#### Search Emails
Execute email search in the configured mailbox based on provided search criteria. If permissions allow, action can search in mailboxes other than the one provided in the integration configuration. Action is async, please adjust action timeout in IDE accordingly. Action is not working on Chronicle entities. 
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Search in Mailbox|By default, the search will be executed in the default mailbox specified in the integration configuration. If permissions allow, action can search in other mailboxes as well. Parameter accepts multiple values as a comma separated string. Note that it’s not recommended to perform a search against a big number of mailboxes with this action, for complex searches it is recommended to use Exchange Extension Pack.|True|String|Default Mailbox|
|Folder Name|Specify the mailbox folder to search in. '/' separator can be used to specify a subfolder to search in, example: Inbox/Subfolder|False|String|Inbox|
|Subject Filter|Specify the subject of the email to search for. Filter works with “contains” logic.|False|String||
|Sender Filter|Specify the sender of the email to search for. Filter works with “equals” logic.|False|String||
|Time Frame (minutes)|Specify time frame in minutes to search emails for.|False|String||
|Max Emails To Return|Specify how many emails action should return. If value is not provided, API default is used.|False|String||
|Only Unread|If enabled, action will search only for unread emails.|False|Boolean|false|
|Select All Fields For Return|If enabled, action will return all available fields for the found email.|False|Boolean|false|
|How many mailboxes to process in a single batch|Specify how many mailboxes action should process in a single batch (single connection to O365). If nothing is provided, default value of 25 will be used.|False|String|25|
|Limit the Amount of Information Returned in the JSON Result|If enabled, the amount of information returned by the action will be limited only to the key email fields.|False|Boolean|false|
|Disable the Action JSON Result|If enabled, action will not return JSON result.|False|Boolean|false|
|Recipient Filter|Filter condition, specify who should be the recipient of needed emails|False|String||
|Body Regex Filter|Specify a regex pattern that needs to be searched in body part of the email.|False|String||
|Message IDs|A comma-separated list of message ids that need to be searched. Note: this filter has priority over the other ones.|False|String||
|Start Time|Specify the start time for the email search. Format: ISO 8601. This parameter has a priority over "Time Frame (minutes)".|False|String||
|End Time|Specify the end time for the email search. Format: ISO 8601. If nothing is provided and "Start Time" is valid then this parameter will use current time.|False|String||
|Search in all mailboxes|If checked, search in all mailboxes accessible.|False|Boolean|false|



##### JSON Results
```json
[{"Mailbox": "abcd@g.com", "Emails": [{"id": "xxxx", "createdDateTime": "2024-01-12T07:48:13Z", "lastModifiedDateTime": "2024-01-12T08:25:54Z", "changeKey": "xxxx", "categories": [], "receivedDateTime": "2024-01-12T07:48:14Z", "sentDateTime": "2024-01-12T07:48:10Z", "hasAttachments": false, "internetMessageId": "xxxx", "subject": "xxxx", "bodyPreview": "xxxx", "importance": "normal", "parentFolderId": "xxxx", "conversationId": "xxxx", "conversationIndex": "xxxx", "isDeliveryReceiptRequested": null, "isReadReceiptRequested": false, "isRead": true, "isDraft": false, "webLink": "dddm", "inferenceClassification": "focused", "body": {"contentType": "text", "content": "xxxx"}, "sender": {"emailAddress": {"name": "xxxx", "address": "xxxx"}}, "from": {"emailAddress": {"name": "xxxx", "address": "xxxx"}}, "toRecipients": [{"emailAddress": {"name": "xxxx", "address": "xxxx"}}], "ccRecipients": [], "bccRecipients": [], "replyTo": [], "flag": {"flagStatus": "notFlagged"}}]}]
```



#### Send Email
Send email from a specific mailbox to an arbitrary list of recipients. Action can send either plain text or html emails. If permissions allow, action can send an email from a mailbox different that is specified in the integration configuration. Note: Action is not running on Chronicle entities.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Send From|Specify the optional email address from which if permissions allow, email should be sent. By default, the email will be sent from the default mailbox specified in the integration configuration.|True|String|Default Mailbox|
|Subject|Specify the mail subject part.|True|String||
|Send to|Specify the arbitrary comma separated list of email addresses for the email recipients. For example: user1@company.co, user2@company.co|True|String||
|CC|Specify the arbitrary comma separated list of email addresses to be put in the CC field of email. Format is the same as for the "Send to" field.|False|String||
|BCC|Arbitrary comma separated list of email addresses to be put in the BCC field of email. Format is the same as for the "Send to" field.|False|String||
|Attachments Paths|Specify the attachments to be added, parameter expects full paths to be provided, for example: /<work directory>/file1.pdf. Parameter accepts multiple values as a comma separated string.|False|String||
|Mail Content Type|Specify the type of email content: either plain text or html.|False|List|Text|
|Mail Content|Specify the email body part.|True|String||
|Reply-To Recipients|Specify a comma-separated list of recipients that will be used in the "Reply-To" header. Note: The Reply-To header is added when the originator of the message wants any replies to the message to go to that particular email address rather than the one in the "From:" address.|False|String||
|Attachment Location|Location where the attachments to be added are stored. By default, the action attempts to get the attachment from the Google Cloud storage bucket, another option is to fetch it from the local file system.|True|List|GCP Bucket|
|Base64 Encoded Certificate|Base64 encoded certificate used for S/MIME digital signing.|False|Password|*****|
|Base64 Encoded Private Key|Base64 encoded private key used for S/MIME digital signing.|False|Password|*****|
|Base64 Encoded Recipient Certificate|Base64 encoded recipient certificate used for encryption.|False|Password|*****|



##### JSON Results
```json
{"createdDateTime": "2024-01-30T16:50:27Z", "lastModifiedDateTime": "2024-01-30T16:50:27Z", "changeKey": "cxsdjjh", "categories": [], "receivedDateTime": "2024-01-30T16:50:27Z", "sentDateTime": "2024-01-30T16:50:27Z", "hasAttachments": false, "internetMessageId": "sdfhsjdfhjsdjfd", "subject": "Testing", "bodyPreview": "bbcbcb", "importance": "normal", "parentFolderId": "id", "conversationId": "id", "conversationIndex": "sfsdfds", "isDeliveryReceiptRequested": false, "isReadReceiptRequested": false, "isRead": true, "isDraft": false, "webLink": "https://www.example.com/about", "inferenceClassification": "focused", "body": {"contentType": "html", "content": "hdhdhd"}, "sender": {"emailAddress": {"name": "sdjsdjs", "address": "example@mail.com"}}, "from": {"emailAddress": {"name": "jdsjdjs", "address": "example@mail.com"}}, "toRecipients": [{"emailAddress": {"name": "example@mail.com", "address": "example@mail.com"}}], "ccRecipients": [], "bccRecipients": [], "replyTo": [], "uniqueBody": {"contentType": "html", "content": "ssfsf"}, "flag": {"flagStatus": "notFlagged"}, "id": "xxxxx"}
```



#### Send Thread Reply
Send a message as a reply to the email thread. If permissions allow, action can send an email from a mailbox different that is specified in the integration configuration. Note: Action is not running on Chronicle entities.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Send From|Specify the optional email address from which if permissions allow, email should be sent. By default, the email will be sent from the default mailbox specified in the integration configuration.|True|String|Default Mailbox|
|Mail ID|Specify the ID or internetMessageId of the message to which you want to send a reply.|True|String||
|Folder Name|Specify the mailbox folder to search in. '/' separator can be used to specify a subfolder to search in, example: Inbox/Subfolder|True|String|Inbox|
|Attachments Paths|Specify the attachments to be added, parameter expects full paths to be provided, for example: /<work directory>/file1.pdf. Parameter accepts multiple values as a comma separated string.|False|String||
|Mail Content|Specify the email body part.|True|String||
|Reply All|If enabled, action will send a reply to all recipients related to the original email. Note: this parameter has priority over “Reply To“ parameter.|False|Boolean||
|Reply To|Specify a comma-separated list of emails to which you want to send this reply. If nothing is provided and “Reply All“ is disabled, action will only send a reply to the sender of the email. If “Reply All“ is enabled, action will ignore this parameter.|False|String||
|Attachment Location|Location where the attachments to be added are stored. By default, the action attempts to get the attachment from the Google Cloud storage bucket, another option is to fetch it from the local file system.|True|List|GCP Bucket|



##### JSON Results
```json
{"id": "xxxx", "createdDateTime": "2024-02-02T10:57:18Z", "lastModifiedDateTime": "2024-02-02T10:57:23Z", "changeKey": "dsf+oAAQLaPjk", "categories": [], "receivedDateTime": "2024-02-02T10:57:20Z", "sentDateTime": "2024-02-02T10:57:19Z", "hasAttachments": true, "internetMessageId": "sdfhsjdfhjsdjfd", "subject": "RE: reply checking", "bodyPreview": "Reply check kr", "importance": "normal", "parentFolderId": "id", "conversationId": "id", "conversationIndex": "sdghfjfke", "isDeliveryReceiptRequested": false, "isReadReceiptRequested": false, "isRead": true, "isDraft": false, "webLink": "https://www.example.com/about", "inferenceClassification": "focused", "body": {"contentType": "text", "content": "Reply check kr"}, "sender": {"emailAddress": {"name": "aff", "address": "ddxsm@a.com"}}, "from": {"emailAddress": {"name": "fasf", "address": "ddxsm@a.com"}}, "toRecipients": [{"emailAddress": {"name": "wf", "address": "ddxsm@a.com"}}], "ccRecipients": [], "bccRecipients": [], "replyTo": [], "uniqueBody": {"contentType": "html", "content": "Reply check"}, "flag": {"flagStatus": "notFlagged"}}
```



#### Send Vote Email
Send email with easy answering options, to allow stakeholders to be included in workflow processes. This action uses Google SecOps HTML templates to format the email. If permissions allow, the action sends an email from a mailbox different than the one specified in the integration configuration. Note: This action is not running on Google SecOps entities.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Send From|Optional email address to send an email from (if permissions allow it). By default, the email is sent from the default mailbox specified in the integration configuration.|True|String|Default Mailbox|
|Subject|Email subject.|True|String||
|Send to|Arbitrary comma-separated list of email addresses for the email recipients, for example, user1@company.co, user2@company.co.|True|String||
|CC|Arbitrary comma-separated list of email addresses to use in the CC email field. Use the same format as for the "Send to" field.|False|String||
|BCC|Arbitrary comma-separated list of email addresses to use in the BCC email field. Use the same format for the "Send to" field.|False|String||
|Attachments Paths|Specify the attachments to be added, parameter expects full paths to be provided, for example: /<work directory>/file1.pdf. Parameter accepts multiple values as a comma separated string.|False|String||
|Email HTML Template|The question you would like to ask, or describe the decision you would like the recipient to be able to respond to|True|EmailContent|Email HTML Template|
|Structure of voting options|Structure of the vote to send to the recipients.|True|List|Yes/No|
|Reply-To Recipients|Comma-separated list of recipients used in the Reply-To header. Note: The Reply-To header is added to force email replies to specific email addresses instead of the email sender address stated in the From field.|False|String||
|Attachment Location|Location where the attachments to be added are stored. By default, the action attempts to get the attachment from the Google Cloud storage bucket, another option is to fetch it from the local file system.|True|List|GCP Bucket|



##### JSON Results
```json
{"createdDateTime": "2024-01-30T16:50:27Z", "lastModifiedDateTime": "2024-01-30T16:50:27Z", "changeKey": "xxxxx", "categories": [], "receivedDateTime": "2024-01-30T16:50:27Z", "sentDateTime": "2024-01-30T16:50:27Z", "hasAttachments": false, "internetMessageId": "<abcd.prod.com>", "subject": "Testing", "bodyPreview": "bbcbcb", "importance": "normal", "parentFolderId": "xxxxxxx", "conversationId": "xxxxx", "conversationIndex": "xxxxxx", "isDeliveryReceiptRequested": false, "isReadReceiptRequested": false, "isRead": true, "isDraft": false, "webLink": "https://www.example.com/about", "inferenceClassification": "focused", "body": {"contentType": "html", "content": "hdhdhd"}, "sender": {"emailAddress": {"name": "sdjsdjs", "address": "abcd@example.com"}}, "from": {"emailAddress": {"name": "jdsjdjs", "address": "abcd@gm.com"}}, "toRecipients": [{"emailAddress": {"name": "abc@example.com", "address": "abc@example.com"}}], "ccRecipients": [], "bccRecipients": [], "replyTo": [], "uniqueBody": {"contentType": "html", "content": "ssfsf"}, "flag": {"flagStatus": "notFlagged"}, "id": "xxxxx"}
```



#### Wait For Vote Email Results
Wait for the user response based on the vote email sent using the Send Vote Email action. This action is asynchronous. Adjust the action timeout in the IDE accordingly. This action is not working on Google SecOps entities.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Vote Mail Sent From|By default, the email is sent from the default mailbox specified in the integration configuration. In this parameter optionally a different value can be specified, if the vote mail was sent from a different mailbox.|True|String|Default Mailbox|
|Mail ID|ID or internetMessageId of the vote email that the action waits for. If the message was sent using Send Vote Email action, select SendVoteEmail.JSONResult|id or Send Email.JsonResult|internetMessageId field as a placeholder. The Search Emails action also can return email IDs.|True|String||
|Wait for All Recipients to Reply?|If selected, the action waits for responses from all recipients until timeout and doesn't complete execution receiving the first response.|False|Boolean|False|
|Wait Stage Exclude pattern|Regular expression to exclude specific replies from the wait stage. The regular expression works with the email subject and body. For example, you can use this parameter to exclude  automatic Out of Office emails wait for an actual user reply.|False|String||
|Folder to Check for Reply|Email folder in the mailbox that was used to send the email with question to search for the user reply in. Parameter also accepts a comma separated list of folders to check the user response in multiple folders. '/' separator can be used to specify a subfolder to search in, example: Inbox/Subfolder|False|String|Inbox|
|Folder to check for Sent Mail|Parameter can be used to specify mailbox email folder (mailbox that was used to send the email with question) to search for the sent mail in this folder. Parameter also accepts a comma separated list of folders to check the user response in multiple folders. Parameter is case sensitive. '/' separator can be used to specify a subfolder to search in, example: Inbox/Subfolder|False|String|Sent Items|
|Fetch Response Attachments|If selected and the recipient replies with an attachment, the action fetches the recipient response and adds it as an attachment for the action result.|False|Boolean|False|



##### JSON Results
```json
{"Responses": [{"recipient": "aaa@aaa.com", "vote": "Approve"}]}
```



#### Get Mailbox Account Out Of Facility Settings
Get the mailbox account out of facility (OOF) settings for the provided Google SecOps User entity. Note: This action uses the beta version of Microsoft Graph APIs.
Timeout - 600 Seconds



##### JSON Results
```json
[{"Entity": "jame.bond@ex.com", "EntityResult": {"@odata.context": "https://abc.com", "id": "abcb", "availability": "Offline", "activity": "Offline", "statusMessage": null, "outOfOfficeSettings": {"message": null, "isOutOfOffice": false}}}, {"Entity": "exchang@ex.com", "EntityResult": {"@odata.context": "https://abc.com", "id": "djds", "availability": "Offline", "activity": "Offline", "statusMessage": null, "outOfOfficeSettings": {"message": null, "isOutOfOffice": false}}}]
```



#### Mark Email as Junk
Mark an email as junk for a specific mailbox. This action adds the email sender to the list of blocked senders and moves the message to the Junk Email folder. Note: This action uses the beta version of Microsoft Graph APIs and is not running on Google SecOps entities.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Search In Mailbox|A mailbox to search for an email in. By default, the action  attempts to search for the email in the default mailbox that you specified in the integration configuration. With correct permissions, the action can execute a search in other mailboxes. Parameter accepts multiple values as a comma separated string.|True|String|Default Mailbox|
|Folder Name|A mailbox folder to search in.|True|String|Inbox|
|Mail IDs|Specify the mail ids or internetMessageIds to mark as junk. Parameter accepts multiple values as a comma separated string.|True|String||



##### JSON Results
```json

```



#### Ping
Test Connectivity
Timeout - 600 Seconds



#### Remove Block Domain
Remove specified email domains from a message rule in the given Mailbox. If the rule becomes empty, it will be deleted.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Domains|Comma-separated list of sender domains to remove (e.g., example.com).|False|String||
|Mailboxes|Mailboxes where the message rule exists. Can be a comma-separated list of user principal names.|True|String|Default Mailbox|
|Rule Name|Name of the message rule to remove these domains from.|True|String|Google SecOps - Blocked Domains|
|How many mailboxes to process in a single batch|Specify how many mailboxes action should process in a single batch. If nothing is provided, default value of 20 will be used.|False|String|20|



##### JSON Results
```json
[  
  {  
    "Entity": "example.com",  
    "EntityResult": {  
      "successful_mailboxes": [  
        "user@example.com"  
      ],  
      "failed_mailboxes": []  
    }  
  }  
]
```









## Connectors
#### Microsoft Graph Mail Connector
Connector can be used to fetch emails from the Microsoft Graph Mail service. Connector dynamic list can be used to filter specific values from the email body and subject parts using regexes. By default, regex is used to filter out the urls from the email.

|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Environment Field Name|Describes the name of the field where the environment name is stored.If environment field isn't found, environment is ""|False|String||
|Environment Regex Pattern|A regex pattern to run on the value found in the "Environment Field Name" field.Default is .* to catch all and return value unchanged.Used to allow the user to manipulate the environment field via regex logicIf regex pattern is null or empty, or the environment value is null, the final environment result is ""|False|String|.*|
|Email exclude pattern|Regular expression to exclude specific emails from being ingested by the connector. Works with both subject and body part of email. Example is, to exclude mass mailing emails like news from being ingested.|False|String||
|Azure AD Endpoint|Azure AD endpoint to connect to. Can be different for different tenant types.|True|String|https://login.microsoftonline.com|
|Microsoft Graph Endpoint|Microsoft Graph endpoint to connect to.  Can be different for different tenant types.|True|String|https://graph.microsoft.com|
|Mail Address|Mail address to use for connector.|True|String||
|Client ID|For Office 365 Oauth authentication, Client (Application) ID of Azure Active Directory App that will be used for the integration.|True|String||
|Client Secret|For Office 365 Oauth authentication, secret can be provided for the auth flow.|True|Password|*****|
|Microsoft Entra ID Directory ID|For Microsoft 365 OAuth authentication, the tenant (directory) ID of the Microsoft Entra ID application that you used in the integration.|True|String||
|Folder to check for emails|Parameter can be used to specify email folder on the mailbox to search for the emails. Parameter is case sensitive. '/' separator can be used to specify a subfolder to search in, example: Inbox/Subfolder|True|String|Inbox|
|Offset Time In Hours|Number of hours before the first connector iteration to retrieve emails from. This parameter applies to the initial connector iteration after you enable the connector for the first time, or used as a fallback value in cases where connector's last run timestamp expires.|True|Int|24|
|Max Emails Per Cycle|Fetch X emails per connector cycle|True|Int|10|
|Unread Emails Only|If checked, cases will be pulled only from unread emails|False|Boolean|false|
|Mark Emails as Read|If checked, after the emails have been pulled they will be marked as read.|False|Boolean|false|
|Disable Overflow|If enabled, the connector will ignore the Siemplify overflow mechanism when creating alerts.|False|Boolean|false|
|Attach Original EML|If checked, the original email will be attached to the case info as an eml file.|False|Boolean|false|
|Original Received Mail Prefix|Prefix to add to the extracted event keys (to, from,subject,…) from the original email received in the monitored mailbox.|False|String|orig|
|Attached Mail File Prefix|Prefix to add to the extracted event keys (to, from,subject,…) from the attached mail file received with the email in the monitored mailbox.|False|String|attach|
|Create a Separate Siemplify Alert per Attached Mail File|If enabled, connector will create multiple alerts, 1 alert per attached mail file. This behavior can be useful when processing email with multiple mail files attached and Siemplify event mapping set to create entities from attached mail file.|False|Boolean|false|
|Headers to add to events|Specify what values should be filtered from the "internetMessageHeaders" list and what will be added to the Siemplify event. By default, all headers are added, if only specific headers are needed - specify them as a comma separated list by their name, example: "DKIM-Signature", "Received", "From". If no internetHeaders should be added specify a keyword: None|False|String||
|Case Name Template|When provided, connector will add a new key called "custom_case_name" to the Siemplify Event. It can used to have a customer case name. Please refer to the documentation portal for more details. You can provide placeholders in the following format: [name of the field]. Example: Phishing - [event_mailbox]. Note: connector will use first Siemplify Event for placeholders. Only keys that have string value will be handled.|False|String||
|Alert Name Template|If provided, connector will use this value for Siemplify Alert Name. Please refer to the documentation portal for more details. You can provide placeholders in the following format: [name of the field]. Example: Phishing - [event_mailbox]. Note: connector will use first Siemplify Event for placeholders. Only keys that have string value will be handled. If nothing is provided or user provides an invalid template, connector will use the default alert name.|False|String||
|Proxy Server Address|The address of the proxy server to use.|False|String||
|Proxy Username|The proxy username to authenticate with.|False|String||
|Proxy Password|The proxy password to authenticate with.|False|Password|*****|
|Mail field source|If enabled, user's mailbox address will be fetched from the 'mail' attribute of user's details. Otherwise, user's mailbox address will be fetched from the 'userPrincipalName' field.|False|Boolean|false|
|Verify SSL|If enabled, verify the SSL certificate for the connection to the Microsoft Graph Mail server is valid.|False|Boolean|true|
|Base64 Encoded Private Key|Specify a base64 encoded private key that will be used to decrypt the email.|False|Password|*****|
|Base64 Encoded Certificate|Specify a base64 encoded certificate that will be used to decrypt the email.|False|Password|*****|
|Base64 Encoded CA certificate|Specify a base64 encoded trusted CA certificate for signature verification.|False|Password|*****|
|Extract URLs from HTML Email Part|If enabled, connector will try to extract URLs from HTML part of email. This will allow connector to extract complex URLs, but URLs from plain text part of email will not be extracted with this method. Extracted URLs will be available in urls_from_html_part event field.|False|Boolean|true|
|Event Fields to Exclude|Comma-separated list of event fields to exclude from events. Example: field1,field2|False|String||
|Exclude Attachments|If enabled, connector will not ingest email attachments and add them to cases.|False|Boolean|false|
|Bypass S/MIME Signature Verification|If enabled, the connector will ingest S/MIME signed emails without requiring a Base64 Encoded CA certificate for signature verification. The message body, headers, and attachments will be extracted directly.|False|Boolean|false|




