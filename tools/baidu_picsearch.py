from collections.abc import Generator
from typing import Any
import json
import requests

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage


class BaiduPicsearchTool(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage]:
        # 获取API密钥和查询参数
        api_key = tool_parameters.get("baidu_api_key", "")
        query = tool_parameters.get("query", "")
        app_id = tool_parameters.get("baidu_app_id", "")

        if not app_id:
            yield self.create_text_message("Missing Baidu App ID configuration")
            return

        try:
            # 第一步：获取conversation_id
            conv_url = "https://qianfan.baidubce.com/v2/app/conversation"
            conv_payload = json.dumps({"app_id": app_id}, ensure_ascii=False)

            conv_headers = {
                "Content-Type": "application/json",
                "X-Appbuilder-Authorization": f"Bearer {api_key}",
            }

            # 发送会话创建请求
            conv_response = requests.post(
                conv_url,
                headers=conv_headers,
                data=conv_payload.encode("utf-8"),
                timeout=10,
            )

            if conv_response.status_code != 200:
                yield self.create_text_message("Failed to create conversation")
                return

            conv_data = conv_response.json()
            if "conversation_id" not in conv_data:
                yield self.create_text_message("Invalid conversation response")
                return

            # 第二步：执行查询
            search_url = "https://qianfan.baidubce.com/v2/app/conversation/runs"
            search_payload = json.dumps(
                {
                    "app_id": app_id,
                    "query": query,
                    "conversation_id": conv_data["conversation_id"],
                    "stream": False,
                },
                ensure_ascii=False,
            )

            search_headers = {
                "Content-Type": "application/json",
                "X-Appbuilder-Authorization": f"Bearer {api_key}",
            }

            # 发送搜索请求
            search_response = requests.post(
                search_url,
                headers=search_headers,
                data=search_payload.encode("utf-8"),
                timeout=30,
            )

            if search_response.status_code != 200:
                yield self.create_text_message("Search request failed")
                return

            try:
                response_json = search_response.json()
                answer = response_json["answer"]
                urls = json.loads(answer)

                for url in urls["urls"]:
                    yield self.create_link_message(url)

                # 返回最终结果
                yield self.create_json_message({"status": "success", "data": urls})
            except Exception as e:
                yield self.create_text_message(f"Unexpected error: {str(e)}")

        except requests.exceptions.RequestException as e:
            yield self.create_text_message(f"Network error: {str(e)}")
        except json.JSONDecodeError:
            yield self.create_text_message("Invalid API response format")
        except Exception as e:
            yield self.create_text_message(f"Unexpected error: {str(e)}")
