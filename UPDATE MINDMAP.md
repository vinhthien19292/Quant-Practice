# Update Mindmap — Code & Content Sync

**Purpose**: Document the sync pipeline between (a) Claude chat changes, (b) local OneDrive folder, (c) GitHub repo, (d) live GitHub Pages, (e) Tab S PWA. Read this before making any change if you're rusty on the workflow.

**Companion doc**: `UPDATE PROGRESS.md` covers learning progress (mastery marks) sync — a separate dimension from code sync.

---

## TL;DR — 3-click update

```
Change file → GitHub Desktop → Commit → Push → done
```

Total time: ~2 minutes end-to-end (30 sec push + 1-2 min Pages deploy).

---

## Architecture

```
┌──────────────────────────────────────────────────────────────┐
│  CLAUDE CHAT (desktop app)                                   │
│  - You describe change                                       │
│  - Claude edits files in D:\OneDrive\1. Quant\Quant-Practice\│
└──────────────────────────┬───────────────────────────────────┘
                           │ (files change on disk)
                           ▼
┌──────────────────────────────────────────────────────────────┐
│  LOCAL FOLDER (OneDrive-synced)                              │
│  D:\OneDrive\1. Quant\Quant-Practice\                        │
│  - Contains git repo (.git/ hidden folder)                   │
│  - Also synced to OneDrive cloud (backup)                    │
└──────────────────────────┬───────────────────────────────────┘
                           │ (GitHub Desktop detects diff)
                           ▼
┌──────────────────────────────────────────────────────────────┐
│  GITHUB DESKTOP APP                                          │
│  - Shows changed files in sidebar                            │
│  - You type summary + Commit + Push                          │
└──────────────────────────┬───────────────────────────────────┘
                           │ (git push origin main)
                           ▼
┌──────────────────────────────────────────────────────────────┐
│  GITHUB REPO                                                 │
│  github.com/vinhthien19292/Quant-Practice                    │
│  - Version history (rollback anytime)                        │
│  - Backup redundancy (in addition to OneDrive)               │
└──────────────────────────┬───────────────────────────────────┘
                           │ (GitHub Pages auto-deploy, ~1-2 min)
                           ▼
┌──────────────────────────────────────────────────────────────┐
│  LIVE URL                                                    │
│  https://vinhthien19292.github.io/Quant-Practice/            │
│  → auto-redirects to Quant-Roadmap.html                      │
└──────────────────────────┬───────────────────────────────────┘
                           │ (Tab S opens URL, cached in PWA)
                           ▼
┌──────────────────────────────────────────────────────────────┐
│  TAB S — PWA APP                                             │
│  Icon ⚛ Quant on home screen → fullscreen atlas             │
│  Pull-to-refresh to load latest                              │
└──────────────────────────────────────────────────────────────┘
```

---

## Scenario 1: Claude edits files via chat

**Situation**: You ask Claude in a chat "add L3 lesson" or "fix typo in L2 §3".

**Steps**:

1. Claude uses Edit/Write tools on files in `D:\OneDrive\1. Quant\Quant-Practice\`
2. When Claude reports done, **open GitHub Desktop**
3. Sidebar left shows all changed files (green dot for modified, plus for new, minus for deleted)
4. Review the changes if you want (click a file to see diff)
5. Bottom-left: type Summary (e.g. `Add L3 Derivatives lesson`)
6. Click **Commit to main**
7. Top toolbar: click **Push origin**
8. Wait ~30 seconds
9. GitHub Pages deploys automatically in ~1-2 min
10. Tab S: open Quant icon → pull-to-refresh (drag down from top) → new content live

**No re-upload, no reinstall.**

---

## Scenario 2: You edit files yourself

**Situation**: You want to fix a typo without asking Claude, or add a note.

**Steps**:

1. Open the file in any editor (Notepad++, VS Code, even Notepad)
2. Edit + save
3. GitHub Desktop → same 3 clicks (Commit → Push)
4. Same result

**Warning**: don't edit files while Claude is working — creates merge conflicts.

---

## Scenario 3: New chat with Claude (context reset)

**Situation**: Previous chat hit usage limit or you started fresh.

**Steps**:

1. Open Claude desktop app → project **Quant Practice** (already has imported knowledge)
2. Paste this bootstrap prompt:

   ```
   Read D:\OneDrive\1. Quant\Quant-Practice\UPDATE MINDMAP.md and
   D:\OneDrive\1. Quant\Quant-Practice\UPDATE PROGRESS.md to
   understand the atlas project's code sync and progress sync workflows.
   Also read ROADMAP.md for curriculum structure.

   Today I want to: [describe task]

   Standing rules (also in the docs):
   - Content in English, chat with me in Vietnamese
   - Rigor: MFE-level with proofs + intuition, not high-school VN style
   - Concept IDs stable forever, never rename existing IDs
   - Never touch *.notes.md files, backup/, Notebooks/, PDF/, Data/, References/
   - Don't modify D:\OneDrive\1. Quant\World Quant - Master of Financial Engineering
   - After ANY build/edit, remind me to (1) commit+push code via GitHub Desktop,
     (2) export progress JSON if session was long, (3) update the UPDATE *.md docs
     if workflow changed
   ```

3. Attach latest progress JSON from `backup/` folder (optional — helps Claude see actual mastery state)

---

## PWA on Tab S — no reinstall on updates

The installed Quant icon on Tab S home screen is a **PWA wrapper** that loads content from GitHub Pages each time you open it.

**Updates propagate automatically**:
- Content changes (HTML, CSS, JS, lessons, atlas layout) → just pull-to-refresh in the app
- No reinstall, no re-download

**Reinstall ONLY needed when**:
- Manifest changes (app name, icon file, `start_url`) — rare
- Chrome cache gets corrupted (very rare)

**How to reinstall if needed**:
1. Long-press Quant icon on home screen → Uninstall
2. Open Chrome → paste URL → ⋮ → Install and create shortcut → Install
3. Icon reappears, up-to-date

---

## Progress data — NOT synced automatically

Mastery marks (Learning/Mastered) live in browser `localStorage`, tied to URL.

- **Desktop Chrome** vs **Tab S Chrome** = separate localStorage = separate progress
- Same URL used on both devices, but localStorage doesn't sync across devices

**Sync manually** (weekly):
1. On device with latest marks: Atlas → click 📊 Progress button → **Backup JSON** → download file
2. Save file to `D:\OneDrive\1. Quant\Quant-Practice\backup\` (already gitignored, stays private)
3. On other device: Atlas → 📊 Progress → **Restore JSON** → pick the file
4. Progress merges

**Recommendation**: pick ONE source of truth (usually desktop for easier clicking). Tab S = read-only during the week. Weekly review on desktop.

---

## Common commands / clicks

| Task | Where | How |
|---|---|---|
| Update after Claude edit | GitHub Desktop | Commit → Push (2 clicks) |
| Roll back last change | GitHub Desktop | History tab → right-click commit → Revert |
| See what changed | GitHub Desktop | Changes tab → click file → view diff |
| Emergency undo before push | GitHub Desktop | File in Changes → right-click → Discard changes |
| Force refresh Tab S | Chrome PWA | Pull-to-refresh (drag down from top) |
| Force redeploy Pages | GitHub.com | Settings → Pages → make any change → Save |
| See Pages deploy status | GitHub.com | Actions tab → latest workflow run |

---

## Troubleshooting

**"Push failed" in GitHub Desktop**
- Likely: someone else changed repo (unlikely for you)
- Fix: click **Fetch origin** → **Pull** → then Push again

**"Merge conflict"**
- You edited file locally + Claude edited same file
- Fix: GitHub Desktop shows conflict → open file, look for `<<<<<<<` markers → keep the version you want → save → GitHub Desktop → Commit → Push

**Tab S shows old version**
- Fix 1: Pull-to-refresh (drag down)
- Fix 2: Close app fully (recent apps → swipe up) → reopen
- Fix 3: Clear Chrome cache: Chrome settings → Privacy → Clear browsing data → last hour

**Atlas 404 on Pages**
- Check: URL should be `https://vinhthien19292.github.io/Quant-Practice/` OR append `Quant-Roadmap.html`
- Check: `index.html` file exists in repo root (it's the redirect stub)

**MathJax formulas show as `$f(x)$` text**
- CDN blocked or slow
- Fix: refresh page, wait 5-10 sec for CDN load
- Long-term: run `setup_offline.py` to bundle MathJax locally (already done in current setup)

**OneDrive complains about `.git/` folder**
- Rare, but if OneDrive shows sync errors on `.git/`:
  - Close GitHub Desktop
  - Wait for OneDrive to finish syncing
  - Reopen GitHub Desktop
- Long-term fix: move `Quant-Practice/` out of OneDrive to `D:\Projects\` (use git as sync instead)

---

## What NEVER to commit

Already in `.gitignore`, but for awareness:

- `backup/*.json` — personal progress data
- `Notebooks/` — Jupyter drills with your own answers
- `PDF/` — generated PDF handouts
- `Data/` — financial data files (may be sensitive)
- `References/` — books (copyright risk)
- `*.notes.md` — your personal notes
- `.vscode/`, `__pycache__/`, `.ipynb_checkpoints/` — editor/tool junk

If you ever accidentally commit sensitive files: **stop, nuke the repo, recreate**. Once pushed, it's in git history forever.

---

## Backup redundancy

You have 3 independent backups now:

1. **OneDrive cloud** — auto-syncs everything in `D:\OneDrive\1. Quant\Quant-Practice\` (including gitignored files like backup/)
2. **GitHub repo** — public code, full version history, unlimited retention
3. **Local disk** — your working copy on the PC

Lose any ONE, the others survive. Belt-and-suspenders.

---

## Standing rules for Claude

These rules apply in ANY chat working on this project.

1. **Language**: content in English, chat in Vietnamese
2. **Rigor level**: MFE-textbook (proofs + intuition + worked examples), not high-school Vietnamese style
3. **Concept IDs**: NEVER rename existing IDs. Adding new is fine.
4. **Personal files**: NEVER touch `*.notes.md`, `backup/`, `Notebooks/`, `PDF/`, `Data/`, `References/`
5. **Other folders**: NEVER modify `D:\OneDrive\1. Quant\World Quant - Master of Financial Engineering`
6. **Post-build reminder** (MANDATORY): after ANY file edit/creation, remind user to:
   - Commit + Push via GitHub Desktop (code sync)
   - Export progress JSON if session was long (progress sync)
   - Update `UPDATE MINDMAP.md` or `UPDATE PROGRESS.md` if workflow changed
7. **Token discipline**: batch related changes into single messages, avoid ping-pong for small fixes
8. **Verify before claim**: don't say "done" without checking the file actually saved

---

## Quick reference URLs

- **Live atlas**: https://vinhthien19292.github.io/Quant-Practice/
- **GitHub repo**: https://github.com/vinhthien19292/Quant-Practice
- **Pages settings**: https://github.com/vinhthien19292/Quant-Practice/settings/pages
- **Local folder**: `D:\OneDrive\1. Quant\Quant-Practice\`

---

*Last updated: 2026-08-01 — initial version*
