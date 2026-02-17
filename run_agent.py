from agent.markdown_agent import MarkdownAgent

agent = MarkdownAgent()

issues, fixes = agent.run("input/sample.md")

print("\nIssues Found:")
for issue in issues:
    print("-", issue)

print("\nFix Suggestions:")
for fix in fixes:
    print("-", fix)
