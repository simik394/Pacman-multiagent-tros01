# Lesson Learned: Minimax Alpha-Beta Analysis

## Analýza logů (Strom prohledávání)
1.  **Navigace v logu**: Soubory `strom_kompletni.txt` mohou být extrémně dlouhé (tisíce řádků).
    -   Pro nalezení konkrétní větvě (např. tah `14-9`) je efektivní použít `grep -n` pro získání čísla řádku a následně číst relevantní blok.
    -   Příklad: `grep -n "^  ├─ 14-9 (MIN)" strom_kompletni.txt`

2.  **Interpretace [α cut-off] a [β cut-off]**:
    -   V `testvaluefunc.jl` je logika ořezávání implementována takto:
        -   **[α cut-off]**: Nastává v uzlu hráče MIN, když hodnota podstromu je menší nebo rovna Alpha (kterou drží MAX předek). Znamená to, že MAX by tuto větev nikdy nevybral, protože má lepší alternativu.
        -   **[β cut-off]**: Nastává v uzlu hráče MAX, když hodnota podstromu je větší nebo rovna Beta (kterou drží MIN předek). Znamená to, že MIN by tuto větev nikdy "nepustil" k realizaci.

3.  **Heuristika (Skóre)**:
    -   Hodnoty skóre kolem 1700 v této implementaci reflektují kombinaci materiálu (král = 300) a velkých pozičních bonusů (vzdálenost králů, sevření = až 1000 bodů).
    -   Skóre 99999 / -99999 indikuje terminální stav (výhra/prohra).

## Spouštění simulace
-   Skript `testvaluefunc.jl` lze spustit s parametrem `save_trees=true` pro generování podrobných logů.
-   Výstupy se ukládají do adresáře `simulation_outputs/run_<timestamp>`.

## Quarto Code Embedding
- **Issue:** The `quarto-ext/include-code-files` extension (v1.0.0 via `quarto add`) expects `# start snippet name` markers and `snippet="name"` attribute, which conflicts with the standard `#| region: name` syntax used in Quarto cells.
- **Solution:** Patched `_extensions/quarto-ext/include-code-files/include-code-files.lua` to support both `snippet` and `region` attributes, and added regex support for `#| region: name` / `#| endregion: name` markers.
- **Key Takeaway:** Always check the specific syntax requirements of Quarto extensions as they may differ from core Quarto features. When in doubt, checking the `.lua` filter source code is the most reliable way to debug.

## Quarto Project Structure
- **Output Directory Preference:** All PDF outputs should target the `out/pdfs/` directory (e.g., `project.output-dir: out/pdfs` in `_quarto.yml`) for consistency and to keep the root directory clean.
- **Path Resolution in Staging:** When using wrapper scripts to render from a staging location (to handle Obsidian syntax), care must be taken with relative paths (e.g., `include()`). Rendering from a temporary file within the project root (`.__temp_filename.qmd`) is safer than moving files to a subdirectory, as it preserves relative path resolution for included code files.
