# -*- coding: utf-8 -*-


class CustomUserAgentMiddleware(object):
    def process_request(self, request, spider):
        ug = "Baiduspider"
        request.headers["User-Agent"] = ug


class CustomHeadersMiddleware(object):
    def process_request(self, request, spider):
        request.headers["Accept-Language"] = "zh-CN,zh"
