import os
from dotenv import load_dotenv
from cli.menu import app
from core.logger import log_info

# Carrega variáveis de ambiente
load_dotenv()

BANNER = """
╔══════════════════════════════════╗
║         AEGIS FRAMEWORK          ║
║     Enterprise CLI Platform      ║
╚══════════════════════════════════╝
Version: 1.0.0
Plugins: 12 Loaded
Status: Ready
"""

if __name__ == '__main__':
    print(BANNER)
    log_info('Inicializando Aegis Hunter-X Core...')
    app()
