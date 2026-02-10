from agent.markdown_agent import MarkdownValidatorAgent

agent = MarkdownValidatorAgent()

issues, fixes = agent.run(
    "input/sample.md",
    "output/fixed_sample.md"
)

print("Detected Issues:")
for i in issues:
    print("-", i)

print("\nSuggested Fixes:")
for f in fixes:
    print("-", f)
