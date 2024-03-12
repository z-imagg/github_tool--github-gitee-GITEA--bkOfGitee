# gitee页面导入仓库功能 调用

gitee页面导入仓库功能 ： https://gitee.com/projects/import/url 

##   分析、调用步骤设计

**gitee页面导入仓库功能 分析、调用步骤设计**

http://giteaz:3000/wiki/wiki/src/branch/main/github_tool/github_to_gitee/gitee__importReopPageApi__analyze__callStepDesign.md


## 调用步骤

**gitee页面导入仓库功能 调用步骤**

1. 填写 目标github仓库们、目标gitee组织， http://giteaz:3000/wiki/wiki/src/branch/main/github_tool/github_to_gitee/MyConfig.py

2. 导入目标github仓库们， ```bash main.sh```

大致过程：
-  2.0  人工获得的材料: 请求模板 ， 参考 [gitee__importReopPageApi__analyze__callStepDesign.md](http://giteaz:3000/wiki/wiki/src/branch/main/github_tool/github_to_gitee/gitee__importReopPageApi__analyze__callStepDesign.md)
-  2.1. 从 请求模板 扣出 请求体模板
-  2.2. 按照 请求体模板， 为每个github仓库 制造出 请求体
-  2.3. 为每个github仓库 的 请求体 关联 一个 请求
-  2.4. 执行 每个github仓库 的 请求 以 导入 该github仓库 到gitee
