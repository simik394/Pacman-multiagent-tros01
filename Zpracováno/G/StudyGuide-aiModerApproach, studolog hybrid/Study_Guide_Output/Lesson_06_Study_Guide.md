# Lekce 6: Plánování a Rozvrhování

Tento studijní průvodce se zaměřuje na rozdíly a spojitosti mezi plánováním a rozvrhováním a představuje klíčové přístupy k řešení plánovacích problémů v umělé inteligenci.

## 1. Plánování vs. Rozvrhování

Ačkoliv jsou tyto dva pojmy úzce propojené, je důležité chápat jejich odlišné role v rozhodovacím procesu.

### 1.1 Úloha Plánování (Planning)

*   **Co řeší?** **Jaké akce** jsou potřeba pro dosažení cílů.
*   **Vstup:** Počáteční stav světa, popis dostupných akcí a jejich efektů, a požadovaný cílový stav.
*   **Výstup:** Sekvence (nebo částečně uspořádaná množina) akcí – **plán**.
*   **Zaměření:** Plánování se primárně soustředí na **kauzální vztahy** mezi akcemi. Řeší, které akce vybrat a v jakém logickém pořadí je provést, aby byly splněny předpoklady dalších akcí a nakonec i samotný cíl. **Nezabývá se konkrétním časem a zdroji.**

### 1.2 Úloha Rozvrhování (Scheduling)

*   **Co řeší?** Jak naplánované aktivity **alokovat na zdroje v čase**.
*   **Vstup:** Skupina aktivit (často výstup z plánovače) a dostupné zdroje s jejich omezeními (kapacita, časová dostupnost).
*   **Výstup:** **Rozvrh**, který specifikuje, kdy a kde se každá aktivita provede.
*   **Zaměření:** Cílem je optimalizovat využití zdrojů, minimalizovat celkový čas, vyhnout se konfliktům a dodržet časové termíny.

**Vztah:** Typicky **plánování předchází rozvrhování**. Někdy je však výhodné řešit obě úlohy současně, například když existuje mnoho možných plánů, ale jen málo z nich má přípustný rozvrh.

## 2. Jazyk pro Definici Plánování (PDDL)

Pro formalizaci plánovacích problémů se používá **Planning Domain Definition Language (PDDL)**. Umožňuje definovat:
*   **Počáteční stav:** Konjunkce základních, bezfunkčních a pozitivních atomů (fluentů), např. `At(C1, SFO) ∧ At(P1, SFO)`. Platí zde předpoklad uzavřeného světa (co není uvedeno, je nepravdivé).
*   **Cíl:** Konjunkce literálů (mohou být i negativní), které popisují požadovaný stav.
*   **Akce (Action Schemas):** Šablony pro akce, které obsahují:
    *   **Název a parametry:** Např. `Fly(p, from, to)`.
    *   **Předpoklady (PRECOND):** Konjunkce literálů, které musí platit, aby akce mohla být provedena.
    *   **Efekty (EFFECT):** Konjunkce literálů, které popisují, jak se stav světa po provedení akce změní. Literály, které se mají stát pravdivými, jsou v **add listu**, a ty, které se mají stát nepravdivými, v **delete listu**.

## 3. Přístupy k Plánování

### 3.1 Plánování jako Prohledávání Stavového Prostoru

Toto je nejběžnější přístup, kde:
*   **Uzly** odpovídají stavům světa.
*   **Hrany** odpovídají akcím.
*   **Cílem** je nalézt cestu z počátečního stavu do cílového.

#### a) Dopředné prohledávání (Progression Planning)

*   **Princip:** Začíná se v počátečním stavu a aplikují se akce, dokud se nedosáhne cílového stavu.
*   **Výhody:** Intuitivní, umožňuje použití velmi silných, doménově nezávislých heuristik.
*   **Nevýhody:** Může prohledávat velké množství nerelevantních akcí (např. v problému nákupu knihy existují miliony akcí `Buy(isbn)`).
*   **Heuristiky:** Úspěch této metody závisí na kvalitních heuristikách, které odhadují vzdálenost do cíle. Tyto heuristiky se často získávají z **relaxovaných problémů** (např. ignorováním negativních efektů akcí).

#### b) Zpětné prohledávání (Regression Planning)

*   **Princip:** Začíná se u cíle a postupuje se "dozadu" aplikací inverzních akcí. Stav zde není jeden konkrétní stav, ale **množina stavů** popsaná konjunkcí literálů.
*   **Výhody:** Prohledává pouze **relevantní akce**, tedy takové, které přispívají k dosažení cíle. To výrazně snižuje faktor větvení.
*   **Nevýhody:** Je složitější a obtížněji se pro něj definují dobré heuristiky.

### 3.2 Plánování jako Splňování Podmínek (CSP) nebo Booleovská Splnitelnost (SAT)

Plánovací problém pro pevně danou délku plánu `k` lze převést na:
*   **CSP:** Proměnné mohou reprezentovat akce v každém časovém kroku nebo fluenty v každém stavu. Podmínky zajišťují logickou konzistenci (efekty akcí, splnění předpokladů).
*   **SAT (SATPLAN):** Problém se převede na velkou booleovskou formuli. Pokud je formule splnitelná, model (přiřazení pravdivostních hodnot) kóduje platný plán.
    *   **Postup:**
        1.  Vytvoří se propozice pro každý fluent a každou akci v každém časovém kroku až do `k`.
        2.  Přidají se axiomy: počáteční stav, cíl v čase `k`, a tzv. **successor-state axioms**, které definují, jak se stav mění mezi kroky.
        3.  Výsledná formule se předá SAT-solveru.
    *   Tento přístup je překvapivě efektivní díky moderním a vysoce optimalizovaným SAT-solverům.

### 3.3 Plánování v Prostoru Plánů (Partial-Order Planning)

*   **Princip:** Místo prohledávání stavů se prohledává prostor **částečně uspořádaných plánů**.
*   **Začátek:** Prázdný plán, který obsahuje jen počáteční stav a cíl.
*   **Kroky:** Algoritmus iterativně identifikuje **nedostatky (flaws)** v plánu (např. nesplněný předpoklad) a opravuje je přidáním nové akce nebo uspořádávacího omezení (`A musí být před B`).
*   **Výhody:** Flexibilní, řídí se principem **nejmenšího závazku (least commitment)** – odkládá rozhodnutí o přesném pořadí akcí, dokud to není nutné. Dobře řeší problémy s nezávislými podproblémy.
*   **Nevýhody:** Složitější na implementaci a v současnosti méně výkonný než nejlepší dopředné plánovače.

### 3.4 Plánovací Graf (Planning Graph)

Plánovací graf je datová struktura používaná pro extrakci plánu nebo pro odhad heuristik.
*   **Struktura:** Orientovaný graf organizovaný do střídajících se vrstev **stavů (literálů) `Sᵢ`** a **akcí `Aᵢ`**.
*   **Expanze grafu:** Graf se postupně staví od `S₀` (počáteční stav). `Aᵢ` obsahuje všechny akce, jejichž předpoklady jsou v `Sᵢ`. `Sᵢ₊₁` obsahuje všechny efekty akcí z `Aᵢ`.
*   **Mutexy:** Graf zaznamenává páry akcí nebo literálů, které se vzájemně vylučují (nemohou nastat současně).
*   **Využití:**
    1.  **Heuristika:** Počet vrstev potřebných k dosažení cílových literálů (bez mutexů) je velmi dobrou (a přípustnou) heuristikou pro dopředné prohledávání. Toto je základ úspěchu plánovače **FF (Fast Forward)**.
    2.  **Algoritmus GRAPHPLAN:** Přímo hledá řešení v plánovacím grafu pomocí zpětného prohledávání. Pokud řešení nenajde, rozšíří graf o další vrstvu a zkusí to znovu.
