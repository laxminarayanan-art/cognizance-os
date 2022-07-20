from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "input.html")


def addition(request):

    num1 = request.POST['num1']
    num2 = request.POST['num2']

    if num1.isdigit() and num2.isdigit():
        first_num = int(num1)
        second_num = int(num2)
        r = first_num + second_num

        return render(request, "result.html", {"result": r})
    else:
        r = "please enter digit"
        return render(request, "result.html", {"result": r})


def subtraction(request):

    num1 = request.POST['num1']
    num2 = request.POST['num2']

    if num1.isdigit() and num2.isdigit():
        first_num= int(num1)
        second_num = int(num2)
        r = first_num - second_num

        return render(request, "result.html", {"result": r})
    else:
        r = "Please enter digit"
        return render(request, "result.html", {"result": r})


def multiplication(request):

    num1 = request.POST['num1']
    num2 = request.POST['num2']

    if num1.isdigit() and num2.isdigit():
        first_num= int(num1)
        second_num = int(num2)
        r = first_num * second_num

        return render(request, "result.html", {"result": r})
    else:
        r = "please enter digit"
        return render(request, "result.html", {"result": r})



def division(request):

    num1 = request.POST['num1']
    num2 = request.POST['num2']

    
    if num1.isdigit() and num2.isdigit():
        first_num = int(num1)
        second_num = int(num2)

        if second_num == 0:
            r = "(Zero divide error)zero cant be divided"
            return render(request, "result.html", {"result": r})
        else:
            r = first_num / second_num
            return render(request, "result.html", {"result": r})
    else:
        r = "please enter digit"
        return render(request, "result.html", {"result": r})