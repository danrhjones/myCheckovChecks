from checkov.terraform.checks.resource.base_resource_check import BaseResourceCheck
from checkov.common.models.enums import CheckResult, CheckCategories

class TagCheck(BaseResourceCheck):
    def __init__(self):
        name = "check tags"
        checkov_id = "MY_AWS_1"
        supported_resources = ['*']
        categories = [CheckCategories.GENERAL_SECURITY]
        super().__init__(name=name, id=checkov_id, categories=categories, supported_resources=supported_resources)

    def scan_resource_conf(self, conf):
        if conf.get("tags", []):
            if any(elem in conf["tags"][0]  for elem in ["dg", "Programme"]):
#             if set(conf["tags"][0]).issubset(["dg", "Programme"]):
                return CheckResult.PASSED
        return CheckResult.FAILED


scanner = TagCheck()
