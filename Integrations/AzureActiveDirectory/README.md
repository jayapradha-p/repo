
# AzureActiveDirectory

Azure Active Directory (Azure AD) is Microsoft's cloud-based identity and access management service, which helps your employees sign in and access  both internal and external resources.

Python Version - V3_11
#### Parameters
|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Login API Root|None|False|String||
|API Root|None|False|String||
|Client ID|None|True|String||
|Client Secret|None|True|Password||
|Directory ID|None|True|String||
|Verify SSL|None|False|Boolean||


#### Dependencies
| |
|-|
|certifi-2024.7.4-py3-none-any.whl|
|chardet-5.2.0-py3-none-any.whl|
|TIPCommon-1.0.10-py3-none-any.whl|
|idna-3.8-py3-none-any.whl|
|charset_normalizer-3.3.2-py3-none-any.whl|
|requests-2.32.3-py3-none-any.whl|
|urllib3-2.2.2-py3-none-any.whl|


## Actions
#### Add User To a Group
Add user to a specific Azure AD group. Action expects Siemplify user entity in username@domain format and group id in 00e40000-1971-439d-80fc-d0e000001dbd format.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Group ID|Azure AD group id in 00e40000-1971-439d-80fc-d0e000001dbd format.|True|None||



#### Disable Account
Disable account in Azure Active Directory. Action expects Siemplify user entity in username@domain format.
Timeout - 600 Seconds



#### Enrich User
Enrich Siemplify User entity with information from Azure Active Directory. Action expects Siemplify user entity in username@domain format.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Fields To Return|A comma-separated list of fields that you want to return. If nothing is provided, action will return fields that are considered to be default by API.|False|None||
|Include MFA Details|If enabled, action will return MFA details about the user.|False|None||
|Include Last Sign In Details|If selected, the action retrieves the user's sign-in activity, including both interactive and non-interactive sign-in timestamps.|False|None||



#### Enrich Host
Enrich Siemplify Host entity with information from Azure Active Directory. Action finds a match for a provided Host entity based on the devices displayName field in Azure AD
Timeout - 600 Seconds



#### Enable Account
Enable account in Azure Active Directory. Action expects Siemplify user entity in username@domain format.
Timeout - 600 Seconds



#### Force Password Update
Force password update for user so the user will have to change their password on next login. Action expects Siemplify user entity in username@domain format.
Timeout - 600 Seconds



#### Is User In a Group
Check if user has membership in a specific Azure AD group. Action expects Siemplify user entity in username@domain format and group id in 00e40000-1971-439d-80fc-d0e000001dbd format.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Group ID|Azure AD group id in 00e40000-1971-439d-80fc-d0e000001dbd format.|True|None||



#### Remove User from a Group
Remove User from the specified group. Note: The user name can be provided either as a Siemplify entity or as an action input parameter. If the user name is passed to action both as an entity and input parameter - action will be executed on the input parameter. User name should be specified in username@domain format.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|User Name|Specify user name to remove from the target group. User name should be specified in username@domain format. Parameter accepts multiple values as a comma separated string.|False|None||
|Group Name|Specify group name to remove user from.|False|None||
|Group ID|Specify the ID of the group from which you want to remove the user. If both "Group Name" and "Group ID" are provided, then "Group ID" will have priority. Example of the id: 00e40000-1971-439d-80fc-d0e000001dbd.|False|None||



#### List Groups
List Azure Active Directory groups based on the specified search criteria. Note that action is not working on Siemplify entities. Additionally, filtering is working on the Name field.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Order By|Specifies the result order. Groups are sorted by their display name.|False|None||
|Results Limit|Specify max number of groups to return.|False|None||
|Filter Logic|Specify what filter logic should be applied. Filtering is working on the Name field.|False|None||
|Filter Value|Specify what value should be used in the filter. If “Equal“ is selected, action will try to find the exact match among results and if “Contains“ is selected, action will try to find results that contain that substring. If nothing is provided in this parameter, the filter will not be applied. Filtering is working on the Name field.|False|None||



#### List Users
List Azure Active Directory users based on the specified search criteria. Note that action is not working on Siemplify entities. Additionally, advanced filtering is working on the Username (userPrincipalName) field.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Filter|Specifies which fields will be included in the results. By default, we will return all the fields.|False|None||
|Order By Field|Specifies the field based on which the results are ordered.|False|None||
|Order By|Specifies the result order.|False|None||
|Results Limit|Specify max number of users to return.|False|None||
|Advanced Filter Logic|Specify what filter logic should be applied. Advanced filtering is working on the Username (userPrincipalName) field.|False|None||
|Advanced Filter Value|Specify what value should be used in the filter. If “Equal“ is selected, action will try to find the exact match among results and if “Contains“ is selected, action will try to find results that contain that substring. If nothing is provided in this parameter, the filter will not be applied.  Advanced filtering is working on the Username (userPrincipalName) field.|False|None||



#### List User's Groups Membership
List Azure AD groups user is a member of. Note: The user name can be provided either as a Siemplify entity or as an action input parameter. If the user name is passed to action both as an entity and input parameter - action will be executed on the input parameter. User name should be specified in username@domain format.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|User Name|Specify user name to return groups membership for. User name should be specified in username@domain format. Parameter accepts multiple values as a comma separated string.|False|None||
|Return Only Security Enabled Groups|If enabled, only security groups that the user is a member of will be returned.|False|None||
|Return Detailed Groups Information|If enabled, detailed information on the AD groups will be returned.|False|None||
|Filter Key|Specify the key that needs to be used to filter groups.|False|None||
|Filter Logic|Specify what filter logic should be applied. Filtering logic is working based on the value  provided in the "Filter Key" parameter.|False|None||
|Filter Value|Specify what value should be used in the filter. If "Equal" is selected, action will try to find the exact match among results and if "Contains" is selected, action will try to find results that contain that substring. If nothing is provided in this parameter, the filter will not be applied. Filtering logic is working based on the value  provided in the "Filter Key" parameter.|False|None||
|Max Records To Return|Specify how many records to return. If nothing is provided, action will return 50 records.|False|None||



#### Ping
Test connectivity to the Azure Active Directory service with parameters provided at the integration configuration page on the Marketplace tab.
Timeout - 600 Seconds



#### List Members in the Group
List members in the specified Azure AD group.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Max Records To Return|Specify how many records to return. If nothing is provided, action will return 50 records.|False|None||
|Group Name|Specify group name to return user list for.|False|None||
|Group ID|Specify the ID of the group in which you want to list the members. If both "Group Name" and "Group ID" are provided, then "Group ID" will have priority. Example of the id: 00e40000-1971-439d-80fc-d0e000001dbd.|False|None||
|Filter Key|Specify the key that needs to be used to filter group members.|False|None||
|Filter Logic|Specify what filter logic should be applied. Filtering logic is working based on the value  provided in the "Filter Key" parameter.|False|None||
|Filter Value|Specify what value should be used in the filter. If “Equal“ is selected, action will try to find the exact match among results and if "Contains" is selected, action will try to find results that contain that substring. If nothing is provided in this parameter, the filter will not be applied. Filtering logic is working based on the value  provided in the "Filter Key" parameter.|False|None||



#### Revoke User Session
Revoke user session. Supported entities: Username, Email Address (username that matches email regex).
Timeout - 600 Seconds



#### Get Manager Contact Details
Get manager contact details for user. Action expects Siemplify user entity in username@domain format.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Fields To Return|A comma-separated list of fields that you want to return. If nothing is provided, the action will return the Display Name, Mobile Phone, and Mail.|False|None||
|Include MFA Details|If enabled, action will return MFA details about the user.|False|None||
|Include Last Sign In Details|If selected, the action retrieves the user's sign-in activity, including both interactive and non-interactive sign-in timestamps.|False|None||



#### Reset User Password
Change user password to the password specified in the action. User will have to change their password on next login. Action expects User to change password for as  SecOps User entity in username@domain format or as an action input parameter. If the User name is passed to action both as a SecOps entity and input parameter - action will be executed on the input parameter.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Username|User name to change password for. Parameter expects value in a username@domain format and accepts multiple values as a comma separated string.|False|None||
|Password|User Authentication password.|True|None||









