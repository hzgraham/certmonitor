def handle_uploaded_file(f):
    with open('dashboard/test.txt', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
