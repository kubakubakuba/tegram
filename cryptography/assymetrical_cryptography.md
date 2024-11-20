Už jste někdy slyšeli o asymetrické kryptografii? Dnes na ni narazíme prakticky všude, kde je potřeba zapezpečit nějaké citlivé informace.

Na rozdíl od symetrické kryptografie, kde se pro šifrování a dešifrování používá stejný klíč, asymetrická kryptografie pracuje s dvěma různými klíči – veřejným a soukromým. Veřejný klíč je k dispozici každému, zatímco soukromý klíč si jeho vlastník musí pečlivě chránit.

Představme si, že Alice chce poslat Bobovi tajnou zprávu. Aby zajistila, že nikdo kromě Boba zprávu nepřečte, využije Bobův veřejný klíč, který je dostupný všem. Zprávu zašifruje pomocí tohoto klíče a pošle ji Bobovi. Nyní už zprávu může dešifrovat pouze Bob, a to za pomoci svého soukromého klíče, který má jen on.

Ale co když chce Bob odpovědět a zároveň Alici přesvědčit, že zpráva skutečně pochází od něj? Bob může k zašifrování použít svůj soukromý klíč a Alice použije jeho veřejný klíč, aby zprávu dešifrovala. Tím je zaručeno, že zpráva opravdu pochází od Boba, protože pouze on má přístup ke svému soukromému klíči.

Tato technika nejen že umožňuje šifrování a dešifrování zpráv, ale také poskytuje důležité vlastnosti, jako je autenticita (Alice ví, že je zpráva od Boba) a integrita (zpráva nebyla cestou změněna). Této technice ověřování se také říká digitální podpis.

Jedním z běžných příkladů použití asymetrické kryptografie je protokol HTTPS, který šifruje komunikaci mezi vaším prohlížečem a webovými servery. V tomto případě jsou veřejné a soukromé klíče používány k zabezpečení přenosu citlivých informací, jako jsou hesla nebo platební údaje.