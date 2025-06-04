from django.shortcuts import render

# Create your views here.
def custom_page(request):
    return render(request, 'enigmaapp/custom_page.html')

def about(request):
    return render(request, 'enigmaapp/about_page.html')

def algorithms(request):
    return render(request, 'enigmaapp/algorithms_page.html')

def playground(request):
    encrypted_message = None  # Initialize the result variable

    if request.method == "POST":
        message = request.POST.get('message', '')  # Get message input
        shift = int(request.POST.get('shift', 0))  # Get shift input

        def caesar_cipher(text, shift):
            alphabet = 'abcdefghijklmnopqrstuvwxyz'
            result = ''
            for char in text:
                if char in alphabet:
                    index = alphabet.index(char)
                    new_index = (index + shift) % 26
                    result += alphabet[new_index]
                else:
                    result += char
            return result

        encrypted_message = caesar_cipher(message, shift)

    
    return render(request, 'enigmaapp/playground_page.html', {'encrypted_message': encrypted_message})


def history(request):
    return render(request, 'enigmaapp/history_page.html')
