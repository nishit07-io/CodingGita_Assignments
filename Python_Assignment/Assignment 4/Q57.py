extension = input().strip().lower()

match extension:
	case "py":
		print("Python File")
	case "txt":
		print("Text File")
	case "pdf":
		print("PDF File")
	case "jpg":
		print("Image File")
	case _:
		print("Unknown File Type")
