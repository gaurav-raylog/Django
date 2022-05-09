# importing django httpResponse module to send a response
from django.http import HttpResponse
# importing render module to render the actual HTML file on home path
from django.shortcuts import render

# home path


def home(request):
    # rendering the actualy HTML file on the path of home
    return render(request, 'index2.html')

# remove punctuation path


def analyze(request):
    # getting the text from HTML file
    user_text = request.POST.get('text', 'default') 

    # getting the checkbox info from HTML file
    remove_punc = request.POST.get('removepunc', 'off')
    full_caps = request.POST.get('fullycaps', 'off')
    line_remover = request.POST.get('lineremover', 'off')
    charcounter = request.POST.get('charcounter', 'off')
    wordcounter = request.POST.get('wordcounter', 'off')

    # removing puncuation marks if user checked it
    if remove_punc == "on":
        # punctuation values
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""

        # running for loop to iterate user_text into analyzed
        for char in user_text:
            if char not in punctuations:
                analyzed = analyzed + char

        # parameters
        params = {'purpose': 'Removed Punctuation', 'analyzed_text': analyzed}

        # rendering the analyze2.html file
        return render(request, 'analyze2.html', params)

    # elif for capitalize property
    elif(full_caps == "on"):
        analyzed = ""

        # running for loop to capitalize each value in user_text
        for char in user_text:
            analyzed = analyzed + char.upper()

        # parameters
        params = {'purpose': 'Change to Uppercase', 'analyzed_text': analyzed}

        # rendering the analyze2.html file
        return render(request, 'analyze2.html', params)

    # elif for removing line property
    elif(line_remover == "on"):
        analyzed = ""

        # for loop to remove new line in user_text
        for char in user_text:
            if char != '\n':
                analyzed = analyzed + char

        # parameters
        params = {'purpose': 'Line Removed', 'analyzed_text': analyzed}

        # rendering the analyze2.html file
        return render(request, 'analyze2.html', params)

    # elif for char counter property
    elif(charcounter == "on"):
        analyzed = len(user_text)

        # parameters
        params = {'purpose': 'Character Counter', 'analyzed_text': 'Number of Characters: ' + str(analyzed)}

        # rendering the analyze2.html file
        return render(request, 'analyze2.html', params)

    # elif for word counter property
    elif(wordcounter == "on"):
        analyzed = len(user_text.split())

        # parameters
        params = {'purpose': 'Character Counter', 'analyzed_text': 'Number of Words: ' + str(analyzed)}

        # rendering the analyze2.html file
        return render(request, 'analyze2.html', params)

    # rendering error message if user did not checked any box
    else:
        return HttpResponse("Please check the box to analyze text.")
