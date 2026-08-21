import requests
import config


class ApiClient:
    """
    API客户端类，用于发送HTTP请求
    """

    def __init__(self):
        # 默认params参数
        self.common_params = {
            "mock_uid": config.mock_uid,
            "mock_uuid": config.mock_uuid,
            "_super_": config._super_
        }

    def request(
            self,
            method,
            url,
            params=None,
            data=None,
            json=None,
            headers=None
    ):
        """
        发送HTTP请求

        :param method: 请求方法，如GET、POST等
        :param url: 请求URL
        :param params: URL参数
        :param data: 表单数据
        :param json: JSON数据
        :param headers: 请求头
        :return: 响应对象
        """

        # 合并公共参数和接口参数
        params = {
            **self.common_params,
            **(params or {})
        }

        try:

            response = requests.request(
                method=method,
                url=url,
                params=params,
                data=data,
                json=json,
                headers=headers,
                timeout=10  # 设置超时时间为10秒
            )
            response.raise_for_status()  # 如果响应状态码不是200，抛出异常
            return response
        
        except requests.RequestException as exc:
            raise RuntimeError(f"HTTP请求失败: {url}") from exc