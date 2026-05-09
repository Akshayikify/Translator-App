from django.shortcuts import render
from translate import Translator
def translate_lang(request):
    translation=""
    if request.method=='POST':
        text=request.POST["Text"]
        language=request.POST["language"]
        translator=Translator(to_lang=language)
        translation=translator.translate(text)
    return render(request,'translator_app/index.html',{'translation':translation,'title':'home'})