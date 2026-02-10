import re
import requests

def validate_markdown(file_path):
    issues = []
    fixes = []

    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    fixed_content = content

    if content.count("**") % 2 != 0:
        issues.append("Unclosed bold (** )")
        fixes.append("Add closing **")
        fixed_content += "**"

    if content.count("_") % 2 != 0:
        issues.append("Unclosed italic (_)")
        fixes.append("Add closing _")
        fixed_content += "_"

    links = re.findall(r"\((https?://[^\s]+)\)", content)

    for link in links:
        try:
            r = requests.head(link, timeout=5)
            if r.status_code >= 400:
                issues.append(f"Broken link: {link}")
                fixes.append(f"Replace or remove link: {link}")
                fixed_content = fixed_content.replace(link, "#")
        except:
            issues.append(f"Broken link: {link}")
            fixes.append(f"Replace or remove link: {link}")
            fixed_content = fixed_content.replace(link, "#")

    return issues, fixes, fixed_content
