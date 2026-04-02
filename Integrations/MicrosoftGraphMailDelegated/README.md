
# MicrosoftGraphMailDelegated

This integration version uses Delegated Authentication in Microsoft 365 and requires interactive login of the user on behalf of which integration should communicate with Microsoft 365. To configure this integration, provide all parameters except for Refresh Token, and save the integration configuration, then run “Get Authorization” and “Generate Token” actions to get the token and then provide it in integration configuration to finish the process. Microsoft 365 and Office 365 deliver the power of cloud productivity to businesses of all sizes, helping save time, money, and free up valued resources. The Microsoft 365 and Office 365 plans combine the familiar Microsoft Office desktop suite with cloud-based versions of Microsoft's next-generation communications and collaboration services (including Office for the web, Microsoft Exchange Online, Microsoft Teams, and Microsoft SharePoint Online) to help users be productive from virtually anywhere through the Internet. This integration uses Microsoft Graph Mail API to communicate with Microsoft 365 and Office 365 services.

Python Version - V3_11


#### Dependencies
| |
|-|
|PyJWT-2.9.0-py3-none-any.whl|
|googleapis_common_protos-1.73.1-py3-none-any.whl|
|protobuf-6.33.6-cp39-abi3-manylinux2014_x86_64.whl|
|soupsieve-2.6-py3-none-any.whl|
|google_auth_httplib2-0.3.0-py3-none-any.whl|
|TIPCommon-2.3.5-py3-none-any.whl|
|pycparser-3.0-py3-none-any.whl|
|google_api_python_client-2.188.0-py3-none-any.whl|
|pcodedmp-1.2.6-py2.py3-none-any.whl|
|requests_toolbelt-1.0.0-py2.py3-none-any.whl|
|easygui-0.98.3-py2.py3-none-any.whl|
|EnvironmentCommon-1.0.1-py2.py3-none-any.whl|
|exceptiongroup-1.2.2-py3-none-any.whl|
|oletools-0.60.2-py2.py3-none-any.whl|
|python_dateutil-2.9.0.post0-py2.py3-none-any.whl|
|setuptools-80.9.0-py3-none-any.whl|
|urllib3-2.6.3-py3-none-any.whl|
|olefile-0.47-py2.py3-none-any.whl|
|charset_normalizer-3.4.0-py3-none-any.whl|
|cryptography-42.0.8-cp39-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl|
|lark-1.1.9-py3-none-any.whl|
|charset_normalizer-3.4.6-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl|
|compressed_rtf-1.0.6.tar.gz|
|tzlocal-5.2-py3-none-any.whl|
|pyasn1_modules-0.4.2-py3-none-any.whl|
|chardet-5.2.0-py3-none-any.whl|
|emaildata-0.3.4-py3-none-any.whl|
|sniffio-1.3.1-py3-none-any.whl|
|anyio-4.13.0-py3-none-any.whl|
|siemplify_html2text-2020.1.16-py3-none-any.whl|
|icalendar-6.0.1-py3-none-any.whl|
|RTFDE-0.1.2-py3-none-any.whl|
|extract_msg-0.52.0-py3-none-any.whl|
|requests-2.32.5-py3-none-any.whl|
|h11-0.16.0-py3-none-any.whl|
|pyparsing-3.3.2-py3-none-any.whl|
|pycryptodome-3.23.0-cp37-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl|
|pyOpenSSL-24.1.0-py3-none-any.whl|
|tzdata-2024.2-py2.py3-none-any.whl|
|cachetools-5.5.0-py3-none-any.whl|
|cffi-2.0.0-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.whl|
|google_api_core-2.30.0-py3-none-any.whl|
|proto_plus-1.27.2-py3-none-any.whl|
|colorclass-2.2.2-py2.py3-none-any.whl|
|pyasn1-0.6.3-py3-none-any.whl|
|rsa-4.9.1-py3-none-any.whl|
|google_auth-2.47.0-py3-none-any.whl|
|msoffcrypto_tool-5.4.2-py3-none-any.whl|
|red-black-tree-mod-1.20.tar.gz|
|certifi-2026.2.25-py3-none-any.whl|
|idna-3.11-py3-none-any.whl|
|pyopenssl-25.3.0-py3-none-any.whl|
|ebcdic-1.1.1-py2.py3-none-any.whl|
|IMAPClient-3.0.1-py2.py3-none-any.whl|
|typing_extensions-4.15.0-py3-none-any.whl|
|pyth3-0.7-py3-none-any.whl|
|cryptography-46.0.6-cp311-abi3-manylinux_2_34_x86_64.whl|
|beautifulsoup4-4.12.3-py3-none-any.whl|
|httpx-0.28.1-py3-none-any.whl|
|six-1.16.0-py2.py3-none-any.whl|
|uritemplate-4.2.0-py3-none-any.whl|
|pytz-2024.2-py2.py3-none-any.whl|
|httpcore-1.0.9-py3-none-any.whl|
|httplib2-0.31.2-py3-none-any.whl|


## Actions
#### Delete Email
You can use the Delete Email action to delete one or more emails from a mailbox. This action deletes emails based on your search criteria. With the appropriate permissions, the Delete Email action can move emails into different mailboxes. This action is asynchronous. Adjust the action timeout in the Google SecOps IDE accordingly. This action doesn't run on Google SecOps entities.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
||A filter condition that specifies the period in minutes to search for emails.||None||
||If selected, the action searches only for unread emails.||None||
||The number of mailboxes to process in a single batch (a single connection to the Microsoft 365 server). The default value is 25.||None||
||If enabled, the amount of information returned by the action will be limited only to the key email fields.||None||
||If enabled, action will not return JSON result.||None||
||The default mailbox to execute the delete operation in. If permissions allow it, the action executes search in other mailboxes. This parameter accepts multiple values as a comma-separated string.||None||
||A mailbox folder in which to search for an email. To specify a subfolder, use the “/” forward slash, such as {Inbox/Subfolder}.||None||
||A filter condition to search for emails with specific email IDs. This parameter accepts a comma-separated list of email IDs to search for. If this parameter is provided, the search ignores the Subject Filter and Sender Filter parameters.||None||
||A filter condition that specifies the email subject to search for. This filter uses the contains logic.||None||
||A filter condition that specifies the sender of requested emails. This filter uses the equals logic.||None||



#### Get Mailbox Account Out Of Facility Settings
Use the Get Mailbox Account Out Of Facility Settings action to retrieve the mailbox account out of facility (OOF) settings for the Google SecOps User entity provided. The Get Mailbox Account Out Of Facility Settings action uses the beta version of Microsoft Graph API. This action runs on the Google SecOps User entity.
Timeout - 600 Seconds



#### Send Vote Email
Use the Send Vote Email action to send emails with the predefined answering options. This action uses Google SecOps HTML templates to format the email. With appropriate permissions, the Send Vote Email action can send emails from a mailbox other than the default one. This action doesn't run on Google SecOps entities.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
||An optional email address from which to send an email if permissions allow it. By default, the email is sent from the default mailbox that is specified in the integration configuration.||None||
||The email subject.||None||
||A comma-separated list of email addresses for the email recipients, such as user1@example.com, user2@example.com.||None||
||A comma-separated list of email addresses for the email CC field, such as user1@example.com, user2@example.com.||None||
||A comma-separated list of email addresses for the email BCC field, such as user1@example.com, user2@example.com.||None||
||A comma-separated list of paths for file attachments stored on the server, for example, /{FILE_DIRECTORY}/file.pdf, /{FILE_DIRECTORY}/image.jpg.||None||
||The type of the HTML template to use. The default value is Email HTML Template.||None||
||The structure of the vote to send to recipients. The possible values are Yes/No or Approve/Reject. The default value is Yes/No.||None||
||A comma-separated list of recipients to use in the Reply-To header. Use the Reply-To header to redirect reply emails to the specific email address instead of the sender address that is stated in the From field.||None||
||A location where the attachments are stored. By default, the action attempts to upload attachments from the Cloud Storage bucket. The possible values are GCP Bucket or Local File System. The default value is GCP Bucket.||None||



#### Extract Data from Attached EML
Use the Extract Data From Attached EML action to retrieve data from the email EML attachments and return it in the action results. This action supports the .eml, .msg, and .ics file formats. This action doesn't run on Google SecOps entities.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
||The default mailbox to execute the search operation in. If permissions allow it, the action can search in other mailboxes. This parameter accepts multiple values as a comma-separated string.||None||
||A mailbox folder in which to search for an email. To specify a subfolder, use the “/” forward slash, such as {Inbox/Subfolder}.||None||
||A filter condition to search for emails with specific email IDs or internetMessageId values. This parameter accepts a comma-separated list of email IDs to search for.||None||
||A JSON definition that contains regular expressions to apply to the attached email file and generate additional key values in the action JSON result. The example of this parameter value is as follows: {ips: \b\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}\b}||None||



#### Download Attachments from Email
Use the Download Attachments From Email action to download attachments from emails based on the criteria provided. This action doesn't run on Google SecOps entities. This action is asynchronous. Adjust the script timeout value in the Google SecOps IDE. The action replaces the “/” forward slash and “\”  backslash characters in the names of the downloaded attachments with the “_” underscore character.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
||The default mailbox to execute the search operation in. If permissions allow it, the action can search in other mailboxes. This parameter accepts multiple values as a comma-separated string.||None||
||A mailbox folder in which to search for an email. To specify a subfolder, use the “/” forward slash, such as {Inbox/Subfolder}.||None||
||A location to save the downloaded attachments. By default, the action attempts to save the attachment to the Cloud Storage bucket. Saving an attachment to the local file system is a fallback option. The possible values are GCP Bucket and Local File System. The default value is GCP Bucket.||None||
||A path to download attachments to. When saving attachments to the Cloud Storage bucket or a local file system, the action expects you to specify the download path in the Unix-like format, such as"/tmp/test"||None||
||A filter condition to search for emails with specific email IDs or internetMessageId values. This parameter accepts a comma-separated list of email IDs to search for. If this parameter is provided, the search ignores the Subject Filter and Sender Filter parameters.||None||
||A filter condition that specifies the email subject to search for. This filter uses the contains logic.||None||
||A filter condition that specifies the sender of requested emails. This filter uses the equals logic.||None||
||If selected, the action downloads attachments from EML files.||None||
||If selected, the action downloads attachments to the unique path provided in the Download Path parameter to avoid overwriting any previously downloaded attachments.||None||
||The number of mailboxes to process in a single batch (a single connection to the Microsoft 365 server). The default value is 25.||None||



#### Forward Email
Use the Forward Email action to forward emails that include previous threads. With the appropriate permissions, this action can send emails from a mailbox different than the one specified in the integration configuration. This action doesn't run on Google SecOps entities.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
||A location where the attachments are stored. By default, the action attempts to upload attachments from the Cloud Storage bucket. The possible values are GCP Bucket or Local File System. The default value is GCP Bucket.||None||
||An optional email address from which to send an email if permissions allow it. By default, the email is sent from the default mailbox that is specified in the integration configuration.||None||
||The email ID or the internetMessageId value of the email to forward.||None||
||A mailbox folder in which to search for an email. To specify a subfolder, use the “/” forward slash, such as {Inbox/Subfolder}.||None||
||The email subject.||None||
||A comma-separated list of email addresses for the email recipients, such as user1@example.com, user2@example.com.||None||
||A comma-separated list of email addresses for the email CC field, such as user1@example.com, user2@example.com.||None||
||A comma-separated list of email addresses for the email BCC field, such as user1@example.com, user2@example.com.||None||
||A comma-separated list of paths for file attachments stored on the server, for example, /{FILE_DIRECTORY}/file.pdf, /{FILE_DIRECTORY}/image.jpg.||None||
||The email body.||None||



#### Save Email to the Case
Use the Save Email To The Case action to save emails or email attachments to the Google SecOps Case Wall. With the appropriate permissions, this action can save emails from mailboxes other than the one provided in the integration configuration. This action doesn't run on Google SecOps entities.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
||The default mailbox in which to execute the search operation. If permissions allow it, the action can search in other mailboxes.||None||
||A mailbox folder in which to search for an email. To specify a subfolder, use the “/” forward slash, such as {Inbox/Subfolder}.||None||
||The email ID or the internetMessageId value to search for. This parameter accepts a comma-separated list of email IDs to search for. If you used the Send Mail action to send emails, set the parameter value to the {SendEmail.JSONResult|id} or {SendEmail.JSONResult|internetMessageId}  placeholder.||None||
||If selected, the action saves only attachments from the specified email.||None||
||If you select the Save Only Email Attachments parameter, the action only saves attachments specified by this parameter. This parameter accepts multiple values as a comma-separated string.||None||
||If selected, the action encodes the email file into the base64 format.||None||
||If selected, the action saves the specified email to the action Case Wall in Google Secops.||None||



#### Search Emails
Use the Search Emails action to execute email search in the default mailbox based on the provided search criteria. With appropriate permissions, this action can run a search in other mailboxes. This action is asynchronous. Adjust the action timeout in the Google SeOps IDE accordingly. This action doesn't run on Google SecOps entities.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
||The default mailbox to execute the search operation in. If permissions allow it, the action can search in other mailboxes. This parameter accepts multiple values as a comma-separated string. For complex searches against a significant number of mailboxes, use the Exchange Extension Pack integration.||None||
||A mailbox folder to execute the search in. To specify a subfolder, use the “/” forward slash, such as {Inbox/Subfolder}.||None||
||A filter condition that specifies the email subject to search for. This filter uses the contains logic.||None||
||A filter condition that specifies the sender of requested emails. This filter uses the equals logic.||None||
||A filter condition that specifies the period in minutes to search for emails.||None||
||The number of emails for the action to return. If you don't set a value, the action uses the API default value. The default value is 10.||None||
||If selected, the action searches only for unread emails.||None||
||If selected, the action returns all available fields for the obtained email.||None||
||The number of mailboxes to process in a single batch (a single connection to the Microsoft 365 server). The default value is 25.||None||
||If enabled, the amount of information returned by the action will be limited only to the key email fields.||None||
||If enabled, action will not return JSON result.||None||



#### Wait For Email From User
Use the Wait For Email From User action to wait for the user's response that is based on an email sent using the Send Email action. This action is asynchronous. Adjust the action timeout in the Google SecOps IDE accordingly. This action doesn't run on Google SecOps entities.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
||The ID of the email. If you used the Send Mail action to send emails, set the parameter value to the {SendEmail.JSONResult|id} or {SendEmail.JSONResult|internetMessageId} placeholder.||None||
||If selected, the action waits for responses from all recipients until reaching timeout or proceeding with the first reply.||None||
||A regular expression to exclude specific replies from the wait stage. This parameter works with the email body. For example, if you configure the “Out of Office.*” regular expression, the action doesn't consider automatic out-of-office messages as recipient replies and waits for an actual user reply.||None||
||A mailbox email folder to search for the user reply in. The search is run in the mailbox which the email containing a question was sent from. This parameter accepts a comma-separated list of folders to check the user response in multiple folders. This parameter is case-sensitive. The default value is Inbox.||None||
||If selected and the recipient reply contains attachments, the action fetches the reply and adds it as an attachment to the action result.||None||
||If enabled, the amount of information returned by the action will be limited only to the key email fields.||None||
||If enabled, action will not return JSON result.||None||



#### Generate Token
Use the Generate Token action to obtain a refresh token for the integration configuration with delegated authentication. Use the authorization URL that you received in the Get Authorization action. This action doesn't run on Google SecOps entities. After you generate the refresh token for the first time, we recommend you to configure and activate the Refresh Token Renewal Job so the job automatically renews and keeps the refresh token valid.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
||An authorization URL that you received in the Get Authorization action. The URL is required to request a refresh token.||None||



#### Send Email HTML
Use the Send Email HTML action to send emails you use the Google SecOps HTML template from a specific mailbox to an arbitrary list of recipients. With appropriate permissions, the action can send emails from a mailbox other than the default one. This action doesn't run on Google SecOps entities.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
||An optional email address from which to send an email if permissions allow it. By default, the email is sent from the default mailbox that is specified in the integration configuration||None||
||The email subject.||None||
||A comma-separated list of email addresses for the email recipients, such as user1@example.com, user2@example.com.||None||
||A comma-separated list of email addresses for the email CC field, such as user1@example.com, user2@example.com.||None||
||A comma-separated list of email addresses for the email BCC field, such as user1@example.com, user2@example.com.||None||
||A comma-separated list of paths for file attachments stored on the server, for example, /{FILE_DIRECTORY}/file.pdf, /{FILE_DIRECTORY}/image.jpg.||None||
||The type of the HTML template to use. The default value is Email HTML Template.||None||
||A comma-separated list of recipients to use in the Reply-To header. Use the Reply-To header to redirect reply emails to the specific email address instead of the sender address that is stated in the From field.||None||
||A location where the attachments are stored. By default, the action attempts to upload attachments from the Cloud Storage bucket. The possible values are GCP Bucket or Local File System. The default value is GCP Bucket.||None||



#### Wait For Vote Email Results
Use the Wait For Vote Email Results action to wait for the user response based on the vote email sent using the Send Vote Email action. This action is asynchronous. Adjust the action timeout in the Google SecOps IDE accordingly. This action doesn't run on Google SecOps entities.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
||The mailbox from which an email is sent using the Send Vote Email action. The default value is the mailbox that you specified in the integration configuration. Optionally, you can set a different value for this parameter if the vote mail is sent from a different mailbox.||None||
||The ID of the email. If the email is sent using the Send Vote Email action, set the parameter value to the SendVoteEmail.JSONResult|id or SendEmail.JSONResult|internetMessageId placeholder. To return email IDs, you can use the Search Emails action.||None||
||If selected, the action waits for responses from all recipients until reaching timeout or proceeding with the first reply. Selected by default.||None||
||A regular expression to exclude specific replies from the wait stage. This parameter works with the email body. For example, if you configure the “Out of Office.*” regular expression, the action doesn't consider automatic out-of-office messages as recipient replies and waits for an actual user reply.||None||
||A mailbox email folder to search for the user reply. The action searches in the mailbox from which you sent the email with a question. This parameter accepts a comma-separated list of folders to check the user response in multiple folders. To specify a subfolder, use the “/” forward slash, such as {Inbox/Subfolder}. This parameter is case-sensitive. The default value is Inbox.||None||
||A mailbox folder to search for the sent mail. The action searches in the mailbox from which you sent the email with a question. This parameter accepts a comma-separated list of folders to check the user response in multiple folders. To specify a subfolder, use the “/” forward slash, such as {Inbox/Subfolder}. This parameter is case-sensitive. The default value is Sent Items.||None||
||If selected and the recipient reply contains attachments, the action fetches the reply and adds it as an attachment to the action result.||None||



#### Move Email To Folder
Use the Move Email To Folder action to move one or multiple emails from the source email folder to the other folder in the mailbox. With the appropriate permissions, this action can move emails to other mailboxes different from the one that is provided in the integration configuration. This action is asynchronous. Adjust the action timeout in the Google SecOps IDE accordingly. This action doesn't run on Google SecOps entities.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
||The default mailbox to execute the move operation in. If permissions allow it, the action can search in other mailboxes as well. This parameter accepts multiple values as a comma-separated string.||None||
||A source folder from which to move the email. To specify a subfolder, use the “/” forward slash, such as {Inbox/Subfolder}.||None||
||A destination folder to move the email to. Provide the parameter value in the following format: {Inbox/folder_name/subfolder_name}. This parameter is case-insensitive.||None||
||A filter condition to search for emails with specific email IDs. This parameter accepts a comma-separated list of email IDs to search for. If you configure this parameter, the search ignores the Subject Filter and Sender Filter parameters.||None||
||A filter condition that specifies the email subject to search for. This filter uses the contains logic.||None||
||A filter condition that specifies the sender of requested emails. This filter uses the equals logic.||None||
||A filter condition that specifies the period in minutes to search for emails.||None||
||If selected, the action searches only for unread emails.||None||
||The number of mailboxes to process in a single batch (a single connection to the Microsoft 365 server). The default value is 25.||None||
||If enabled, the amount of information returned by the action will be limited only to the key email fields.||None||
||If enabled, action will not return JSON result.||None||



#### Run Microsoft Search Query
Use the Run Microsoft Search Query action to perform a search using Microsoft Search engine. The search bases on the constructed basic or advanced query that you specify. For more information about Microsoft Search, see Overview of the Microsoft Search API in Microsoft Graph (https://learn.microsoft.com/en-us/graph/search-concept-overview). This action doesn’t run on Google SecOps entities.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
||A comma-separated list of expected resource types for the search response. The possible values are as follows: event, message, driveItem, externalItem, site, list, listItem, drive, chatMessage, person, acronym, bookmark.||None||
||The fields to return in the search response. If you don’t configure this parameter, the action returns all available fields.||None||
||The query to run the search. For more information about the search query examples, see Use the Microsoft Search API to search Outlook messages(https://learn.microsoft.com/en-us/graph/search-concept-messages).||None||
||The maximum number of rows for the action to return. If you don’t configure this parameter, the action uses the default value. The default value is 25.||None||
||The full search payload to use instead of constructing the search query with other action parameters. Format the search payload as a JSON string. If you configure this parameter, the action ignores all other parameters.||None||



#### Send Thread Reply
Use the Send Thread Reply action to send a message as a reply to the email thread. With appropriate permissions, the action can send emails from a mailbox other than the one specified in the integration configuration. This action doesn't run on Google SecOps entities.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
||An optional email address from which to send emails if permissions allow it. By default, the action sends emails from the default mailbox that is specified in the integration configuration.||None||
||The email ID or the internetMessageId value of the email to reply to.||None||
||A mailbox folder in which to search for an email. To specify a subfolder, use the “/” forward slash, such as {Inbox/Subfolder}.||None||
||A comma-separated list of paths for file attachments stored on the server, for example, /{FILE_DIRECTORY}/file.pdf, /{FILE_DIRECTORY}/image.jpg.||None||
||The email body.||None||
||If selected, the action sends a reply to all recipients related to the original email. Not selected by default. This parameter has priority over the Reply To parameter.||None||
||A comma-separated list of emails to reply to. If you don't set a value and the Reply All checkbox is clear, the action only sends a reply to the original email sender. If you select the Reply All checkbox, the action ignores this parameter.||None||
||A location where the attachments are stored. By default, the action attempts to upload attachments from the Cloud Storage bucket. The possible values are GCP Bucket or Local File System. The default value is GCP Bucket.||None||



#### Send Email
Use the Send Email action to send emails from a specific mailbox to an arbitrary list of recipients. This action can send either plain text or HTML-formatted emails. With appropriate permissions, the action can send emails from a mailbox different than the one specified in the integration configuration. This action doesn't run on Google SecOps entities.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
||An optional email address from which to send emails if permissions allow it. By default, the action sends emails from the default mailbox specified in the integration configuration.||None||
||The email subject.||None||
||A comma-separated list of email addresses for the email recipients, such as user1@example.com, user2@example.com.||None||
||A comma-separated list of email addresses for the email CC field, such as user1@example.com, user2@example.com.||None||
||A comma-separated list of email addresses for the email BCC field, such as user1@example.com, user2@example.com.||None||
||A comma-separated list of paths for file attachments stored on the server, for example, /{FILE_DIRECTORY}/file.pdf, /{FILE_DIRECTORY}/image.jpg.||None||
||The type of the email content. The default value is Text.||None||
||The email body.||None||
||A comma-separated list of recipients to use in the Reply-To header. Use the Reply-To header to redirect reply emails to the specific email address instead of the sender address that is stated in the From field.||None||
||A location where the attachments are stored. By default, the action attempts to upload attachments from the Cloud Storage bucket. The possible values are GCP Bucket or Local File System. The default value is GCP Bucket.||None||



#### Mark Email as Junk
Use the Mark Email as Junk action to mark emails as junk in a specified mailbox. This action adds the email sender to the list of blocked senders and moves the message to the Junk Email folder. The Mark Email as Junk action uses the beta version of Microsoft Graph API. This action doesn't run on Google SecOps entities.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
||A mailbox to search for an email in. By default, the action attempts to search for the email in the default mailbox that you specified in the integration configuration. To execute a search in other mailboxes, configure appropriate permissions for the action. This parameter accepts multiple values as a comma-separated string.||None||
||A mailbox folder in which to search for an email. To specify a subfolder, use the “/” forward slash, such as {Inbox/Subfolder}.||None||
||A comma-separated string of the mail IDs or internetMessageId values of the emails to mark as junk.||None||



#### Get Authorization
Use the Get Authorization action to obtain a link with the access code for the integration configuration with delegated authentication. Copy the whole link and use it in the Generate Token action to get the refresh token. This action doesn't run on Google SecOps entities.
Timeout - 600 Seconds



#### Ping
Use the Ping action to test connectivity to the Microsoft Graph mail service. This action doesn't run on Google SecOps entities.
Timeout - 600 Seconds



#### Mark Email as Not Junk
Use the Mark Email as Not Junk action to mark emails as not junk in a specific mailbox. This action removes the sender from the list of blocked senders and moves the message to the Inbox folder. The Mark Email as Not Junk action uses the beta version of Microsoft Graph API. This action doesn't run on Google SecOps entities.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
||A mailbox to search for an email in. By default, the action attempts to search for the email in the default mailbox that you specified in the integration configuration. To execute a search in other mailboxes, configure appropriate permissions for the action. This parameter accepts multiple values as a comma-separated string.||None||
||A mailbox folder in which to search for an email. To specify a subfolder, use the “/” forward slash, such as {Inbox/Subfolder}.||None||
||A comma-separated string of the mail IDs or internetMessageId values of the emails to mark as not junk.||None||






## Jobs

#### Refresh Token Renewal Job
Token renewal job should be used to periodically update the refresh token configured for the integration. By default, the refresh token expires every 90 days, making integration unusable upon expiration. It is recommended to run this job every 7 or 14 days to make sure that refresh token will be up to date.

|Name|IsMandatory|Type|DefaultValue|
|----|-----------|----|------------|
|||None||
|||None||



## Connectors
#### Microsoft Graph Mail Delegated Connector
Connector can be used to fetch emails from the Microsoft Graph Mail service. Connector dynamic list can be used to filter specific values from the email body and subject parts using regexes. By default, regex is used to filter out the urls from the email. This connector uses Delegated Authentication in Microsoft 365 and requires interactive login of the user on behalf of which integration should communicate with Microsoft 365. To configure the connector, make sure that the integration configuration is already finished, and the refresh token needed to communicate with Office 365 is generated.

|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
||The name of the field where the environment name is stored. If the environment field isn't found, the environment is the default environment. The default value is ""||None||
||A regular expression pattern to run on the value found in the Environment Field Name field. This parameter lets you manipulate the environment field using the regular expression logic. Use the default value .* to retrieve the required raw Environment Field Name value. If the regular expression pattern is null or empty, or the environment value is null, the final environment result is the default environment.||None|.*|
||A regular expression to exclude specific emails from ingestion, such as spam or news. This parameter works with both the subject and body of the email.||None||
||The Microsoft Entra endpoint to connect to. The default value is https://login.microsoftonline.com.||None|https://login.microsoftonline.com|
||The Microsoft Graph endpoint to connect to. The default value is https://graph.microsoft.com.||None|https://graph.microsoft.com|
||An email address for the connector to use.||None||
||The refresh token that you obtained after you generated a token.||None||
||For Microsoft 365 OAuth 2.0 authentication, the application (client) ID of the Microsoft Entra application that is used in the integration.||None||
||For Microsoft 365 OAuth 2.0 authentication, the client secret value that is provided for the authentication flow.||None||
||For Microsoft 365 OAuth authentication, the tenant (directory) ID of the Microsoft Entra ID application that you used in the integration.||None||
||An email folder to search for the emails. This parameter accepts a comma-separated list of folders to check the user response in multiple folders. To specify a subfolder, use the “/” forward slash, such as {Inbox/Subfolder}. This parameter is case-sensitive. The default value is Inbox.||None|Inbox|
||The number of hours before the first connector iteration to retrieve the incidents from. This parameter applies to the initial connector iteration after you enable the connector for the first time. The connector can use this parameter as a fallback value when the timestamp from the latest connector iteration expires.||None|24|
||The maximum number of emails to fetch for every connector iteration.||None|10|
||If selected, the connector creates cases only for unread emails.||None|false|
||If selected, the connector marks ingested emails as read.||None|false|
||If selected, the connector ignores the Google SecOps overflow mechanism.||None|false|
||If selected, the integration verifies that the SSL certificate for connecting to the Microsoft Graph server is valid.||None|true|
||Specify a base64 encoded private key that will be used to decrypt the email.||None||
||Specify a base64 encoded certificate that will be used to decrypt the email.||None||
||Specify a base64 encoded trusted CA certificate for signature verification.||None||
||If selected, the connector retrieves the mailbox address from the user details “mail” attribute. If not selected, the integration retrieves the mailbox address from the “userPrincipalName” field. Selected by default.||None|true|
||A prefix to add to the extracted event keys (for example, to, from, or subject) from the original email received in the monitored mailbox. The default value is orig.||None|orig|
||A prefix to add to the extracted event keys (for example, to, from, or subject) from the attached email file received in the monitored mailbox. The default value is attach.||None|attach|
||If selected, the connector creates multiple alerts, with one alert for every attached email file. This behavior is useful when you process emails with multiple email files attached and set the Google SecOps event mapping to create entities from attached email files.||None|false|
||If selected, the connector attaches the original email to the case info as an EML file.||None|false|
||A comma-separated string of email headers to add to Google SecOps events, such as “DKIM-Siganture”, “Received”, “From”. You can provide an exact match for headers or set this parameter value as a regular expression. The connector filters the configured values from the “internetMessageHeaders” list and adds them to the Google SecOps event. By default, the connector adds all available headers. To prevent the connector from adding headers to the event, set the parameter value as follows: None.||None||
||A custom case name. When you configure this parameter, the connector adds a new key called custom_case_name to the Google SecOps event. You can provide placeholders in the following format: [name of the field]. Example: Phishing - [event_mailbox]. For placeholders, the connector uses the first Google SecOps event. The connector only handles keys that contain the string value.||None||
||A custom alert name. You can provide placeholders in the following format: [name of the field]. Example: Phishing - [event_mailbox]. For placeholders, the connector uses the first Google SecOps event. The connector only handles keys that contain the string value. If you configure an invalid template or don't set a value, the connector uses the default alert name.||None||
||The address of the proxy server to use.||None||
||The proxy server username to authenticate with.||None||
||The proxy password to authenticate with.||None||




