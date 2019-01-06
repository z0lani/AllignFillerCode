while autoallign:

	sensor1 = getsensor1() #(returns boolean)
	sensor2 = getsensor2() #(returns boolean)
	sensor3 = getsensor3() #(returns boolean)
	sensor4 = getsensor4() #(returns boolean)
	trigger = gettrigger()

	if not sensor1 and not sensor2 and not sensor3 and not sensor4:  	#1
		pass	#listen for sensor activity
	if not sensor1 and not sensor2 and not sensor3 and sensor4: 		#2
		pass	#turn left until state four
	if not sensor1 and not sensor2 and sensor3 and not sensor4:  		#3
		pass	#turn right until state four
	if not sensor1 and not sensor2 and sensor3 and sensor4: 			#4
		pass#while sensor1 and sensor2 and not sensor3 and not sensor4:
				#if trigger:
					#placeGamePiece()
				#if not sensor1 and not sensor2 and not sensor3 and not sensor4:
					#turn 180
	if not sensor1 and sensor2 and not sensor3 and not sensor4: 		#5
		pass	#turn left until state six -> state four
	if not sensor1 and sensor2 and not sensor3 and sensor4: 			#6
		pass	#turn left until state four
	if not sensor1 and sensor2 and sensor3 and not sensor4: 			#7
		pass	#turn right until state four
	if not sensor1 and sensor2 and sensor3 and sensor4: 				#8
		pass	#turn right until state four~~~calibrate
	if sensor1 and not sensor2 and not sensor3 and not sensor4: 		#9
		pass	#turn right until state eleven -> state four
	if sensor1 and not sensor2 and not sensor3 and sensor4: 			#10
		pass	#turn left until state four
	if sensor1 and not sensor2 and sensor3 and not sensor4:  			#11
		pass	#turn right until state four
	if sensor1 and not sensor2 and sensor3 and sensor4: 				#12
		pass	#turn left until state four~~~calibrate
	if sensor1 and sensor2 and not sensor3 and not sensor4: 			#13
		pass	#reverse until state sixteen
	if sensor1 and sensor2 and not sensor3 and sensor4: 				#14
		pass	#turn left until state four~~~>90 turn
	if sensor1 and sensor2 and sensor3 and not sensor4: 				#15
		pass	#turn right until state four~~~>90 turn
	if sensor1 and sensor2 and sensor3 and sensor4:	 					#16
		pass	#turn ____ until state four
				#facing perpendicular to retro tape line