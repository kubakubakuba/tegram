from manim import *

#######################################
# Comment this when doing a final render
# config.quality = "low_quality"
#######################################

class CryptographyComparison(Scene):
	def construct(self):
		# Symmetric Cryptography Animation

		# Introduce Alice and Bob with their labels
		alice_icon = SVGMobject("alice.svg").scale(0.8)
		bob_icon = SVGMobject("bob.svg").scale(0.8)
		alice_label = Text("Alice").next_to(alice_icon, DOWN)
		bob_label = Text("Bob").next_to(bob_icon, DOWN)
		symetric_cryptography = Text("Symetrická kryptografie", font_size=24)
		alice = VGroup(alice_icon, alice_label)
		bob = VGroup(bob_icon, bob_label)
		alice.to_edge(LEFT, buff=1)
		bob.to_edge(RIGHT, buff=1)
		symetric_cryptography.to_edge(DOWN)
		self.play(FadeIn(alice), FadeIn(bob), FadeIn(symetric_cryptography))
		self.wait(1)

		# Shared secret key
		secret_key_icon = SVGMobject("public_key.svg").set_color(YELLOW).scale(0.5)
		secret_key_label = Text("Sdílený tajný klíč", font_size=24)
		secret_key = VGroup(secret_key_icon, secret_key_label).arrange(DOWN, buff=0.1)
		secret_key.move_to(UP * 2)

		self.play(FadeIn(secret_key))
		self.wait(1)

		# Copy secret key to Alice and Bob
		alice_secret_key = secret_key_icon.copy().move_to(alice.get_center() + UP * 1.5)
		bob_secret_key = secret_key_icon.copy().move_to(bob.get_center() + UP * 1.5)
		self.play(
			TransformFromCopy(secret_key_icon, alice_secret_key),
			TransformFromCopy(secret_key_icon, bob_secret_key)
		)
		self.wait(1)

		# Alice wants to send a secret message
		message = Text("zpráva", color=BLUE).scale(0.70)
		self.play(Write(message))
		self.wait(1)

		self.play(
			ApplyMethod(message.next_to, alice, UP*3.5),
			run_time=1.5
		)
		
		# Alice encrypts the message with the secret key
		self.play(message.animate.set_color(YELLOW))
		lock_icon = SVGMobject("lock.svg").set_color(YELLOW).scale(0.25)
		lock_icon.next_to(message, LEFT)
		
		encrypted_message = VGroup(lock_icon, message)
		self.play(FadeIn(lock_icon))
		self.wait(1)

		# Arrow from Alice to Bob representing the encrypted message
		arrow_to_bob = Arrow(alice.get_right(), bob.get_left(), buff=0.5)
		ab_path = arrow_to_bob.copy().shift(UP * 0.5)
		message_path = arrow_to_bob.copy()
		self.play(
			GrowArrow(arrow_to_bob),
			MoveAlongPath(encrypted_message, ab_path),
			run_time=2
		)
		self.wait(1)

		# Bob decrypts the message using the secret key
		self.play(
			Indicate(bob_secret_key),
			bob_secret_key.animate.scale(1.2),
			run_time=1
		)
		self.play(bob_secret_key.animate.scale(1/1.2))
		self.wait(0.5)
		self.play(
			encrypted_message[1].animate.set_color(BLUE),
			FadeOut(encrypted_message[0])
		)
		decrypted_message = encrypted_message[1]
		
		self.play(
			ApplyMethod(decrypted_message.next_to, bob, UP*3.5),
			run_time=1.5
		)
		
		self.wait(1)

		# Clean up before asymmetric cryptography
		self.play(
			FadeOut(secret_key),
			FadeOut(alice_secret_key),
			FadeOut(bob_secret_key),
			FadeOut(decrypted_message),
			FadeOut(arrow_to_bob),
			FadeOut(message)
		)
		self.wait(1)

		# Asymmetric Cryptography Animation

		asymetric_cryptography = Text("Asymetrická kryptografie", font_size=24)
		asymetric_cryptography.to_edge(UP)
		self.play(ReplacementTransform(symetric_cryptography, asymetric_cryptography))

		# Bob's public and private keys
		public_key_icon = SVGMobject("private_key.svg").set_color(GREEN).scale(0.5)
		private_key_icon = SVGMobject("private_key.svg").set_color(RED).scale(0.5)
		public_key_label = Text("Bobův publickey", font_size=24)
		private_key_label = Text("Bobův privatekey", font_size=24)
		public_key = VGroup(public_key_icon, public_key_label).arrange(DOWN, buff=0.1)
		private_key = VGroup(private_key_icon, private_key_label).arrange(DOWN, buff=0.1)
		public_key.next_to(bob, UP, buff=0.5)
		private_key.next_to(bob, DOWN, buff=0.5)
		self.play(FadeIn(public_key), FadeIn(private_key))
		self.wait(1)

		# Alice wants to send a secret message
		message1 = Text("zpráva", color=BLUE).scale(0.70)
		message1.next_to(alice, UP)
		self.play(Write(message1))
		self.wait(1)

		# Alice uses Bob's public key to encrypt the message
		public_key_copy = public_key_icon.copy().move_to(alice.get_center() + UP*2.5)
		self.play(TransformFromCopy(public_key_icon, public_key_copy))
		self.wait(0.5)

		self.play(message1.animate.set_color(YELLOW))
		lock_icon = SVGMobject("lock.svg").set_color(YELLOW).scale(0.25)
		lock_icon.next_to(message1, LEFT)
		encrypted_message = VGroup(lock_icon, message1)
		self.play(FadeIn(lock_icon))
		self.play(FadeOut(public_key_copy))
		self.wait(1)

		# Arrow from Alice to Bob representing the encrypted message
		arrow_to_bob = Arrow(alice.get_right(), bob.get_left(), buff=0.5)
		channel = Text("Nezabezpečený kanál", font_size=18)
		channel.next_to(arrow_to_bob, UP)
		self.play(FadeIn(channel))

		# Create a new path slightly below the arrow
		message_path = arrow_to_bob.copy().shift(DOWN * 0.5)

		self.play(
			GrowArrow(arrow_to_bob),
			MoveAlongPath(encrypted_message, message_path),
			run_time=2
		)
		self.wait(1)

		# Bob decrypts the message using his private key
		self.play(
			Indicate(private_key_icon),
			private_key_icon.animate.scale(1.2),
			run_time=1
		)
		self.play(private_key_icon.animate.scale(1/1.2))
		self.wait(0.5)
		self.play(
			encrypted_message[1].animate.set_color(BLUE),
			FadeOut(encrypted_message[0])
		)
		self.wait(1)

		self.play(
			FadeOut(message1),
			FadeOut(channel),
			FadeOut(arrow_to_bob)
		)

		# Bob replies and wants to ensure authenticity
		bob_reply = Text("odpověď", color=BLUE).scale(0.70)
		bob_reply.next_to(bob, DOWN)
		self.play(Write(bob_reply))
		self.wait(1)

		# Bob uses his private key to sign the reply (digital signature)
		signature_icon = SVGMobject("signature.svg").set_color(RED).scale(0.5)
		signature_icon.next_to(bob_reply, LEFT)
		signed_message = VGroup(signature_icon, bob_reply)
		self.play(FadeIn(signature_icon))
		self.wait(1)

		# Arrow from Bob to Alice representing the signed message
		arrow_to_alice = Arrow(bob.get_left(), alice.get_right(), buff=0.5)
		signed_message_path = arrow_to_alice.copy().shift(UP * 0.5)
		self.play(
			GrowArrow(arrow_to_alice),
			MoveAlongPath(signed_message, signed_message_path),
			run_time=2
		)
		self.wait(1)

		# Alice uses Bob's public key to verify the signature
		public_key_copy = public_key_icon.copy().move_to(alice.get_center() + UP*2.5)
		self.play(TransformFromCopy(public_key_icon, public_key_copy))
		self.wait(0.5)
		self.play(Indicate(public_key_copy))
		self.wait(0.5)
		self.play(
			FadeOut(signature_icon),
			bob_reply.animate.set_color(GREEN)
		)
		self.wait(1)

		# Displaying the concept of digital signature
		signature_explanation = Text(
			"Digitální podpis zaručuje autenticitu a integritu",
			font_size=24
		)
		signature_explanation.to_edge(UP)
		self.play(ReplacementTransform(asymetric_cryptography, signature_explanation))
		self.wait(2)

		self.play(
			FadeOut(alice),
			FadeOut(bob),
			FadeOut(public_key),
			FadeOut(private_key),
			FadeOut(bob_reply),
			FadeOut(arrow_to_alice),
			FadeOut(public_key_copy)
		)

		# Mention HTTPS as an example
		https_example = Text(
			"HTTPS využívá asymetrickou kryptografii k zabezpečení komunikace",
			font_size=24
		)
		self.play(ReplacementTransform(signature_explanation, https_example))
		self.wait(2)
