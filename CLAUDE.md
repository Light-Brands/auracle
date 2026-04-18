# CLAUDE.md — auracle (Claude-specific notes)

**Read [`AGENTS.md`](./AGENTS.md) first.** It is canonical. Notes below are Claude-only.

## Session start

1. `git fetch origin && git log --oneline origin/main -20` — local `main` lags origin
   heavily (hundreds of commits). Always check the real head before assuming state.
2. Skim recent commits — they're tiny and focused, and they tell you whether you're
   in a code task or an editorial pass.
3. There's no root `CHANGELOG.md` / `TODO.md`. Closest equivalents:
   - `book/sovereignty-series/vol-1-see/review-state.json` (editorial pass tracker)
   - `book/sovereignty-series/vol-1-see/unified-woven-integration-plan.md` (active roadmap)

## Worktree rule

Other Claude sessions often run editorial passes here concurrently. Before any
non-trivial edit, run from the QIE root:

```bash
bin/qie worktree auto <short-slug>
```

Idempotent. **Required** when you'll run `npm run dev|build|test:ci`, touch `app/`
source, or modify `app/reader/chapters.ts` or any chapter MD under
`book/sovereignty-series/vol-N/chapters/`. **Skip** for read-only exploration or a
single-line doc fix.

## Commands

- `npm run dev` / `build` — Next 14 App Router. Reader does fs reads of `book/` MD at
  request time; book tree must be intact for build.
- `npm run validate` — type-check + lint + format:check. Run before pushing.
- `npm run lint:fix` / `format` — eslint-config-next + Prettier.
- `npm run test:ci` — Jest. CI marks this `continue-on-error`; tests are largely absent.
- Pre-commit hook runs lint-staged + `tsc --noEmit`. Don't pass `--no-verify` — fix
  the underlying issue.

## Commits

- Format: `{emoji} {imperative} {description}`. See `git log` for the team's emoji
  vocabulary. CI quality job greps `app/`+`components/` for `console.log` — strip them.
- Stage files explicitly. In the same bash block as `git commit`, run
  `git diff --cached --stat` and verify the file count — concurrent sessions can
  rewrite the index between `git add` and `git commit`.
- PR to `main` via `gh pr create`. Don't merge yourself unless asked.

## Skill auto-suggestions to ignore

The vercel plugin auto-injects skill suggestions on file reads. In this repo, ignore
unless explicitly requested:

- `bootstrap` / `next-upgrade` (on `package.json`) — Next 14 is intentional, do not
  propose upgrade.
- `next-cache-components` (on `next.config.js`) — app doesn't use Next 16 cache APIs.
- `react-best-practices` (on any `.tsx`) — fine if you're rewriting that component;
  do not run unsolicited app/ review passes (focus is editorial).
- `workflow` (on `.github/workflows/*.yml`) — these are GitHub Actions, not Vercel WDK.

## Quirks

- `tsconfig.json` has `strict: false`. Don't trust the compiler for shape bugs.
- `content/` (videos) is gitignored — lesson playback links to `/content/*.mp4` will
  404 in local dev unless you populate it.
- `next.config.js` allows remote images from `images.unsplash.com` only.
- Branch `claude/doctrine-bootstrap` is far ahead of `main` (~937 commits). It is a
  long-lived integration branch — **branch from `main`, not from it.**
- For editorial tasks: edit the chapter file first, then decide whether to re-merge
  into `vol-N-complete-manuscript.md` (check recent commits for the pattern). Don't
  regenerate `.docx`/`.epub` unless the task asks for it.
