# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_dysmsapi20170525 import models as dysmsapi_20170525_models
from alibabacloud_tea_util import models as util_models


class Client(OpenApiClient):
    """
    *\
    """
    def __init__(
        self, 
        config: open_api_models.Config,
    ):
        super().__init__(config)
        self._endpoint_rule = 'central'
        self._endpoint_map = {
            'ap-northeast-1': 'dysmsapi.ap-southeast-1.aliyuncs.com',
            'ap-northeast-2-pop': 'dysmsapi.ap-southeast-1.aliyuncs.com',
            'ap-south-1': 'dysmsapi.ap-southeast-1.aliyuncs.com',
            'ap-southeast-1': 'dysmsapi.ap-southeast-1.aliyuncs.com',
            'ap-southeast-2': 'dysmsapi.ap-southeast-1.aliyuncs.com',
            'ap-southeast-3': 'dysmsapi.ap-southeast-1.aliyuncs.com',
            'ap-southeast-5': 'dysmsapi.ap-southeast-1.aliyuncs.com',
            'cn-beijing': 'dysmsapi-proxy.cn-beijing.aliyuncs.com',
            'eu-central-1': 'dysmsapi.ap-southeast-1.aliyuncs.com',
            'eu-west-1': 'dysmsapi.ap-southeast-1.aliyuncs.com',
            'eu-west-1-oxs': 'dysmsapi.ap-southeast-1.aliyuncs.com',
            'me-east-1': 'dysmsapi.ap-southeast-1.aliyuncs.com',
            'rus-west-1-pop': 'dysmsapi.ap-southeast-1.aliyuncs.com',
            'us-east-1': 'dysmsapi.ap-southeast-1.aliyuncs.com',
            'us-west-1': 'dysmsapi.ap-southeast-1.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('dysmsapi', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def add_short_url_with_options(
        self,
        request: dysmsapi_20170525_models.AddShortUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.AddShortUrlResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dysmsapi_20170525_models.AddShortUrlResponse().from_map(
            self.do_rpcrequest('AddShortUrl', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_short_url_with_options_async(
        self,
        request: dysmsapi_20170525_models.AddShortUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.AddShortUrlResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dysmsapi_20170525_models.AddShortUrlResponse().from_map(
            await self.do_rpcrequest_async('AddShortUrl', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_short_url(
        self,
        request: dysmsapi_20170525_models.AddShortUrlRequest,
    ) -> dysmsapi_20170525_models.AddShortUrlResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_short_url_with_options(request, runtime)

    async def add_short_url_async(
        self,
        request: dysmsapi_20170525_models.AddShortUrlRequest,
    ) -> dysmsapi_20170525_models.AddShortUrlResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_short_url_with_options_async(request, runtime)

    def add_sms_sign_with_options(
        self,
        request: dysmsapi_20170525_models.AddSmsSignRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.AddSmsSignResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dysmsapi_20170525_models.AddSmsSignResponse().from_map(
            self.do_rpcrequest('AddSmsSign', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_sms_sign_with_options_async(
        self,
        request: dysmsapi_20170525_models.AddSmsSignRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.AddSmsSignResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dysmsapi_20170525_models.AddSmsSignResponse().from_map(
            await self.do_rpcrequest_async('AddSmsSign', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_sms_sign(
        self,
        request: dysmsapi_20170525_models.AddSmsSignRequest,
    ) -> dysmsapi_20170525_models.AddSmsSignResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_sms_sign_with_options(request, runtime)

    async def add_sms_sign_async(
        self,
        request: dysmsapi_20170525_models.AddSmsSignRequest,
    ) -> dysmsapi_20170525_models.AddSmsSignResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_sms_sign_with_options_async(request, runtime)

    def add_sms_template_with_options(
        self,
        request: dysmsapi_20170525_models.AddSmsTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.AddSmsTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dysmsapi_20170525_models.AddSmsTemplateResponse().from_map(
            self.do_rpcrequest('AddSmsTemplate', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_sms_template_with_options_async(
        self,
        request: dysmsapi_20170525_models.AddSmsTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.AddSmsTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dysmsapi_20170525_models.AddSmsTemplateResponse().from_map(
            await self.do_rpcrequest_async('AddSmsTemplate', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_sms_template(
        self,
        request: dysmsapi_20170525_models.AddSmsTemplateRequest,
    ) -> dysmsapi_20170525_models.AddSmsTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_sms_template_with_options(request, runtime)

    async def add_sms_template_async(
        self,
        request: dysmsapi_20170525_models.AddSmsTemplateRequest,
    ) -> dysmsapi_20170525_models.AddSmsTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_sms_template_with_options_async(request, runtime)

    def create_short_param_with_options(
        self,
        request: dysmsapi_20170525_models.CreateShortParamRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.CreateShortParamResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dysmsapi_20170525_models.CreateShortParamResponse().from_map(
            self.do_rpcrequest('CreateShortParam', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_short_param_with_options_async(
        self,
        request: dysmsapi_20170525_models.CreateShortParamRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.CreateShortParamResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dysmsapi_20170525_models.CreateShortParamResponse().from_map(
            await self.do_rpcrequest_async('CreateShortParam', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_short_param(
        self,
        request: dysmsapi_20170525_models.CreateShortParamRequest,
    ) -> dysmsapi_20170525_models.CreateShortParamResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_short_param_with_options(request, runtime)

    async def create_short_param_async(
        self,
        request: dysmsapi_20170525_models.CreateShortParamRequest,
    ) -> dysmsapi_20170525_models.CreateShortParamResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_short_param_with_options_async(request, runtime)

    def delete_short_url_with_options(
        self,
        request: dysmsapi_20170525_models.DeleteShortUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.DeleteShortUrlResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dysmsapi_20170525_models.DeleteShortUrlResponse().from_map(
            self.do_rpcrequest('DeleteShortUrl', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_short_url_with_options_async(
        self,
        request: dysmsapi_20170525_models.DeleteShortUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.DeleteShortUrlResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dysmsapi_20170525_models.DeleteShortUrlResponse().from_map(
            await self.do_rpcrequest_async('DeleteShortUrl', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_short_url(
        self,
        request: dysmsapi_20170525_models.DeleteShortUrlRequest,
    ) -> dysmsapi_20170525_models.DeleteShortUrlResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_short_url_with_options(request, runtime)

    async def delete_short_url_async(
        self,
        request: dysmsapi_20170525_models.DeleteShortUrlRequest,
    ) -> dysmsapi_20170525_models.DeleteShortUrlResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_short_url_with_options_async(request, runtime)

    def delete_sms_sign_with_options(
        self,
        request: dysmsapi_20170525_models.DeleteSmsSignRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.DeleteSmsSignResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dysmsapi_20170525_models.DeleteSmsSignResponse().from_map(
            self.do_rpcrequest('DeleteSmsSign', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_sms_sign_with_options_async(
        self,
        request: dysmsapi_20170525_models.DeleteSmsSignRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.DeleteSmsSignResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dysmsapi_20170525_models.DeleteSmsSignResponse().from_map(
            await self.do_rpcrequest_async('DeleteSmsSign', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_sms_sign(
        self,
        request: dysmsapi_20170525_models.DeleteSmsSignRequest,
    ) -> dysmsapi_20170525_models.DeleteSmsSignResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_sms_sign_with_options(request, runtime)

    async def delete_sms_sign_async(
        self,
        request: dysmsapi_20170525_models.DeleteSmsSignRequest,
    ) -> dysmsapi_20170525_models.DeleteSmsSignResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_sms_sign_with_options_async(request, runtime)

    def delete_sms_template_with_options(
        self,
        request: dysmsapi_20170525_models.DeleteSmsTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.DeleteSmsTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dysmsapi_20170525_models.DeleteSmsTemplateResponse().from_map(
            self.do_rpcrequest('DeleteSmsTemplate', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_sms_template_with_options_async(
        self,
        request: dysmsapi_20170525_models.DeleteSmsTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.DeleteSmsTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dysmsapi_20170525_models.DeleteSmsTemplateResponse().from_map(
            await self.do_rpcrequest_async('DeleteSmsTemplate', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_sms_template(
        self,
        request: dysmsapi_20170525_models.DeleteSmsTemplateRequest,
    ) -> dysmsapi_20170525_models.DeleteSmsTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_sms_template_with_options(request, runtime)

    async def delete_sms_template_async(
        self,
        request: dysmsapi_20170525_models.DeleteSmsTemplateRequest,
    ) -> dysmsapi_20170525_models.DeleteSmsTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_sms_template_with_options_async(request, runtime)

    def modify_sms_sign_with_options(
        self,
        request: dysmsapi_20170525_models.ModifySmsSignRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.ModifySmsSignResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dysmsapi_20170525_models.ModifySmsSignResponse().from_map(
            self.do_rpcrequest('ModifySmsSign', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_sms_sign_with_options_async(
        self,
        request: dysmsapi_20170525_models.ModifySmsSignRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.ModifySmsSignResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dysmsapi_20170525_models.ModifySmsSignResponse().from_map(
            await self.do_rpcrequest_async('ModifySmsSign', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_sms_sign(
        self,
        request: dysmsapi_20170525_models.ModifySmsSignRequest,
    ) -> dysmsapi_20170525_models.ModifySmsSignResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_sms_sign_with_options(request, runtime)

    async def modify_sms_sign_async(
        self,
        request: dysmsapi_20170525_models.ModifySmsSignRequest,
    ) -> dysmsapi_20170525_models.ModifySmsSignResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_sms_sign_with_options_async(request, runtime)

    def modify_sms_template_with_options(
        self,
        request: dysmsapi_20170525_models.ModifySmsTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.ModifySmsTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dysmsapi_20170525_models.ModifySmsTemplateResponse().from_map(
            self.do_rpcrequest('ModifySmsTemplate', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_sms_template_with_options_async(
        self,
        request: dysmsapi_20170525_models.ModifySmsTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.ModifySmsTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dysmsapi_20170525_models.ModifySmsTemplateResponse().from_map(
            await self.do_rpcrequest_async('ModifySmsTemplate', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_sms_template(
        self,
        request: dysmsapi_20170525_models.ModifySmsTemplateRequest,
    ) -> dysmsapi_20170525_models.ModifySmsTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_sms_template_with_options(request, runtime)

    async def modify_sms_template_async(
        self,
        request: dysmsapi_20170525_models.ModifySmsTemplateRequest,
    ) -> dysmsapi_20170525_models.ModifySmsTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_sms_template_with_options_async(request, runtime)

    def query_send_details_with_options(
        self,
        request: dysmsapi_20170525_models.QuerySendDetailsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.QuerySendDetailsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dysmsapi_20170525_models.QuerySendDetailsResponse().from_map(
            self.do_rpcrequest('QuerySendDetails', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_send_details_with_options_async(
        self,
        request: dysmsapi_20170525_models.QuerySendDetailsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.QuerySendDetailsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dysmsapi_20170525_models.QuerySendDetailsResponse().from_map(
            await self.do_rpcrequest_async('QuerySendDetails', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_send_details(
        self,
        request: dysmsapi_20170525_models.QuerySendDetailsRequest,
    ) -> dysmsapi_20170525_models.QuerySendDetailsResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_send_details_with_options(request, runtime)

    async def query_send_details_async(
        self,
        request: dysmsapi_20170525_models.QuerySendDetailsRequest,
    ) -> dysmsapi_20170525_models.QuerySendDetailsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_send_details_with_options_async(request, runtime)

    def query_short_url_with_options(
        self,
        request: dysmsapi_20170525_models.QueryShortUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.QueryShortUrlResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dysmsapi_20170525_models.QueryShortUrlResponse().from_map(
            self.do_rpcrequest('QueryShortUrl', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_short_url_with_options_async(
        self,
        request: dysmsapi_20170525_models.QueryShortUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.QueryShortUrlResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dysmsapi_20170525_models.QueryShortUrlResponse().from_map(
            await self.do_rpcrequest_async('QueryShortUrl', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_short_url(
        self,
        request: dysmsapi_20170525_models.QueryShortUrlRequest,
    ) -> dysmsapi_20170525_models.QueryShortUrlResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_short_url_with_options(request, runtime)

    async def query_short_url_async(
        self,
        request: dysmsapi_20170525_models.QueryShortUrlRequest,
    ) -> dysmsapi_20170525_models.QueryShortUrlResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_short_url_with_options_async(request, runtime)

    def query_sms_sign_with_options(
        self,
        request: dysmsapi_20170525_models.QuerySmsSignRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.QuerySmsSignResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dysmsapi_20170525_models.QuerySmsSignResponse().from_map(
            self.do_rpcrequest('QuerySmsSign', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_sms_sign_with_options_async(
        self,
        request: dysmsapi_20170525_models.QuerySmsSignRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.QuerySmsSignResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dysmsapi_20170525_models.QuerySmsSignResponse().from_map(
            await self.do_rpcrequest_async('QuerySmsSign', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_sms_sign(
        self,
        request: dysmsapi_20170525_models.QuerySmsSignRequest,
    ) -> dysmsapi_20170525_models.QuerySmsSignResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_sms_sign_with_options(request, runtime)

    async def query_sms_sign_async(
        self,
        request: dysmsapi_20170525_models.QuerySmsSignRequest,
    ) -> dysmsapi_20170525_models.QuerySmsSignResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_sms_sign_with_options_async(request, runtime)

    def query_sms_template_with_options(
        self,
        request: dysmsapi_20170525_models.QuerySmsTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.QuerySmsTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dysmsapi_20170525_models.QuerySmsTemplateResponse().from_map(
            self.do_rpcrequest('QuerySmsTemplate', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_sms_template_with_options_async(
        self,
        request: dysmsapi_20170525_models.QuerySmsTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.QuerySmsTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dysmsapi_20170525_models.QuerySmsTemplateResponse().from_map(
            await self.do_rpcrequest_async('QuerySmsTemplate', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_sms_template(
        self,
        request: dysmsapi_20170525_models.QuerySmsTemplateRequest,
    ) -> dysmsapi_20170525_models.QuerySmsTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_sms_template_with_options(request, runtime)

    async def query_sms_template_async(
        self,
        request: dysmsapi_20170525_models.QuerySmsTemplateRequest,
    ) -> dysmsapi_20170525_models.QuerySmsTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_sms_template_with_options_async(request, runtime)

    def send_batch_sms_with_options(
        self,
        request: dysmsapi_20170525_models.SendBatchSmsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.SendBatchSmsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dysmsapi_20170525_models.SendBatchSmsResponse().from_map(
            self.do_rpcrequest('SendBatchSms', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def send_batch_sms_with_options_async(
        self,
        request: dysmsapi_20170525_models.SendBatchSmsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.SendBatchSmsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dysmsapi_20170525_models.SendBatchSmsResponse().from_map(
            await self.do_rpcrequest_async('SendBatchSms', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def send_batch_sms(
        self,
        request: dysmsapi_20170525_models.SendBatchSmsRequest,
    ) -> dysmsapi_20170525_models.SendBatchSmsResponse:
        runtime = util_models.RuntimeOptions()
        return self.send_batch_sms_with_options(request, runtime)

    async def send_batch_sms_async(
        self,
        request: dysmsapi_20170525_models.SendBatchSmsRequest,
    ) -> dysmsapi_20170525_models.SendBatchSmsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.send_batch_sms_with_options_async(request, runtime)

    def send_sms_with_options(
        self,
        request: dysmsapi_20170525_models.SendSmsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.SendSmsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dysmsapi_20170525_models.SendSmsResponse().from_map(
            self.do_rpcrequest('SendSms', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def send_sms_with_options_async(
        self,
        request: dysmsapi_20170525_models.SendSmsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.SendSmsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dysmsapi_20170525_models.SendSmsResponse().from_map(
            await self.do_rpcrequest_async('SendSms', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def send_sms(
        self,
        request: dysmsapi_20170525_models.SendSmsRequest,
    ) -> dysmsapi_20170525_models.SendSmsResponse:
        runtime = util_models.RuntimeOptions()
        return self.send_sms_with_options(request, runtime)

    async def send_sms_async(
        self,
        request: dysmsapi_20170525_models.SendSmsRequest,
    ) -> dysmsapi_20170525_models.SendSmsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.send_sms_with_options_async(request, runtime)
