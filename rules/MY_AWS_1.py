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
        bad_ones = ['aws_s3_access_point', 'chieck']
        if conf.get("__address__").split(".")[0] in bad_ones:
            return CheckResult.UNKNOWN

        if conf.get("tags_all", []):
            if any(elem in conf["tags_all"][0]  for elem in ["dg", "Programme"]):
                return CheckResult.PASSED
        return CheckResult.FAILED


scanner = TagCheck()
