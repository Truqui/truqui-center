---
name: new-issue
description: Create a GitHub issue (feature or bug) interactively and publish it via gh CLI
allowed-tools: Bash(gh issue create:*), Bash(gh auth status:*), Bash(git remote get-url origin:*), Read, Glob, Grep
---

# New GitHub Issue

Help me create and publish a GitHub issue for this Django project.

## Step 1 — Check environment

Before asking anything, silently run:
- `gh auth status` to verify the GitHub CLI is authenticated
- `git remote get-url origin` to confirm the repository

If `gh` is not authenticated, stop and tell the user to run `gh auth login` first.

## Step 2 — Ask the issue type

Ask the user: is this a **feature request** or a **bug report**?

## Step 3 — Read the relevant template

Based on the answer, silently read only the corresponding file:
- Feature → `.github/ISSUE_TEMPLATE/feature_request.md`
- Bug → `.github/ISSUE_TEMPLATE/bug_report.md`

This defines the exact structure to use when drafting. Do not hardcode any template structure in this skill.

## Step 4 — Gather the remaining information

Ask these questions one by one in a conversational way. Do not dump them all at once.

Depending on type:

   **If feature:**
   - What problem does this feature solve? Who is affected?
   - Do you have an idea for the implementation, or should I propose one based on the code?

   **If bug:**
   - What happens vs. what should happen?
   - What are the steps to reproduce it?

3. **Title**: Ask for a short, descriptive title for the issue.

## Step 5 — Analyse the code

Silently explore the project structure to understand the relevant code. Read files like models.py, views.py, urls.py, serializers.py, etc. that seem related to what the user described. If you are unsure where to look, ask the user: "¿Tienes algún archivo o módulo concreto en mente, o prefieres que lo explore yo?".

## Step 6 — Draft the issue

Using the template read in Step 3, generate the full issue body filling in all sections. Strip out the HTML comments (`<!-- ... -->`). If the user said they have no implementation idea, propose one based on what you found in the code.

---

## Step 7 — Review and confirm

Show the user the complete draft with title and body. Ask:

> ¿Te parece bien este borrador o quieres hacer algún cambio antes de publicarlo?

Wait for explicit approval. Allow the user to request edits and regenerate before proceeding.

## Step 8 — Publish to GitHub

Once the user approves, run:

```bash
gh issue create \
  --title "<title>" \
  --body "<body>" \
  --label "<enhancement|bug>"
```

Show the URL of the created issue at the end.
