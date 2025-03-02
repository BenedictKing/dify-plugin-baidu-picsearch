from typing import Any

from dify_plugin import ToolProvider
from dify_plugin.errors.tool import ToolProviderCredentialValidationError


class BaiduPicsearchProvider(ToolProvider):
    def _validate_credentials(self, credentials: dict[str, Any]) -> None:
        try:
            api_key = credentials.get("baidu_api_key", "")
            if not api_key.startswith("bce-v3/"):
                raise ToolProviderCredentialValidationError(
                    "Invalid Baidu API Key format. Must start with 'bce-v3/'"
                )
            if len(api_key) != 75:  # length validation
                raise ToolProviderCredentialValidationError("API Key length invalid")
        except Exception as e:
            raise ToolProviderCredentialValidationError(str(e))
