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


class BootDiagnosticsInstanceView(Model):
    """The instance view of a virtual machine boot diagnostics.

    :param console_screenshot_blob_uri: The console screenshot blob URI.
    :type console_screenshot_blob_uri: str
    :param serial_console_log_blob_uri: The Linux serial console log blob Uri.
    :type serial_console_log_blob_uri: str
    :param status: The status of a virtual machine's boot diagnostics. It will
     not be set if there are no errors.
    :type status: ~azure.mgmt.compute.v2018_04_01.models.InstanceViewStatus
    """

    _attribute_map = {
        'console_screenshot_blob_uri': {'key': 'consoleScreenshotBlobUri', 'type': 'str'},
        'serial_console_log_blob_uri': {'key': 'serialConsoleLogBlobUri', 'type': 'str'},
        'status': {'key': 'status', 'type': 'InstanceViewStatus'},
    }

    def __init__(self, *, console_screenshot_blob_uri: str=None, serial_console_log_blob_uri: str=None, status=None, **kwargs) -> None:
        super(BootDiagnosticsInstanceView, self).__init__(**kwargs)
        self.console_screenshot_blob_uri = console_screenshot_blob_uri
        self.serial_console_log_blob_uri = serial_console_log_blob_uri
        self.status = status
