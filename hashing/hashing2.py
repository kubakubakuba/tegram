from manim import *

#######################################
#comment this when doing a final render
#config.quality = "low_quality"
#######################################

class HashingWithDatabase2(Scene):
	def construct(self):
		user_table = MobjectTable(
			[
				[Text("Jméno"), Text("Heslo")],
				[Text("alice"),  Text("6a28415...", color=RED)],
				[Text("bob"),    Text("6a28415...", color=RED)],
				[Text("tegram", color="#529cc7"), Text("32f631d...", color="#529cc7")],
				[Text("rick"),   Text("1b4237f...")],
			],
			include_outer_lines=True
		)

		self.play(Create(user_table))
		self.wait(5)

		self.play(FadeOut(user_table))
