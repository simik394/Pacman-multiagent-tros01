# Lekce 4: Splňování Podmínek (Constraint Satisfaction Problems - CSP)

Tento studijní průvodce se zabývá speciální třídou problémů, které lze efektivněji řešit využitím jejich vnitřní struktury – proměnných a omezujících podmínek.

## 1. Co je Úloha na Splňování Podmínek?

Na rozdíl od předchozích metod, které považovaly stavy za nedělitelné "černé skříňky", CSP přistupuje ke stavům strukturovaně. **Úloha na splňování podmínek (Constraint Satisfaction Problem - CSP)** je tvořena třemi hlavními komponentami:

1.  **X: Množina proměnných (Variables)**
    *   Konečná množina proměnných `{X₁, ..., Xₙ}`, které popisují stav světa. V problému barvení mapy jsou proměnnými jednotlivé regiony (státy).

2.  **D: Množina domén (Domains)**
    *   Pro každou proměnnou `Xᵢ` je definován její **definiční obor `Dᵢ`**, což je množina povolených hodnot `{v₁, ..., vₖ}`. V problému barvení mapy je doménou pro každý region množina `{červená, zelená, modrá}`.

3.  **C: Množina podmínek (Constraints)**
    *   Podmínky (omezení), které specifikují povolené kombinace hodnot pro proměnné. Podmínka je tvořena párem `⟨scope, rel⟩`, kde `scope` je n-tice proměnných, kterých se podmínka týká, a `rel` je relace definující přípustné hodnoty. Například podmínka, že dva sousední regiony nesmí mít stejnou barvu, je `SA ≠ WA`.

**Řešením CSP** je takové přiřazení hodnot všem proměnným, aby byly splněny všechny podmínky. Formálněji řečeno:

*   **Přiřazení (Assignment):** Přiřazení hodnot některým nebo všem proměnným.
*   **Konzistentní (nebo legální) přiřazení:** Přiřazení, které neporušuje žádnou podmínku.
*   **Úplné přiřazení:** Přiřazení, ve kterém mají hodnotu všechny proměnné.
*   **Řešení (Solution):** Konzistentní a zároveň úplné přiřazení.

### 1.1 Příklady CSP

*   **Barvení mapy:** Proměnné jsou regiony, domény jsou barvy, podmínky zakazují stejnou barvu pro sousední regiony.
*   **8 královen (8 Queens):** Proměnné jsou sloupce, domény jsou řádky (1-8), podmínky zakazují, aby se dvě královny ohrožovaly.
*   **Sudoku:** Proměnné jsou políčka (81), domény jsou číslice (1-9), podmínky vyžadují unikátnost číslic v každém řádku, sloupci a 3x3 boxu.
*   **Kryptoaritemetické hádanky (např. SEND + MORE = MONEY):** Proměnné jsou písmena, domény číslice (0-9), podmínky jsou algebraické rovnice a unikátnost přiřazení.
*   **Reálné úlohy:** Tvorba univerzitních rozvrhů, plánování výroby, alokace zdrojů.

## 2. Způsoby Řešení CSP

### 2.1 Matematické Metody (Operační výzkum)

Operační výzkum se snaží najít optimální řešení problému při daných omezeních. Problém je často modelován pomocí matematických rovnic a nerovnic. Příkladem je **lineární programování**, kde jsou podmínky i cílová funkce lineární.

### 2.2 Booleovská Splnitelnost (SAT)

Problém CSP lze převést na problém **Booleovské splnitelnosti (SAT)**.
1.  Podmínky se převedou na logické formule v konjunktivní normální formě (CNF).
2.  Hledá se takové ohodnocení (přiřazení `true`/`false`) proměnných, aby byla výsledná formule pravdivá.
Tento problém je NP-úplný, ale existují pro něj vysoce optimalizované řešiče (např. založené na **DPLL algoritmu**).

### 2.3 Využití Stavového Prostoru

Nejpřirozenějším přístupem v rámci UI je formulovat CSP jako problém prohledávání stavového prostoru.

*   **Stav:** Částečné přiřazení hodnot proměnným.
*   **Počáteční stav:** Prázdné přiřazení (žádná proměnná nemá hodnotu).
*   **Akce:** Přiřazení hodnoty jedné z dosud nepřiřazených proměnných.
*   **Cílový test:** Zjišťuje, zda je přiřazení úplné a konzistentní.

Standardní prohledávací algoritmy (jako DFS) by byly neefektivní kvůli obrovskému faktoru větvení. Proto se pro CSP používá specializovaný algoritmus **zpětného prohledávání (Backtracking Search)**.

#### Algoritmus Backtrackingu

Backtracking je forma prohledávání do hloubky, která postupně přiřazuje hodnoty jednotlivým proměnným.

1.  Vybere se dosud nepřiřazená proměnná.
2.  Postupně se zkouší přiřadit jí hodnoty z její domény.
3.  Pro každou hodnotu se zkontroluje, zda je **konzistentní** s dosud přiřazenými hodnotami.
    *   Pokud **ano**, pokračuje se rekurzivně s další proměnnou.
    *   Pokud **ne**, zkusí se další hodnota.
4.  Pokud pro danou proměnnou dojdou hodnoty, algoritmus se **vrátí zpět (backtrack)** k předchozí proměnné a zkusí pro ni jinou hodnotu.

Tento základní algoritmus lze výrazně zefektivnit pomocí **šíření podmínek (constraint propagation)**, což je forma inference, a heuristik pro výběr proměnných a hodnot.
