# Threat Model (Public Repo Boundary)

## Goal

定義此公開 repo 的可見邊界，避免外洩核心技術資產。

## Explicitly Out of Scope

- Business workflow and decision policy
- Prompt templates and prompt engineering assets
- Real user/customer data and private schemas
- Internal service topology and routing logic

## Allowed Surface

- Generic preprocessing pipeline
- Test fixtures with synthetic content
- CLI and SDK integration patterns
- CI/CD and quality practices
