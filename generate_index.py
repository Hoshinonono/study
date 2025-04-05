import os

MARKDOWN_DIR = "./"
INDEX_FILE = "index.md"

def generate_index():
    """docs フォルダ内の Markdown ファイルを一覧表示する index.md を生成"""
    files = [f for f in os.listdir(MARKDOWN_DIR) if f.endswith(".md") and f != "index.md" and f != "README.md"]
    files.sort()  # アルファベット順にソート

    index_content = "# Documentation Index\n\n"
    
    index_content += "[![GitHub Pepository](https://img.shields.io/static/v1?label=GitHub+Pepository&message=+&color=FC02FF&logo=github)](https://github.com/Hoshinonono/study)\n\n";
    index_content += "目次は自動生成です。\n\n"
    index_content += "## Pages\n\n"

    for file in files:
        file_title = file.replace(".md", "").replace("-", " ").title()
        index_content += f"- [{file_title}]({file})\n"

    with open(INDEX_FILE, "w", encoding="utf-8") as f:
        f.write(index_content)

if __name__ == "__main__":
    generate_index()
