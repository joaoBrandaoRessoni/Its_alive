from cx_Freeze import setup, Executable

setup(
    name="Help",  # Nome do projeto (qualquer um)
    version="1.0",
    description="Simulação para aula de SO",
    executables=[Executable("virus.py", target_name="Help.exe")]
)