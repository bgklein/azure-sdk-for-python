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


class ForestSummary(Model):
    """The forest summary for an ADDS domain.

    :param forest_name: The forest name.
    :type forest_name: str
    :param domain_count: The domain count.
    :type domain_count: int
    :param site_count: The site count.
    :type site_count: int
    :param monitored_dc_count: The number of domain controllers that are
     monitored by Azure Active Directory Connect Health.
    :type monitored_dc_count: int
    :param total_dc_count: The total domain controllers.
    :type total_dc_count: int
    :param domains: The list of domain controller names.
    :type domains: list[str]
    :param sites: The list of site names.
    :type sites: list[str]
    """

    _attribute_map = {
        'forest_name': {'key': 'forestName', 'type': 'str'},
        'domain_count': {'key': 'domainCount', 'type': 'int'},
        'site_count': {'key': 'siteCount', 'type': 'int'},
        'monitored_dc_count': {'key': 'monitoredDcCount', 'type': 'int'},
        'total_dc_count': {'key': 'totalDcCount', 'type': 'int'},
        'domains': {'key': 'domains', 'type': '[str]'},
        'sites': {'key': 'sites', 'type': '[str]'},
    }

    def __init__(self, *, forest_name: str=None, domain_count: int=None, site_count: int=None, monitored_dc_count: int=None, total_dc_count: int=None, domains=None, sites=None, **kwargs) -> None:
        super(ForestSummary, self).__init__(**kwargs)
        self.forest_name = forest_name
        self.domain_count = domain_count
        self.site_count = site_count
        self.monitored_dc_count = monitored_dc_count
        self.total_dc_count = total_dc_count
        self.domains = domains
        self.sites = sites
