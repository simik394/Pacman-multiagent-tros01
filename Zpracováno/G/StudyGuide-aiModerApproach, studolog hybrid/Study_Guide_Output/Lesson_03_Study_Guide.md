# Lekce 3: Řešení Úloh ve Stavovém Prostoru

Tento studijní průvodce se zaměřuje na formalizaci problémů a algoritmy prohledávání stavového prostoru, které tvoří základ mnoha systémů umělé inteligence.

## 1. Úvod do Řešení Úloh

Mnoho problémů v UI lze formalizovat jako hledání cesty od počátečního stavu k cílovému stavu. K tomu potřebujeme tři hlavní komponenty:
1.  **Definice problému:** Co je počáteční situace.
2.  **Definice cíle:** Jak vypadá požadovaný koncový stav.
3.  **Akce:** Jaké operace můžeme provádět, abychom se přesouvali mezi stavy.

Příkladem mohou být Hanojské věže, kde cílem je přesunout disky z jedné tyčky na druhou za dodržení určitých pravidel (přesun jen jednoho disku, větší nelze na menší).

### 1.1 Abstraktní Reprezentace

Pro řešení problémů používáme dva klíčové principy:
*   **Generalizace:** Zobecnění skupiny podobných problémů nalezením jejich společných rysů. Místo řešení "cesty z Aradu do Bukurešti" řešíme obecný problém "nalezení cesty mezi dvěma městy".
*   **Abstrakce:** Zjednodušení problému zanedbáním nedůležitých detailů. Například při plánování trasy autem zanedbáváme detaily jako rádio, počasí nebo přesné pohyby volantem.

### 1.2 Stavový Prostor

**Stavový prostor** je abstraktní model úlohy, který se skládá z:
*   **Stavů:** Situace, které mohou v problému nastat.
*   **Akcí (přechodů):** Operace, které nás přesouvají z jednoho stavu do druhého.

Stavový prostor může být definován:
*   **Explicitně:** Všechny stavy a přechody jsou přímo dány (např. mapa pro navigaci).
*   **Implicitně:** Stavy a přechody jsou generovány podle pravidel (např. šachy, kde stavy vznikají platnými tahy).

## 2. Formální Definice Problému

Problém můžeme formálně definovat pomocí pěti komponent:
1.  **Počáteční stav (Initial State):** Stav, ve kterém se agent na začátku nachází (např. `In(Arad)`).
2.  **Akce (Actions):** Popis možných akcí, které jsou agentovi k dispozici. Funkce `ACTIONS(s)` vrací množinu akcí proveditelných ve stavu `s`.
3.  **Přechodový model (Transition Model):** Popis toho, co jednotlivé akce dělají. Funkce `RESULT(s, a)` vrací stav, který je výsledkem provedení akce `a` ve stavu `s`. Společně s počátečním stavem a akcemi definuje **stavový prostor**.
4.  **Cílový test (Goal Test):** Určuje, zda daný stav je cílovým stavem.
5.  **Cena cesty (Path Cost):** Funkce, která přiřazuje číselnou cenu každé cestě. Obvykle je to součet cen jednotlivých kroků.

**Řešením** problému je sekvence akcí, která vede z počátečního stavu do cílového stavu. **Optimální řešení** je řešení s nejnižší cenou cesty.

## 3. Algoritmy Prohledávání

Algoritmy prohledávání systematicky zkoumají stavový prostor, aby nalezly řešení. Pracují s **prohledávacím stromem**, kde:
*   **Kořen** je počáteční stav.
*   **Větve** jsou akce.
*   **Uzly** odpovídají stavům.

Algoritmy udržují:
*   **Frontu (Fringe / Open List):** Seznam dosud nenavštívených (nerozvinutých) uzlů.
*   **Prozkoumanou množinu (Explored Set / Closed List):** Seznam již navštívených (rozvinutých) uzlů, aby se předešlo cyklům a redundantním cestám.

Základní operací je **rozvinutí (expanze)** uzlu, což znamená aplikaci všech možných akcí na daný stav a přidání výsledných uzlů (následníků) do fronty.

### 3.1 Slepé (Neinformované) Algoritmy

Tyto algoritmy nemají žádné další informace o problému kromě jeho definice. Všechny následníky považují za rovnocenné.

*   **Prohledávání do šířky (Breadth-First Search - BFS):**
    *   Používá frontu typu **FIFO (First-In, First-Out)**.
    *   Vždy rozvíjí nejméně hluboký uzel.
    *   **Vlastnosti:**
        *   **Úplnost:** Ano, vždy najde řešení, pokud existuje.
        *   **Optimalita:** Ano, pokud mají všechny kroky stejnou cenu.
        *   **Složitost (časová i paměťová):** O(b^d), kde `b` je faktor větvení a `d` je hloubka řešení. Je velmi náročný na paměť.

*   **Prohledávání s uniformní cenou (Uniform-Cost Search - UCS):**
    *   Rozšíření BFS, které řeší ohodnocené přechody.
    *   Fronta je **prioritní fronta** uspořádaná podle ceny cesty `g(n)`.
    *   Vždy rozvíjí uzel s nejnižší cenou cesty.
    *   **Vlastnosti:**
        *   **Úplnost a Optimalita:** Ano, pokud jsou ceny kroků nezáporné.
        *   Složitost závisí na ceně optimálního řešení C*.

*   **Prohledávání do hloubky (Depth-First Search - DFS):**
    *   Používá frontu typu **LIFO (Last-In, First-Out)**, často implementováno rekurzivně.
    *   Vždy rozvíjí nejhlubší uzel.
    *   **Vlastnosti:**
        *   **Úplnost:** Ne, může uvíznout v nekonečné větvi.
        *   **Optimalita:** Ne.
        *   **Paměťová složitost:** O(bm), kde `m` je maximální hloubka. Je velmi úsporný na paměť.

*   **Prohledávání s omezenou hloubkou (Depth-Limited Search - DLS):**
    *   Varianta DFS, která prohledává jen do předem dané hloubky `l`. Řeší problém nekonečných větví, ale je neúplný, pokud `l < d`.

*   **Iterativní prohlubování (Iterative Deepening Search - IDS):**
    *   Kombinuje výhody BFS a DFS.
    *   Opakovaně spouští DLS s postupně se zvyšující hloubkou (0, 1, 2, ...).
    *   **Vlastnosti:** Stejné jako BFS (úplný, optimální), ale s paměťovou náročností DFS.

*   **Obousměrné prohledávání (Bidirectional Search):**
    *   Prohledává současně od počátečního stavu dopředu a od cílového stavu dozadu.
    *   Řešení je nalezeno, když se obě fronty protnou.
    *   Výrazně snižuje složitost na O(b^(d/2)), ale je náročné na implementaci (vyžaduje schopnost prohledávat "pozpátku") a paměť.

### 3.2 Informované (Heuristické) Algoritmy

Tyto algoritmy používají **heuristickou funkci `h(n)`**, která odhaduje cenu cesty z uzlu `n` do nejbližšího cíle. Heuristika je klíčová pro efektivní řešení složitých problémů.

*   **Uspořádané prohledávání (Greedy Best-First Search):**
    *   Rozvíjí uzel, který se zdá být nejblíže k cíli. Používá `f(n) = h(n)`.
    *   Je "chamtivý", protože se snaží co nejrychleji přiblížit k cíli, i když to může vést do slepé uličky.
    *   Není úplný ani optimální.

*   **Algoritmus A***:
    *   Nejznámější a nejrozšířenější informovaný algoritmus.
    *   Hodnotí uzly kombinací ceny cesty od počátku `g(n)` a heuristického odhadu do cíle `h(n)`.
    *   **Vyhodnocovací funkce: `f(n) = g(n) + h(n)`**
    *   Používá prioritní frontu seřazenou podle `f(n)`.
    *   **Vlastnosti:**
        *   **Úplnost a Optimalita:** Ano, pokud je heuristika **přípustná (admissible)**, tzn. nikdy nepřecení skutečnou cenu do cíle (`h(n) <= h*(n)`).

*   **Gradientní prohledávání (Hill-Climbing):**
    *   Lokální prohledávací metoda, která neudržuje celý prohledávací strom.
    *   Začíná v nějakém stavu a iterativně se posouvá do nejlepšího sousedního stavu, dokud nedosáhne vrcholu ("peak"), ze kterého již nevede cesta vzhůru.
    *   Může uvíznout v **lokálním maximu**.

### 3.3 Náhodné Algoritmy

Tyto algoritmy zavádějí do prohledávání prvek náhody, často proto, aby se vymanily z lokálních extrémů.

*   **Simulované žíhání (Simulated Annealing):**
    *   Inspirováno procesem žíhání kovů.
    *   Podobné gradientnímu prohledávání, ale s určitou pravděpodobností přijímá i horší řešení.
    *   Tato pravděpodobnost závisí na "teplotě" `T`, která se v čase postupně snižuje. Na začátku (vysoká teplota) je pravděpodobnost přijetí horšího řešení vyšší, což umožňuje "přeskočit" lokální minima. Ke konci (nízká teplota) se algoritmus chová spíše jako gradientní prohledávání.

*   **Genetické algoritmy (Genetic Algorithms - GA):**
    *   Inspirováno biologickou evolucí.
    *   Pracuje s **populací** stavů (jedinců).
    *   V každém kroku vybírá jedince na základě jejich "zdatnosti" (fitness) a vytváří novou generaci pomocí operací **křížení (crossover)** a **mutace (mutation)**.

## 4. General Problem Solver (GPS)

Historicky významný algoritmus (Newell & Simon, 1961), který řešil úlohy metodou postupného rozkladu na podúlohy. Pracoval na základě výpočtu **diferencí** mezi aktuálním a cílovým stavem a snažil se tuto diferenci zmenšit aplikací vhodných operátorů.
