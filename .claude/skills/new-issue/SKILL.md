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

## Step 2 — Ask for a task description

Ask the user for a free-text description of what they want, in their own words: a feature idea, a problem, a bug — whatever they have in mind. Do not ask about type, title, or structure yet.

## Step 3 — Infer the issue

From the description, infer:
- **Type**: feature request or bug report
- **Title**: a short, descriptive title
- **Problem**: the problem to solve (feature) or the actual-vs-expected behavior (bug)
- **High-level solution**: product-level only. Light technical framing is fine (e.g. "add a way to configure X from the admin"), but no implementation detail — no file paths, model/field definitions, class/module names, admin/queries/views specifics.

If the description doesn't give enough to infer one or more of these with reasonable confidence, ask a targeted follow-up for each gap, keeping them to a minimum — don't fall back to a full one-by-one questionnaire.

## Step 4 — Read the relevant template

Based on the inferred type, silently read only the corresponding file:
- Feature → `.github/ISSUE_TEMPLATE/feature_request.md`
- Bug → `.github/ISSUE_TEMPLATE/bug_report.md`

This defines the exact structure to use when drafting. Do not hardcode any template structure in this skill.

## Step 5 — Draft the issue

Using the template read in Step 4, generate the full issue body filling in all sections. Strip out the HTML comments (`<!-- ... -->`).

The issue must describe the problem and a high-level solution only — no technical implementation details (no file paths, model/field definitions, class names, admin/queries/views specifics, etc.). Those decisions belong in the planning step once work on the issue starts, not in the issue itself.

The conversation with the user can be in any language, but the issue title and body must always be written in English.

## Step 6 — Review and confirm

Show the user the complete draft with title and body, including the inferred type. Ask (in the language of the conversation) whether the draft looks good or needs changes before publishing. If the inferred type was wrong, redo Steps 4–5 with the correct template.

Wait for explicit approval. Allow the user to request edits and regenerate before proceeding.

## Step 7 — Publish to GitHub

Once the user approves, run:

```bash
gh issue create \
  --title "<title>" \
  --body "<body>" \
  --label "<enhancement|bug>"
```

Show the URL of the created issue at the end.
