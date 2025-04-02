import requests
from typing import Any, Dict, Optional

# Placeholder classes for demonstration purposes.
class HttpRequest:
    def __init__(self, method: str, url: str, headers: Dict[str, str], payload: Any):
        self.method = method
        self.url = url
        self.headers = headers
        self.payload = payload

class HttpResponse:
    def __init__(self, status_code: int, body: str):
        self.status_code = status_code
        self.body = body

# Dummy implementation of RequestManager.
class RequestManager:
    def create_request(self, method: str, url: str, headers: Dict[str, str],
                       params: Dict[str, str], payload: Any) -> HttpRequest:
        # For a real-world scenario, params might be merged into the URL or used separately.
        # Here we simply pass payload along as data.
        return HttpRequest(method, url, headers, payload)

# Dummy implementation of ProxyServer.
class ProxyServer:
    def forward_request(self, request: HttpRequest) -> None:
        # In a real proxy, this would modify or route the request.
        # Here we simply log that the request is being "forwarded".
        print(f"[Proxy] Forwarding {request.method} request to {request.url}.")

    def handle_forwarding_error(self, error: Exception) -> None:
        # Log the error and decide what to do. For this dummy, we just print.
        print(f"[Proxy] Error during request forwarding: {error}")

class HTTPClient:
    """
    HTTPClient: Responsible for sending HTTP requests and receiving responses.
    
    Contracts:
      - Send HTTP requests (GET, POST) to target servers.
      - Receive HTTP responses from target servers.
    
    Collaborates with:
      - RequestManager: Constructs the request.
      - ProxyServer: Optionally forwards the request.
    """
    
    def __init__(self, request_manager: RequestManager, proxy_server: Optional[ProxyServer] = None):
        self.request_manager = request_manager
        self.proxy_server = proxy_server
        self.last_response: Optional[HttpResponse] = None

    def send_request(self, url: str, data: Any, req_type: str, headers: Dict[str, str]) -> None:
        """
        Sends an HTTP request to the target.
        
        Pre-conditions:
          - url is a valid URL.
          - req_type is a valid HTTP method (e.g., 'GET', 'POST').
        Post-conditions:
          - The request is sent and a response is received.
        """
        # 1. Construct an HTTP request using RequestManager.
        request = self.request_manager.create_request(req_type, url, headers, params={}, payload=data)
        
        # 2. If a ProxyServer is configured, forward the request.
        if self.proxy_server is not None:
            try:
                self.proxy_server.forward_request(request)
            except Exception as e:
                self.proxy_server.handle_forwarding_error(e)
                # Abort the sending process if forwarding fails.
                return
        
        # 3. Send the HTTP request and store the response.
        self.last_response = self._send_http(request)
    
    def receive_response(self) -> Optional[HttpResponse]:
        """
        Returns the last received HTTP response.
        """
        return self.last_response

    def get_status_code(self) -> int:
        """
        Returns the status code of the last received HTTP response.
        """
        if self.last_response is not None:
            return self.last_response.status_code
        raise RuntimeError("No response available. Send a request first.")

    def get_response_body(self) -> str:
        """
        Returns the body of the last received HTTP response.
        """
        if self.last_response is not None:
            return self.last_response.body
        raise RuntimeError("No response available. Send a request first.")

    def _send_http(self, request: HttpRequest) -> HttpResponse:
        """
        Sends the HTTP request using the requests library.
        In a production environment, additional error handling, timeouts,
        and logging would be recommended.
        """
        try:
            # For GET requests, send the payload as query parameters.
            if request.method.upper() == "GET":
                response = requests.get(request.url, headers=request.headers, params=request.payload)
            else:
                # For POST or other methods, send the payload as JSON.
                response = requests.request(request.method, request.url, headers=request.headers, json=request.payload)
            
            return HttpResponse(response.status_code, response.text)
        except Exception as e:
            # Here, we simply raise an error, but logging and error handling can be improved.
            raise RuntimeError(f"HTTP request failed: {e}")

# Example usage:
if __name__ == "__main__":
    # Create instances of the dummy collaborator classes.
    req_manager = RequestManager()
    proxy_server = ProxyServer()
    
    # Initialize the HTTPClient with a RequestManager and optionally a ProxyServer.
    client = HTTPClient(request_manager=req_manager, proxy_server=proxy_server)
    
    # Send a POST request to a sample API endpoint.
    test_url = "https://httpbin.org/post"  # httpbin.org is a testing service for HTTP requests.
    test_data = {"key": "value"}
    test_headers = {"Content-Type": "application/json"}
    
    client.send_request(test_url, data=test_data, req_type="POST", headers=test_headers)
    
    # Retrieve and print response details.
    response = client.receive_response()
    if response:
        print("Status Code:", client.get_status_code())
        print("Response Body:", client.get_response_body())
