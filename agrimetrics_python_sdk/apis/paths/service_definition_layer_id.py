from agrimetrics_python_sdk.paths.service_definition_layer_id.get import ApiForget
from agrimetrics_python_sdk.paths.service_definition_layer_id.delete import ApiFordelete
from agrimetrics_python_sdk.paths.service_definition_layer_id.patch import ApiForpatch


class ServiceDefinitionLayerId(
    ApiForget,
    ApiFordelete,
    ApiForpatch,
):
    pass
