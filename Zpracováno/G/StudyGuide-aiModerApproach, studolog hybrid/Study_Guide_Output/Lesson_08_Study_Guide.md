# Lekce 8: Použití Znalostí v Učení

Tento průvodce se zaměřuje na to, jak mohou agenti využívat již existující (apriorní) znalosti k urychlení a zefektivnění procesu učení. Místo toho, aby se učili od nuly, mohou stavět na tom, co již vědí.

## 1. Klasifikace Znalostí

Znalosti můžeme dělit podle různých kritérií, což nám pomáhá pochopit jejich povahu a způsob, jakým je lze reprezentovat a využít.

### 1.1 Podle Formalizovatelnosti

*   **Explicitní znalosti:** Jsou to znalosti, které jsou plně formalizované, artikulované a snadno sdělitelné. Příkladem jsou matematické vzorce nebo pravidla v manuálu.
*   **Implicitní znalosti:** Tyto znalosti jsou primárně skryté v datech a nejsou přímo formulovány. Například vzory v nákupním chování zákazníků, které odhalí algoritmus strojového učení.
*   **Tacitní znalosti:** Jde o nevědomé a těžko sdělitelné znalosti, které jsou skryty v myslích expertů. Příkladem je intuice zkušeného lékaře při stanovování diagnózy. Tacitní znalosti je velmi obtížné formalizovat.

### 1.2 Podle Obsahu

*   **Deklarativní znalosti:** Popisují, co platí, tedy fakta o světě. Například: "Všechny kočky jsou savci." Jsou to výroky o stavu věcí.
*   **Procedurální znalosti:** Popisují, jak postupovat, tedy návody a procesy. Například: "Postup pro výměnu pneumatiky." Jsou to znalosti o tom, jak provádět akce.

## 2. Požadavky na Znalosti

Aby byly znalosti v systémech umělé inteligence efektivně využitelné, měly by splňovat několik klíčových požadavků:
*   **Transparentnost:** Znalosti by měly být srozumitelné a jejich fungování by mělo být snadno pochopitelné pro člověka.
*   **Modularita:** Mělo by být možné snadno přidávat, odebírat nebo měnit jednotlivé části znalostní báze bez narušení celého systému.
*   **Modifikovatelnost:** Systém by měl umožňovat snadnou aktualizaci a úpravu znalostí.
*   **Užitečnost:** Znalosti musí být relevantní pro řešení daného problému a přispívat k dosažení cílů agenta.

## 3. Reprezentace Znalostí v AI

Existuje několik zavedených formalismů pro reprezentaci znalostí v systémech umělé inteligence.

### 3.1 Predikátová Logika

*   Jedná se o rozšíření výrokové logiky, které umožňuje pracovat s objekty, jejich vlastnostmi a vztahy.
*   Základními stavebními kameny jsou **predikáty** (vyjadřují vlastnosti nebo vztahy, např. `JeClovek(x)`), **funkce** (mapují objekty na jiné objekty, např. `Matka(x)`), **logické spojky** (∧, ∨, ¬, ⇒) a **kvantifikátory** (∀ – obecný, ∃ – existenční).
*   Umožňuje formulovat složité a obecné výroky o světě, což je klíčové pro pokročilé usuzování.

### 3.2 Sémantické Sítě

*   Grafová reprezentace, která popisuje realitu jako soubor **objektů (uzlů)** a **relací (hran)** mezi nimi.
*   Například uzly "Pes" a "Savec" mohou být spojeny hranou s popiskem "JeDruh" (SubsetOf). Uzel "Fido" a "Pes" mohou být spojeny hranou "JeInstance" (MemberOf).
*   Hlavní výhodou je intuitivní vizualizace a efektivní mechanismus pro **dědičnost** (inheritance), kdy objekty dědí vlastnosti od svých nadřazených kategorií.

### 3.3 Rámce (Frames)

*   Komplexní datová struktura, která se stala inspirací pro objektově orientované programování (OOP).
*   Rámec reprezentuje typický objekt nebo koncept (např. rámec pro "Pokoj v hotelu").
*   Obsahuje:
    *   **Data (sloty):** Atributy, které popisují objekt (např. `Počet_lůžek`, `Má_koupelnu`).
    *   **Meta-data:** Informace o datech (např. výchozí hodnota pro `Počet_lůžek` je 2).
    *   **Procedury (démoni):** Funkce, které se aktivují při čtení nebo zápisu do slotu (např. procedura `if-added` pro přepočet ceny).

### 3.4 Pravidla (Rules)

*   Znalosti jsou reprezentovány ve formě **IF-THEN** pravidel (podmínka-akce).
*   Například: `IF (teplota < 18°C) AND (topení_je_vypnuté) THEN (zapni_topení)`.
*   Tento přístup je základem **expertních systémů** (rule-based systems), kde se usuzování provádí řetězením těchto pravidel.

### 3.5 Případy (Cases)

*   Znalosti jsou uchovávány ve formě konkrétních, v minulosti vyřešených problémů (případů).
*   Při řešení nového problému systém hledá v databázi nejpodobnější starý případ a adaptuje jeho řešení.
*   Tento přístup se nazývá **případové usuzování (Case-Based Reasoning - CBR)** a je užitečný v doménách, kde je těžké formulovat obecná pravidla, ale existuje bohatá historie zkušeností.

## 4. Učení s Využitím Apriorních Znalostí

Tradiční induktivní učení hledá hypotézu `h`, která nejlépe odpovídá datům. Učení založené na znalostech (Knowledge-Based Learning) rozšiřuje tento model o **apriorní znalosti (Background Knowledge)**.

Logická formulace učení vypadá takto:
`Hypothesis ∧ Descriptions |= Classifications`

To znamená, že hypotéza spolu s popisy příkladů musí logicky implikovat jejich klasifikace. Pokud přidáme apriorní znalosti, rovnice se změní:
`Background ∧ Hypothesis ∧ Descriptions |= Classifications`

Apriorní znalosti hrají dvě klíčové role:
1.  **Omezují prostor hypotéz:** Generovaná hypotéza musí být konzistentní nejen s daty, ale i s apriorními znalostmi.
2.  **Zjednodušují hypotézu:** Apriorní znalosti mohou "pomoci" s vysvětlením pozorování, takže samotná hypotéza může být mnohem jednodušší a snáze nalezitelná.

**Příklad:**
Při učení se konceptu "Dědeček(x, y)", pokud systém již zná koncept "Rodič(x, y)", je výsledná hypotéza `∃z (Rodič(x, z) ∧ Rodič(z, y))` mnohem jednodušší než hypotéza, která by musela být odvozena pouze z primitivních predikátů jako `Matka` a `Otec`.
