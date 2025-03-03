## baidu_picsearch

**Author:** BenedictKing
**Version:** 0.0.1
**Type:** tool

### Description

![Dify样例流程图](./images/guide1.png)  
*图1: Dify中插件调用流程图*

![输出效果图](./images/guide2.png)  
*图2: 搜索结果示例*

### 使用说明

1. **导入应用配置**  
   创建新应用，选择DSL导入功能：
   ```bash
   dify-example.yml  # 示例应用配置文件
   ```

2. **配置会话变量**  
   在Dify会话变量中添加或修改以下两个必需参数，分别填入（参考示意图：![guide3](./images/guide3.png）：
   - `baiduapikey`: 百度图像搜索API密钥
   - `baiduappid`: 百度开发者应用ID

> 如何获取：请登录百度AI开放平台，创建应用后获取API Key和App ID

### 异常处理

**问题描述：** 安装插件时遇到异常信息：plugin verification has been enabled, and the plugin you want to install has a bad signature，应该如何处理？

**解决办法：** 在 .env 配置文件的末尾添加 `FORCE_VERIFYING_SIGNATURE=false` 字段即可解决该问题。添加该字段后，Dify 平台将允许安装所有未在 Dify Marketplace 上架（审核）的插件，可能存在安全隐患。


