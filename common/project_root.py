from pathlib import Path

def get_project_root():
    """
    自动查找项目根目录
    规则：向上查找包含 README.md 或 .git 的目录
    """
    current = Path(__file__).resolve()

    for parent in current.parents:
        if (parent / "README.md").exists() or (parent / ".git").exists():
            return parent

    raise Exception("无法找到项目根目录（缺少标识文件）")