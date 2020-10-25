state = {
    "kustomize_version": "3.6.1",
    "kubectl_hns_version": "v0.5.3"
}

import os
import sys
import tempfile
sys.path.insert(0, os.path.abspath('lib'))

from state import *
from e2e import *
from downloads import *
from git import *
from kubectl import *
from kubectlhns import *
from kustomize import *
from random import randint



def main():
    if not "kubernetes_version" in state:
        update_state(state, { "kubernetes_version": get_kubernetes_version("stable") })
    kubectl = local_kubectl()
    kubectl.version()
    args = ["get", "ns"]
    print(kubectl.exec_and_parse_json(args))



if __name__ == "__main__":
    main()