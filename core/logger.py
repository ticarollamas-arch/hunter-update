from rich.console import Console
from rich.theme import Theme

custom_theme = Theme({
    'info': 'cyan',
    'success': 'green',
    'warning': 'yellow',
    'error': 'red bold'
})
console = Console(theme=custom_theme)

def log_info(msg: str):
    console.print(f'[info][+] {msg}[/info]')

def log_success(msg: str):
    console.print(f'[success][✓] {msg}[/success]')

def log_warning(msg: str):
    console.print(f'[warning][!] {msg}[/warning]')

def log_error(msg: str):
    console.print(f'[error][-] {msg}[/error]')
