
# ActiveDirectory

Microsoft Active Directory integration facilitates the centralized management and synchronization of Windows user accounts with Security Center's administrator and cardholder accounts.

Python Version - V3_11
#### Parameters
|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Server||True|String|x.x.x.x|
|Username||True|String|user@domain.com|
|Domain||True|String|domain.com|
|Password||True|Password|*****|
|Custom Query Fields||False|String||
|CA Certificate File - parsed into Base64 String||False|String||
|Use SSL||False|Boolean|False|


#### Dependencies
| |
|-|
|requests-2.33.1-py3-none-any.whl|
|urllib3-2.6.3-py3-none-any.whl|
|certifi-2026.4.22-py3-none-any.whl|
|TIPCommon-1.0.10-py3-none-any.whl|
|pyasn1-0.6.3-py3-none-any.whl|
|chardet-7.4.3-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl|
|ldap3-2.9.1-py2.py3-none-any.whl|
|idna-3.13-py3-none-any.whl|
|charset_normalizer-3.4.7-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl|


## Actions
#### Copy of Enrich entities
Enrich Hostname or Username entities with Active Directory properties
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Mark entities as internal|Specify whether successfully enriched entities should be automatically marked as “Internal Entity”|False|Boolean||
|Specific Attribute Names To Enrich With|Provide a comma separated list of attribute names to enrich the entities with. If nothing is provided - action will enrich with all available attributes. If an attribute contains a few values - it will be enriched with all of the available values. Parameter is case sensitive.|False|String||
|Should Case Wall Table be filtered by the specified Attributes?|If checked, the Case Wall Table for this action will only present the specified attributes, found in the “Specific Attribute Names To Enrich With” parameter.|False|Boolean|false|
|Should JSON result be filtered by the specified Attributes?|If checked, the JSON result for this action will only return the specified attributes, found in the “Specific Attribute Names To Enrich With” parameter.|False|Boolean|false|



##### JSON Results
```json
"[{\"Entity\": \"test\", \"EntityResult\": {\"accountExpires\": [\"9999-12-31 23:59:59.999999+00:00\"], \"adminCount\": [1], \"badPasswordTime\": [\"2021-03-02 15:33:46.599745+00:00\"], \"badPwdCount\": [0], \"cn\": [\"test\"], \"codePage\": [0], \"countryCode\": [0], \"dSCorePropagationData\": [\"2021-05-06 22:11:27+00:00\", \"1601-01-01 00:00:00+00:00\"], \"displayName\": [\"test\"], \"distinguishedName\": [\"CN=test,CN=Users,DC=xxxxb2019,DC=local\"], \"garbageCollPeriod\": [1209600], \"givenName\": [\"test\"], \"homeMDB\": [\"CN=Mailbox Database 0058301203,CN=Databases,CN=Exchange Administrative Group (FYDIBOHF23SPDLT),CN=Administrative Groups,CN=mwc,CN=Microsoft Exchange,CN=Services,CN=Configuration,DC=xxxxb2019,DC=local\"], \"instanceType\": [4], \"internetEncoding\": [0], \"lastLogoff\": [\"1601-01-01 00:00:00+00:00\"], \"lastLogon\": [\"2021-03-08 21:49:57.418140+00:00\"], \"lastLogonTimestamp\": [\"2021-03-02 15:33:50.881191+00:00\"], \"legacyExchangeDN\": [\"/o=mwc/ou=Exchange Administrative Group (FYDIBOHF23SPDLT)/cn=Recipients/cn=d01b6cf255d54dd3923474833475df49-test\"], \"logonCount\": [3], \"mDBUseDefaults\": [true], \"mail\": [\"test@xxxxb2019.local\"], \"mailNickname\": [\"test\"], \"memberOf\": [\"CN=ADDGroups,CN=Users,DC=xxxxb2019,DC=local\", \"CN=US Staff,CN=Users,DC=xxxxb2019,DC=local\", \"CN=Domain Admins,CN=Users,DC=xxxxb2019,DC=local\"], \"msDS-UserPasswordExpiryTimeComputed\": [132627588006240398], \"msExchAddressBookFlags\": [1], \"msExchArchiveQuota\": [104857600], \"msExchArchiveWarnQuota\": [94371840], \"msExchBypassAudit\": [false], \"msExchCalendarLoggingQuota\": [6291456], \"msExchDelegateListLink\": [\"CN=Administrator,CN=Users,DC=xxxxb2019,DC=local\"], \"msExchDumpsterQuota\": [31457280], \"msExchDumpsterWarningQuota\": [20971520], \"msExchELCMailboxFlags\": [130], \"msExchGroupSecurityFlags\": [0], \"msExchHomeServerName\": [\"/o=mwc/ou=Exchange Administrative Group (FYDIBOHF23SPDLT)/cn=Configuration/cn=Servers/cn=xxxxB2019-EX\"], \"msExchMDBRulesQuota\": [256], \"msExchMailboxAuditEnable\": [false], \"msExchMailboxAuditLogAgeLimit\": [7776000], \"msExchMailboxFolderSet\": [0], \"msExchMailboxGuid\": [{\"encoded\": \"123456==\", \"encoding\": \"base64\"}], \"msExchMailboxSecurityDescriptor\": [{\"encoded\": \"123456==\", \"encoding\": \"base64\"}], \"msExchModerationFlags\": [6], \"msExchPoliciesIncluded\": [\"123-123-123-123-123\", \"{123-123-123-123-123}\"], \"msExchProvisioningFlags\": [0], \"msExchRBACPolicyLink\": [\"CN=Default Role Assignment Policy,CN=Policies,CN=RBAC,CN=mwc,CN=Microsoft Exchange,CN=Services,CN=Configuration,DC=xxxxb2019,DC=local\"], \"msExchRecipientDisplayType\": [1073741824], \"msExchRecipientSoftDeletedStatus\": [0], \"msExchRecipientTypeDetails\": [1], \"msExchTextMessagingState\": [302120705, 16842751], \"msExchTransportRecipientSettingsFlags\": [0], \"msExchUMDtmfMap\": [\"emailAddress:837887372\", \"lastNameFirstName:873728378\", \"firstNameLastName:837887372\"], \"msExchUMEnabledFlags2\": [-1], \"msExchUserAccountControl\": [0], \"msExchUserCulture\": [\"en-US\"], \"msExchVersion\": [88218628259840], \"msExchWhenMailboxCreated\": [\"2021-03-02 03:40:00+00:00\"], \"name\": [\"test\"], \"objectCategory\": [\"CN=Person,CN=Schema,CN=Configuration,DC=xxxxb2019,DC=local\"], \"objectClass\": [\"top\", \"person\", \"organizationalPerson\", \"user\"], \"objectGUID\": [\"{123-123-123-123-123}\"], \"objectSid\": [\"S-1-5-21-123-123-123-123\"], \"primaryGroupID\": [513], \"protocolSettings\": [\"RemotePowerShell\\u00a71\"], \"proxyAddresses\": [\"SMTP:test@xxxxb2019.local\"], \"pwdLastSet\": [\"2021-03-02 03:40:00.624041+00:00\"], \"sAMAccountName\": [\"test\"], \"sAMAccountType\": [805306368], \"showInAddressBook\": [\"CN=Mailboxes(VLV),CN=All System Address Lists,CN=Address Lists Container,CN=mwc,CN=Microsoft Exchange,CN=Services,CN=Configuration,DC=xxxxb2019,DC=local\", \"CN=All Mailboxes(VLV),CN=All System Address Lists,CN=Address Lists Container,CN=mwc,CN=Microsoft Exchange,CN=Services,CN=Configuration,DC=xxxxb2019,DC=local\", \"CN=All Recipients(VLV),CN=All System Address Lists,CN=Address Lists Container,CN=mwc,CN=Microsoft Exchange,CN=Services,CN=Configuration,DC=xxxxb2019,DC=local\", \"CN=Default Global Address List,CN=All Global Address Lists,CN=Address Lists Container,CN=mwc,CN=Microsoft Exchange,CN=Services,CN=Configuration,DC=xxxxb2019,DC=local\", \"CN=All Users,CN=All Address Lists,CN=Address Lists Container,CN=mwc,CN=Microsoft Exchange,CN=Services,CN=Configuration,DC=xxxxb2019,DC=local\"], \"sn\": [\"user2\"], \"uSNChanged\": [102817], \"uSNCreated\": [28739], \"userAccountControl\": [512], \"userPrincipalName\": [\"test@xxxxb2019.local\"], \"whenChanged\": [\"2021-05-06 22:11:27+00:00\"], \"whenCreated\": [\"2021-03-02 03:40:00+00:00\"]}}, {\"Entity\": \"xxxxB2019-EX\", \"EntityResult\": {\"accountExpires\": [\"9999-12-31 23:59:59.999999+00:00\"], \"badPasswordTime\": [\"1601-01-01 00:00:00+00:00\"], \"badPwdCount\": [0], \"cn\": [\"xxxxB2019-EX\"], \"codePage\": [0], \"countryCode\": [0], \"dNSHostName\": [\"xxxxB2019-EX.xxxxb2019.local\"], \"dSCorePropagationData\": [\"2021-03-01 22:14:54+00:00\", \"2021-03-01 22:14:54+00:00\", \"2021-03-01 22:13:05+00:00\", \"2021-03-01 22:13:04+00:00\", \"1601-07-14 22:36:49+00:00\"], \"distinguishedName\": [\"CN=xxxxB2019-EX,CN=Computers,DC=xxxxb2019,DC=local\"], \"instanceType\": [4], \"isCriticalSystemObject\": [false], \"lastLogoff\": [\"1601-01-01 00:00:00+00:00\"], \"lastLogon\": [\"2021-05-27 16:45:33.537247+00:00\"], \"lastLogonTimestamp\": [\"2021-05-21 02:00:28.131941+00:00\"], \"localPolicyFlags\": [0], \"logonCount\": [884], \"mail\": [], \"memberOf\": [\"CN=Exchange Install Domain Servers,CN=Microsoft Exchange System Objects,DC=xxxxb2019,DC=local\", \"CN=Managed Availability Servers,OU=Microsoft Exchange Security Groups,DC=xxxxb2019,DC=local\", \"CN=Exchange Trusted Subsystem,OU=Microsoft Exchange Security Groups,DC=xxxxb2019,DC=local\", \"CN=Exchange Servers,OU=Microsoft Exchange Security Groups,DC=xxxxb2019,DC=local\"], \"msDS-SupportedEncryptionTypes\": [28], \"msDS-UserPasswordExpiryTimeComputed\": [9223372036854775807], \"msExchCapabilityIdentifiers\": [1], \"msExchRMSComputerAccountsBL\": [\"CN=FederatedEmail.123-123-123-123-123,CN=Users,DC=xxxxb2019,DC=local\"], \"name\": [\"xxxxB2019-EX\"], \"objectCategory\": [\"CN=Computer,CN=Schema,CN=Configuration,DC=xxxxb2019,DC=local\"], \"objectClass\": [\"top\", \"person\", \"organizationalPerson\", \"user\", \"computer\"], \"objectGUID\": [\"{123-123-123-123-123}\"], \"objectSid\": [\"S-1-5-21-123-123-123-123\"], \"operatingSystem\": [\"Windows Server 2019 Standard Evaluation\"], \"operatingSystemVersion\": [\"10.0 (17763)\"], \"primaryGroupID\": [515], \"pwdLastSet\": [\"2021-05-01 14:28:29.910906+00:00\"], \"sAMAccountName\": [\"xxxxB2019-EX$\"], \"sAMAccountType\": [805306369], \"servicePrincipalName\": [\"IMAP/xxxxB2019-EX\", \"IMAP/xxxxB2019-EX.xxxxb2019.local\", \"IMAP4/xxxxB2019-EX\", \"IMAP4/xxxxB2019-EX.xxxxb2019.local\", \"POP/xxxxB2019-EX\", \"POP/xxxxB2019-EX.xxxxb2019.local\", \"POP3/xxxxB2019-EX\", \"POP3/xxxxB2019-EX.xxxxb2019.local\", \"exchangeRFR/xxxxB2019-EX\", \"exchangeRFR/xxxxB2019-EX.xxxxb2019.local\", \"exchangeAB/xxxxB2019-EX\", \"exchangeAB/xxxxB2019-EX.xxxxb2019.local\", \"exchangeMDB/xxxxB2019-EX\", \"exchangeMDB/xxxxB2019-EX.xxxxb2019.local\", \"SMTP/xxxxB2019-EX\", \"SMTP/xxxxB2019-EX.xxxxb2019.local\", \"SmtpSvc/xxxxB2019-EX\", \"SmtpSvc/xxxxB2019-EX.xxxxb2019.local\", \"TERMSRV/xxxxB2019-EX\", \"TERMSRV/xxxxB2019-EX.xxxxb2019.local\", \"WSMAN/xxxxB2019-EX\", \"WSMAN/xxxxB2019-EX.xxxxb2019.local\", \"RestrictedKrbHost/xxxxB2019-EX\", \"HOST/xxxxB2019-EX\", \"RestrictedKrbHost/xxxxB2019-EX.xxxxb2019.local\", \"HOST/xxxxB2019-EX.xxxxb2019.local\"], \"uSNChanged\": [119324], \"uSNCreated\": [12744], \"userAccountControl\": [4096], \"whenChanged\": [\"2021-05-21 02:00:28+00:00\"], \"whenCreated\": [\"2021-03-01 18:23:27+00:00\"]}}]"
```



#### Add User To Group
Add user to groups.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Group Name|Specify a comma-separated list of groups to which action should add users.|True|String|None|



#### Change User OU
Change a user's Organizational Unit (OU)
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|OU Name|The name of the new user's OU|True|String|None|



#### Disable account
Disable the user account 
Timeout - 600 Seconds



#### Change Host OU
Change a Host's Organizational Unit (OU)
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|OU Name|The name of the new user's OU|True|String|None|



#### Disable computer
Disable a computer account
Timeout - 600 Seconds



#### Enable account
Enable the user account
Timeout - 600 Seconds



#### Enable computer
Enable a computer account
Timeout - 600 Seconds



#### Enrich entities
Enrich Hostname or Username entities with Active Directory properties
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Mark entities as internal|Specify whether successfully enriched entities should be automatically marked as “Internal Entity”|False|Boolean||
|Specific Attribute Names To Enrich With|Provide a comma separated list of attribute names to enrich the entities with. If nothing is provided - action will enrich with all available attributes. If an attribute contains a few values - it will be enriched with all of the available values. Parameter is case sensitive.|False|String||
|Should Case Wall Table be filtered by the specified Attributes?|If checked, the Case Wall Table for this action will only present the specified attributes, found in the “Specific Attribute Names To Enrich With” parameter.|False|Boolean|false|
|Should JSON result be filtered by the specified Attributes?|If checked, the JSON result for this action will only return the specified attributes, found in the “Specific Attribute Names To Enrich With” parameter.|False|Boolean|false|



##### JSON Results
```json
"[{\"Entity\": \"test\", \"EntityResult\": {\"accountExpires\": [\"9999-12-31 23:59:59.999999+00:00\"], \"adminCount\": [1], \"badPasswordTime\": [\"2021-03-02 15:33:46.599745+00:00\"], \"badPwdCount\": [0], \"cn\": [\"test\"], \"codePage\": [0], \"countryCode\": [0], \"dSCorePropagationData\": [\"2021-05-06 22:11:27+00:00\", \"1601-01-01 00:00:00+00:00\"], \"displayName\": [\"test\"], \"distinguishedName\": [\"CN=test,CN=Users,DC=xxxxb2019,DC=local\"], \"garbageCollPeriod\": [1209600], \"givenName\": [\"test\"], \"homeMDB\": [\"CN=Mailbox Database 0058301203,CN=Databases,CN=Exchange Administrative Group (FYDIBOHF23SPDLT),CN=Administrative Groups,CN=mwc,CN=Microsoft Exchange,CN=Services,CN=Configuration,DC=xxxxb2019,DC=local\"], \"instanceType\": [4], \"internetEncoding\": [0], \"lastLogoff\": [\"1601-01-01 00:00:00+00:00\"], \"lastLogon\": [\"2021-03-08 21:49:57.418140+00:00\"], \"lastLogonTimestamp\": [\"2021-03-02 15:33:50.881191+00:00\"], \"legacyExchangeDN\": [\"/o=mwc/ou=Exchange Administrative Group (FYDIBOHF23SPDLT)/cn=Recipients/cn=d01b6cf255d54dd3923474833475df49-test\"], \"logonCount\": [3], \"mDBUseDefaults\": [true], \"mail\": [\"test@xxxxb2019.local\"], \"mailNickname\": [\"test\"], \"memberOf\": [\"CN=ADDGroups,CN=Users,DC=xxxxb2019,DC=local\", \"CN=US Staff,CN=Users,DC=xxxxb2019,DC=local\", \"CN=Domain Admins,CN=Users,DC=xxxxb2019,DC=local\"], \"msDS-UserPasswordExpiryTimeComputed\": [132627588006240398], \"msExchAddressBookFlags\": [1], \"msExchArchiveQuota\": [104857600], \"msExchArchiveWarnQuota\": [94371840], \"msExchBypassAudit\": [false], \"msExchCalendarLoggingQuota\": [6291456], \"msExchDelegateListLink\": [\"CN=Administrator,CN=Users,DC=xxxxb2019,DC=local\"], \"msExchDumpsterQuota\": [31457280], \"msExchDumpsterWarningQuota\": [20971520], \"msExchELCMailboxFlags\": [130], \"msExchGroupSecurityFlags\": [0], \"msExchHomeServerName\": [\"/o=mwc/ou=Exchange Administrative Group (FYDIBOHF23SPDLT)/cn=Configuration/cn=Servers/cn=xxxxB2019-EX\"], \"msExchMDBRulesQuota\": [256], \"msExchMailboxAuditEnable\": [false], \"msExchMailboxAuditLogAgeLimit\": [7776000], \"msExchMailboxFolderSet\": [0], \"msExchMailboxGuid\": [{\"encoded\": \"123456==\", \"encoding\": \"base64\"}], \"msExchMailboxSecurityDescriptor\": [{\"encoded\": \"123456==\", \"encoding\": \"base64\"}], \"msExchModerationFlags\": [6], \"msExchPoliciesIncluded\": [\"123-123-123-123-123\", \"{123-123-123-123-123}\"], \"msExchProvisioningFlags\": [0], \"msExchRBACPolicyLink\": [\"CN=Default Role Assignment Policy,CN=Policies,CN=RBAC,CN=mwc,CN=Microsoft Exchange,CN=Services,CN=Configuration,DC=xxxxb2019,DC=local\"], \"msExchRecipientDisplayType\": [1073741824], \"msExchRecipientSoftDeletedStatus\": [0], \"msExchRecipientTypeDetails\": [1], \"msExchTextMessagingState\": [302120705, 16842751], \"msExchTransportRecipientSettingsFlags\": [0], \"msExchUMDtmfMap\": [\"emailAddress:837887372\", \"lastNameFirstName:873728378\", \"firstNameLastName:837887372\"], \"msExchUMEnabledFlags2\": [-1], \"msExchUserAccountControl\": [0], \"msExchUserCulture\": [\"en-US\"], \"msExchVersion\": [88218628259840], \"msExchWhenMailboxCreated\": [\"2021-03-02 03:40:00+00:00\"], \"name\": [\"test\"], \"objectCategory\": [\"CN=Person,CN=Schema,CN=Configuration,DC=xxxxb2019,DC=local\"], \"objectClass\": [\"top\", \"person\", \"organizationalPerson\", \"user\"], \"objectGUID\": [\"{123-123-123-123-123}\"], \"objectSid\": [\"S-1-5-21-123-123-123-123\"], \"primaryGroupID\": [513], \"protocolSettings\": [\"RemotePowerShell\\u00a71\"], \"proxyAddresses\": [\"SMTP:test@xxxxb2019.local\"], \"pwdLastSet\": [\"2021-03-02 03:40:00.624041+00:00\"], \"sAMAccountName\": [\"test\"], \"sAMAccountType\": [805306368], \"showInAddressBook\": [\"CN=Mailboxes(VLV),CN=All System Address Lists,CN=Address Lists Container,CN=mwc,CN=Microsoft Exchange,CN=Services,CN=Configuration,DC=xxxxb2019,DC=local\", \"CN=All Mailboxes(VLV),CN=All System Address Lists,CN=Address Lists Container,CN=mwc,CN=Microsoft Exchange,CN=Services,CN=Configuration,DC=xxxxb2019,DC=local\", \"CN=All Recipients(VLV),CN=All System Address Lists,CN=Address Lists Container,CN=mwc,CN=Microsoft Exchange,CN=Services,CN=Configuration,DC=xxxxb2019,DC=local\", \"CN=Default Global Address List,CN=All Global Address Lists,CN=Address Lists Container,CN=mwc,CN=Microsoft Exchange,CN=Services,CN=Configuration,DC=xxxxb2019,DC=local\", \"CN=All Users,CN=All Address Lists,CN=Address Lists Container,CN=mwc,CN=Microsoft Exchange,CN=Services,CN=Configuration,DC=xxxxb2019,DC=local\"], \"sn\": [\"user2\"], \"uSNChanged\": [102817], \"uSNCreated\": [28739], \"userAccountControl\": [512], \"userPrincipalName\": [\"test@xxxxb2019.local\"], \"whenChanged\": [\"2021-05-06 22:11:27+00:00\"], \"whenCreated\": [\"2021-03-02 03:40:00+00:00\"]}}, {\"Entity\": \"xxxxB2019-EX\", \"EntityResult\": {\"accountExpires\": [\"9999-12-31 23:59:59.999999+00:00\"], \"badPasswordTime\": [\"1601-01-01 00:00:00+00:00\"], \"badPwdCount\": [0], \"cn\": [\"xxxxB2019-EX\"], \"codePage\": [0], \"countryCode\": [0], \"dNSHostName\": [\"xxxxB2019-EX.xxxxb2019.local\"], \"dSCorePropagationData\": [\"2021-03-01 22:14:54+00:00\", \"2021-03-01 22:14:54+00:00\", \"2021-03-01 22:13:05+00:00\", \"2021-03-01 22:13:04+00:00\", \"1601-07-14 22:36:49+00:00\"], \"distinguishedName\": [\"CN=xxxxB2019-EX,CN=Computers,DC=xxxxb2019,DC=local\"], \"instanceType\": [4], \"isCriticalSystemObject\": [false], \"lastLogoff\": [\"1601-01-01 00:00:00+00:00\"], \"lastLogon\": [\"2021-05-27 16:45:33.537247+00:00\"], \"lastLogonTimestamp\": [\"2021-05-21 02:00:28.131941+00:00\"], \"localPolicyFlags\": [0], \"logonCount\": [884], \"mail\": [], \"memberOf\": [\"CN=Exchange Install Domain Servers,CN=Microsoft Exchange System Objects,DC=xxxxb2019,DC=local\", \"CN=Managed Availability Servers,OU=Microsoft Exchange Security Groups,DC=xxxxb2019,DC=local\", \"CN=Exchange Trusted Subsystem,OU=Microsoft Exchange Security Groups,DC=xxxxb2019,DC=local\", \"CN=Exchange Servers,OU=Microsoft Exchange Security Groups,DC=xxxxb2019,DC=local\"], \"msDS-SupportedEncryptionTypes\": [28], \"msDS-UserPasswordExpiryTimeComputed\": [9223372036854775807], \"msExchCapabilityIdentifiers\": [1], \"msExchRMSComputerAccountsBL\": [\"CN=FederatedEmail.123-123-123-123-123,CN=Users,DC=xxxxb2019,DC=local\"], \"name\": [\"xxxxB2019-EX\"], \"objectCategory\": [\"CN=Computer,CN=Schema,CN=Configuration,DC=xxxxb2019,DC=local\"], \"objectClass\": [\"top\", \"person\", \"organizationalPerson\", \"user\", \"computer\"], \"objectGUID\": [\"{123-123-123-123-123}\"], \"objectSid\": [\"S-1-5-21-123-123-123-123\"], \"operatingSystem\": [\"Windows Server 2019 Standard Evaluation\"], \"operatingSystemVersion\": [\"10.0 (17763)\"], \"primaryGroupID\": [515], \"pwdLastSet\": [\"2021-05-01 14:28:29.910906+00:00\"], \"sAMAccountName\": [\"xxxxB2019-EX$\"], \"sAMAccountType\": [805306369], \"servicePrincipalName\": [\"IMAP/xxxxB2019-EX\", \"IMAP/xxxxB2019-EX.xxxxb2019.local\", \"IMAP4/xxxxB2019-EX\", \"IMAP4/xxxxB2019-EX.xxxxb2019.local\", \"POP/xxxxB2019-EX\", \"POP/xxxxB2019-EX.xxxxb2019.local\", \"POP3/xxxxB2019-EX\", \"POP3/xxxxB2019-EX.xxxxb2019.local\", \"exchangeRFR/xxxxB2019-EX\", \"exchangeRFR/xxxxB2019-EX.xxxxb2019.local\", \"exchangeAB/xxxxB2019-EX\", \"exchangeAB/xxxxB2019-EX.xxxxb2019.local\", \"exchangeMDB/xxxxB2019-EX\", \"exchangeMDB/xxxxB2019-EX.xxxxb2019.local\", \"SMTP/xxxxB2019-EX\", \"SMTP/xxxxB2019-EX.xxxxb2019.local\", \"SmtpSvc/xxxxB2019-EX\", \"SmtpSvc/xxxxB2019-EX.xxxxb2019.local\", \"TERMSRV/xxxxB2019-EX\", \"TERMSRV/xxxxB2019-EX.xxxxb2019.local\", \"WSMAN/xxxxB2019-EX\", \"WSMAN/xxxxB2019-EX.xxxxb2019.local\", \"RestrictedKrbHost/xxxxB2019-EX\", \"HOST/xxxxB2019-EX\", \"RestrictedKrbHost/xxxxB2019-EX.xxxxb2019.local\", \"HOST/xxxxB2019-EX.xxxxb2019.local\"], \"uSNChanged\": [119324], \"uSNCreated\": [12744], \"userAccountControl\": [4096], \"whenChanged\": [\"2021-05-21 02:00:28+00:00\"], \"whenCreated\": [\"2021-03-01 18:23:27+00:00\"]}}]"
```



#### Force password update
Force user password update on the next logon
Timeout - 600 Seconds



#### Release Locked Account
Release locked account
Timeout - 600 Seconds



#### Get Manager Contact Details
Get manager's contact details from active directory
Timeout - 600 Seconds



##### JSON Results
```json
[{"EntityResult": {"primaryGroupID": [513], "logonCount": [6505], "cn": ["user name"], "countryCode": [0], "objectClass": ["top", "person", "organizationalPerson"], "userPrincipalName": ["user@domain.com"], "adminCount": [1], "lastLogonTimestamp": ["2019-01-09 08:42:03.540783+00:00"], "manager": ["CN=user name,OU=R&D,OU=TLV,OU=host name,DC=domain,DC=LOCAL"], "instanceType": [4], "distinguishedName": ["CN=user name,OU=R&D,OU=TLV,OU=host,DC=domain,DC=LOCAL"], "dSCorePropagationData": ["2019-01-14 14:39:16+00:00"], "msDS-SupportedEncryptionTypes": [0], "objectSid": ["id"], "whenCreated": ["2011-11-07 08:00:44+00:00"], "uSNCreated": [7288202], "lockoutTime": ["1601-01-01 00:00:00+00:00"], "badPasswordTime": ["date"], "pwdLastSet": ["date"], "sAMAccountName": ["name"], "objectCategory": ["CN=Person,CN=Schema,CN=Configuration,DC=host,DC=LOCAL"], "lastLogon": ["2019-01-14 17:13:54.463070+00:00"], "objectGUID": ["{id}"], "whenChanged": ["2019-01-14 16:49:01+00:00"], "badPwdCount": [1], "accountExpires": ["9999-12-31 23:59:59.999999"], "displayName": ["user display name"], "name": ["user name"], "memberOf": ["CN=\\u05e7\\u05d1\\u05d5\\u05e6\\u05d4 \\u05d1\\u05e2\\u05d1\\u05e8\\u05d9\\u05ea,OU=TEST,OU=QA,OU=IT,OU=TLV,OU=host,DC=domain,DC=LOCAL", "CN=Organization Management,OU=Microsoft Exchange Security Groups,DC=domain,DC=LOCAL", "CN=Local Admin,OU=Groups,OU=IT,OU=TLV,OU=host,DC=domain,DC=LOCAL"], "codePage": [0], "userAccountControl": [111], "sAMAccountType": [805306368], "uSNChanged": [15301168], "sn": ["last name"], "givenName": ["name"], "lastLogoff": ["1601-01-01 00:00:00+00:00"]}, "Entity": "john_doe@example.com"}]
```



#### Get Group Members
Get the members list of the provided group name in Active Directory
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Group Name|Specify whether the name of the group of which you would like to list down the group members.|True|String||
|Members Type|Specify the member type of the group.|True|List|User|
|Perform Nested Search|Specify whether the action should fetch additional details regarding groups found in the main group.|False|Boolean|false|
|Limit|Specify the maximum number of listings to fetch from Active Directory|True|String|100|



##### JSON Results
```json
[{"cn": "Test Usexx", "displayName": "Test Usexx", "distinguishedName": "CN=Test Usexx,OU=User Accounts,DC=siemplifyxxx,DC=local"}, {"cn": "test usexxx", "displayName": "test usexxx", "distinguishedName": "CN=test usexxx,CN=Users,DC=siemplifyxxx,DC=local"}, {"cn": "test usexxx", "displayName": "test usexxx8", "distinguishedName": "CN=test usexxx,CN=Users,DC=siemplifyxxxx,DC=local"}]
```



#### List User Groups
Get list of all users groups in Active Directory
Timeout - 600 Seconds



##### JSON Results
```json
[{"EntityResult": ["Domain Users"], "Entity": "username@example.local"}]
```



#### Search Active Directory
Search Active Directory with Siemplify, using your personal query.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Query String|Specify the query string you would like to perform in AD.|True|String||
|Limit|Specify the maximum number of listings to fetch from Active Directory.|False|String||



##### JSON Results
```json
[{"primaryGroupID": [513], "logonCount": [6505], "cn": ["user name"], "countryCode": [0], "objectClass": ["top", "person", "organizationalPerson"], "userPrincipalName": ["user@domain.com"], "adminCount": [1], "lastLogonTimestamp": ["2019-01-09 08:42:03.540783+00:00"], "manager": ["CN=user name,OU=R&D,OU=TLV,OU=host name,DC=domain,DC=LOCAL"], "instanceType": [4], "distinguishedName": ["CN=user name,OU=R&D,OU=TLV,OU=host,DC=domain,DC=LOCAL"], "dSCorePropagationData": ["2019-01-14 14:39:16+00:00"], "msDS-SupportedEncryptionTypes": [0], "objectSid": ["id"], "whenCreated": ["2011-11-07 08:00:44+00:00"], "uSNCreated": [7288202], "lockoutTime": ["1601-01-01 00:00:00+00:00"], "badPasswordTime": ["date"], "pwdLastSet": ["date"], "sAMAccountName": ["name"], "objectCategory": ["CN=Person,CN=Schema,CN=Configuration,DC=host,DC=LOCAL"], "lastLogon": ["2019-01-14 17:13:54.463070+00:00"], "objectGUID": ["{id}"], "whenChanged": ["2019-01-14 16:49:01+00:00"], "badPwdCount": [1], "accountExpires": ["9999-12-31 23:59:59.999999"], "displayName": ["user display name"], "name": ["user name"], "memberOf": ["CN=\\u05e7\\u05d1\\u05d5\\u05e6\\u05d4 \\u05d1\\u05e2\\u05d1\\u05e8\\u05d9\\u05ea,OU=TEST,OU=QA,OU=IT,OU=TLV,OU=host,DC=domain,DC=LOCAL", "CN=Organization Management,OU=Microsoft Exchange Security Groups,DC=domain,DC=LOCAL", "CN=Local Admin,OU=Groups,OU=IT,OU=TLV,OU=host,DC=domain,DC=LOCAL"], "codePage": [0], "userAccountControl": [111], "sAMAccountType": [805306368], "uSNChanged": [15301168], "sn": ["last name"], "givenName": ["name"], "lastLogoff": ["1601-01-01 00:00:00+00:00"]}]
```



#### Set User Password
Set a user's password
Note - For this action, please make sure to have a verified SSL connection and a strong password that will match the password rules in your organization
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|New Password|New Password|True|Password|*****|



#### Remove User From Group
Remove user from groups.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Group Name|Specify a comma-separated list of groups from which action should remove users.|True|String|None|



#### Update attributes of an AD User
Update attributes of an existing Active Directory users.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Attribute Name|The name of the attribute to update. Default: Description.|True|String|Description|
|Attribute Value|The attribute value to update.|True|String|None|



#### Is User In Group
Check whether a user is a member of a specific group
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|GroupName|Group name to be checked. e.g. Administrators. Please make sure group name is spelled correctly, and exists in Active Directory.|True|String||



##### JSON Results
```json
[{"EntityResult": true, "Entity": "VICKIE.B@SIEMPLIFY.CO"}, {"EntityResult": false, "Entity": "F.ATTACKER4@GMAIL.COM"}, {"EntityResult": true, "Entity": "test.user10@siemplifylab.local"}]
```



#### Update attributes of an AD Host
Update attributes of an existing Active Directory hosts.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Attribute Name|The name of the attribute to update. Default: Description.|True|String|Description|
|Attribute Value|The attribute value to update.|True|String|None|



#### Ping
Test Active Directory connectivity
Timeout - 600 Seconds









