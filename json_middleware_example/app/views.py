from django.shortcuts import render
from django.http import JsonResponse


def index(request):
    if request.method == "POST":
        json_data = request.json
        print("Data from client: ", json_data)

        if json_data is None:
            data = {"status": "failed", "error": "Content-type: application/json required"}
            status_code = 400
        elif json_data == {}:
            data = {"status": "failed", "error": "Invalid data"}
            status_code = 400
        else:
            data = {"status": "ok", "data": json_data.get("data")}
            status_code = 200

        return JsonResponse(data, status=status_code)

    return render(request, "index.html")
