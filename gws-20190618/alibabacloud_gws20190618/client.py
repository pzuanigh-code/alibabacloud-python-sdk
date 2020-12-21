# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.core import TeaCore
from typing import Dict

from alibabacloud_tea_rpc.client import Client as RPCClient
from alibabacloud_tea_rpc import models as rpc_models
from alibabacloud_gws20190618 import models as gws_20190618_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient


class Client(RPCClient):
    def __init__(
        self, 
        config: rpc_models.Config,
    ):
        super().__init__(config)
        self._endpoint_rule = 'regional'
        self._endpoint_map = {
            'ap-southeast-3': 'gws.ap-northeast-3.aliyuncs.com',
            'cn-hangzhou-finance': 'ecd.cn-hangzhou-finance.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('gws', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def set_cluster_dnat_with_options(
        self,
        request: gws_20190618_models.SetClusterDnatRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gws_20190618_models.SetClusterDnatResponse:
        UtilClient.validate_model(request)
        return gws_20190618_models.SetClusterDnatResponse().from_map(
            self.do_request('SetClusterDnat', 'HTTPS', 'POST', '2019-06-18', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def set_cluster_dnat_with_options_async(
        self,
        request: gws_20190618_models.SetClusterDnatRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gws_20190618_models.SetClusterDnatResponse:
        UtilClient.validate_model(request)
        return gws_20190618_models.SetClusterDnatResponse().from_map(
            await self.do_request_async('SetClusterDnat', 'HTTPS', 'POST', '2019-06-18', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def set_cluster_dnat(
        self,
        request: gws_20190618_models.SetClusterDnatRequest,
    ) -> gws_20190618_models.SetClusterDnatResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_cluster_dnat_with_options(request, runtime)

    async def set_cluster_dnat_async(
        self,
        request: gws_20190618_models.SetClusterDnatRequest,
    ) -> gws_20190618_models.SetClusterDnatResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_cluster_dnat_with_options_async(request, runtime)

    def create_service_linked_role_with_options(
        self,
        request: gws_20190618_models.CreateServiceLinkedRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gws_20190618_models.CreateServiceLinkedRoleResponse:
        UtilClient.validate_model(request)
        return gws_20190618_models.CreateServiceLinkedRoleResponse().from_map(
            self.do_request('CreateServiceLinkedRole', 'HTTPS', 'POST', '2019-06-18', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def create_service_linked_role_with_options_async(
        self,
        request: gws_20190618_models.CreateServiceLinkedRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gws_20190618_models.CreateServiceLinkedRoleResponse:
        UtilClient.validate_model(request)
        return gws_20190618_models.CreateServiceLinkedRoleResponse().from_map(
            await self.do_request_async('CreateServiceLinkedRole', 'HTTPS', 'POST', '2019-06-18', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def create_service_linked_role(
        self,
        request: gws_20190618_models.CreateServiceLinkedRoleRequest,
    ) -> gws_20190618_models.CreateServiceLinkedRoleResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_service_linked_role_with_options(request, runtime)

    async def create_service_linked_role_async(
        self,
        request: gws_20190618_models.CreateServiceLinkedRoleRequest,
    ) -> gws_20190618_models.CreateServiceLinkedRoleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_service_linked_role_with_options_async(request, runtime)

    def describe_cluster_connections_with_options(
        self,
        request: gws_20190618_models.DescribeClusterConnectionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gws_20190618_models.DescribeClusterConnectionsResponse:
        UtilClient.validate_model(request)
        return gws_20190618_models.DescribeClusterConnectionsResponse().from_map(
            self.do_request('DescribeClusterConnections', 'HTTPS', 'POST', '2019-06-18', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def describe_cluster_connections_with_options_async(
        self,
        request: gws_20190618_models.DescribeClusterConnectionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gws_20190618_models.DescribeClusterConnectionsResponse:
        UtilClient.validate_model(request)
        return gws_20190618_models.DescribeClusterConnectionsResponse().from_map(
            await self.do_request_async('DescribeClusterConnections', 'HTTPS', 'POST', '2019-06-18', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def describe_cluster_connections(
        self,
        request: gws_20190618_models.DescribeClusterConnectionsRequest,
    ) -> gws_20190618_models.DescribeClusterConnectionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_cluster_connections_with_options(request, runtime)

    async def describe_cluster_connections_async(
        self,
        request: gws_20190618_models.DescribeClusterConnectionsRequest,
    ) -> gws_20190618_models.DescribeClusterConnectionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_cluster_connections_with_options_async(request, runtime)

    def describe_cluster_addomain_with_options(
        self,
        request: gws_20190618_models.DescribeClusterADDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gws_20190618_models.DescribeClusterADDomainResponse:
        UtilClient.validate_model(request)
        return gws_20190618_models.DescribeClusterADDomainResponse().from_map(
            self.do_request('DescribeClusterADDomain', 'HTTPS', 'POST', '2019-06-18', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def describe_cluster_addomain_with_options_async(
        self,
        request: gws_20190618_models.DescribeClusterADDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gws_20190618_models.DescribeClusterADDomainResponse:
        UtilClient.validate_model(request)
        return gws_20190618_models.DescribeClusterADDomainResponse().from_map(
            await self.do_request_async('DescribeClusterADDomain', 'HTTPS', 'POST', '2019-06-18', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def describe_cluster_addomain(
        self,
        request: gws_20190618_models.DescribeClusterADDomainRequest,
    ) -> gws_20190618_models.DescribeClusterADDomainResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_cluster_addomain_with_options(request, runtime)

    async def describe_cluster_addomain_async(
        self,
        request: gws_20190618_models.DescribeClusterADDomainRequest,
    ) -> gws_20190618_models.DescribeClusterADDomainResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_cluster_addomain_with_options_async(request, runtime)

    def set_cluster_addomain_with_options(
        self,
        request: gws_20190618_models.SetClusterADDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gws_20190618_models.SetClusterADDomainResponse:
        UtilClient.validate_model(request)
        return gws_20190618_models.SetClusterADDomainResponse().from_map(
            self.do_request('SetClusterADDomain', 'HTTPS', 'POST', '2019-06-18', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def set_cluster_addomain_with_options_async(
        self,
        request: gws_20190618_models.SetClusterADDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gws_20190618_models.SetClusterADDomainResponse:
        UtilClient.validate_model(request)
        return gws_20190618_models.SetClusterADDomainResponse().from_map(
            await self.do_request_async('SetClusterADDomain', 'HTTPS', 'POST', '2019-06-18', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def set_cluster_addomain(
        self,
        request: gws_20190618_models.SetClusterADDomainRequest,
    ) -> gws_20190618_models.SetClusterADDomainResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_cluster_addomain_with_options(request, runtime)

    async def set_cluster_addomain_async(
        self,
        request: gws_20190618_models.SetClusterADDomainRequest,
    ) -> gws_20190618_models.SetClusterADDomainResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_cluster_addomain_with_options_async(request, runtime)

    def describe_instance_policy_with_options(
        self,
        request: gws_20190618_models.DescribeInstancePolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gws_20190618_models.DescribeInstancePolicyResponse:
        UtilClient.validate_model(request)
        return gws_20190618_models.DescribeInstancePolicyResponse().from_map(
            self.do_request('DescribeInstancePolicy', 'HTTPS', 'POST', '2019-06-18', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def describe_instance_policy_with_options_async(
        self,
        request: gws_20190618_models.DescribeInstancePolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gws_20190618_models.DescribeInstancePolicyResponse:
        UtilClient.validate_model(request)
        return gws_20190618_models.DescribeInstancePolicyResponse().from_map(
            await self.do_request_async('DescribeInstancePolicy', 'HTTPS', 'POST', '2019-06-18', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def describe_instance_policy(
        self,
        request: gws_20190618_models.DescribeInstancePolicyRequest,
    ) -> gws_20190618_models.DescribeInstancePolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_policy_with_options(request, runtime)

    async def describe_instance_policy_async(
        self,
        request: gws_20190618_models.DescribeInstancePolicyRequest,
    ) -> gws_20190618_models.DescribeInstancePolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_instance_policy_with_options_async(request, runtime)

    def set_instance_policy_with_options(
        self,
        request: gws_20190618_models.SetInstancePolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gws_20190618_models.SetInstancePolicyResponse:
        UtilClient.validate_model(request)
        return gws_20190618_models.SetInstancePolicyResponse().from_map(
            self.do_request('SetInstancePolicy', 'HTTPS', 'POST', '2019-06-18', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def set_instance_policy_with_options_async(
        self,
        request: gws_20190618_models.SetInstancePolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gws_20190618_models.SetInstancePolicyResponse:
        UtilClient.validate_model(request)
        return gws_20190618_models.SetInstancePolicyResponse().from_map(
            await self.do_request_async('SetInstancePolicy', 'HTTPS', 'POST', '2019-06-18', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def set_instance_policy(
        self,
        request: gws_20190618_models.SetInstancePolicyRequest,
    ) -> gws_20190618_models.SetInstancePolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_instance_policy_with_options(request, runtime)

    async def set_instance_policy_async(
        self,
        request: gws_20190618_models.SetInstancePolicyRequest,
    ) -> gws_20190618_models.SetInstancePolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_instance_policy_with_options_async(request, runtime)

    def describe_available_resource_with_options(
        self,
        request: gws_20190618_models.DescribeAvailableResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gws_20190618_models.DescribeAvailableResourceResponse:
        UtilClient.validate_model(request)
        return gws_20190618_models.DescribeAvailableResourceResponse().from_map(
            self.do_request('DescribeAvailableResource', 'HTTPS', 'POST', '2019-06-18', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def describe_available_resource_with_options_async(
        self,
        request: gws_20190618_models.DescribeAvailableResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gws_20190618_models.DescribeAvailableResourceResponse:
        UtilClient.validate_model(request)
        return gws_20190618_models.DescribeAvailableResourceResponse().from_map(
            await self.do_request_async('DescribeAvailableResource', 'HTTPS', 'POST', '2019-06-18', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def describe_available_resource(
        self,
        request: gws_20190618_models.DescribeAvailableResourceRequest,
    ) -> gws_20190618_models.DescribeAvailableResourceResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_available_resource_with_options(request, runtime)

    async def describe_available_resource_async(
        self,
        request: gws_20190618_models.DescribeAvailableResourceRequest,
    ) -> gws_20190618_models.DescribeAvailableResourceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_available_resource_with_options_async(request, runtime)

    def set_cluster_policy_with_options(
        self,
        request: gws_20190618_models.SetClusterPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gws_20190618_models.SetClusterPolicyResponse:
        UtilClient.validate_model(request)
        return gws_20190618_models.SetClusterPolicyResponse().from_map(
            self.do_request('SetClusterPolicy', 'HTTPS', 'POST', '2019-06-18', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def set_cluster_policy_with_options_async(
        self,
        request: gws_20190618_models.SetClusterPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gws_20190618_models.SetClusterPolicyResponse:
        UtilClient.validate_model(request)
        return gws_20190618_models.SetClusterPolicyResponse().from_map(
            await self.do_request_async('SetClusterPolicy', 'HTTPS', 'POST', '2019-06-18', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def set_cluster_policy(
        self,
        request: gws_20190618_models.SetClusterPolicyRequest,
    ) -> gws_20190618_models.SetClusterPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_cluster_policy_with_options(request, runtime)

    async def set_cluster_policy_async(
        self,
        request: gws_20190618_models.SetClusterPolicyRequest,
    ) -> gws_20190618_models.SetClusterPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_cluster_policy_with_options_async(request, runtime)

    def describe_cluster_policy_with_options(
        self,
        request: gws_20190618_models.DescribeClusterPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gws_20190618_models.DescribeClusterPolicyResponse:
        UtilClient.validate_model(request)
        return gws_20190618_models.DescribeClusterPolicyResponse().from_map(
            self.do_request('DescribeClusterPolicy', 'HTTPS', 'POST', '2019-06-18', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def describe_cluster_policy_with_options_async(
        self,
        request: gws_20190618_models.DescribeClusterPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gws_20190618_models.DescribeClusterPolicyResponse:
        UtilClient.validate_model(request)
        return gws_20190618_models.DescribeClusterPolicyResponse().from_map(
            await self.do_request_async('DescribeClusterPolicy', 'HTTPS', 'POST', '2019-06-18', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def describe_cluster_policy(
        self,
        request: gws_20190618_models.DescribeClusterPolicyRequest,
    ) -> gws_20190618_models.DescribeClusterPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_cluster_policy_with_options(request, runtime)

    async def describe_cluster_policy_async(
        self,
        request: gws_20190618_models.DescribeClusterPolicyRequest,
    ) -> gws_20190618_models.DescribeClusterPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_cluster_policy_with_options_async(request, runtime)

    def set_instance_name_with_options(
        self,
        request: gws_20190618_models.SetInstanceNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gws_20190618_models.SetInstanceNameResponse:
        UtilClient.validate_model(request)
        return gws_20190618_models.SetInstanceNameResponse().from_map(
            self.do_request('SetInstanceName', 'HTTPS', 'POST', '2019-06-18', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def set_instance_name_with_options_async(
        self,
        request: gws_20190618_models.SetInstanceNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gws_20190618_models.SetInstanceNameResponse:
        UtilClient.validate_model(request)
        return gws_20190618_models.SetInstanceNameResponse().from_map(
            await self.do_request_async('SetInstanceName', 'HTTPS', 'POST', '2019-06-18', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def set_instance_name(
        self,
        request: gws_20190618_models.SetInstanceNameRequest,
    ) -> gws_20190618_models.SetInstanceNameResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_instance_name_with_options(request, runtime)

    async def set_instance_name_async(
        self,
        request: gws_20190618_models.SetInstanceNameRequest,
    ) -> gws_20190618_models.SetInstanceNameResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_instance_name_with_options_async(request, runtime)

    def set_image_name_with_options(
        self,
        request: gws_20190618_models.SetImageNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gws_20190618_models.SetImageNameResponse:
        UtilClient.validate_model(request)
        return gws_20190618_models.SetImageNameResponse().from_map(
            self.do_request('SetImageName', 'HTTPS', 'POST', '2019-06-18', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def set_image_name_with_options_async(
        self,
        request: gws_20190618_models.SetImageNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gws_20190618_models.SetImageNameResponse:
        UtilClient.validate_model(request)
        return gws_20190618_models.SetImageNameResponse().from_map(
            await self.do_request_async('SetImageName', 'HTTPS', 'POST', '2019-06-18', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def set_image_name(
        self,
        request: gws_20190618_models.SetImageNameRequest,
    ) -> gws_20190618_models.SetImageNameResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_image_name_with_options(request, runtime)

    async def set_image_name_async(
        self,
        request: gws_20190618_models.SetImageNameRequest,
    ) -> gws_20190618_models.SetImageNameResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_image_name_with_options_async(request, runtime)

    def set_cluster_name_with_options(
        self,
        request: gws_20190618_models.SetClusterNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gws_20190618_models.SetClusterNameResponse:
        UtilClient.validate_model(request)
        return gws_20190618_models.SetClusterNameResponse().from_map(
            self.do_request('SetClusterName', 'HTTPS', 'POST', '2019-06-18', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def set_cluster_name_with_options_async(
        self,
        request: gws_20190618_models.SetClusterNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gws_20190618_models.SetClusterNameResponse:
        UtilClient.validate_model(request)
        return gws_20190618_models.SetClusterNameResponse().from_map(
            await self.do_request_async('SetClusterName', 'HTTPS', 'POST', '2019-06-18', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def set_cluster_name(
        self,
        request: gws_20190618_models.SetClusterNameRequest,
    ) -> gws_20190618_models.SetClusterNameResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_cluster_name_with_options(request, runtime)

    async def set_cluster_name_async(
        self,
        request: gws_20190618_models.SetClusterNameRequest,
    ) -> gws_20190618_models.SetClusterNameResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_cluster_name_with_options_async(request, runtime)

    def stop_instance_with_options(
        self,
        request: gws_20190618_models.StopInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gws_20190618_models.StopInstanceResponse:
        UtilClient.validate_model(request)
        return gws_20190618_models.StopInstanceResponse().from_map(
            self.do_request('StopInstance', 'HTTPS', 'POST', '2019-06-18', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def stop_instance_with_options_async(
        self,
        request: gws_20190618_models.StopInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gws_20190618_models.StopInstanceResponse:
        UtilClient.validate_model(request)
        return gws_20190618_models.StopInstanceResponse().from_map(
            await self.do_request_async('StopInstance', 'HTTPS', 'POST', '2019-06-18', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def stop_instance(
        self,
        request: gws_20190618_models.StopInstanceRequest,
    ) -> gws_20190618_models.StopInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.stop_instance_with_options(request, runtime)

    async def stop_instance_async(
        self,
        request: gws_20190618_models.StopInstanceRequest,
    ) -> gws_20190618_models.StopInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.stop_instance_with_options_async(request, runtime)

    def start_instance_with_options(
        self,
        request: gws_20190618_models.StartInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gws_20190618_models.StartInstanceResponse:
        UtilClient.validate_model(request)
        return gws_20190618_models.StartInstanceResponse().from_map(
            self.do_request('StartInstance', 'HTTPS', 'POST', '2019-06-18', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def start_instance_with_options_async(
        self,
        request: gws_20190618_models.StartInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gws_20190618_models.StartInstanceResponse:
        UtilClient.validate_model(request)
        return gws_20190618_models.StartInstanceResponse().from_map(
            await self.do_request_async('StartInstance', 'HTTPS', 'POST', '2019-06-18', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def start_instance(
        self,
        request: gws_20190618_models.StartInstanceRequest,
    ) -> gws_20190618_models.StartInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.start_instance_with_options(request, runtime)

    async def start_instance_async(
        self,
        request: gws_20190618_models.StartInstanceRequest,
    ) -> gws_20190618_models.StartInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.start_instance_with_options_async(request, runtime)

    def set_instance_user_with_options(
        self,
        request: gws_20190618_models.SetInstanceUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gws_20190618_models.SetInstanceUserResponse:
        UtilClient.validate_model(request)
        return gws_20190618_models.SetInstanceUserResponse().from_map(
            self.do_request('SetInstanceUser', 'HTTPS', 'POST', '2019-06-18', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def set_instance_user_with_options_async(
        self,
        request: gws_20190618_models.SetInstanceUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gws_20190618_models.SetInstanceUserResponse:
        UtilClient.validate_model(request)
        return gws_20190618_models.SetInstanceUserResponse().from_map(
            await self.do_request_async('SetInstanceUser', 'HTTPS', 'POST', '2019-06-18', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def set_instance_user(
        self,
        request: gws_20190618_models.SetInstanceUserRequest,
    ) -> gws_20190618_models.SetInstanceUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_instance_user_with_options(request, runtime)

    async def set_instance_user_async(
        self,
        request: gws_20190618_models.SetInstanceUserRequest,
    ) -> gws_20190618_models.SetInstanceUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_instance_user_with_options_async(request, runtime)

    def restart_instance_with_options(
        self,
        request: gws_20190618_models.RestartInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gws_20190618_models.RestartInstanceResponse:
        UtilClient.validate_model(request)
        return gws_20190618_models.RestartInstanceResponse().from_map(
            self.do_request('RestartInstance', 'HTTPS', 'POST', '2019-06-18', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def restart_instance_with_options_async(
        self,
        request: gws_20190618_models.RestartInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gws_20190618_models.RestartInstanceResponse:
        UtilClient.validate_model(request)
        return gws_20190618_models.RestartInstanceResponse().from_map(
            await self.do_request_async('RestartInstance', 'HTTPS', 'POST', '2019-06-18', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def restart_instance(
        self,
        request: gws_20190618_models.RestartInstanceRequest,
    ) -> gws_20190618_models.RestartInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.restart_instance_with_options(request, runtime)

    async def restart_instance_async(
        self,
        request: gws_20190618_models.RestartInstanceRequest,
    ) -> gws_20190618_models.RestartInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.restart_instance_with_options_async(request, runtime)

    def is_user_admin_with_options(
        self,
        request: gws_20190618_models.IsUserAdminRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gws_20190618_models.IsUserAdminResponse:
        UtilClient.validate_model(request)
        return gws_20190618_models.IsUserAdminResponse().from_map(
            self.do_request('IsUserAdmin', 'HTTPS', 'POST', '2019-06-18', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def is_user_admin_with_options_async(
        self,
        request: gws_20190618_models.IsUserAdminRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gws_20190618_models.IsUserAdminResponse:
        UtilClient.validate_model(request)
        return gws_20190618_models.IsUserAdminResponse().from_map(
            await self.do_request_async('IsUserAdmin', 'HTTPS', 'POST', '2019-06-18', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def is_user_admin(
        self,
        request: gws_20190618_models.IsUserAdminRequest,
    ) -> gws_20190618_models.IsUserAdminResponse:
        runtime = util_models.RuntimeOptions()
        return self.is_user_admin_with_options(request, runtime)

    async def is_user_admin_async(
        self,
        request: gws_20190618_models.IsUserAdminRequest,
    ) -> gws_20190618_models.IsUserAdminResponse:
        runtime = util_models.RuntimeOptions()
        return await self.is_user_admin_with_options_async(request, runtime)

    def get_connect_ticket_with_options(
        self,
        request: gws_20190618_models.GetConnectTicketRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gws_20190618_models.GetConnectTicketResponse:
        UtilClient.validate_model(request)
        return gws_20190618_models.GetConnectTicketResponse().from_map(
            self.do_request('GetConnectTicket', 'HTTPS', 'POST', '2019-06-18', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def get_connect_ticket_with_options_async(
        self,
        request: gws_20190618_models.GetConnectTicketRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gws_20190618_models.GetConnectTicketResponse:
        UtilClient.validate_model(request)
        return gws_20190618_models.GetConnectTicketResponse().from_map(
            await self.do_request_async('GetConnectTicket', 'HTTPS', 'POST', '2019-06-18', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def get_connect_ticket(
        self,
        request: gws_20190618_models.GetConnectTicketRequest,
    ) -> gws_20190618_models.GetConnectTicketResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_connect_ticket_with_options(request, runtime)

    async def get_connect_ticket_async(
        self,
        request: gws_20190618_models.GetConnectTicketRequest,
    ) -> gws_20190618_models.GetConnectTicketResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_connect_ticket_with_options_async(request, runtime)

    def describe_instances_with_options(
        self,
        request: gws_20190618_models.DescribeInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gws_20190618_models.DescribeInstancesResponse:
        UtilClient.validate_model(request)
        return gws_20190618_models.DescribeInstancesResponse().from_map(
            self.do_request('DescribeInstances', 'HTTPS', 'POST', '2019-06-18', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def describe_instances_with_options_async(
        self,
        request: gws_20190618_models.DescribeInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gws_20190618_models.DescribeInstancesResponse:
        UtilClient.validate_model(request)
        return gws_20190618_models.DescribeInstancesResponse().from_map(
            await self.do_request_async('DescribeInstances', 'HTTPS', 'POST', '2019-06-18', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def describe_instances(
        self,
        request: gws_20190618_models.DescribeInstancesRequest,
    ) -> gws_20190618_models.DescribeInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_instances_with_options(request, runtime)

    async def describe_instances_async(
        self,
        request: gws_20190618_models.DescribeInstancesRequest,
    ) -> gws_20190618_models.DescribeInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_instances_with_options_async(request, runtime)

    def describe_images_with_options(
        self,
        request: gws_20190618_models.DescribeImagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gws_20190618_models.DescribeImagesResponse:
        UtilClient.validate_model(request)
        return gws_20190618_models.DescribeImagesResponse().from_map(
            self.do_request('DescribeImages', 'HTTPS', 'POST', '2019-06-18', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def describe_images_with_options_async(
        self,
        request: gws_20190618_models.DescribeImagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gws_20190618_models.DescribeImagesResponse:
        UtilClient.validate_model(request)
        return gws_20190618_models.DescribeImagesResponse().from_map(
            await self.do_request_async('DescribeImages', 'HTTPS', 'POST', '2019-06-18', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def describe_images(
        self,
        request: gws_20190618_models.DescribeImagesRequest,
    ) -> gws_20190618_models.DescribeImagesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_images_with_options(request, runtime)

    async def describe_images_async(
        self,
        request: gws_20190618_models.DescribeImagesRequest,
    ) -> gws_20190618_models.DescribeImagesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_images_with_options_async(request, runtime)

    def describe_clusters_with_options(
        self,
        request: gws_20190618_models.DescribeClustersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gws_20190618_models.DescribeClustersResponse:
        UtilClient.validate_model(request)
        return gws_20190618_models.DescribeClustersResponse().from_map(
            self.do_request('DescribeClusters', 'HTTPS', 'POST', '2019-06-18', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def describe_clusters_with_options_async(
        self,
        request: gws_20190618_models.DescribeClustersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gws_20190618_models.DescribeClustersResponse:
        UtilClient.validate_model(request)
        return gws_20190618_models.DescribeClustersResponse().from_map(
            await self.do_request_async('DescribeClusters', 'HTTPS', 'POST', '2019-06-18', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def describe_clusters(
        self,
        request: gws_20190618_models.DescribeClustersRequest,
    ) -> gws_20190618_models.DescribeClustersResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_clusters_with_options(request, runtime)

    async def describe_clusters_async(
        self,
        request: gws_20190618_models.DescribeClustersRequest,
    ) -> gws_20190618_models.DescribeClustersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_clusters_with_options_async(request, runtime)

    def delete_instance_with_options(
        self,
        request: gws_20190618_models.DeleteInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gws_20190618_models.DeleteInstanceResponse:
        UtilClient.validate_model(request)
        return gws_20190618_models.DeleteInstanceResponse().from_map(
            self.do_request('DeleteInstance', 'HTTPS', 'POST', '2019-06-18', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def delete_instance_with_options_async(
        self,
        request: gws_20190618_models.DeleteInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gws_20190618_models.DeleteInstanceResponse:
        UtilClient.validate_model(request)
        return gws_20190618_models.DeleteInstanceResponse().from_map(
            await self.do_request_async('DeleteInstance', 'HTTPS', 'POST', '2019-06-18', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def delete_instance(
        self,
        request: gws_20190618_models.DeleteInstanceRequest,
    ) -> gws_20190618_models.DeleteInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_instance_with_options(request, runtime)

    async def delete_instance_async(
        self,
        request: gws_20190618_models.DeleteInstanceRequest,
    ) -> gws_20190618_models.DeleteInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_instance_with_options_async(request, runtime)

    def delete_image_with_options(
        self,
        request: gws_20190618_models.DeleteImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gws_20190618_models.DeleteImageResponse:
        UtilClient.validate_model(request)
        return gws_20190618_models.DeleteImageResponse().from_map(
            self.do_request('DeleteImage', 'HTTPS', 'POST', '2019-06-18', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def delete_image_with_options_async(
        self,
        request: gws_20190618_models.DeleteImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gws_20190618_models.DeleteImageResponse:
        UtilClient.validate_model(request)
        return gws_20190618_models.DeleteImageResponse().from_map(
            await self.do_request_async('DeleteImage', 'HTTPS', 'POST', '2019-06-18', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def delete_image(
        self,
        request: gws_20190618_models.DeleteImageRequest,
    ) -> gws_20190618_models.DeleteImageResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_image_with_options(request, runtime)

    async def delete_image_async(
        self,
        request: gws_20190618_models.DeleteImageRequest,
    ) -> gws_20190618_models.DeleteImageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_image_with_options_async(request, runtime)

    def delete_cluster_with_options(
        self,
        request: gws_20190618_models.DeleteClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gws_20190618_models.DeleteClusterResponse:
        UtilClient.validate_model(request)
        return gws_20190618_models.DeleteClusterResponse().from_map(
            self.do_request('DeleteCluster', 'HTTPS', 'POST', '2019-06-18', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def delete_cluster_with_options_async(
        self,
        request: gws_20190618_models.DeleteClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gws_20190618_models.DeleteClusterResponse:
        UtilClient.validate_model(request)
        return gws_20190618_models.DeleteClusterResponse().from_map(
            await self.do_request_async('DeleteCluster', 'HTTPS', 'POST', '2019-06-18', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def delete_cluster(
        self,
        request: gws_20190618_models.DeleteClusterRequest,
    ) -> gws_20190618_models.DeleteClusterResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_cluster_with_options(request, runtime)

    async def delete_cluster_async(
        self,
        request: gws_20190618_models.DeleteClusterRequest,
    ) -> gws_20190618_models.DeleteClusterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_cluster_with_options_async(request, runtime)

    def create_instance_with_options(
        self,
        request: gws_20190618_models.CreateInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gws_20190618_models.CreateInstanceResponse:
        UtilClient.validate_model(request)
        return gws_20190618_models.CreateInstanceResponse().from_map(
            self.do_request('CreateInstance', 'HTTPS', 'POST', '2019-06-18', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def create_instance_with_options_async(
        self,
        request: gws_20190618_models.CreateInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gws_20190618_models.CreateInstanceResponse:
        UtilClient.validate_model(request)
        return gws_20190618_models.CreateInstanceResponse().from_map(
            await self.do_request_async('CreateInstance', 'HTTPS', 'POST', '2019-06-18', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def create_instance(
        self,
        request: gws_20190618_models.CreateInstanceRequest,
    ) -> gws_20190618_models.CreateInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_instance_with_options(request, runtime)

    async def create_instance_async(
        self,
        request: gws_20190618_models.CreateInstanceRequest,
    ) -> gws_20190618_models.CreateInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_instance_with_options_async(request, runtime)

    def create_image_with_options(
        self,
        request: gws_20190618_models.CreateImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gws_20190618_models.CreateImageResponse:
        UtilClient.validate_model(request)
        return gws_20190618_models.CreateImageResponse().from_map(
            self.do_request('CreateImage', 'HTTPS', 'POST', '2019-06-18', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def create_image_with_options_async(
        self,
        request: gws_20190618_models.CreateImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gws_20190618_models.CreateImageResponse:
        UtilClient.validate_model(request)
        return gws_20190618_models.CreateImageResponse().from_map(
            await self.do_request_async('CreateImage', 'HTTPS', 'POST', '2019-06-18', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def create_image(
        self,
        request: gws_20190618_models.CreateImageRequest,
    ) -> gws_20190618_models.CreateImageResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_image_with_options(request, runtime)

    async def create_image_async(
        self,
        request: gws_20190618_models.CreateImageRequest,
    ) -> gws_20190618_models.CreateImageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_image_with_options_async(request, runtime)

    def create_cluster_with_options(
        self,
        request: gws_20190618_models.CreateClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gws_20190618_models.CreateClusterResponse:
        UtilClient.validate_model(request)
        return gws_20190618_models.CreateClusterResponse().from_map(
            self.do_request('CreateCluster', 'HTTPS', 'POST', '2019-06-18', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def create_cluster_with_options_async(
        self,
        request: gws_20190618_models.CreateClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gws_20190618_models.CreateClusterResponse:
        UtilClient.validate_model(request)
        return gws_20190618_models.CreateClusterResponse().from_map(
            await self.do_request_async('CreateCluster', 'HTTPS', 'POST', '2019-06-18', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def create_cluster(
        self,
        request: gws_20190618_models.CreateClusterRequest,
    ) -> gws_20190618_models.CreateClusterResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_cluster_with_options(request, runtime)

    async def create_cluster_async(
        self,
        request: gws_20190618_models.CreateClusterRequest,
    ) -> gws_20190618_models.CreateClusterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_cluster_with_options_async(request, runtime)

    def get_endpoint(
        self,
        product_id: str,
        region_id: str,
        endpoint_rule: str,
        network: str,
        suffix: str,
        endpoint_map: Dict[str, str],
        endpoint: str,
    ) -> str:
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)
