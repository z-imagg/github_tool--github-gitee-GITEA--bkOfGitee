import git

from alive_progress import alive_bar

class GitPyCloneProgressC(git.remote.RemoteProgress):
    def __init__(self):
        super().__init__()
        self.limit=100
        self.bar=alive_bar(self.limit, manual=True)
        self.bar.__enter__()


    def update(self, op_code, cur_count, max_count=None, message=''):
        if len(message) != 0:
            # print(op_code, cur_count, max_count, message)
            pass
        rate:float=cur_count/max_count
        self.bar(rate*self.limit)
        # if cur_count==max_count:
        #     self.bar.__exit__(None,None,None)
        # print(self._cur_line)
          
# repo = git.Repo.clone_from(url="git@gitee/xx/xx.git", to_path="xx/xx/xx", progress=GitPyCloneProgressC())
