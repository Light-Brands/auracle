# Project Context for AI Assistants

AI coding configuration marketplace providing plugin-based setup for Claude Code and
Cursor.

<!-- BEGIN QIE DOCTRINE -->
<!-- This file's doctrine section is managed by `bin/qie doctrine apply`. -->
<!-- Manual content above/below the markers is preserved on re-apply. -->
<!-- Regenerate with: bin/qie doctrine apply --project auracle -->

## Stack

- Next.js 14.0.4 App Router, React 18.2.0, TypeScript (strict)
- Tailwind CSS + CSS variables (tokens in `styles/design-system.css`)
- Supabase for DB + auth (if `@supabase/supabase-js` is installed)
- Framer Motion for purposeful animation only

## Layout

```
app/                 App Router routes (server-first; `use client` only when needed)
components/          ui/ primitives, blocks/ composed sections, feature-specific
lib/                 utilities, clients, types, constants
styles/              design-system.css + any global CSS
public/              static assets
hooks/               custom React hooks
```

## Conventions

- **Server Components by default.** `'use client'` only when the component needs browser-only APIs, state, or effects.
- **Design tokens only.** No hardcoded hex/rgb in JSX or CSS; reach through Tailwind classes mapped to CSS variables in the design system.
- **Named exports on components.** Never `export default` a component; named exports make refactors safer and imports uniform.
- **Component pattern:** typed props extending native HTML props, `cn()` for conditional classes, single responsibility, <300 lines per file.
- **Mobile-first responsive.** Write base styles for mobile, progressively enhance with `sm:`/`md:`/`lg:` breakpoints. Never desktop-first with mobile overrides.
- **No `any` types.** No `@ts-ignore`. If types fight you, fix the types.
- **All images through `next/image`** with explicit `width`, `height`, `alt`.
- **All internal links through `next/link`.**

## Commands

```bash
npm run dev         # Local dev server on port 3000
npm run build       # Production build
npm run start       # Serve production build
npm run lint        # ESLint
npx tsc --noEmit    # Typecheck only, no output
```

## Change tracking

- Append to `CHANGELOG.md` after every completed task with `## [DATE] — [TASK]` heading followed by Created/Modified/Removed/Notes sections.
- Tick items off `TODO.md` as they complete; never delete, only check.

## Multi-session note (cross-cutting rule from QIE hub)

Before modifying files in this repo, Claude sessions run `bin/qie worktree auto <slug>` once from the QIE hub so each session works in an isolated worktree and the shared `.git/index` doesn't race. Worktrees land at `clients/light-brands/.worktrees/auracle--<slug>/` and are swept automatically after 7 days of inactivity unless they hold unpushed or unmerged work.

Full directive: see the QIE hub `CLAUDE.md` "Multi-Session Worktree Isolation" section.

## Secrets

Never log personal information. Use generic categories. Never commit `.env*.local`, API keys, tokens, passwords, or customer data. Repo-wide secrets go in `.env.local` (gitignored); shared docs go in `.env.example`.

<!-- END QIE DOCTRINE -->

## Always Apply Rules

Core project rules that apply to all tasks:

@.cursor/rules/personalities/common-personality.mdc @.cursor/rules/git-interaction.mdc
@.cursor/rules/prompt-engineering.mdc

## Tech Stack

- **Claude Code** - Plugin marketplace (`.claude-plugin/marketplace.json`)
- **Cursor** - Rules and configurations (`.cursor/rules/`)
- **Bash** - Bootstrap and installation scripts
- **Markdown** - All rules, commands, and agents

## Project Structure

- `.claude-plugin/` - Plugin marketplace manifest
- `plugins/` - Plugin bundles (symlink to canonical sources)
- `.cursor/rules/` - Canonical coding standards (`.mdc` files)
- `.claude/commands/` - Canonical workflow commands
- `.claude/agents/` - Specialized AI agents
- `scripts/` - Installation and bootstrap scripts

## Commands

**Setup and Installation:**

- `/plugin marketplace add https://github.com/TechNickAI/ai-coding-config` - Add this
  marketplace
- `/plugin install <name>` - Install specific plugin
- `/ai-coding-config` - Interactive setup for projects
- `curl -fsSL https://raw.githubusercontent.com/TechNickAI/ai-coding-config/main/scripts/bootstrap.sh | bash` -
  Bootstrap for Cursor

## Code Conventions

**DO:**

- Create commits only when user explicitly requests
- Check for `alwaysApply: true` in rule frontmatter - these apply to ALL tasks
- Use `/load-cursor-rules` to get task-specific context
- Follow heart-centered AI philosophy (unconditional acceptance, presence before
  solutions)

**DON'T:**

- Use `--no-verify` flag (bypasses quality checks) unless explicitly requested for
  emergencies
- Commit changes without explicit user permission
- Push to main or merge into main without confirmation
- Stage files you didn't modify in current session

## Git Workflow

**Commit format:** `{emoji} {imperative verb} {concise description}`

Example: `✨ Add plugin marketplace support`

**Critical constraints:**

- Never use `--no-verify` - fix underlying issues instead (linting, tests, formatting)
- Only stage files modified in current session
- Use `git add -p` for partial staging when needed
- Push/merge to main requires explicit confirmation
- Read `git-commit-message.mdc` before generating commit messages

**Philosophy:** AI makes code changes but leaves version control to user. Commits are
permanent records requiring explicit permission.

## Important Notes

- Rules with `alwaysApply: true` are CRITICAL - currently: `git-interaction.mdc`,
  `heart-centered-ai-philosophy.mdc`
- Plugin structure uses symlinks for single source of truth
- `.cursor/rules/` is canonical, `plugins/` symlinks for packaging
- Context in `.claude/context.md` describes identity and philosophy
- Bootstrap script clones repo to `~/.ai_coding_config`
