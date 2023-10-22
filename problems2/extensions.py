def main():
    user_input=input("File name: ")
    input_formatted=user_input.lower().strip()
    print(extension(input_formatted))

def extension(filename):
    if filename.endswith(".gif"):
        return "image/gif"
    elif filename.endswith(".jpg") or filename.endswith(".jpeg") :
        return "image/jpeg"
    elif filename.endswith(".png"):
        return "image/png"
    elif filename.endswith(".pdf"):
        return "application/pdf"
    elif filename.endswith(".txt"):
        return "text/plain"
    elif filename.endswith(".zip"):
        return "application/zip"
    else:
        return "application/octet-stream"

main()