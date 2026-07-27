# playbook - 1




**Enabled:** True

**Version:** 1

**Type:** Playbook

**Priority:** 2

**Playbook Simulator:** False


### Playbook Trigger
**Trigger Type:** All

**Conditions Operator:** And

##### Conditions
|Key|Operator|Value|
|---|--------|-----|
||Equals||


### Involved Steps (Unordered)
|Step Name|Description|Integration|Original Action|
|---------|-----------|-----------|---------------|
|Siemplify_Case Comment_1|Add a comment to the case the current alert has been grouped to|Siemplify|Case Comment|
|Siemplify_Get Similar Cases_1|Search for similar cases and return their Ids|Siemplify|Get Similar Cases|
|Siemplify_Case Tag_1|Add given tag to the case the current alert is grouped to|Siemplify|Case Tag|
|Siemplify_Assign Case_1|Use the "Assign Case" action to assign the case to a user.|Siemplify|Assign Case|

