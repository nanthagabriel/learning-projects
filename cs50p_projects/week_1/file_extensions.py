# - FILE EXTENSIONS
# User input of suffix extension type
file = input("File name: ").strip().lower()

# Jpeg and Jpg
if file.endswith("jpg") or file.endswith("jpeg"):
    print("image/jpeg")

# Gif
elif file.endswith("gif"):
    print("image/gif")

# Png
elif file.endswith("png"):
    print("image/png")

# Pdf
elif file.endswith("pdf"):
    print("application/pdf")

# Txt
elif file.endswith("txt"):
    print("text/plain")

# Zip
elif file.endswith("zip"):
    print("application/zip")

#  Other suffix or no suffix at all
else:
    print("application/octet-stream")