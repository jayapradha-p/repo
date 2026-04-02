from __future__ import annotations

from exchangelib.errors import MalformedResponseError
from exchangelib.properties import Rule
from exchangelib.services.common import EWSAccountService
from exchangelib.util import MNS, create_element, set_xml_value


PRIORITY = 1
IS_ENABLED = "true"
IS_IN_ERROR = "false"


class UpdateInboxRules(EWSAccountService):
    SERVICE_NAME = "UpdateInboxRules"

    def call(
        self,
        operation,
        rule_id=None,
        rule_name=None,
        condition=None,
        action=None,
        items=None,
        folder_id=None,
    ):
        payload = self.get_payload(
            operation, rule_id, rule_name, condition, action, items, folder_id
        )
        response = self._get_elements(payload=payload)

        for element in response:
            if isinstance(element, Exception):
                return repr(element)

        return True

    def create_element_with_value(self, name, value):
        element = create_element(name)
        set_xml_value(element, value, version=self.account.version)
        return element

    def get_payload(
        self,
        operation,
        rule_id=None,
        rule_name=None,
        condition=None,
        action=None,
        items=None,
        folder_id=None,
    ):
        update_inbox_rules = create_element("m:%s" % self.SERVICE_NAME)
        update_inbox_rules.append(
            self.create_element_with_value("m:RemoveOutlookRuleBlob", "true")
        )
        operations = create_element("m:Operations")

        if operation == "delete":
            operation = create_element("t:DeleteRuleOperation")
            operation.append(self.create_element_with_value("t:RuleId", rule_id))
        elif operation == "create":
            operation = create_element("t:CreateRuleOperation")
            operation.append(
                self.get_rule_payload(
                    rule_id, rule_name, condition, action, items, folder_id
                )
            )
        elif operation == "update":
            operation = create_element("t:SetRuleOperation")
            operation.append(
                self.get_rule_payload(
                    rule_id, rule_name, condition, action, items, folder_id
                )
            )

        if operation:
            operations.append(operation)

        update_inbox_rules.append(operations)
        return update_inbox_rules

    def get_rule_payload(
        self,
        rule_id,
        rule_name,
        condition,
        action,
        items,
        folder_id
    ):
        rule = create_element("t:Rule")

        if rule_id:
            rule.append(self.create_element_with_value("t:RuleId", rule_id))

        rule.append(self.create_element_with_value("t:DisplayName", rule_name))
        rule.append(self.create_element_with_value("t:Priority", PRIORITY))
        rule.append(self.create_element_with_value("t:IsEnabled", IS_ENABLED))
        rule.append(self.create_element_with_value("t:IsInError", IS_IN_ERROR))
        rule.append(self.get_conditions_payload(condition, items))
        rule.append(self.get_actions_payload(action, folder_id))

        return rule

    def get_conditions_payload(self, condition, items):
        conditions = create_element("t:Conditions")

        if condition == "contains_sender_strings":
            condition = create_element("t:ContainsSenderStrings")

            for item in items:
                condition.append(
                    self.create_element_with_value("t:String", item)
                )

        if condition == "from_addresses":
            condition = create_element("t:FromAddresses")

            for item in items:
                address = create_element("t:Address")
                address.append(
                    self.create_element_with_value("t:EmailAddress", item)
                )
                condition.append(address)

        conditions.append(condition)
        return conditions

    def get_actions_payload(self, action, folder_id=None):
        actions = create_element("t:Actions")

        if action == "mark_as_junk":
            move_to_folder = create_element("t:MoveToFolder")
            move_to_folder.append(
                create_element("t:FolderId", {"Id": folder_id})
            )
            actions.append(move_to_folder)

        if action == "delete":
            actions.append(
                self.create_element_with_value("t:Delete", "true")
            )

        if action == "permanent_delete":
            actions.append(
                self.create_element_with_value("t:PermanentDelete", "true")
            )

        actions.append(
            self.create_element_with_value("t:StopProcessingRules", "true")
        )

        return actions


class GetInboxRules(EWSAccountService):
    SERVICE_NAME = "GetInboxRules"
    element_container_name = "{%s}InboxRules" % MNS

    def call(self, mailbox_address):
        payload = self.get_payload(mailbox_address)

        response = self._get_elements(payload=payload)

        try:
            for item in response:
                if isinstance(item, Exception):
                    raise item

                yield Rule.from_xml(elem=item, account=self.account)

        except MalformedResponseError:
            return []

    def get_payload(self, mailbox_address):
        get_inbox_rules = create_element("m:%s" % self.SERVICE_NAME)
        mailbox_smtp_address = create_element("m:MailboxSmtpAddress")
        set_xml_value(
            mailbox_smtp_address, mailbox_address, version=self.account.version
        )
        get_inbox_rules.append(mailbox_smtp_address)
        return get_inbox_rules
