from pathlib import Path
from datetime import datetime
from schemas import RenameJob
def scan_directory2(path: Path) -> list[Path]:
    path_list = []
    if not path.is_dir():
        return path_list
    for item in path.iterdir():
        if item.is_file() and item.suffix == ".md":
            path_list.append(item)
    return path_list

def scan_directory(path: Path) -> list[Path]:
    if not path.is_dir():
        return []
    return list(path.glob("*.md"))

#它接受一个 Path（单个文件路径）和一个 date_format 字符串（比如 "%Y-%m-%d"），
# 返回新文件名字符串（比如 "2024-01-15.md"）。
def generate_new_name(path: Path,date_format: str) -> str:
    timestamp = path.stat().st_mtime
    modify_time = datetime.fromtimestamp(timestamp)
    formatted_time = modify_time.strftime(date_format)
    return formatted_time+".md"

# build_rename_jobs。
# 它接受 directory: Path 和 date_format: str，返回 list[RenameJob]。
# 内部调用 scan_directory 和 generate_new_name，把结果组装成 RenameJob 列表。
def build_rename_jobs(directory: Path, date_format: str) -> list[RenameJob]:
    rename_list=[]
    md_path = scan_directory(directory)
    for item in md_path:
        new_name = generate_new_name(item, date_format)
        rename_list.append(
            RenameJob(
                file_path=item,
                new_name=new_name,
            )
        )
    return rename_list
#最后一个核心函数：resolve_conflicts。
#接受 list[RenameJob]，返回 list[RenameJob]。逻辑是：如果多个文件的 new_name 相同，
# 从第二个开始改成 2024-01-15_2.md、2024-01-15_3.md，以此类推。
def resolve_conflicts(jobs: list[RenameJob]) -> list[RenameJob]:
    set_list = set()
    for item in jobs:
        original_path = Path(item.new_name)
        stem = original_path.stem
        suffix = original_path.suffix
        i = 2
        current_name = item.new_name
        while current_name in set_list:
            current_name = f"{stem}_{i}{suffix}"
            i = i+1
        item.new_name = current_name
        set_list.add(current_name)
    return jobs





    # new_name = generate_new_name(directory,date_format)





# if __name__ == "__main__":
    # path=Path(r"D:\python_project\CLI_rename\markdown-renamer\README.md")
    # timeline=path.stat().st_mtime
    # modify_time = datetime.fromtimestamp(timeline)
    # formatted_time = modify_time.strftime("%Y-%m-%d %H:%M:%S")
    # print(formatted_time)








# from pathlib import Path
#
# p = Path(".")
# print(p.is_dir)
# print(p.is_dir())

