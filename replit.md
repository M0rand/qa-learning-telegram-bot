# Workspace

## Overview

pnpm workspace monorepo using TypeScript. Each package manages its own dependencies. Also includes a standalone Python (Flask) boilerplate app.

## Stack

- **Monorepo tool**: pnpm workspaces
- **Node.js version**: 24
- **Package manager**: pnpm
- **TypeScript version**: 5.9
- **API framework**: Express 5
- **Database**: PostgreSQL + Drizzle ORM
- **Validation**: Zod (`zod/v4`), `drizzle-zod`
- **API codegen**: Orval (from OpenAPI spec)
- **Build**: esbuild (CJS bundle)

## Python App (`python-app/`)

A standalone Flask boilerplate. Runs via the "Python App" workflow on port 5000.

- **Runtime**: Python 3.11
- **Framework**: Flask 3
- **Entry point**: `python-app/app.py`
- **Config**: `python-app/src/config.py` (reads from `.env`)
- **Routes**: registered in `python-app/src/routes/`
  - `GET /health` — health check
  - `GET /example/` — list items (stub)
  - `POST /example/` — create item (stub)

### Python Key Commands

- `cd python-app && python3 app.py` — run the Flask server
- Copy `.env.example` → `.env` and set your values before running

## Key Commands

- `pnpm run typecheck` — full typecheck across all packages
- `pnpm run build` — typecheck + build all packages
- `pnpm --filter @workspace/api-spec run codegen` — regenerate API hooks and Zod schemas from OpenAPI spec
- `pnpm --filter @workspace/db run push` — push DB schema changes (dev only)
- `pnpm --filter @workspace/api-server run dev` — run API server locally

See the `pnpm-workspace` skill for workspace structure, TypeScript setup, and package details.
