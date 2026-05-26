from django.shortcuts import render

def gst_calculator(request):
    result = None

    if request.method == "POST":
        price = float(request.POST['price'])
        gst = float(request.POST['gst'])

        result = price + (price * gst / 100)

    return render(request, 'math.html', {'result': result})