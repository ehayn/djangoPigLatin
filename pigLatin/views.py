from django.http import HttpResponse
from django.shortcuts import render

def home(request):
	return render(request, 'home.html')
	
def about(request):
	return render(request, 'about.html')
	
def translate(request):
	original = request.GET['originaltext']
	translation = ''
	for word in original.split():
		if word[0] in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
			translation += word
			translation += 'way '
		else:
			#consonant
			translation += word[1:]
			translation += word[0] + 'ay '
	return render(request, 'translate.html', {'original':original, 'translation':translation})