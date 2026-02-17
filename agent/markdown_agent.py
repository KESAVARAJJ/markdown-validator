# from google.adk.agent import Agent
from tools.markdown_validator import validate_markdown
import os


class MarkdownAgent:
    def __init__(self):
        print("AI Agent Initialized (Google ADK style)")

    def run(self, input_file):
        print("Agent reading markdown file...")

        issues, fixes, fixed_content = validate_markdown(input_file)

        os.makedirs("output", exist_ok=True)

        output_file = "output/fixed_sample.md"
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(fixed_content)

        return issues, fixes
