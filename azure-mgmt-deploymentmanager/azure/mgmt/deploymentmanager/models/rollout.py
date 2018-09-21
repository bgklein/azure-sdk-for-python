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

from .tracked_resource import TrackedResource


class Rollout(TrackedResource):
    """Defines the rollout resource.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Fully qualified resource Id for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
    :vartype id: str
    :ivar name: The name of the resource
    :vartype name: str
    :ivar type: The type of the resource. Ex-
     Microsoft.Compute/virtualMachines or Microsoft.Storage/storageAccounts.
    :vartype type: str
    :param tags: Resource tags.
    :type tags: dict[str, str]
    :param location: Required. The geo-location where the resource lives
    :type location: str
    :param identity: Identity for the resource.
    :type identity: ~azure.mgmt.deploymentmanager.models.Identity
    :param build_version: Required. The version of the build being deployed.
    :type build_version: str
    :param artifact_source_id: The reference to the ARM resource Id where the
     payload is located.
    :type artifact_source_id: str
    :param target_service_topology_id: Required. The reference to the resource
     Id of the service topology from which services are chosen to be deployed.
    :type target_service_topology_id: str
    :param step_groups: Required. The list of steps that define the
     orchestration.
    :type step_groups: list[~azure.mgmt.deploymentmanager.models.Step]
    :ivar status: The current status of the rollout.
    :vartype status: str
    :ivar total_retry_attempts: The cardinal count of total number of retries
     performed on the rollout at a given time.
    :vartype total_retry_attempts: int
    :ivar operation_info: Operational information of the rollout.
    :vartype operation_info:
     ~azure.mgmt.deploymentmanager.models.RolloutOperationInfo
    :ivar services: Set of detailed step result information on target resource
     groups.
    :vartype services: list[~azure.mgmt.deploymentmanager.models.Service]
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'location': {'required': True},
        'build_version': {'required': True},
        'target_service_topology_id': {'required': True},
        'step_groups': {'required': True},
        'status': {'readonly': True},
        'total_retry_attempts': {'readonly': True},
        'operation_info': {'readonly': True},
        'services': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'location': {'key': 'location', 'type': 'str'},
        'identity': {'key': 'identity', 'type': 'Identity'},
        'build_version': {'key': 'properties.buildVersion', 'type': 'str'},
        'artifact_source_id': {'key': 'properties.artifactSourceId', 'type': 'str'},
        'target_service_topology_id': {'key': 'properties.targetServiceTopologyId', 'type': 'str'},
        'step_groups': {'key': 'properties.stepGroups', 'type': '[Step]'},
        'status': {'key': 'properties.status', 'type': 'str'},
        'total_retry_attempts': {'key': 'properties.totalRetryAttempts', 'type': 'int'},
        'operation_info': {'key': 'properties.operationInfo', 'type': 'RolloutOperationInfo'},
        'services': {'key': 'properties.services', 'type': '[Service]'},
    }

    def __init__(self, **kwargs):
        super(Rollout, self).__init__(**kwargs)
        self.identity = kwargs.get('identity', None)
        self.build_version = kwargs.get('build_version', None)
        self.artifact_source_id = kwargs.get('artifact_source_id', None)
        self.target_service_topology_id = kwargs.get('target_service_topology_id', None)
        self.step_groups = kwargs.get('step_groups', None)
        self.status = None
        self.total_retry_attempts = None
        self.operation_info = None
        self.services = None
