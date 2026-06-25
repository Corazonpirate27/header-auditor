import requests
from rich.console import Console
from rich.table import Table

console = Console()

SECURITY_HEADERS = [
    "X-Frame-Options",
    "X-Content-Type-Options",
    "Content-Security-Policy",
    "Strict-Transport-Security",
    "Referrer-Policy",
    "Permissions-Policy"
]

def check_headers(url: str) -> dict:
    response = requests.get(url, timeout=5)
    return response.headers

def audit(url: str) -> None:
    console.print(f"\n[bold blue]Auditing {url}...[/bold blue]\n")
    headers = check_headers(url)
    table = Table(title="Security Headers Report")
    table.add_column("Header", style="cyan")
    table.add_column("Status", style="white")
    table.add_column("Risk", style="white")
    for header in SECURITY_HEADERS:
        if header in headers:
            table.add_row(header, "✅ Found", "None")
        else:
            table.add_row(header, "❌ Missing", "Vulnerable")
    console.print(table)

if __name__ == "__main__":
    url = input("Enter URL to audit: ")
    audit(url)



