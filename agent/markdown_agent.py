import os
from tools.markdown_validator import validate_markdown


class MarkdownValidatorAgent:

    def run(self, input_md, output_md):
        issues, fixes, fixed_content = validate_markdown(input_md)

        os.makedirs(os.path.dirname(output_md), exist_ok=True)

        with open(output_md, "w", encoding="utf-8") as f:
            f.write(fixed_content)

        return issues, fixes
