a, b, c = map(int, input().split())

if b**2 - 4 * a * c > 0:
	x1 = int((-b + (b**2 - 4 * a * c)**0.5) // 2 // a)
	x2 = int((-b - (b**2 - 4 * a * c)**0.5) // 2 // a)
	print('Two different roots x1=', x1,' , x2=', x2, sep='')
		
elif b**2 - 4 * a * c == 0:
	x = int( -b // 2 // a )
	print("Two same roots x=", x, sep='')
	
else:
	print("No real root")
