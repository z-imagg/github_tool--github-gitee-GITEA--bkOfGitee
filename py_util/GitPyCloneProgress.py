import git

from tqdm import tqdm

class GitPyCloneProgressC(git.remote.RemoteProgress):
    def __init__(self):
        super().__init__()
        self.pbar = tqdm()


    def update(self, op_code, cur_count, max_count=None, message=''):
        self.pbar.total = max_count
        self.pbar.n = cur_count
        self.pbar.refresh()

          
# repo = git.Repo.clone_from(url="git@gitee/xx/xx.git", to_path="xx/xx/xx", progress=GitPyCloneProgressC())
