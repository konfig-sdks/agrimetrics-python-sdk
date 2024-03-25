from agrimetrics_python_sdk.paths.data_sets_data_set_id.get import ApiForget
from agrimetrics_python_sdk.paths.data_sets_data_set_id.put import ApiForput
from agrimetrics_python_sdk.paths.data_sets_data_set_id.delete import ApiFordelete
from agrimetrics_python_sdk.paths.data_sets_data_set_id.patch import ApiForpatch


class DataSetsDataSetId(
    ApiForget,
    ApiForput,
    ApiFordelete,
    ApiForpatch,
):
    pass
