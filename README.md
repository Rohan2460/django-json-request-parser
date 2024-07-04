# JSON request parser middleware for Django

Simple Django middleware for parsing JSON data from HTTP request 
If the Content-Type of a POST request is "application/json", the JSON data is parsed and stored in the `HttpRequest.json` attribute.

## HttpRequest.json Data Types

- **Default (Not accessed):** `None`
- **Success:** `dict`
- **Error:** Empty `dict`

### Example

```python
from django.http import JsonResponse

def my_view(request):
    if request.method == "POST":
        data = request.json
        return JsonResponse({'message': 'JSON received', 'data': data.get('message')})
    else:
        return JsonResponse({'error': 'Invalid content type or method'}, status=400)
```

## Documentation

For more details on Django middleware, refer to the [Django Middleware Documentation](https://docs.djangoproject.com/en/5.0/topics/http/middleware/).

## License

This project is licensed under the MIT License.

---

Improve the code and adjust it according to your project's needs. Contributions and suggestions are welcome!
