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

from .schedule_policy import SchedulePolicy


class SimpleSchedulePolicy(SchedulePolicy):
    """Simple policy schedule.

    All required parameters must be populated in order to send to Azure.

    :param schedule_policy_type: Required. Constant filled by server.
    :type schedule_policy_type: str
    :param schedule_run_frequency: Frequency of the schedule operation of this
     policy. Possible values include: 'Invalid', 'Daily', 'Weekly'
    :type schedule_run_frequency: str or
     ~azure.mgmt.recoveryservicesbackup.models.ScheduleRunType
    :param schedule_run_days: List of days of week this schedule has to be
     run.
    :type schedule_run_days: list[str or
     ~azure.mgmt.recoveryservicesbackup.models.DayOfWeek]
    :param schedule_run_times: List of times of day this schedule has to be
     run.
    :type schedule_run_times: list[datetime]
    :param schedule_weekly_frequency: At every number weeks this schedule has
     to be run.
    :type schedule_weekly_frequency: int
    """

    _validation = {
        'schedule_policy_type': {'required': True},
    }

    _attribute_map = {
        'schedule_policy_type': {'key': 'schedulePolicyType', 'type': 'str'},
        'schedule_run_frequency': {'key': 'scheduleRunFrequency', 'type': 'str'},
        'schedule_run_days': {'key': 'scheduleRunDays', 'type': '[DayOfWeek]'},
        'schedule_run_times': {'key': 'scheduleRunTimes', 'type': '[iso-8601]'},
        'schedule_weekly_frequency': {'key': 'scheduleWeeklyFrequency', 'type': 'int'},
    }

    def __init__(self, **kwargs):
        super(SimpleSchedulePolicy, self).__init__(**kwargs)
        self.schedule_run_frequency = kwargs.get('schedule_run_frequency', None)
        self.schedule_run_days = kwargs.get('schedule_run_days', None)
        self.schedule_run_times = kwargs.get('schedule_run_times', None)
        self.schedule_weekly_frequency = kwargs.get('schedule_weekly_frequency', None)
        self.schedule_policy_type = 'SimpleSchedulePolicy'