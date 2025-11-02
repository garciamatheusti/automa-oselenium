# Este estudo ainda está em andamento, iniciei o projeto a alguns meses e durante estudos conheci outras tecnologias que seriam mais interessantes, então acharão bugs, atualizarei sempre que possível.
# main.py
import time
from selenium.common.exceptions import NoSuchElementException
from utils.drivers import iniciar_driver
from utils.profiles import criar_perfil, remover_perfil
from utils.loggers import configurar_logger
from config import VIDEO_URL, WAIT_TIME, VIDEO_WATCH_TIME, CYCLE_DELAY

logger = configurar_logger()

def esperar_e_atualizar(driver):
    """Verifica se o vídeo carregou, caso contrário atualiza a página."""
    max_tentativas = 3
    for tentativa in range(max_tentativas):
        try:
            driver.find_element("tag name", "video")
            return True
        except NoSuchElementException:
            logger.warning(f"Tentativa {tentativa + 1}/{max_tentativas} - Página não carregada. Atualizando...")
            driver.refresh()
            time.sleep(WAIT_TIME)
    return False

def iniciar_video(driver):
    """Inicia e silencia o vídeo."""
    body = driver.find_element("tag name", "body")
    body.send_keys("k")  # Play
    time.sleep(1)
    body.send_keys("m")  # Mute

def ciclo_execucao():
    """Executa um ciclo completo de abertura, reprodução e fechamento."""
    perfil1 = criar_perfil()
    perfil2 = criar_perfil()
    perfil3 = criar_perfil()
    perfil4 = criar_perfil()
    try:
        driver1 = iniciar_driver(perfil1)
        driver2 = iniciar_driver(perfil2)
        driver3 = iniciar_driver(perfil3)
        driver4 = iniciar_driver(perfil4)

        for d in [driver1, driver2]:
            d.get(VIDEO_URL)
            esperar_e_atualizar(d)

        time.sleep(WAIT_TIME)

        iniciar_video(driver1)
        iniciar_video(driver2)

        logger.info("Reproduzindo vídeos por alguns segundos, aqui começar a achar a primeira problemática contra a IA do google")
        time.sleep(VIDEO_WATCH_TIME)

        driver1.quit()
        driver2.quit()
        driver3.quit()
        driver4.quit()
    finally:
        remover_perfil(perfil1)
        remover_perfil(perfil2)
        remover_perfil(perfil3)
        remover_perfil(perfil4)
        logger.info("Perfis removidos e drivers encerrados.")

def main():
    logger.info("Iniciando automação Chrome")
    while True:
        ciclo_execucao()
        logger.info(f"Aguardando {CYCLE_DELAY} segundos antes do próximo ciclo, o ideal é ficar de olho no tempo e sempre mudar essa variável para mais integridade contra a IA")
        time.sleep(CYCLE_DELAY)

if __name__ == "__main__":
    main()
