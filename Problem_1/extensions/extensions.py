file_name = input("File name: ")
file_name = file_name.lower()
file_name = file_name.replace(" ", "")
# Subtrings images
substring_gif = ".gif"
substring_jpg = ".jpg"
substring_jpeg = ".jpeg"
substring_png = ".png"
# Substrings aplicattion
substring_pdf = ".pdf"
substring_txt = ".txt"
substring_zip = ".zip"
substring_bin = ".bin"

if substring_gif in file_name:
    print("image/gif")
elif substring_jpg in file_name:
    print("image/jpeg")
elif substring_jpeg in file_name:
    print("image/jpeg")
elif substring_png in file_name:
    print("image/png")
elif substring_pdf in file_name:
    print("application/pdf")
elif substring_txt in file_name:
    print("text/plain")
elif substring_zip in file_name:
    print("application/zip")
elif substring_bin in file_name:
    print("application/octet-stream")
else:
    print("application/octet-stream")