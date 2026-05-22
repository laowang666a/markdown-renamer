#  markdown-renamer

## 📖 这个工具是什么？
**markdown-renamer** 是一个用 Python 编写的高效命令行工具，旨在帮助开发者/用户快速完成文件夹内的markdown文件的改名

## 使用示例
# 预览模式，不修改文件
python main.py ./my_notes "%Y-%m-%d" --dry-run

# 正式执行
python main.py ./my_notes "%Y-%m-%d" 
# 参数：
  dir       目标文件夹路径（必填）
  format    日期格式，如 "%Y-%m-%d"（必填）
  -d        预览模式，不实际修改文件（可选）


## 🛠️ 安装方式
### 前提条件
* Python 3.8 或更高版本
### 通过 pip 安装 (推荐)
你可以直接通过 pip 安装到全局或虚拟环境中：
```bash
pip install -r requirements.txt


