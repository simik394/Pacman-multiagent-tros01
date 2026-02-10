# Lekce 10: Počítačové Vidění

Počítačové vidění je vědní a technologická disciplína, jejímž cílem je vytvářet stroje, které jsou schopné "vidět" a interpretovat vizuální informace z okolního světa, podobně jako lidé.

## 1. Typické Úlohy Počítačového Vidění

Počítačové vidění řeší širokou škálu úloh, které lze rozdělit do několika kategorií:
*   **Rozpoznávání (Recognition):** Identifikace a klasifikace objektů ve scéně. Například rozpoznání obličeje, značky auta nebo typu zvířete.
*   **Analýza pohybu (Motion Analysis):** Sledování objektů v čase, odhad jejich rychlosti a trajektorie. Příkladem je sledování chodců ve videu.
*   **Rekonstrukce scény (Scene Reconstruction):** Vytváření 3D modelů scény z 2D obrázků. Toho se využívá například ve virtuální realitě nebo robotice.
*   **Restaurace obrazu (Image Restoration):** Odstraňování šumu, rozmazání a jiných degradací z obrazu za účelem zlepšení jeho kvality.

Typický proces zpracování obrazu má několik kroků:
1.  **Snímání a digitalizace:** Pořízení obrazu (např. kamerou) a jeho převod do digitální podoby. Zahrnuje i OCR (Optical Character Recognition) pro text.
2.  **Předzpracování:** Úpravy obrazu pro zlepšení kvality, např. odstranění šumu.
3.  **Segmentace obrazu:** Rozdělení obrazu na smysluplné části nebo objekty.
4.  **Popis objektů:** Extrakce charakteristických rysů (features) z každého objektu.
5.  **Porozumění obsahu obrazu:** Interpretace a klasifikace objektů a celé scény.

## 2. Základní Charakteristiky Digitálního Obrazu

Digitální obraz je reprezentován mřížkou pixelů. Jeho kvalita je určena dvěma hlavními parametry:
*   **Vzorkování (Sampling):** Určuje **rozlišení** obrazu, tedy počet pixelů, ze kterých se skládá. Vyšší rozlišení znamená více detailů.
*   **Kvantování (Quantization):** Určuje počet možných hodnot (úrovní jasu nebo barev), které může každý pixel nabývat. Například 8bitový černobílý obraz má 256 úrovní šedi.

## 3. Detekce Hran

Hrany jsou místa v obraze, kde dochází k prudké změně jasu. Jsou to základní stavební kameny pro rozpoznávání objektů.
*   **Základní myšlenka:** Hrany lze detekovat hledáním míst s největším **gradientem** (změnou) jasu, což se matematicky provádí pomocí **derivace** obrazové funkce.
*   **Problém se šumem:** Reálné obrazy obsahují šum, který způsobuje malé, náhodné změny jasu. Přímá aplikace derivace by vedla k detekci velkého množství falešných hran.
*   **Řešení - Vyhlazení:** Před derivováním je nutné obraz **vyhladit**, aby se potlačil šum. To se provádí zprůměrováním hodnoty každého pixelu s hodnotami jeho sousedů.

### 3.1 Konvoluce

Vyhlazení je příkladem operace zvané **konvoluce**. Při konvoluci je nová hodnota každého pixelu vypočtena jako **vážená lineární kombinace** hodnot pixelů v jeho okolí. Váhy jsou definovány malou maticí, která se nazývá **konvoluční jádro (kernel)**. Pro vyhlazení se často používá Gaussovo jádro, které dává největší váhu centrálnímu pixelu a váhy se postupně snižují směrem od středu.

## 4. Rosenblattův Perceptron

*   Navržen Frankem Rosenblattem v roce 1958, je to jeden z prvních a nejjednodušších modelů umělé neuronové sítě.
*   Byl inspirován fungováním lidského oka a jeho původním úkolem bylo rozpoznávat znaky abecedy z pole optických snímačů o rozměrech 20x20.
*   Jedná se o algoritmus pro **binární klasifikaci**. Na základě váženého součtu vstupních hodnot rozhoduje, zda vstup patří do jedné ze dvou tříd. `Výstup = f(Σ(váha_i * vstup_i))`
*   **Struktura Perceptronu:**
    1.  **Receptory (S-jednotky):** Vstupní vrstva, která přijímá data (např. pixely obrazu).
    2.  **Asociativní elementy (A-jednotky):** Mezivrstva s pevně danými vahami, která provádí jednoduchou extrakci rysů.
    3.  **Reagující elementy (R-jednotky):** Výstupní vrstva, která sečte vážené signály z A-jednotek a na základě prahové funkce vydá výstup (např. 0 nebo 1). Váhy vedoucí do této vrstvy se během učení upravují.

## 5. Konvoluční Neuronová Síť (CNN)

*   Moderní a velmi úspěšný typ **hluboké (vícevrstvé), dopředné (feed-forward)** neuronové sítě, který je standardem pro úlohy analýzy obrazu.
*   **Klíčová vlastnost:** Neurony v jedné vrstvě nejsou propojeny se všemi neurony v předchozí vrstvě, ale pouze s **malou lokální oblastí** (tzv. receptivním polem). Tato operace je matematicky ekvivalentní konvoluci, odtud název.
*   Tato architektura umožňuje síti postupně se učit hierarchii rysů:
    *   První vrstvy se naučí detekovat jednoduché rysy jako hrany a rohy.
    *   Další vrstvy kombinují tyto jednoduché rysy do složitějších vzorů (textury, části objektů).
    *   Hluboké vrstvy rozpoznávají celé objekty.
*   Výstupem CNN je obvykle **vektor pravděpodobností**, který udává, s jakou pravděpodobností vstupní obraz patří do jednotlivých předdefinovaných kategorií (např. 80% kočka, 15% pes, 5% liška).
