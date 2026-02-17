import re
import requests


def validate_markdown(file_path):
    issues = []
    fixes = []

    # Read file
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    fixed_content = content

    # Check bold formatting (**)
    if content.count("**") % 2 != 0:
        issues.append("Unclosed bold (**)")
        fixes.append("Add closing **")
        fixed_content += "**"

    # Check italic formatting (_)
    if content.count("_") % 2 != 0:
        issues.append("Unclosed italic (_)")
        fixes.append("Add closing _")
        fixed_content += "_"

    # Check links
    links = re.findall(r"\((https?://[^\s]+)\)", content)

    for link in links:
        try:
            response = requests.head(link, timeout=5)
            if response.status_code >= 400:
                issues.append(f"Broken link: {link}")
                fixes.append(f"Replace or remove link: {link}")
                fixed_content = fixed_content.replace(link, "#")

        except requests.RequestException:
            issues.append(f"Broken link: {link}")
            fixes.append(f"Replace or remove link: {link}")
            fixed_content = fixed_content.replace(link, "#")

    return issues, fixes, fixed_content
