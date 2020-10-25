import datetime
import downloads
import json
import os
import e2e


def local_kubectl_hns():
    return KubectlHns("kubectl-hns")


class KubectlHns(object):
    def __init__(self, bin, env=None):
        if env is None:
            env = os.environ.copy()
        self.bin = os.path.expanduser(bin)
        self.env = env

    def __repr__(self):
        s = "KubectlHns:" + self.bin
        return s

    # add_to_path ensures that kubectl is on the provider environ
    def add_to_path(self, env):
        d = os.path.dirname(self.bin)
        env["PATH"] = d + ":" + env["PATH"]

    def exec(self, args):
        return downloads.exec([self.bin] + args, env=self.env).strip()

    def exec_and_parse_json(self, args):
        j = downloads.exec([self.bin, "-ojson"] + args, env=self.env).strip()
        return json.loads(j)
