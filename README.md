# multiclass_text_classification_ML
klasifikace krátkých textů

Načtěte soubor “dataset_rss.csv”, sloupce jsou odděleny čárkou. Data obsahují titulky, perex
a URL novinových článků. Data jsou seřazena náhodně.

Ze sloupce “url” získejte hlavní kategorii článku, která bude dále sloužit jako label pro
výsledný klasifikátor. Hlavní kategorii článku lze z URL získat jako první část cesty za
doménou. Např. pro článek s URL
“https://www.novinky.cz/zahranicni/evropa/clanek/islamsky-stat-se-prihlasil-k-utoku-vrusku-40005455” je to kategorie “zahranicni”, podkategorii “evropa” můžete
ignorovat. Každý článek patří právě do jedné hlavní kategorie.

Vytvořte klasifikátor, který bude na základě titulku/perexu nebo obojího články
klasifikovat do kategorií.

 
