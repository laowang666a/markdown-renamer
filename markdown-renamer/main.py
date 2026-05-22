import argparse

from core import*
from pathlib import Path

def main():
    #1、创建解析器
    parser = argparse.ArgumentParser(
        description="Markdown 文件批量改名利器 (MD-Rename CLI)",
        epilog="使用示例: python main.py ./docs YYYY-MM-DD"
    )

    #2、添加参数

    parser.add_argument("dir", type=str, help="目标文件夹路径")

    parser.add_argument("format", type=str, help="需要修改成的日期格式")
    parser.add_argument("-d", "--dry-run", action="store_true", help="预览模式：只打印改名效果，不实际修改文件")
    args = parser.parse_args()


    target_dir = Path(args.dir)
    target_format = args.format


    rename_list = build_rename_jobs(target_dir, target_format)
    jobs = resolve_conflicts(rename_list)
    if args.dry_run:
        print("🔍 当前运行在 [预览模式]，不会真正修改磁盘文件。\n" + "-" * 40)
        # 如果是 dry-run 模式，只打印提示
        print(f"⚠️ [DRY RUN 模式] 将要执行的操作：")
        for item in jobs:
            print(f"将文件{item.file_path.stem}.md,改名为{item.new_name}")
        print(f"  (系统未做任何真实修改)")
    else:
        for item in jobs:
            new_path = item.file_path.with_name(item.new_name)

            item.file_path.rename(new_path)
        print(f"成功修改 {len(jobs)}个md文件名字")

if __name__ == "__main__":
    main()



