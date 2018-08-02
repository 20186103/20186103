varA=15
varB=5
if type(varA)==str or type(varB)==str:
	print('string involved')
elif varA>varB:
	print('Bigger')
elif varA<varB:
	print('smaller')
else:
	print('equal')
