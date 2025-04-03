import requests

class ProxyServer:
    def forward_request(self, request: HttpRequest) -> HttpResponse:
        # Log the intercepted request details.
        print(f"[Proxy] Intercepting {request.method} request to {request.url}")
        
        # Forward the request without modifying it.
        try:
            if request.method.upper() == "GET":
                # For GET requests, use the payload as query parameters.
                response = requests.get(request.url, headers=request.headers, params=request.payload)
            else:
                # forward the request body as JSON if applicable.
                response = requests.request(request.method, request.url, headers=request.headers, json=request.payload)
            
            print("[Proxy] Request forwarded successfully.")
            return HttpResponse(response.status_code, response.text, dict(response.headers))
        except Exception as error:
            self.handle_forwarding_error(error)
            raise RuntimeError("Proxy forwarding failed") from error

    def handle_forwarding_error(self, error: Exception) -> None:
        # Log the error details.
        print(f"[Proxy] Error during request forwarding: {error}")
