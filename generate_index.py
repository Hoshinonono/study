# index.mdの内容を生成するpythonファイルです
# フォルダ探索をすることで目次を自動生成します
import os

# 現在のディレクトリファイル
INDEX_FILE = "index.md"
depth = int(2)

# フォルダ名かファイル名が以下に一致するものは探索を禁止する
ban_list = ['.github', 'README.md']

# index.mdに書き込む内容をcontentに追加する
content = "# Documentation Index\n\n"
content += "[![GitHub Pepository](https://img.shields.io/static/v1?label=GitHub+Pepository&message=+&color=FC02FF&logo=github)](https://github.com/Hoshinonono/study)\n\n";
content += "目次は自動生成です。\n\n"
content += "## Pages\n\n"

def generate_index(path):
    global content
    global depth
    """path フォルダ内のディレクトリまたはファイルを一覧表示する"""
    files = [f for f in os.listdir(path)]

    for file in files:
        if os.path.isfile(os.path.join(path, file)) and (not file in ban_list) and file.endswith(".md"):
            file_title = file.replace(".md", "").replace("-", " ").title()
            file_path = path + "/" + file
            content += f"- [{file_title}]({file_path})\n"

    # 深さが6よりも大きくなる場合は探索を打ち切る
    # Markdownの ### h3 みたいなのが6までだったと思うので
    if depth >= 6: return

    for folder in files:
        if os.path.isdir(os.path.join(path, folder)) and (not folder in ban_list):
            depth += 1
            content += "#" * depth
            content += f" {folder}\n\n"
            generate_index(path + "/" + folder)
            depth -= 1
    
    content += "\n"

if __name__ == "__main__":
    generate_index("./")
    with open(INDEX_FILE, "w", encoding="utf-8") as f:
        f.write(content)
