Určitě jste již někdy slyšeli o datových únicích, víte však jak by se bezpečně měla ukládat hesla?

Pojďme se dnes pobavit o hashování.

Většina aplikací po vás v dnešní době vyžaduje uživatelské jméno a heslo pro přihlášení k vašemu účtu a jelikož je potřeba zkontrolovat jestli účet patří vám musí se toto heslo někam uložit.

Nejjednoduší je heslo společně s vaším jménem uložit někam do databáze, takzvaně v plaintextu. Velkou nevýhodou je, že nyní kdokoliv kdo získá přístup k této databázi uživatelů přímo uvidí vaše heslo a může se s ním zkusit přihlásit na jiné platformě.

Proto velmi často využíváme hashování. Hashovací funkce je taková funkce, která pro každá vstupní data vygeneruje nějaký výstup, který je vždy stejný pro stejná vstupní data. Ale při změně vstupních dat byť jen o jeden bit je výstup kompletně změněn. Neexistuje způsob jak se od hashe dostat zpět ke vstupním datům, hashování je jednosměrné.

Proto když nahradíme data v tabulce hashi hesel, už nemůžeme tak jednoduše zjistit, kdo má jaké heslo. Vyvstává zde ale další problém - stejná hesla mají stejný hash. Když například alici unikne heslo v plaintextu, útočník s  přístupem k databázi tak získá přístup i k heslu boba.

Řešením je takzvaný salt hashing - v něm ke každému heslu vygenerujeme ještě náhodný string který před hashováním přidáme ke vstupnímu heslu. Pokud se vstupní heslo + salt po zahashování shodují s uloženým hashem - uživatel zadal správné heslo a je vpuštěn na web!

Data o tom, zda se váš email objevil v nějakém data breachi můžete zjistit na haveibeenpwned.com. 