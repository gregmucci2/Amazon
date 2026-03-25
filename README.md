# Amazon

Repository for testing AWS Inspector vulnerability scanning with GitHub Actions.

## Amazon Inspector Setup

This repository is configured with Amazon Inspector to automatically scan for vulnerabilities on every push and pull request.

### How to view scan results:
1. Go to the **Actions** tab to see workflow runs
2. Check the **Checks** tab on pull requests for real-time results
3. Download artifacts to view detailed reports (JSON, CSV, Markdown)

### Vulnerability Scanning Features:
- ✅ Scans on every push to main
- ✅ Scans on every pull request
- ✅ Daily scheduled scans
- ✅ Replaces Dependabot with Amazon Inspector

---
Last updated: 2026-03-25