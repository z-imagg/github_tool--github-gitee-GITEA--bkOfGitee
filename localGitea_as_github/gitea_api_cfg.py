#!/usr/bin/env python
# -*- coding: <encoding name> -*-


gitea_base_url:str="https://github.local"
gitea_token:str="ab2a90dc37210a4f9aee91ab959bfa3fc1f6ba6a"

#gitea歉意接口超时时长设置为300秒，但实测 即使接口返回超时，但是该迁移还在进行 并且迁移是正常结束的
gitea_migrate_api_timeout_seconds=30