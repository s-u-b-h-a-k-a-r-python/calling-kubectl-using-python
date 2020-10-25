import datetime
import os

import downloads
import e2e

def local_kustomize():
    return Kustomize("kustomize")


class Kustomize(object):
    def __init__(self, bin, env=None):
        if env is None:
            env = os.environ.copy()
        self.bin = os.path.expanduser(bin)
        self.env = env

    def __repr__(self):
        s = "Kustomize:" + self.bin
        return s

    # add_to_path ensures that kustomize is on the provider environ
    def add_to_path(self, env):
        d = os.path.dirname(self.bin)
        env["PATH"] = d + ":" + env["PATH"]

    def create_with_namespace(self, namespace, dir):
        stdout = self.exec(["create", "--autodetect", "--namespace", namespace], dir)
        return stdout

    def build(self, output, dir):
        stdout = self.exec(["build", "-o", output], dir)
        return stdout

    def version(self):
        stdout = self.exec(["version"])
        return stdout

    def exec(self, args, dir=None):
        return downloads.exec(
            [self.bin] + args, cwd=dir, env=self.env
        ).strip()
