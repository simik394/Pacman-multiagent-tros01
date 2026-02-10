# Lessons Learned — Verification 2026-02-10

## 1. English draughts vs International draughts
- **Backward pawn capture**: In English draughts, pawns can ONLY jump forward. Backward jumps are a rule of International draughts (10×10 board). The code had a comment incorrectly claiming backward jumps are allowed in English draughts.
- **Promotion during jump**: In English draughts, when a pawn reaches the crown row during a multi-jump, it is promoted AND the turn ends immediately. No further jumps are allowed in that turn. This differs from some other variants.

## 2. Code-report synchronization
- Heuristic code had 5 components (~3000 points of scoring impact) that were completely undocumented in the formal equations. This created a false impression that only 7 components existed.
- Safety zone defined differently in code (rectangular area) vs equations (exact fields). Always define game constants as exact field sets, not geometric approximations.

## 3. Context-dependent bug impact
- Both engine bugs are irrelevant for king-only endgames (the specific test scenario), but would produce illegal moves in midgame positions with pawns. Always verify the scope of bugs before panicking.

## 4. Julia syntax
- `const` cannot be used inside functions in Julia. Use regular variables or define constants at module scope.
