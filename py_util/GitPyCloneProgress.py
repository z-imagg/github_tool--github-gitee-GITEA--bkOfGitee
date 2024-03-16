import git

class GitPyCloneProgressC(git.remote.RemoteProgress):
    def __init__(self):
        super().__init__()

    def update(self, op_code, cur_count, max_count=None, message=''):
        if len(message) != 0:
            print(op_code, cur_count, max_count, message)
        print(self._cur_line)
          
# repo = git.Repo.clone_from(url="git@gitee/xx/xx.git", to_path="xx/xx/xx", progress=GitPyCloneProgressC())
