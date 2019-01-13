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


class AutoUserSpecification(Model):
    """Specifies the parameters for the auto user that runs a task on the Batch
    service.

    :param scope: The scope for the auto user. The default value is task.
     Possible values include: 'Task', 'Pool'
    :type scope: str or ~azure.mgmt.batch.models.AutoUserScope
    :param elevation_level: The elevation level of the auto user. nonAdmin -
     The auto user is a standard user without elevated access. admin - The auto
     user is a user with elevated access and operates with full Administrator
     permissions. The default value is nonAdmin. Possible values include:
     'NonAdmin', 'Admin'
    :type elevation_level: str or ~azure.mgmt.batch.models.ElevationLevel
    """

    _attribute_map = {
        'scope': {'key': 'scope', 'type': 'AutoUserScope'},
        'elevation_level': {'key': 'elevationLevel', 'type': 'ElevationLevel'},
    }

    def __init__(self, scope=None, elevation_level=None):
        super(AutoUserSpecification, self).__init__()
        self.scope = scope
        self.elevation_level = elevation_level
