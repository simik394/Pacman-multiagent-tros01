# Lekce 11: Agenti a Roboti

Tento průvodce se zabývá robotikou, autonomními agenty a architekturami, které řídí jejich chování.

## 1. Robotika

**Robotika** je disciplína na pomezí informatiky, strojírenství a umělé inteligence, která se zabývá návrhem, konstrukcí a provozem robotů – fyzických agentů, kteří manipulují s fyzickým světem.

### 1.1 Typy Robotů

Roboty lze kategorizovat do několika hlavních skupin:
*   **Průmyslové roboty (Manipulátory):** Jsou to robotická ramena, která jsou fyzicky ukotvena na svém pracovišti, například na montážní lince. Jejich hlavním úkolem je manipulace s objekty. Jsou nejrozšířenějším typem průmyslových robotů.
*   **Mobilní roboty:** Pohybují se ve svém prostředí pomocí kol, nohou nebo jiných mechanismů. Příklady zahrnují autonomní vozidla (UGV), drony (UAV), podvodní vozidla (AUV) a planetární rovery.
*   **Humanoidní roboty:** Svým vzhledem a často i pohybem napodobují člověka. Jsou příkladem mobilních manipulátorů, kteří kombinují mobilitu s schopností manipulace.

## 2. Autonomní Robot

**Autonomní robot** je inteligentní stroj schopný vykonávat úkoly samostatně bez přímé lidské pomoci.
*   **Nejdůležitější vlastnost:** Schopnost vnímat své okolí a reagovat na nepředvídatelné změny v něm.
*   **Základní části:**
    1.  **Senzory (Sensors):** Umožňují robotovi vnímat prostředí (např. kamery, lasery, gyroskopy).
    2.  **Řídicí jednotka (Controller):** "Mozek" robota, který zpracovává data ze senzorů a rozhoduje o akcích.
    3.  **Efektory (Effectors) / Aktuátory (Actuators):** Vykonávají fyzické akce (např. motory v kolech, kloubech ramene, chapadla).

## 3. Prostředí Agenta

Vlastnosti prostředí zásadně ovlivňují návrh agenta. Prostředí může být:
*   **Plně pozorovatelné (Fully Observable) / Částečně pozorovatelné (Partially Observable):** Má agent v každém okamžiku přístup k úplnému stavu prostředí? Reálný svět je pro roboty téměř vždy částečně pozorovatelný.
*   **Deterministické (Deterministic) / Stochastické (Stochastic):** Je další stav prostředí plně určen aktuálním stavem a akcí agenta? Pohyb reálných robotů je stochastický kvůli skluzu kol, nepřesnostem motorů atd.
*   **Epizodické (Episodic) / Sekvenční (Sequential):** Skládá se život agenta z nezávislých epizod, nebo současná akce ovlivňuje budoucí rozhodnutí? Robotika je typicky sekvenční.
*   **Statické (Static) / Dynamické (Dynamic):** Mění se prostředí, zatímco agent přemýšlí? Svět, ve kterém se roboti pohybují, je dynamický.
*   **Diskrétní (Discrete) / Spojité (Continuous):** Je stavový prostor, čas a akce agenta tvořen konečným počtem hodnot, nebo spojitým rozsahem? Robotika se typicky odehrává ve spojitém prostoru a čase.
*   **Jednoagentové (Single-agent) / Multiagentní (Multi-agent):** Působí v prostředí jeden agent, nebo více? Doprava je typickým multiagentním prostředím.

## 4. Senzorický Subsystém

*   **Pasivní senzory:** Zachytávají signály z prostředí (např. **kamera**, **gyroskop**, **tlačítka**).
*   **Aktivní senzory:** Vysílají do prostředí signál a detekují jeho odraz (např. **sonar**, **laserové dálkoměry (lidar)**, **GPS**).
*   **Lokální vs. Distribuované:** Senzory mohou být součástí robota (lokální) nebo rozmístěné v prostředí (distribuované).

## 5. Příklady Historických Robotů

*   **Shakey (konec 60. let):** První univerzální mobilní robot schopný vnímání, plánování a provádění akcí. Během jeho vývoje vznikl mimo jiné i slavný prohledávací algoritmus A*.
*   **Genghis (80. léta):** Šestinohý chodící robot od Rodneyho Brookse, který demonstroval principy reaktivního řízení a subsumpční architektury.
*   **Cog a Kismet (90. léta):** Humanoidní roboti z MIT zaměření na kognitivní vědu a sociální interakci mezi člověkem a robotem.
*   **Coco:** Humanoidní robot inspirovaný tělem gorily pro studium pohybu.

## 6. Typy Agentů

### 6.1 Reaktivní Agent (Simple Reflex Agent)

*   Nejjednodušší typ agenta. Jedná na základě **pravidel typu podmínka-akce**.
*   Rozhoduje se pouze na základě **aktuálního vjemu**, ignoruje historii.
*   Nevytváří si vnitřní model světa ani složité plány.
*   Příklad: Jednoduchý robotický vysavač, který změní směr, když narazí do zdi.

### 6.2 Deliberativní Agent (Model-based / Goal-based Agent)

*   Pokročilejší typ agenta, který překonává omezení reaktivních agentů.
*   Udržuje si **vnitřní stav (model světa)**, který reprezentuje aspekty prostředí, jež nejsou aktuálně viditelné.
*   Má explicitně definované **cíle**, kterých se snaží dosáhnout.
*   **Plánuje** sekvence akcí, které vedou ke splnění cílů.
*   Příklad: Robot, který plánuje optimální trasu pro doručení balíku, přičemž zvažuje překážky a alternativní cesty na základě mapy (svého modelu světa).

## 7. Subsumpční Architektura

*   Navržena Rodneym Brooksem. Je to způsob dekompozice chování agenta do několika **vrstev**.
*   Každá vrstva implementuje určité chování (např. "vyhni se překážce", "jdi vpřed").
*   Vrstvy spolu "soupeří" o řízení agenta. Nižší, základnější vrstvy (např. vyhýbání se) mají **přednost** a mohou "potlačit" (subsume) příkazy z vyšších vrstev (např. "jdi k cíli").
*   Jedná se o reaktivní, zdola nahoru budovanou architekturu.

## 8. Celulární Automat (Cellular Automaton)

*   Dynamický systém, který je **diskrétní v prostoru a čase**.
*   Skládá se z pravidelné mřížky **buněk**, kde každá buňka může být v jednom z konečného počtu stavů.
*   Stav každé buňky v dalším časovém kroku je určen **lokální přechodovou funkcí**, která závisí na aktuálním stavu buňky a stavech jejích **sousedů**.
*   **Využití:**
    *   **Simulace přírodních jevů:** Šíření požáru, růst krystalů, šíření epidemií.
    *   **Teoretická informatika:** Modelování výpočetních procesů (např. Turingův stroj).
    *   **Fyzika:** Modelování dynamiky plynů a termodynamických procesů.
    *   **Kryptografie:** Generování pseudonáhodných čísel pro šifrovací algoritmy.
    Jeden z nejznámějších příkladů je "Hra života" (Game of Life) od Johna Conwaye.
