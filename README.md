# Skripty k videům pro Tegram Reels

Všechna videa jsou napsána v markdownu (mluvená část videa, může se trochu lišit of finální části).

Pro renderování videí je použit [manim](https://docs.manim.community/en/stable/index.html).

Doporučuji vytvořit python venv, pak spustit venv konzoli přes `source .venv/bin/activate`.

Kompilace manimu skriptu přes `python3 -m manim video.py`.

Pro rychlejší generaci doporučuji nastavit `config.quality = "low_quality"`, toto je při finálním renderu důležité zakomentovat, ať se video vyrenderuje v plné kvalitě.