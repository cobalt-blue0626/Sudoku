base=[1,2,3,4,5,6,7,8,9]
# sudoku=input("Please input the sudoku question: ")
sudoku=[[[0,4,0],[8,0,7],[2,0,0]],
		[[2,1,0],[0,0,0],[8,0,0]],
		[[0,0,0],[0,9,0],[4,0,1]],
		[[3,0,0],[0,0,5],[7,0,6]],
		[[0,0,2],[7,0,8],[5,0,0]],
		[[9,0,5],[6,0,0],[0,0,4]],
		[[5,0,1],[0,6,0],[0,0,0]],
		[[0,0,4],[0,0,0],[0,2,7]],
		[[0,0,9],[7,0,8],[0,5,0]]]
sudoku_row=[]
for i in [0,3,6]:
	for j in range(3):
		row=sudoku[i][j]+sudoku[i+1][j]+sudoku[i+2][j]
		sudoku_row.append(row)
# print(sudoku_row)
sudoku_column=[]
for i in range(len(sudoku_row[0])):
	column=[]
	for j in range(len(sudoku_row)):
		column+=[sudoku_row[j][i]]
	sudoku_column.append(column)
# print(sudoku_column)
sudoku_chunk=[]
for i in sudoku:
	chunk=[]
	for j in i:
		chunk+=j
	sudoku_chunk.append(chunk)
# print(sudoku_chunk)
#====================================================
def chunk_base(chunk_number):
	result=set(base)-(set(sudoku_chunk[chunk_number])-{0})
	return list(result)
def empty_location(chunk_number):
	empty_loc=[]
	for row in range(3):
		for column in range(3):
			if sudoku[chunk_number][row][column]==0:
				location=((chunk_number%3)*3+column,(chunk_number//3)*3+row)
				empty_loc+=[location]
	return list(set(empty_loc))
def location_base(location_tuple):
	x,y=location_tuple
	chunk_number=x//3+(y//3)*3
	chunk_b=set(chunk_base(chunk_number))
	location_b=chunk_b-(set(sudoku_row[y])-{0})-(set(sudoku_column[x])-{0})
	return list(location_b)
def permutation(lst):
    if len(lst) == 0:
        return []
    if len(lst) == 1:
        return [lst] 
    l=[] 
    for i in range(len(lst)):
       m = lst[i]
       remLst = lst[:i] + lst[i+1:] 
       for p in permutation(remLst):
           l.append([m] + p)
    return l
#====================================================
#print(empty_location(0))
all_chunk_base_name=["chunk0_base","chunk1_base","chunk2_base","chunk3_base","chunk4_base","chunk5_base","chunk6_base","chunk7_base","chunk8_base"]
all_chunk_base=[]
def all_chunk_base_per(n):
	chunkn_base=permutation(chunk_base(n))
	for empty in empty_location(n):#[(2, 0), (0, 2), (1, 1), (2, 1)]
		empty_po=empty_location(n).index(empty)
		location_b=location_base(empty)
		for base in permutation(chunk_base(n)):
			#print(base,empty_po,location_b)
			if not (base[empty_po] in location_b) and (base in chunkn_base):
				chunkn_base.remove(base)
	return chunkn_base
for n in range(9):
	all_chunk_base.append(all_chunk_base_per(n))
all_chunk_base_dic=dict(zip(all_chunk_base_name,all_chunk_base))
#====================================================
def copi(lis):
	new_one=[]
	for r in lis:
		row1=[]
		for e in r:
			row1+=[e]
		new_one.append(row1)
	return new_one
sudoku_solution_row=copi(sudoku_row)
def sudoku_solution_col(a):
	sudoku_solution_column=[]
	for i in range(len(a[0])):
		column=[]
		for j in range(len(a)):
			column+=[a[j][i]]
		sudoku_solution_column.append(column)
	return sudoku_solution_column


def place_the_sol(n,chunkn_sol):
	global sudoku_solution_row
	for po in empty_location(n):#[(2, 0), (0, 2), (1, 1), (2, 1)]
		x,y=po# x=2, y=0
		i=empty_location(n).index(po)
		sudoku_solution_row[y][x]=chunkn_sol[i]


def valid_or_not(sudoku_solution_r):
	t_f=True
	for j1 in sudoku_solution_r:
		for i1 in [1,2,3,4,5,6,7,8,9]:
			if j1.count(i1)>1:
				t_f=False
	for j2 in sudoku_solution_col(sudoku_solution_r):
		for i2 in [1,2,3,4,5,6,7,8,9]:
			if j2.count(i2)>1:
				t_f=False
	return t_f
#print(sudoku_row)
i=0
ans=[]
for chunk0_sol in all_chunk_base_dic["chunk0_base"]:
	if ans!=[]:
		break
	sudoku_solution_row=copi(sudoku_row)
	place_the_sol(0,chunk0_sol)
	true_false=valid_or_not(sudoku_solution_row)
	#print(0)
	if true_false:
		for chunk1_sol in all_chunk_base_dic["chunk1_base"]:
			if ans!=[]:
				break
			sudoku_solution_row=copi(sudoku_row)
			place_the_sol(0,chunk0_sol)
			place_the_sol(1,chunk1_sol)
			true_false=valid_or_not(sudoku_solution_row)
			#print(1)
			if true_false:
				for chunk2_sol in all_chunk_base_dic["chunk2_base"]:
					if ans!=[]:
						break
					sudoku_solution_row=copi(sudoku_row)
					#print(123456,sudoku_solution_row)
					place_the_sol(0,chunk0_sol)
					place_the_sol(1,chunk1_sol)
					place_the_sol(2,chunk2_sol)
					true_false=valid_or_not(sudoku_solution_row)
					#print(2)
					#print(sudoku_solution_row)
					if true_false:
						for chunk3_sol in all_chunk_base_dic["chunk3_base"]:
							if ans!=[]:
								break
							sudoku_solution_row=copi(sudoku_row)
							place_the_sol(0,chunk0_sol)
							place_the_sol(1,chunk1_sol)
							place_the_sol(2,chunk2_sol)
							place_the_sol(3,chunk3_sol)
							true_false=valid_or_not(sudoku_solution_row)
							#print(3)
							if true_false:
								for chunk4_sol in all_chunk_base_dic["chunk4_base"]:
									if ans!=[]:
										break
									sudoku_solution_row=copi(sudoku_row)
									place_the_sol(0,chunk0_sol)
									place_the_sol(1,chunk1_sol)
									place_the_sol(2,chunk2_sol)
									place_the_sol(3,chunk3_sol)
									place_the_sol(4,chunk4_sol)
									#print(4)
									true_false=valid_or_not(sudoku_solution_row)
									if true_false:
										for chunk5_sol in all_chunk_base_dic["chunk5_base"]:
											if ans!=[]:
												break
											sudoku_solution_row=copi(sudoku_row)
											place_the_sol(0,chunk0_sol)
											place_the_sol(1,chunk1_sol)
											place_the_sol(2,chunk2_sol)
											place_the_sol(3,chunk3_sol)
											place_the_sol(4,chunk4_sol)
											place_the_sol(5,chunk5_sol)
											#print(5)
											#print(sudoku_solution_row)
											true_false=valid_or_not(sudoku_solution_row)
											if true_false:
												for chunk6_sol in all_chunk_base_dic["chunk6_base"]:
													if ans!=[]:
														break
													sudoku_solution_row=copi(sudoku_row)
													place_the_sol(0,chunk0_sol)
													place_the_sol(1,chunk1_sol)
													place_the_sol(2,chunk2_sol)
													place_the_sol(3,chunk3_sol)
													place_the_sol(4,chunk4_sol)
													place_the_sol(5,chunk5_sol)
													place_the_sol(6,chunk6_sol)
													#print(6)
													true_false=valid_or_not(sudoku_solution_row)
													if true_false:
														for chunk7_sol in all_chunk_base_dic["chunk7_base"]:
															if ans!=[]:
																break
															sudoku_solution_row=copi(sudoku_row)
															place_the_sol(0,chunk0_sol)
															place_the_sol(1,chunk1_sol)
															place_the_sol(2,chunk2_sol)
															place_the_sol(3,chunk3_sol)
															place_the_sol(4,chunk4_sol)
															place_the_sol(5,chunk5_sol)
															place_the_sol(6,chunk6_sol)
															place_the_sol(7,chunk7_sol)
															#print(7)
															true_false=valid_or_not(sudoku_solution_row)
															if true_false:
																for chunk8_sol in all_chunk_base_dic["chunk8_base"]:
																	if ans!=[]:
																		break
																	sudoku_solution_row=copi(sudoku_row)
																	place_the_sol(0,chunk0_sol)
																	place_the_sol(1,chunk1_sol)
																	place_the_sol(2,chunk2_sol)
																	place_the_sol(3,chunk3_sol)
																	place_the_sol(4,chunk4_sol)
																	place_the_sol(5,chunk5_sol)
																	place_the_sol(6,chunk6_sol)
																	place_the_sol(7,chunk7_sol)
																	place_the_sol(8,chunk8_sol)
																	#print(8)
																	true_false=valid_or_not(sudoku_solution_row)
																	i+=1
																	#print(i)
																	if true_false:
																		ans=list(sudoku_solution_row)
																		#print(ans)
																		#print("Finish")
print("The question: ")
for i in sudoku_row:
	print(i)
print("The answer: ")
for i in ans:
	print(i)



















