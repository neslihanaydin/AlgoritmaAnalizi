def identity_matris(n):
	myMatrix = []
	for i in range(n):
		myMatrix.append([])
		for j in range(n):
			myMatrix[i].append(0)


def invert_matris(A, tol = None):
	k = 1
	n = len(A)
	BM = A #copy_matris(A)
	I = identity_matris(n)
	IM = I #copy_matris(I)
	
	indices = list(range(n))
	
	for fd in range(n):
		fdScalar = 1.0/BM[fd][fd]
		for j in range(n):
			BM[fd][j] *= fdScalar
			IM[fd][j] *= fdScalar
		for i in indices[0:fd]+indices[fd+1:]:
			crScalar = BM[i][fd]
			for j in range(n):
				BM[i][j] = BM[i][j] - crScalar*BM[fd][i]
				I[i][j] = I[i][j] - crScalar*I[fd][i]
				k += 1
	return IM,k

matris = [1,2,5,6]
print ( invert_matris(matris))
			
