import markdown
from collections import defaultdict
from pathlib import Path

class Node:
    """Represents markdown file in context of sidebar hierarchy"""
    def __init__(self, path: Path, title: str, priority: str):
        self.path = path
        self.title = title
        self.priority = int(priority)
        self.children = []

    def add_child(self, node):
        self.children.append(node)

def get_all_md_files() -> list:
    """Return list of files with .md extension"""
    script_dir = Path(__file__).parent.resolve()
    return list(Path(f"{script_dir}/docs").glob("*.md"))

def extract_metadata(path: Path) -> dict:
    """Get metadata of markdown file"""
    content = path.read_text()
    md = markdown.Markdown(extensions=["meta"])
    md.convert(content)
    formatted_meta = {k: v[0] for k, v in md.Meta.items()}
    return formatted_meta

def build_tree(files: list) -> Node:
    """Build tree out of files and return root object"""
    root = Node(title="root", path=None, priority="0")
    nodes = {}
    orphans = defaultdict(list)
    for file in files:
        metadata = extract_metadata(file)        
        node = Node(path=file, title=metadata["title"], priority=metadata.get("priority", "0"))
        parent = metadata.get("parent", "root")

        if parent in nodes:
            nodes[parent].add_child(node)
        else:
            orphans[parent].append(node)
        nodes[node.title] = node

    for parent, children in orphans.items():
        if parent in nodes:
            nodes[parent].children.extend(children)
        elif parent != "root":
            nodes[parent] = Node(title=parent, path=None, priority="0")
            nodes[parent].children.extend(children)
            orphans["root"].append(nodes[parent])
    root.children.extend(orphans["root"])
    return root

def generate_sidebar_content(node: Node, indent) -> str:
    """Recursively generate _Sidebar.md content"""
    sidebar_content = ""
    if node.path:
        link = "https://dummylink.com"
        sidebar_content += ' ' * indent + f"* [{node.title}]({link})\n"
    elif node.title != "root":
        sidebar_content += ' ' * indent + f"* [{node.title}]\n"
    try:
        for child in sorted(node.children, key=lambda child: (-child.priority, child.title)):
            sidebar_content += generate_sidebar_content(child, indent + 1)
    except Exception as e:
        print(e)
        print([(x.title, x.priority) for x in node.children])

    return sidebar_content

def save_sidebar(sidebar_content: str) -> None:
    wiki_dir = Path(__file__).parent.resolve()
    with open(f"{wiki_dir}/docs/_sidebar.md", "w") as f:
        f.write(sidebar_content)

if __name__ == "__main__":
    files = get_all_md_files()
    root = build_tree(files)
    sidebar_content = generate_sidebar_content(root, -1)
    save_sidebar(sidebar_content)