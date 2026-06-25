import typer
from rich.console import Console
from rich.markdown import Markdown
from core.logger import log_info, log_success, log_warning, log_error
from core.engine import HunterEngine

console = Console()
app = typer.Typer(help='Aegis Hunter-X CLI Platform')
engine = HunterEngine()

@app.command()
def doctor():
    """Verifica a saúde do sistema e dependências ativas"""
    log_info('Iniciando diagnóstico do sistema...')
    import sys
    import requests
    
    if sys.version_info >= (3, 11):
        log_success(f'Python Version OK: {sys.version.split()[0]}')
    else:
        log_warning('Recomenda-se Python 3.11+')
        
    if engine.api_key:
        log_success('LLM_API_KEY detectada no ambiente.')
    else:
        log_error('LLM_API_KEY ausente. Configure o arquivo .env.')
        
    log_success('Diagnóstico concluído. Status: Ready.')

@app.command()
def analyze(target: str = typer.Argument(..., help='Alvo ou contexto para análise')):
    """Envia um contexto para análise heurística do Hunter-X"""
    log_info(f'Iniciando módulo de análise para: {target}')
    result = engine.ask_llm(f'Analise o seguinte contexto/alvo sob a ótica de segurança: {target}')
    
    if result:
        console.print('\n')
        console.print(Markdown(result))
        console.print('\n')
        log_success('Relatório gerado com sucesso.')
    else:
        log_error('Falha ao gerar relatório de análise.')

@app.command()
def interactive():
    """Inicia o menu interativo padrão"""
    while True:
        console.print('\n[bold cyan]=== AEGIS HUNTER-X TOOLBOX ===[/bold cyan]')
        console.print('[1] Recon (Reconhecimento e Contexto)')
        console.print('[2] Analyze (Análise de Vulnerabilidades)')
        console.print('[3] Doctor (Health Check)')
        console.print('[4] Sair')
        
        choice = typer.prompt('Selecione uma opção', type=int)
        
        if choice == 1:
            ctx = typer.prompt('Insira os dados de recon (ex: headers, nmap output)')
            analyze(f'[RECON DATA] {ctx}')
        elif choice == 2:
            ctx = typer.prompt('Insira o código ou endpoint para análise')
            analyze(f'[VULN ANALYSIS] {ctx}')
        elif choice == 3:
            doctor()
        elif choice == 4:
            log_info('Encerrando Aegis Hunter-X. Stay safe.')
            break
        else:
            log_warning('Opção inválida.')
