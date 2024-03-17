import git

from tqdm import tqdm

class GitPyCloneProgressC(git.remote.RemoteProgress):
    def __init__(self,progressTitle:str):
        super().__init__()
        #进度条标题
        self.progressTitle=progressTitle

    def update(self, op_code, cur_count, max_count=None, message=''):
        if getattr(self,"pbar",None) is None:
            #第一次更新进度时，才初始化进度条。 不然，空仓库也会初始化进度条
            self.pbar = tqdm(desc=self.progressTitle)

        self.pbar.total = max_count
        self.pbar.n = cur_count
        self.pbar.refresh()

          
# repo = git.Repo.clone_from(url="git@gitee/xx/xx.git", to_path="xx/xx/xx", progress=GitPyCloneProgressC())
