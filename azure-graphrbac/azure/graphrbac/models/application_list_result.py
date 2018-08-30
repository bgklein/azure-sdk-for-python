# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ApplicationListResult(Model):
    """Application list operation result.

    :param value: A collection of applications.
    :type value: list[~azure.graphrbac.models.Application]
    :param odatanext_link: The URL to get the next set of results.
    :type odatanext_link: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[Application]'},
        'odatanext_link': {'key': 'odata\\.nextLink', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ApplicationListResult, self).__init__(**kwargs)
        self.value = kwargs.get('value', None)
        self.odatanext_link = kwargs.get('odatanext_link', None)
