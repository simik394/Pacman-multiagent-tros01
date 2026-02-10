# Lekce 2: Vyhodnocování Inteligence Umělých Systémů

Tento studijní průvodce se zabývá fundamentální otázkou: "Mohou stroje myslet?" a zkoumá různé historické i moderní přístupy k hodnocení inteligence umělých systémů.

## 1. Filozofické Dělení Umělé Inteligence

Než se ponoříme do testování, je důležité rozumět různým cílům a hypotézám v rámci UI.

*   **Slabá UI (Weak AI):** Tato hypotéza tvrdí, že stroje mohou **jednat, jako by byly** inteligentní. Cílem je vytvářet užitečné nástroje, které řeší konkrétní problémy, a simulovat lidské mentální schopnosti, abychom lépe porozuměli lidské mysli. Většina současného výzkumu v UI spadá do této kategorie a nezajímá se o to, zda stroj skutečně "myslí".
*   **Silná UI (Strong AI):** Tato hypotéza jde dál a tvrdí, že stroje, které jednají inteligentně, skutečně **myslí** a mají kognitivní stavy, jako je rozumění a vědomí. Nejde jen o simulaci, ale o skutečnou inteligenci.
*   **Specifická UI (Specific AI):** Zaměřuje se na tvorbu programů pro řešení úzce vymezených, specifických úloh (např. hraní šachů, diagnostika nemocí).
*   **Obecná UI (Artificial General Intelligence - AGI):** Cílem je tvorba programů pro obecné řešení úloh a inteligentní jednání srovnatelné s lidskou univerzálností. Takový systém by se dokázal adaptovat na širokou škálu úkolů, podobně jako člověk.

## 2. Rané Úvahy: René Descartes

Francouzský filozof René Descartes (17. století) položil základy mnoha otázek, které jsou relevantní i dnes.

*   **Metodologický skepticizmus:** Descartes prosazoval myšlenku, že skrze systematické pochybování o všem lze dospět k pevným, nepochybným principům vědění.
*   **Racionalizmus vs. Empirizmus:** Byl zastáncem racionalizmu, který považuje rozum za primární a rozhodující zdroj poznání, na rozdíl od empirizmu, který zdůrazňuje smyslovou zkušenost. Tvrdil, že smysly nás mohou klamat.
*   **Dualizmus:** Zavedl myšlenku dualismu těla a mysli. Tělo je materiální, funguje jako stroj, zatímco mysl je nemateriální a je sídlem myšlení a vědomí.

Ve své publikaci "Rozprava o metodě" (1637) Descartes přímo zpochybnil, že by stroje mohly dosáhnout lidské úrovně myšlení. Argumentoval, že strojům chybí **univerzálnost myšlení**. Mohou sice některé úkoly dělat lépe než člověk, ale selžou v mnoha jiných, protože jejich schopnosti jsou úzce vymezené, zatímco lidský rozum je univerzální. Tím předjal mnoho moderních debat o specifické vs. obecné UI.

## 3. Turingův Test: Imitační Hra

Alan Turing (1950) navrhl nahradit vágní otázku "Mohou stroje myslet?" konkrétním behaviorálním testem.

### 3.1 Princip Imitační Hry

Tzv. **Turingův test** (původně "imitační hra") probíhá následovně:
1.  Lidský **tazatel (C)** vede textovou konverzaci se dvěma neviditelnými protějšky.
2.  Jeden protějšek je **člověk (B)**, druhý je **stroj (A)**.
3.  Úkolem tazatele je na základě odpovědí určit, který z protějšků je stroj.
4.  Cílem stroje je **oklamat tazatele**, aby si myslel, že je člověk.

Pokud stroj dokáže tazatele klamat s dostatečnou úspěšností (Turing navrhoval 30 % po pěti minutách konverzace), pak testem prošel.

### 3.2 Definice "Stroje"

Turing se ve svých úvahách omezil na **digitální počítače**, které popsal jako **stroje s diskrétním stavem**. Takový stroj se skládá ze tří hlavních částí:
*   **Paměť (Storage):** Teoreticky nekonečný prostor pro ukládání informací a instrukcí.
*   **Výkonná jednotka (Executive Unit):** Provádí jednotlivé operace.
*   **Řídící jednotka (Control):** Zajišťuje správné provedení instrukcí v daném pořadí.

### 3.3 Námitky proti Možnosti Myslících Strojů

Turing ve svém článku předjímal a vyvracel řadu námitek:
*   **Teologická námitka:** "Myšlení je funkce nesmrtelné duše, kterou Bůh dal člověku, ale ne strojům." Turing argumentuje, že nevidí důvod, proč by Bůh nemohl dát duši i stroji.
*   **Námitka "strkání hlavy do písku":** "Představa myslících strojů je hrozná, doufejme tedy, že nemohou existovat." Toto je emocionální argument, nikoli logický.
*   **Matematická námitka:** Odkazuje na Gödelovy věty o neúplnosti, které ukazují, že v každém dostatečně silném formálním systému existují pravdivá tvrzení, která nelze dokázat. Argument zní, že stroje jsou takovými systémy, ale lidé ne. Turing oponuje, že neexistuje důkaz, že by lidé nebyli omezeni stejným způsobem.
*   **Argument z vědomí:** Tvrdí, že stroj skutečně nemyslí, dokud necítí emoce a není si vědom svých činů. Turing toto elegantně obchází tím, že pokud bychom tento argument brali vážně, nemohli bychom vědět, zda myslí i kdokoli jiný kromě nás samých.

## 4. Myšlenkový Experiment s Čínským Pokojem

Filozof John Searle (1980) představil vlivný argument proti Silné UI.

Představte si člověka, který **neumí čínsky**, zavřeného v místnosti. Tento člověk má k dispozici obrovskou knihu pravidel v jeho rodném jazyce (např. v angličtině). Pravidla mu říkají, jak manipulovat s čínskými znaky. Zvenku mu někdo podává lístky s otázkami v čínštině. Člověk uvnitř nerozumí ani otázkám, ani odpovědím, ale pečlivě sleduje pravidla v knize, která mu říkají, jaké znaky má na základě vstupních znaků napsat na výstupní lístek.

*   **Z vnějšího pohledu:** Systém (člověk + kniha) se chová, jako by rozuměl čínsky. Odpovídá smysluplně na otázky a mohl by projít Turingovým testem.
*   **Z vnitřního pohledu:** Člověk uvnitř místnosti se čínsky nenaučil. Stále jen manipuluje se symboly, kterým nerozumí.

Searlův závěr je, že **syntaxe (manipulace se symboly) není totéž co sémantika (skutečné rozumění)**. A protože počítačové programy nedělají nic jiného než manipulaci se symboly podle pravidel, nemohou samy o sobě nikdy dosáhnout skutečného rozumění.

## 5. Moderní Přístup: Racionální Agenti

Současná UI se z velké části odklonila od filozofických debat a zaměřila se na praktický koncept **racionálních agentů**.

*   **Agent:** Cokoli, co vnímá své prostředí pomocí **senzorů** (sensors) a jedná v něm pomocí **aktuátorů** (actuators).
*   **Prostředí (Environment):** Svět, ve kterém agent existuje a jedná.
*   **Vjem (Percept):** Vstupní data, která agent v daném okamžiku získá ze senzorů.
*   **Sekvence vjemů (Percept Sequence):** Kompletní historie všeho, co agent kdy vnímal.

Základní cyklus interakce je: agent vnímá svět, na základě vjemů provede akci, za kterou může (ale nemusí) dostat odměnu nebo trest, a cyklus se opakuje.

**Funkce agenta (Agent Function)** je matematická abstrakce, která mapuje jakoukoli sekvenci vjemů na akci. Program agenta (Agent Program) je konkrétní implementace této funkce.

**Racionální agent** je takový, který pro každou možnou sekvenci vjemů vybere akci, která **maximalizuje jeho očekávanou míru výkonnosti** (performance measure), na základě dosavadních vjemů a vestavěného vědění.

Tento přístup je pragmatický. Neptá se, zda agent "myslí", ale zda jedná optimálně vzhledem ke svému cíli.
