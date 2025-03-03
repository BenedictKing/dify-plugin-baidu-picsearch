## baidu_picsearch

**Author:** BenedictKing
**Version:** 0.0.1
**Type:** tool

### Description

### 使用说明

1. **配置会话变量**  
   在Dify会话变量中添加以下两个必需参数（参考示意图：![guide3](./images/guide3.png）：
   - `baiduapikey`: 百度图像搜索API密钥
   - `baiduappid`: 百度开发者应用ID

> 如何获取：请登录百度AI开放平台，创建应用后获取API Key和App ID

### 异常处理

**问题描述：** 安装插件时遇到异常信息：plugin verification has been enabled, and the plugin you want to install has a bad signature，应该如何处理？

**解决办法：** 在 .env 配置文件的末尾添加 `FORCE_VERIFYING_SIGNATURE=false` 字段即可解决该问题。添加该字段后，Dify 平台将允许安装所有未在 Dify Marketplace 上架（审核）的插件，可能存在安全隐患。


