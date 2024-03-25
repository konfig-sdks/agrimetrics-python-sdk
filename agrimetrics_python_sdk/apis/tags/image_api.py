# coding: utf-8

"""
    Catalog API

    This API lists data sets available on Agrimetrics platform.

    Generated by: https://konfigthis.com
"""

from agrimetrics_python_sdk.paths.images_image_type_image_id.get import GetRawImage
from agrimetrics_python_sdk.apis.tags.image_api_raw import ImageApiRaw


class ImageApi(
    GetRawImage,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: ImageApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = ImageApiRaw(api_client)
