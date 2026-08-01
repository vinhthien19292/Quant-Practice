# Update Progress — Learning State Sync

**Purpose**: How to track, backup, and sync your learning progress (mastery marks on concepts) across devices and over time. Complementary to `UPDATE MINDMAP.md` which covers code sync via GitHub.

**Two dimensions to sync**:
- **Code/content** (atlas HTML, lessons) → GitHub pipeline → see `UPDATE MINDMAP.md`
- **Learning progress** (which concepts you've mastered) → localStorage + JSON export → **this file**

---

## TL;DR — 3-step ritual

```
Mark concept → Weekly export JSON → Import on other device (optional)
```

Progress lives in browser `localStorage`. Not synced automatically. You control the sync manually.

---

## What "progress" means

The atlas tracks per-concept state in 3 tiers:

| State | Color | When to mark |
|---|---|---|
| **New** | Grey (default) | Never touched this concept |
| **Learning** | Purple ◐ | Started reading, working through examples |
| **Mastered** | Green ✓ | Solved homework/exercises without peeking, could re-derive proofs, could teach it |

**Rule of thumb**:
- Move to **Learning** when you open a lesson and read past section 1
- Move to **Mastered** only after solving problems independently, ideally a week later (spaced review)
- Don't inflate — self-honesty here directly affects future study plan quality

Visual effects:
- Node glow when Mastered (green halo)
- Edge (prerequisite line) lights up when BOTH endpoints Mastered → your knowledge network grows visibly

---

## Where progress lives

**In browser `localStorage`** under 2 keys:
- `qp_mastery` — object mapping concept ID → state (`'mastered'` / `'learning'`)
- `qp_history` — array of state changes with timestamps (last 500 events)

**Tied to URL origin**: `https://vinhthien19292.github.io` = one localStorage bucket. Different URL = different bucket. That's why:
- Desktop Chrome (URL github.io) + Tab S Chrome (URL github.io) → **same URL, but different devices** → **separate localStorage** (not cloud-synced)
- Old `file://` URL from before GitHub setup → **orphaned bucket** (still accessible if you open that file, but ignored on new URL)

---

## Marking workflow

**Where to click**: open atlas → tap any node → sidebar right hiện detail → 3 buttons **New / Learning / Mastered**.

**Or from left nav**: tap concept link → same sidebar opens.

**Auto-save**: click a button = saved immediately to localStorage. No "save" button needed.

**Undo**: click same state again to deactivate (back to previous), or explicit New.

---

## Backup workflow (weekly ritual)

**Recommended cadence**: every Sunday evening, or after a big study session.

**Steps**:
1. Open atlas (desktop or tablet — whichever has the most recent marks)
2. Click **📊 Progress** button in top bar (or `Ctrl+P` on desktop)
3. Progress dashboard opens showing pillar bars + activity log
4. Scroll to **Actions** section at bottom
5. Click **Backup JSON**
6. Browser downloads file: `quant-progress-YYYY-MM-DD.json`
7. Move file to `D:\OneDrive\1. Quant\Quant-Practice\backup\`
   - This folder is in `.gitignore` — never uploaded to GitHub (stays private)
   - OneDrive still syncs it to cloud (redundant backup)

**Naming convention**: keep the default `quant-progress-YYYY-MM-DD.json` — sortable, dated.

**Retention**: keep at least 4 recent backups. Delete older ones or move to `backup/archive/`.

---

## Cross-device sync (Desktop ↔ Tab S)

You have 3 strategies. Pick one, stick to it.

### Strategy A — Single source of truth (SIMPLEST) ⭐

- **Desktop = only place you mark progress**
- Tab S = read-only when studying (don't touch mastery buttons on tablet)
- Weekend review on desktop, mark everything you finished during the week
- **Zero sync needed**

Best for: casual studying on tablet, focused review on desktop.

### Strategy B — Manual bi-directional sync

Every Sunday:
1. Tab S: 📊 Progress → **Backup JSON** → save to Downloads
2. Move file to OneDrive folder (Samsung Files app → move to OneDrive/Quant-Practice/backup/)
3. Wait for OneDrive to sync (~1 min)
4. Desktop: 📊 Progress → **Restore JSON** → pick the file from `backup/`
5. Import **merges** (mastery marks from file override current if newer)

Best for: heavy studying on both devices.

### Strategy C — Text-based sync (no file transfer)

1. Tab S: 📊 Progress → **Export summary** (copies markdown text to clipboard)
2. Paste into a self-message via Telegram/Zalo/email
3. Desktop: open message → copy text → save as `.json` → import

Useful when: OneDrive sync is slow, or you're away from your desk.

---

## Restoring progress after data loss

**Scenarios**:
- Cleared browser cache accidentally
- Switched to a new device
- Chrome uninstalled/reinstalled
- URL changed (e.g., moved from `file://` to `github.io`)

**Recovery**:
1. Open atlas at current URL
2. 📊 Progress → **Restore JSON** → pick most recent backup file
3. Progress reloads

**If no backup exists**: mastery is lost. Only history export tells you what you'd marked. That's why weekly backup is non-negotiable.

---

## Rule: Concept IDs are STABLE forever

Progress lookup uses concept IDs (e.g., `l1-functions`, `l2-limits`, `prob-bayes`). If an ID renames in the code, that concept's progress **cannot be found** — it becomes orphaned in localStorage.

**When Claude edits the atlas**:
- ✅ OK to change display **label** (`"Functions"` → `"Functions & Mappings"`)
- ✅ OK to change **pillar assignment**
- ✅ OK to add new concepts (new IDs)
- ❌ NEVER rename existing IDs
- ❌ NEVER delete concept IDs (mark deprecated instead)

**If you spot Claude renaming an ID → stop and say "revert, keep the old ID"**.

---

## Scenario 1: Weekly review (Sunday recap)

**Sunday evening ritual**:
1. Open atlas on desktop
2. 📊 Progress → look at pillar bars
3. Review activity log — did I actually work on what I planned last week?
4. Mark any concepts I finished that I forgot to mark during the week
5. 📊 → **Backup JSON** → save to `backup/`
6. If Tab S has marks (Strategy B): export from Tab S first, restore to desktop, then backup consolidated version
7. Take 5 min: look at unmarked concepts adjacent to what I mastered → plan next week's targets

**Optional**: Copy the exported markdown summary → paste into a note (Samsung Notes / OneNote) → quick "study log" you can search later.

---

## Scenario 2: New chat with Claude — progress-focused

**When**: you want Claude to help plan next week based on where you are.

**Bootstrap prompt** (paste into new chat, project = Quant Practice):

```
Read D:\OneDrive\1. Quant\Quant-Practice\UPDATE PROGRESS.md and
D:\OneDrive\1. Quant\Quant-Practice\UPDATE MINDMAP.md first.

Attached: my latest quant-progress-YYYY-MM-DD.json from backup/.

Today I want to: [plan next 2 weeks / find weak spots / decide L3 vs L4 next / etc.]

Standing rules (also in the docs):
- Content in English, chat with me in Vietnamese
- Rigor: MFE-level with proofs + intuition, not high-school VN style
- Concept IDs stable forever, never rename
- Never touch *.notes.md files
- Don't modify D:\OneDrive\1. Quant\World Quant - Master of Financial Engineering
- After ANY build/edit, remind me to (1) commit+push code, (2) export progress JSON,
  (3) update docs if workflow changed
```

Attach the JSON file so Claude can see actual mastery state, not guess.

---

## Scenario 3: New chat — build-focused (Claude edits code)

**When**: you want Claude to build L3, fix bugs, add features.

Use bootstrap prompt in `UPDATE MINDMAP.md` Scenario 3. That doc covers code sync.

**Claude's mandatory reminder** (must appear after every build/edit):

> ✅ Done. Before closing chat, remember:
> 1. **Commit + Push** in GitHub Desktop → sync code to tablet
> 2. **Backup JSON** (📊 Progress) → save latest progress to `backup/`
> 3. If workflow/architecture changed, **update UPDATE MINDMAP.md or UPDATE PROGRESS.md**

If Claude forgets this reminder, prompt: "Nhắc lại 3 việc sync đi."

---

## Progress data schema (for reference)

`quant-progress-YYYY-MM-DD.json` structure:

```json
{
  "version": "1.0",
  "exported_at": "2026-08-15T14:30:00.000Z",
  "mastery": {
    "l1-functions": "mastered",
    "l2-limits": "learning",
    "prob-bayes": "mastered"
  },
  "history": [
    {"ts": 1723728000000, "id": "l1-functions", "state": "learning", "prev": "new"},
    {"ts": 1723814400000, "id": "l1-functions", "state": "mastered", "prev": "learning"}
  ]
}
```

**On restore**, `mastery` object replaces current localStorage. `history` is appended (deduplicated by timestamp).

---

## Common issues

**"Restore didn't work"**
- Check: file is valid JSON (not corrupted during transfer)
- Check: `mastery` keys match current concept IDs in atlas (if IDs were renamed by mistake, restore silently ignores unknowns)

**"Progress bar shows wrong percentage"**
- Total concept count changed (atlas added/removed concepts) → percentage recalculates. Denominator changed, not your marks.

**"Marked Mastered but node doesn't glow"**
- Zoom out to see the effect (glow is subtle)
- Refresh page (Ctrl+F5) to reload styles

**"Progress disappeared after clearing browser data"**
- localStorage is cleared with cache. Recover from last backup JSON.

**"Same concept shows different state on desktop vs tablet"**
- Expected. Different localStorage buckets. Pick source of truth (usually desktop) and restore on the other.

---

## Standing rules for Claude (both docs)

These rules apply in ANY chat working on this project. Both `UPDATE MINDMAP.md` and `UPDATE PROGRESS.md` include them so any bootstrap prompt propagates them.

1. **Language**: content in English, chat in Vietnamese
2. **Rigor level**: MFE-textbook (proofs + intuition + worked examples), not high-school Vietnamese style
3. **Concept IDs**: NEVER rename existing IDs. Adding new is fine.
4. **Personal files**: NEVER touch `*.notes.md`, `backup/`, `Notebooks/`, `PDF/`, `Data/`, `References/`
5. **Other folders**: NEVER modify `D:\OneDrive\1. Quant\World Quant - Master of Financial Engineering`
6. **Post-build reminder**: after ANY file edit/creation, remind user to:
   - Commit + Push via GitHub Desktop (code sync)
   - Export progress JSON if session was long (progress sync)
   - Update `UPDATE MINDMAP.md` or `UPDATE PROGRESS.md` if workflow changed
7. **Token discipline**: batch related changes into single messages, avoid ping-pong for small fixes
8. **Verify before claim**: don't say "done" without checking the file actually saved

---

## Quick reference

| Task | Where | How |
|---|---|---|
| Mark concept | Atlas sidebar | Tap Learning or Mastered button |
| See all progress | Atlas top bar | Tap 📊 Progress (or Ctrl+P desktop) |
| Backup weekly | 📊 Progress → Backup JSON | Save to `backup/` folder |
| Restore | 📊 Progress → Restore JSON | Pick file, merges into current |
| Cross-device sync | Export → transfer file → Import | Manual, weekly recommended |
| Reset all progress | 📊 Progress → Reset | ⚠️ irreversible, backup first |

---

## Backup redundancy layers

| Layer | What's backed up | How often |
|---|---|---|
| Browser localStorage | Live progress | Every click (automatic) |
| `backup/*.json` in OneDrive folder | Snapshots | Weekly (you) |
| OneDrive cloud | Full `backup/` folder | Continuous (OneDrive app) |
| Manual archive | Any critical milestones | Ad-hoc (rename JSON, keep forever) |

Note: **NOT on GitHub** (backup/ is gitignored). Progress data stays private.

---

*Last updated: 2026-08-01 — initial version*
