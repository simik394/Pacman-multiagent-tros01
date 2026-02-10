# Lekce 7: Strojové Učení

Tento studijní průvodce se věnuje základním konceptům strojového učení, což je proces, při kterém agent zlepšuje své chování na základě zkušeností.

## 1. Co je Učení?

**Učení** je proces, při kterém agent zlepšuje svůj výkon v budoucích úlohách na základě pozorování světa. Je to klíčová vlastnost inteligentních systémů.

### 1.1 Metody Učení

Existuje mnoho způsobů, jak se agent může učit:
*   **Učení se zapamatováním (Rote Learning):** Agent si ukládá nové poznatky (např. telefonní číslo) bez jejich dalšího zpracování.
*   **Učení se z instrukcí (Learning from Instruction):** Agent přijímá explicitní pokyny od učitele.
*   **Učení se z analogie (Learning by Analogy):** Agent aplikuje znalosti z jedné domény na novou, podobnou doménu.
*   **Učení se na základě vysvětlení (Explanation-Based Learning):** Agent využívá existující znalosti k vysvětlení jednoho příkladu a z toho odvodí obecné pravidlo.
*   **Učení se z příkladů (Inductive Learning):** Agent odvozuje obecné pravidlo z množiny konkrétních příkladů. Toto je nejběžnější forma strojového učení.
*   **Učení se pozorováním a objevováním (Unsupervised Learning):** Agent hledá vzory a struktury v datech bez explicitní zpětné vazby.

### 1.2 Zpětná Vazba v Procesu Učení

Typ zpětné vazby definuje tři hlavní kategorie učení:
1.  **Učení s učitelem (Supervised Learning):** Agent dostává trénovací sadu příkladů, kde každý vstup je spárován se správným výstupem (klasifikací). Učitel poskytuje "správné odpovědi".
2.  **Učení bez učitele (Unsupervised Learning):** Agent dostává pouze vstupy a snaží se v nich najít skryté vzory. Typickým příkladem je **shlukování (clustering)**.
3.  **Zpětnovazební učení (Reinforcement Learning):** Agent se učí na základě odměn a trestů. Po sérii akcí dostane zpětnou vazbu, která mu říká, jak dobře si vedl, ale neříká mu, která konkrétní akce byla správná nebo špatná.

## 2. Empirické Učení z Dat (Induktivní Učení)

Cílem je na základě **trénovací sady** příkladů `(x, y)` nalézt hypotézu (funkci) `h`, která dobře aproximuje neznámou cílovou funkci `f`. Očekáváme, že hypotéza bude dobře fungovat i na nových, dosud neviděných datech (tzv. **testovací sadě**).

### 2.1 Přeučení (Overfitting) vs. Podučení (Underfitting)

*   **Přeučení (Overfitting):**
    *   Nastává, když je model příliš složitý a "zapamatuje si" trénovací data včetně šumu, místo aby se naučil obecný vzor.
    *   Projevuje se tak, že chyba na trénovacích datech je velmi nízká, ale chyba na testovacích datech je vysoká.
    *   Typické pro složité modely (např. hluboké rozhodovací stromy, neuronové sítě s mnoha neurony).

*   **Podučení (Underfitting):**
    *   Nastává, když je model příliš jednoduchý a nedokáže zachytit základní strukturu dat.
    *   Chyba je vysoká jak na trénovacích, tak na testovacích datech.
    *   Typické pro příliš jednoduché modely (např. lineární regrese na nelineárních datech).

Cílem je najít model, který je "tak akorát" složitý a dobře **generalizuje**.

## 3. Paradigmy Učení

### 3.1 Učení jako Prohledávání

Učení lze chápat jako prohledávání **prostoru hypotéz** s cílem nalézt hypotézu, která nejlépe odpovídá datům.
*   **Příklad:** Algoritmus pro učení **rozhodovacích stromů** prohledává prostor možných stromů a v každém kroku se chamtivě rozhoduje, kterým atributem data rozdělit, aby maximalizoval informační zisk. Hledá se optimální struktura i parametry modelu.

### 3.2 Učení jako Aproximace (Optimalizace)

V tomto pohledu máme předem danou strukturu modelu a snažíme se najít jeho optimální parametry.
*   **Příklad:** U **neuronových sítí** je struktura (počet vrstev a neuronů) často daná a učení spočívá v nalezení optimálních vah `w` tak, aby se minimalizovala chybová funkce (loss function) na trénovacích datech. To se obvykle dělá pomocí **gradientního sestupu (gradient descent)**.

## 4. Neuronové Sítě

**Neuronová síť** je výpočetní systém inspirovaný strukturou a funkcí biologických neuronových sítí.
*   Skládá se z propojených **výpočetních jednotek (neuronů)** uspořádaných do vrstev.
*   Každé spojení má **váhu `w`**, která určuje sílu signálu.
*   Každý neuron `j` spočítá vážený součet svých vstupů `inⱼ = Σᵢ wᵢⱼ aᵢ` a aplikuje na něj nelineární **aktivační funkci `g`** (např. sigmoid nebo ReLU), čímž získá svůj výstup `aⱼ = g(inⱼ)`.
*   Učení sítě probíhá úpravou vah (např. algoritmem **zpětného šíření chyby - backpropagation**), aby se minimalizoval rozdíl mezi predikovaným a skutečným výstupem.

## 5. Teoretické Koncepty Učení

### 5.1 PAC Teorie (Probably Approximately Correct Learning)

Tato teorie poskytuje formální rámec pro analýzu, zda se model dokáže efektivně naučit a generalizovat.
*   Zaručuje, že s pravděpodobností alespoň `1-δ` bude chyba naučené hypotézy menší než `ε`.
*   Poskytuje odhady, kolik trénovacích vzorků je potřeba pro dosažení těchto záruk.
*   Pomáhá formalizovat kompromis mezi složitostí modelu (měřenou např. **VC dimenzí**) a potřebným množstvím dat, čímž pomáhá předcházet přeučení.

### 5.2 Teorém "No Free Lunch"

*   **Znění:** Neexistuje žádný univerzálně nejlepší algoritmus strojového učení.
*   **Vysvětlení:** Pokud je algoritmus A lepší než algoritmus B na jedné třídě problémů, pak musí existovat jiná třída problémů, na které je algoritmus B lepší než A.
*   **Důsledek:** Výběr algoritmu musí být přizpůsoben konkrétnímu problému a datům.

### 5.3 Teorém Ošklivého Káčátka

*   **Znění:** Z čistě formálního hlediska jsou si jakékoliv dva objekty stejně podobné (nebo nepodobné), pokud neuplatníme nějaký **bias** (předpoklad) o tom, které atributy jsou důležitější.
*   **Vysvětlení:** Počet atributů, ve kterých se dva objekty shodují, je konstantní, pokud uvážíme všechny možné (i velmi absurdní) atributy.
*   **Důsledek:** Jakákoliv klasifikace nebo učení na základě podobnosti implicitně předpokládá nějaký bias, který nám říká, co je a co není "důležitý" rys.
