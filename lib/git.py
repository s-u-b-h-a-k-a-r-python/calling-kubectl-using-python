import downloads
import os

class Git(object):
    def __init__(self, user_email, user_name, env=None):
        if env is None:
            env = os.environ.copy()
        self.bin = "git"
        self.env = env
        downloads.exec(["chmod", "600", "/root/.ssh/id_rsa"])
        downloads.exec(["git", "config", "--global", "user.email", user_email])
        downloads.exec(["git", "config", "--global", "user.name", user_name])

    def __repr__(self):
        return "Git:" + downloads.exec(["which", "git"])

    def clone(self, repo, directory):
        downloads.exec(["git", "clone", "--recursive", repo, directory])
        self.statedir = directory

    def checkout(self, branch):
        self.exec(["checkout", branch])

    def commit_and_push(self, branch, file, msg):
        self.exec(["add", file])
        self.exec(["commit", "-m", msg])
        self.exec(["push", "origin", "HEAD:%s" % branch])

    def create_remote_tag(self, tag):
        self.exec(["tag", tag])
        self.exec(["push", "origin", tag])

    def get_commit_message(self, commit_hash):
        return self.exec(["show", "--pretty=format:%s", "-s", commit_hash])

    def get_last_commit_hash(self):
        return self.exec(["rev-parse", "HEAD"])

    def get_changed_files(self, revision):
        files = self.exec(
            ["show", "--pretty=", "--name-only", revision]).lstrip().rstrip()
        return files.split("\n")

    def exec(self, args):
        return downloads.exec(
            [self.bin] + args, cwd=self.statedir, env=self.env
        ).strip()
