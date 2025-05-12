@echo off
setlocal

set "arquivo=%~dp0readme.txt"

> "%arquivo%" (
  for /l %%i in (1,1,12) do echo Por favor, nos ajude, você é o único que restou.
)

start "" "%arquivo%"

:: Aguarda 5 segundos
timeout /t 5 /nobreak > nul

:: Fecha o Bloco de Notas (caso esteja aberto)
taskkill /im notepad.exe /f > nul 2>&1

::Roda o Exe
"%~dp0build\exe.win-amd64-3.12\Help.exe"

set "explicacao=%~dp0explicacao.txt"

> "%explicacao%" (
  echo Vamos explicar tudo à você
)

start "" "%explicacao%"

:: Aguarda 5 segundos
timeout /t 5 /nobreak > nul

:: Fecha o Bloco de Notas (caso esteja aberto)
taskkill /im notepad.exe /f > nul 2>&1

:: Depois que terminar, toca o vídeo
start "" "%~dp0final_video\video_sem_marca.mp4"
