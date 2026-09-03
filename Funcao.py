def transpor_acorde(acorde, semitons):
	notas = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
	if not isinstance(acorde, str):
		raise TypeError("O acorde deve ser uma string.")

	acorde = acorde.upper()

	if acorde not in notas:
		raise ValueError("Informe uma nota válida, como C, D# ou A.")

	return notas[(notas.index(acorde) + semitons) % len(notas)]