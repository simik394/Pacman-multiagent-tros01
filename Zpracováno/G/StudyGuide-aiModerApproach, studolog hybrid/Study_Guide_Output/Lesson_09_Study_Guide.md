# Lekce 9: Zpětnovazební Učení (Reinforcement Learning)

Zpětnovazební učení (Reinforcement Learning - RL) je oblast strojového učení, kde se agent učí optimálnímu chování na základě interakce s prostředím. Místo toho, aby dostával explicitní instrukce, co má dělat, učí se z následků svých akcí prostřednictvím odměn a trestů.

## 1. Charakteristiky Zpětnovazebního Učení

RL se liší od ostatních paradigmat učení (např. učení s učitelem) v několika klíčových aspektech:
*   **Aktivní učení:** Agent není pasivním příjemcem dat, ale aktivně prozkoumává prostředí a svými akcemi ovlivňuje, jaká data získá.
*   **Sekvenční povaha:** Interakce s prostředím probíhá v sekvenci kroků. Současná akce může ovlivnit nejen okamžitou odměnu, ale i budoucí stavy a odměny.
*   **Orientace na cíl:** Cílem agenta je maximalizovat kumulativní (celkovou) odměnu v dlouhodobém horizontu, nikoliv jen okamžitý zisk.
*   **Učení bez optimálních příkladů:** Agent se učí metodou pokus-omyl. Nemá k dispozici "správné odpovědi" (optimální akce) pro dané stavy, ale pouze signál odměny, který mu říká, jak dobře si vede.

Každý stav `s` v prostředí může být spojen s určitou **odměnou (reward) R(s)**. Agent se snaží naučit takovou strategii (politiku), která ho povede skrze stavy tak, aby součet (diskontovaných) odměn byl co nejvyšší.

Tento přístup je vhodný zejména pro problémy, kde je obtížné nebo nemožné poskytnout "oštítkovaná" data pro učení s učitelem, například při učení robota chodit nebo při hraní složitých her jako šachy nebo Go.

## 2. Typy Zpětnovazebního Učení

Rozlišujeme dva hlavní scénáře RL:
*   **Pasivní Zpětnovazební Učení (Passive RL):** Agent má **fixní strategii (politiku) π**, která mu předepisuje, jakou akci má provést v každém stavu. Cílem agenta je pouze naučit se, jak dobrá tato strategie je, tj. naučit se **hodnoty užitku U(s)** pro jednotlivé stavy. Tento proces se podobá vyhodnocování politiky (policy evaluation) z Markovských rozhodovacích procesů.
*   **Aktivní Zpětnovazební Učení (Active RL):** Agent nezná optimální strategii a musí se ji naučit. Cílem je nejen zjistit užitek stavů, ale také nalézt optimální politiku π*(s). Klíčovým problémem je zde tzv. **dilema průzkumu vs. využití (exploration vs. exploitation)** – agent se musí rozhodovat, zda provede akci, o které ví, že je dobrá (využití), nebo zda zkusí novou, neprozkoumanou akci, která by mohla být ještě lepší (průzkum).

## 3. Komponenty Učícího se Agenta

Obecný RL agent se skládá z několika částí:
*   **Výkonná komponenta (Performance Component):** Zodpovídá za výběr a provádění akcí v prostředí na základě aktuální strategie.
*   **Učící se komponenta (Learning Component):** Aktualizuje znalosti agenta (např. užitkové funkce nebo politiku) na základě zkušeností (sekvencí stavů, akcí a odměn).
*   **Kritik (Critic):** Poskytuje zpětnou vazbu učící se komponentě tím, že hodnotí, jak dobré byly provedené akce. Tato zpětná vazba je odvozena od odměn získaných z prostředí.
*   **Generátor problémů (Problem Generator):** Navrhuje nové akce nebo sekvence akcí, které mohou vést k prozkoumání nových a potenciálně užitečných částí stavového prostoru (podporuje exploraci).

## 4. Formulace Úlohy: Markovský Rozhodovací Proces (MDP)

Formálním rámcem pro zpětnovazební učení je **Markovský rozhodovací proces (Markov Decision Process - MDP)**. MDP je matematický model pro sekvenční rozhodování ve stochastickém (pravděpodobnostním) prostředí.

### 4.1 Definice MDP

MDP je definováno jako čtveřice `(S, A, P, R)`:
*   `S`: Množina stavů.
*   `A`: Množina akcí.
*   `P(s' | s, a)`: **Přechodová funkce**, která udává pravděpodobnost, že provedením akce `a` ve stavu `s` se agent dostane do stavu `s'`. Klíčová je **Markovská vlastnost**: pravděpodobnost přechodu závisí pouze na aktuálním stavu a akci, nikoliv na celé historii předchozích stavů.
*   `R(s)`: **Funkce odměn**, která přiřazuje číselnou hodnotu (odměnu) každému stavu.

Prostředí je **plně pozorovatelné**, což znamená, že agent v každém okamžiku přesně ví, ve kterém stavu se nachází.

### 4.2 Cíl Agenta v MDP

Cílem agenta je najít **optimální politiku π*(s)**. Politika (strategie) je pravidlo, které agentovi říká, jakou akci `a` má provést v každém stavu `s`. Optimální politika je taková, která maximalizuje **očekávaný kumulativní zisk** (součet diskontovaných odměn):

`Uπ(s) = E[ Σ (γ^t * R(St)) ]`

kde `γ` je diskontní faktor (0 ≤ γ < 1), který určuje váhu budoucích odměn, a `St` je stav v čase `t`.

V kontextu RL agent typicky nezná přechodovou funkci `P` ani funkci odměn `R`. Tyto parametry se musí naučit z interakce s prostředím.
