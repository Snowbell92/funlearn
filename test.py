import os
for file in os.listdir("ExpressionOutput"):
	if file.endswith(".txt"):
		print(file)
		print(os.path.join("ExpressionOutput", file))