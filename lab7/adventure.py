room_list=[]
room=['Walkway: a long staircase to the apartment', 1, None, None, 7]
room_list.append(room)
room=['Kitchen: shelves full of foodstuffs and pans, very dirty', 3, 0, 4, 2]
room_list.append(room)
room=['Bathroom: all kinds of grossness, has a nice towel rack though', None, None, 1, None]
room_list.append(room)
room=['Andres\'s Room: All the other roommate rooms were hard to include.\n All cool guys though.', None, 1, None, None]
room_list.append(room)
room=['Living room: Dusty. Very old TV and printer. Could be cleaned.', None, 5, None, 1]
room_list.append(room)
room=['Sun room: My favorite room. Get stoned, zone out looking at the sunny trees.', 4, None, None, 6]
room_list.append(room)
room=['My room. Nice desk, chair, and TV stand. May have to pack up and move.', None, None, 5, None]
room_list.append(room)
room=['Laundry and Storage: have the box for my TV here.', None, None, 0, None]
room_list.append(room)

current_room=0
done=False

while not done:
	print(room_list[current_room][0])
	print()
	print('current room: ', current_room)
	direction=input('Where to go next? (Cardinal directions N, S, E, W)')
	if direction.upper() == 'N':
		if room_list[current_room][1]!=None:
			current_room=room_list[current_room][1]
		else:
			print('No room in that direction.')
			direction=input('Where to go next? (Cardinal directions N, S, E, W)')
	elif direction.upper() == 'S':
		if room_list[current_room][2]!=None:
			current_room=room_list[current_room][2]
		else:
			print('No room in that direction.')
			direction=input('Where to go next? (Cardinal directions N, S, E, W)')
	elif direction.upper() == 'E':
		if room_list[current_room][3]!=None:
			current_room=room_list[current_room][3]
		else:
			print('No room in that direction.')
			direction=input('Where to go next? (Cardinal directions N, S, E, W)')

	elif direction.upper() == 'W':
		if room_list[current_room][4]!=None:
			current_room=room_list[current_room][4]
		else:
			print('No room in that direction.')
			direction=input('Where to go next? (Cardinal directions N, S, E, W)')
	else:
		direction=input('Use only cardinal directions N, S, E, W: ')
	
