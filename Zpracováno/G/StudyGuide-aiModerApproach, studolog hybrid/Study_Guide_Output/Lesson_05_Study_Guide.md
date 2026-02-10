# Lekce 5: Teorie Her a Prohledávání v Konfliktních Situacích

Tento studijní průvodce se věnuje matematické teorii her, která analyzuje konfliktní rozhodovací situace, a algoritmům, které umožňují umělé inteligenci hrát hry proti protivníkovi.

## 1. Matematická Teorie Her

**Teorie her** je disciplína aplikované matematiky, která analyzuje situace, kde dochází ke střetu zájmů. Jejím cílem je odpovědět na dvě základní otázky:
1.  Která strategie (rozhodnutí) je optimální?
2.  Jak tuto optimální strategii nalézt?

Základním předpokladem je **racionalita hráčů** – každý hráč se snaží maximalizovat svůj vlastní zisk (nebo minimalizovat ztrátu).

### 1.1 Formální Popis Hry

Hra je formálně popsána pomocí:
*   **Množiny hráčů**.
*   **Množin strategií** pro každého hráče (jaké akce může provést).
*   **Výher (užitku)** pro každého hráče při dané kombinaci strategií.

### 1.2 Typy Her

Hry lze klasifikovat podle několika kritérií:
*   **Podle počtu hráčů:** Dvouhráčové, vícehráčové.
*   **Podle typu výhry:**
    *   **Hry s konstantním součtem (Constant-Sum):** Součet výher všech hráčů je vždy stejný. Speciálním případem jsou **hry s nulovým součtem (Zero-Sum)**, kde co jeden hráč získá, druhý ztratí (např. šachy, go).
    *   **Hry s nekonstantním součtem:** Hráči mohou spolupracovat, aby dosáhli oboustranně výhodného výsledku.
*   **Podle míry informace:**
    *   **S úplnou informací (Perfect Information):** Všichni hráči znají kompletní stav hry (např. šachy).
    *   **S neúplnou informací (Imperfect Information):** Hráči neznají všechny informace (např. karetní hry jako poker, kde neznáte karty protihráče).
*   **Podle prvku náhody:**
    *   **Deterministické:** Výsledek tahu je plně určen rozhodnutím hráče (šachy).
    *   **Stochastické (s prvkem náhody):** Výsledek závisí i na náhodě (např. hod kostkou v backgammonu).

V kontextu AI se nejčastěji zabýváme **deterministickými, dvouhráčovými hrami s úplnou informací a nulovým součtem**.

## 2. Hra jako Úloha Prohledávání

Hru můžeme formalizovat jako problém prohledávání, který je definován:
1.  **Počátečním stavem (S₀):** Jak je hra na začátku postavena.
2.  **Funkcí následníků (ACTIONS):** Vrací množinu legálních tahů v daném stavu.
3.  **Přechodovým modelem (RESULT):** Definuje výsledek tahu.
4.  **Testem konce (TERMINAL-TEST):** Zjišťuje, zda hra skončila.
5.  **Užitkovou funkcí (UTILITY):** Přiřazuje konečnému stavu číselnou hodnotu z pohledu jednoho hráče (výhra, prohra, remíza).

Cílem agenta (hráče) je najít **optimální strategii** – takovou, která vede k výsledkům, jež jsou nejlepší možné proti bezchybnému protivníkovi.

## 3. Algoritmus Minimax

**Minimax** je základní algoritmus pro nalezení optimálního tahu. Vychází z předpokladu, že oba hráči hrají optimálně. Hráče označujeme jako **MAX** (snaží se maximalizovat užitek) a **MIN** (snaží se minimalizovat užitek z pohledu MAXe).

Princip:
*   Pro každý uzel v herním stromu se vypočítá **minimaxová hodnota**.
*   **Pro MAXe** je hodnota uzlu maximem hodnot jeho následníků.
*   **Pro MINa** je hodnota uzlu minimem hodnot jeho následníků.
*   **Pro koncové uzly** je hodnota dána užitkovou funkcí.

Algoritmus rekurzivně prohledává herní strom do hloubky, spočítá hodnoty koncových stavů a poté tyto hodnoty "propaguje" nahoru stromem (tzv. "backing up"). Kořenový uzel (aktuální stav) pak získá hodnotu, která představuje nejlepší dosažitelný výsledek pro MAXe, a tah, který k němu vede, je optimální.

**Složitost:** Minimax prohledává celý strom do hloubky `m` s faktorem větvení `b`, takže časová složitost je **O(b^m)**, což je pro většinu reálných her (jako šachy) nepraktické.

## 4. Alfa-Beta Prořezávání (Alpha-Beta Pruning)

**Alfa-beta prořezávání** je optimalizace algoritmu Minimax, která dosahuje stejného výsledku, ale prohledává výrazně menší část herního stromu.

Princip:
Algoritmus si během prohledávání udržuje dvě hodnoty:
*   **α (alfa):** Nejlepší (nejvyšší) hodnota, kterou může **MAX** zaručeně dosáhnout na cestě od kořene k aktuálnímu uzlu.
*   **β (beta):** Nejlepší (nejnižší) hodnota, kterou může **MIN** zaručeně dosáhnout na cestě od kořene k aktuálnímu uzlu.

Prořezávání nastane, když algoritmus zjistí, že daná větev nemůže ovlivnit konečné rozhodnutí:
1.  **U MIN uzlu:** Pokud hodnota některého z jeho následníků je **menší nebo rovna α**, můžeme tuto větev proříznout. Důvod: MAX by nikdy nedovolil, aby se hra do této větve dostala, protože už má k dispozici jinou cestu s garantovanou hodnotou α.
2.  **U MAX uzlu:** Pokud hodnota některého z jeho následníků je **větší nebo rovna β**, můžeme tuto větev proříznout. Důvod: MIN by nikdy nedovolil, aby se hra do této větve dostala, protože už má k dispozici jinou cestu s garantovanou hodnotou β.

**Efektivita:**
*   Při **optimálním seřazení tahů** (kdy jsou nejdříve zkoumány nejlepší tahy) se časová složitost snižuje na **O(b^(m/2))**. To v praxi znamená, že alfa-beta dokáže prohledat zhruba dvakrát hlubší strom než Minimax ve stejném čase.
*   Při náhodném pořadí je složitost zhruba O(b^(3m/4)).

Alfa-beta prořezávání neovlivňuje výsledek – vždy najde stejný optimální tah jako Minimax.
