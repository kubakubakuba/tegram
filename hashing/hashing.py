from manim import *

#######################################
#comment this when doing a final render
#config.quality = "low_quality"
#######################################

class HashingWithDatabase(Scene):
	def construct(self):
		title1 = Text("Hashování").scale(0.8)
		self.play(Write(title1))
		self.wait(2)
		self.play(FadeOut(title1))

		unhashed_passwords = MobjectTable(
			[
				[Text("Jméno"), Text("Heslo")],
				[Text("alice"), Text("heslo123")],
				[Text("bob"),   Text("heslo123")],
				[Text("tegram", color="#529cc7"), Text("tegram123", color="#529cc7")],
				[Text("rick"),  Text("dQw4w9WgXcQ")],
			],
			include_outer_lines=True
		)

		self.play(Create(unhashed_passwords))
		self.wait(3)

		self.play(FadeOut(unhashed_passwords))

		title2 = Text("Hashovací funkce", color=BLUE).scale(0.8)
		self.play(Write(title2))
		self.wait(2)

		password_text = Text("tegram123", color=YELLOW).scale(0.7).shift(UP)
		hash_text = Text("32f631d176675707d3392c35f50bf13d", color=GREEN).scale(0.7).shift(DOWN)

		self.play(Write(password_text))
		self.wait(2)
		self.play(Transform(password_text, hash_text))
		self.wait(3)

		self.play(FadeOut(password_text), FadeOut(hash_text))

		different_password = Text("Tegram123", t2c={"T": RED}, color=YELLOW).scale(0.7).shift(UP)
		different_hash = Text("cba83f01d76fcbbead1c5e27481b942e", color=GREEN).scale(0.7).shift(DOWN)

		self.play(Write(different_password))
		self.wait(2)
		self.play(Transform(different_password, different_hash))
		self.wait(3)

		self.play(FadeOut(different_password), FadeOut(different_hash), FadeOut(title2))

		user_table = MobjectTable(
			[
				[Text("Jméno"), Text("Heslo")],
				[Text("alice"),  Text("6a28415...")],
				[Text("bob"),    Text("6a28415...")],
				[Text("tegram", color="#529cc7"), Text("32f631d...", color="#529cc7")],
				[Text("rick"),   Text("1b4237f...")],
			],
			include_outer_lines=True
		)

		self.play(Create(user_table))
		self.wait(3)

		self.play(FadeOut(user_table))

		title4 = Text("Salted hashing", color=BLUE).scale(0.8)
		self.play(Write(title4))
		self.wait(2)

		salt_explanation = Text(
			"Salt: náhodná data přidaná k heslu", color=GREEN
		).scale(0.7).shift(UP)

		example_salt = Text("tegram123 + salt -> Nový Hash", t2c={"salt": RED}, color=YELLOW).scale(0.7).shift(DOWN)

		self.play(Write(salt_explanation))
		self.wait(2)
		self.play(Write(example_salt))
		self.wait(3)

		self.play(FadeOut(title4), FadeOut(salt_explanation), FadeOut(example_salt))

		salted_table = MobjectTable(
			[
				[Text("Username"), Text("Salt"), Text("Password (Hash)")],
				[Text("alice"), Text("f0b1"), Text("c1f6dcbf...")],
				[Text("bob"), Text("e9a8"), Text("7a91e28e...")],
				[Text("tegram", color="#529cc7"), Text("c7f9", color="#529cc7"), Text("4fd61f32...", color="#529cc7")],
				[Text("rick"), Text("a0c2"), Text("a1832edf...")],
			],
			include_outer_lines=True
		)

		self.play(Create(salted_table))
		self.wait(3)

		self.play(FadeOut(salted_table))

		title6 = Text("Kontrola úniku hesel:", color="#529cc7").scale(0.8).shift(UP)

		haveibeenpwned = Text("haveibeenpwned.com", color=ORANGE).scale(0.8).shift(DOWN)
		self.play(Write(title6), Write(haveibeenpwned))
		self.wait(3)

		self.play(FadeOut(title6), FadeOut(haveibeenpwned))
