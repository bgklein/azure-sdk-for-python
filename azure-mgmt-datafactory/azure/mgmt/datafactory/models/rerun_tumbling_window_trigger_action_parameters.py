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


class RerunTumblingWindowTriggerActionParameters(Model):
    """Rerun tumbling window trigger Parameters.

    All required parameters must be populated in order to send to Azure.

    :param start_time: Required. The start time for the time period for which
     restatement is initiated. Only UTC time is currently supported.
    :type start_time: datetime
    :param end_time: Required. The end time for the time period for which
     restatement is initiated. Only UTC time is currently supported.
    :type end_time: datetime
    :param max_concurrency: Required. The max number of parallel time windows
     (ready for execution) for which a rerun is triggered.
    :type max_concurrency: int
    """

    _validation = {
        'start_time': {'required': True},
        'end_time': {'required': True},
        'max_concurrency': {'required': True, 'maximum': 50, 'minimum': 1},
    }

    _attribute_map = {
        'start_time': {'key': 'startTime', 'type': 'iso-8601'},
        'end_time': {'key': 'endTime', 'type': 'iso-8601'},
        'max_concurrency': {'key': 'maxConcurrency', 'type': 'int'},
    }

    def __init__(self, **kwargs):
        super(RerunTumblingWindowTriggerActionParameters, self).__init__(**kwargs)
        self.start_time = kwargs.get('start_time', None)
        self.end_time = kwargs.get('end_time', None)
        self.max_concurrency = kwargs.get('max_concurrency', None)