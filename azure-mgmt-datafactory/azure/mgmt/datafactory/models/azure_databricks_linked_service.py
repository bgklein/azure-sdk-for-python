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

from .linked_service import LinkedService


class AzureDatabricksLinkedService(LinkedService):
    """Azure Databricks linked service.

    All required parameters must be populated in order to send to Azure.

    :param additional_properties: Unmatched properties from the message are
     deserialized this collection
    :type additional_properties: dict[str, object]
    :param connect_via: The integration runtime reference.
    :type connect_via:
     ~azure.mgmt.datafactory.models.IntegrationRuntimeReference
    :param description: Linked service description.
    :type description: str
    :param parameters: Parameters for linked service.
    :type parameters: dict[str,
     ~azure.mgmt.datafactory.models.ParameterSpecification]
    :param annotations: List of tags that can be used for describing the
     Dataset.
    :type annotations: list[object]
    :param type: Required. Constant filled by server.
    :type type: str
    :param domain: Required. <REGION>.azuredatabricks.net, domain name of your
     Databricks deployment. Type: string (or Expression with resultType
     string).
    :type domain: object
    :param access_token: Required. Access token for databricks REST API. Refer
     to https://docs.azuredatabricks.net/api/latest/authentication.html. Type:
     string (or Expression with resultType string).
    :type access_token: ~azure.mgmt.datafactory.models.SecretBase
    :param existing_cluster_id: The id of an existing cluster that will be
     used for all runs of this job. Type: string (or Expression with resultType
     string).
    :type existing_cluster_id: object
    :param new_cluster_version: The Spark version of new cluster. Type: string
     (or Expression with resultType string).
    :type new_cluster_version: object
    :param new_cluster_num_of_worker: Number of worker nodes that new cluster
     should have. A string formatted Int32, like '1' means numOfWorker is 1 or
     '1:10' means auto-scale from 1 as min and 10 as max. Type: string (or
     Expression with resultType string).
    :type new_cluster_num_of_worker: object
    :param new_cluster_node_type: The node types of new cluster. Type: string
     (or Expression with resultType string).
    :type new_cluster_node_type: object
    :param new_cluster_spark_conf: a set of optional, user-specified Spark
     configuration key-value pairs.
    :type new_cluster_spark_conf: dict[str, object]
    :param new_cluster_custom_tags: Additional tags for cluster resources.
    :type new_cluster_custom_tags: dict[str, object]
    :param encrypted_credential: The encrypted credential used for
     authentication. Credentials are encrypted using the integration runtime
     credential manager. Type: string (or Expression with resultType string).
    :type encrypted_credential: object
    """

    _validation = {
        'type': {'required': True},
        'domain': {'required': True},
        'access_token': {'required': True},
    }

    _attribute_map = {
        'additional_properties': {'key': '', 'type': '{object}'},
        'connect_via': {'key': 'connectVia', 'type': 'IntegrationRuntimeReference'},
        'description': {'key': 'description', 'type': 'str'},
        'parameters': {'key': 'parameters', 'type': '{ParameterSpecification}'},
        'annotations': {'key': 'annotations', 'type': '[object]'},
        'type': {'key': 'type', 'type': 'str'},
        'domain': {'key': 'typeProperties.domain', 'type': 'object'},
        'access_token': {'key': 'typeProperties.accessToken', 'type': 'SecretBase'},
        'existing_cluster_id': {'key': 'typeProperties.existingClusterId', 'type': 'object'},
        'new_cluster_version': {'key': 'typeProperties.newClusterVersion', 'type': 'object'},
        'new_cluster_num_of_worker': {'key': 'typeProperties.newClusterNumOfWorker', 'type': 'object'},
        'new_cluster_node_type': {'key': 'typeProperties.newClusterNodeType', 'type': 'object'},
        'new_cluster_spark_conf': {'key': 'typeProperties.newClusterSparkConf', 'type': '{object}'},
        'new_cluster_custom_tags': {'key': 'typeProperties.newClusterCustomTags', 'type': '{object}'},
        'encrypted_credential': {'key': 'typeProperties.encryptedCredential', 'type': 'object'},
    }

    def __init__(self, **kwargs):
        super(AzureDatabricksLinkedService, self).__init__(**kwargs)
        self.domain = kwargs.get('domain', None)
        self.access_token = kwargs.get('access_token', None)
        self.existing_cluster_id = kwargs.get('existing_cluster_id', None)
        self.new_cluster_version = kwargs.get('new_cluster_version', None)
        self.new_cluster_num_of_worker = kwargs.get('new_cluster_num_of_worker', None)
        self.new_cluster_node_type = kwargs.get('new_cluster_node_type', None)
        self.new_cluster_spark_conf = kwargs.get('new_cluster_spark_conf', None)
        self.new_cluster_custom_tags = kwargs.get('new_cluster_custom_tags', None)
        self.encrypted_credential = kwargs.get('encrypted_credential', None)
        self.type = 'AzureDatabricks'
