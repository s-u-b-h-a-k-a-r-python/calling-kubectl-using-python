import os
import os.path
import tempfile

_artifacts_dir = None


def artifacts_dir():
    global _artifacts_dir
    if _artifacts_dir is None:
        wd = workspace_dir()
        _artifacts_dir = os.path.join(wd, "artifacts")
        os.makedirs(_artifacts_dir, exist_ok=True)
    return _artifacts_dir


_workspace_dir = None


def workspace_dir():
    global _workspace_dir
    if _workspace_dir is None:
        _workspace_dir = os.environ.get("WORKSPACE") or tempfile.mkdtemp(prefix="tmp-e2e")
    return _workspace_dir
