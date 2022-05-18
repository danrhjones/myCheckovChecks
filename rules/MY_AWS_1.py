from checkov.terraform.checks.resource.base_resource_check import BaseResourceCheck
from checkov.common.models.enums import CheckResult, CheckCategories

class TagCheck(BaseResourceCheck):
    def __init__(self):
        name = "check tags"
        checkov_id = "MY_AWS_1"
        supported_resources = ['aws_s3_bucket']
        categories = [CheckCategories.GENERAL_SECURITY]
        super().__init__(name=name, id=checkov_id, categories=categories, supported_resources=supported_resources)

    def scan_resource_conf(self, conf):

        if conf.get("tags", []):
            if set(["dg", "Programme"]).issubset(conf["tags"][0]):
                return CheckResult.PASSED
        return CheckResult.FAILED


scanner = TagCheck()