import sys

# We can directly instantiate connectionpool because we only need is_same_host
# Let's bypass urllib3 __init__ by extracting the is_same_host logic to test

from urllib.parse import urlparse
import socket

def _normalize_host(host, scheme):
    if host.startswith("[") and host.endswith("]"):
        host = host[1:-1]
    if scheme in ("http", "https"):
        host = host.lower()
    return host

def get_host(url):
    p = urlparse(url)
    return p.scheme or None, p.hostname or None, p.port or None

port_by_scheme = {"http": 80, "https": 443}

class DummyPool:
    def __init__(self, scheme, host, port):
        self.scheme = scheme
        self.host = host
        self.port = port

    def is_same_host(self, url, host_check=False):
        if url.startswith("/"):
            return True

        scheme, host, port = get_host(url)
        if host is not None:
            host = _normalize_host(host, scheme=scheme)

        # Use explicit default port for comparison when none is given
        if self.port and not port:
            port = port_by_scheme.get(scheme)
        elif not self.port and port == port_by_scheme.get(scheme):
            port = None

        if (scheme, host, port) == (self.scheme, self.host, self.port):
            return True

        if host_check and host is not None and self.host is not None:
            try:
                host_ip = socket.gethostbyname(host)
                self_host_ip = socket.gethostbyname(self.host)
                if (scheme, host_ip, port) == (self.scheme, self_host_ip, self.port):
                    return True
            except socket.error:
                pass

        return False

pool = DummyPool("http", "localhost", 80)
print(f"Same string, default host_check: {pool.is_same_host('http://localhost:80/')}")
print(f"Diff string, default host_check: {pool.is_same_host('http://127.0.0.1:80/')}")
print(f"Diff string, host_check=True: {pool.is_same_host('http://127.0.0.1:80/', host_check=True)}")

pool_ip = DummyPool("http", "127.0.0.1", 80)
print(f"Diff string 2, host_check=True: {pool_ip.is_same_host('http://localhost:80/', host_check=True)}")
