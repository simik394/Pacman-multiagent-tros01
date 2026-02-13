# Lessons Learned - Rendering Pipeline Fix (2026-02-13)

## 1. `code-overflow: wrap` is HTML-only in Quarto
- The Quarto setting `code-overflow: wrap` only affects HTML output
- For **PDF** output, you need the `fvextra` LaTeX package
- Required config: `\usepackage{fvextra}` + `\DefineVerbatimEnvironment{Highlighting}{Verbatim}{breaklines,commandchars=\\\{\}}`
- This produces wrapped lines with a `↪` continuation indicator

## 2. Quarto code annotations require ordered lists
- Having `# <1>`, `# <2>` markers in source code is necessary but not sufficient
- You MUST add a numbered ordered list directly after the code fence block
- You also need `code-annotations: below` (or `hover`/`select`) in `_quarto.yml`

## 3. Relative include paths are fragile with staging
- When using `include-code-files` Lua filter with Quarto, relative paths like `include="heuristics.jl"` fail if Quarto's CWD is different from the source file's directory
- The Lua filter has a fallback prefix mechanism, but it's unreliable across staging/project-root setups
- **Best practice:** Use absolute paths for code includes, especially when a staging/copying pipeline is involved

## 4. Quarto freeze cache management
- Empty `_freeze` directory means no cached execution results
- `freeze: auto` only caches when cells are first executed; clearing the cache forces re-execution
- When updating heuristic constants, remember to clear freeze to regenerate dependent tables
