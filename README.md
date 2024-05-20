![Exemplo de aplicativo feito com Python e PySide6](https://justcode.com.br/wp-content/uploads/2024/05/app-python-pyside-qt.webp "Exemplo de aplicativo feito com Python e PySide6")

<br>

# Exemplo de como estruturar um projeto com Python e Qt

[![natorsc - app-python-qt](https://img.shields.io/static/v1?label=natorsc&message=app-python-qt&color=blue&logo=github)](https://github.com/natorsc/app-python-qt "Ir para o repositório.")
&emsp;
[![stars - app-python-qt](https://img.shields.io/github/stars/natorsc/app-python-qt?style=social)](https://github.com/natorsc/app-python-qt)
&emsp;
[![forks - app-python-qt](https://img.shields.io/github/forks/natorsc/app-python-qt?style=social)](https://github.com/natorsc/app-python-qt)

[![License MIT](https://img.shields.io/static/v1?label=License&message=MIT&color=blue)](https://badges.mit-license.org/)

[![pdm-managed](https://img.shields.io/badge/pdm-managed-blueviolet)](https://pdm-project.org)

## 📝 Descrição

Repositório exibe uma forma de estruturar um projeto que utiliza a linguagem de programação Python para criar um aplicativo com o binding PySide6 e toolkit gráfico Qt.

- [x] Realizar as traduções com o software Qt Linguist. `pyside6-linguist`.
- [x] Padronizar a geração de arquivos de tradução (`*.ts`). `pyside6-lupdate`.
- [x] Padronizar a compilação dos arquivos de tradução (`*.qm`). `pyside6-lrelease`.
- [x] Padronizar a compilação dos recursos (resources) `*.qrc`. `pyside6-rcc`.
- [x] Criar um binário/executável. `pyside6-deploy`.
- [x] Criar um pacote do Python (`*.tar.gz` e `*.whl`). `pdm build`.
- [x] Criar testes. `python -m unittest`.
- [x] Criar um [Github Actions](https://github.com/features/actions) (`deploy-nuitka.yaml`) para automatizar o processo de deploy com Nuitka.
- [x] Criar um Github Actions (`pdm-test-pypi.yaml`) para automatizar o envio do pacote python (`*.tar.gz` e `*.whl`) para o [https://test.pypi.org/](https://test.pypi.org/).

---

## 🛠 Tecnologias utilizadas

Até o presente momento as seguintes tecnologias são utilizadas na construção do projeto:

[![Python](https://img.shields.io/badge/-Python-blue?logo=python&logoColor=white)](https://www.python.org/ "Ir para o site.")
&emsp;
[![Qt](https://img.shields.io/badge/-Qt-blue?logo=qt&logoColor=white)](https://www.qt.io/ "Ir para o site.")
&emsp;
[![PySide6](https://img.shields.io/badge/-PySide6-blue?logo=pypi&logoColor=white)](https://pypi.org/project/PySide6/ "Ir para o PyPi.")
&emsp;
[![pdm-managed](https://img.shields.io/badge/pdm-managed-blue)](https://pdm-project.org "Ir para o pdm-project.org.")

---

## 🤓 Autor

Repositório feito com 💙 por [Renato Cruz](https://github.com/natorsc) 🤜🤛 Entre em contato!

[![Email](https://img.shields.io/badge/-Email-blueviolet?logo=gmail&logoColor=white)](mailto:natorsc@gmail.com "Enviar e-mail.")

Acompanhe conteúdos sobre programação e tecnologia em:

[![justcode.com.br](https://img.shields.io/badge/-justcode.com.br-grey?logo=wordpress&logoColor=white)](https://justcode.com.br/ "Acessar o justCode.")

Uma das playlist que costumo ouvir quando estou estudando ou "codando" 😁:

[![Spotify](https://img.shields.io/badge/-Spotify-darkgreen?logo=spotify&logoColor=white)](https://open.spotify.com/playlist/1xf3u29puXlnrWO7MsaHL5?si=A-LgwRJXSvOno_e6trpi5w&utm_source=copy-link "Acessar playlist.")

---

## 💝 Doações

Obrigado por sua doação, é através dela que consigo manter este conteúdo 😊.

### Buy me a coffee

[![Buy me a coffee](https://img.shields.io/badge/-Buy%20me%20a%20coffee-red?logo=buymeacoffee&logoColor=white)](https://www.buymeacoffee.com/natorsc "Ajude a manter este projeto com uma doação.")

<img alt="bmc-qrcode" src="https://justcode.com.br/wp-content/uploads/2024/05/bmc-qrcode.webp" title="Ajude a manter este projeto com uma doação." width="150"/>

### Ko-Fi

[![Ko-Fi](https://img.shields.io/badge/-Ko%20Fi-orange?logo=ko-fi&logoColor=white)](https://ko-fi.com/natorsc "Ajude a manter este projeto com uma doação.")

<img alt="ko-fi-qrcode" src="https://justcode.com.br/wp-content/uploads/2024/05/ko-fi-qrcode.webp" title="Ajude a manter este projeto com uma doação." width="150"/>

### Pix

<img alt="pix-qrcode" src="https://justcode.com.br/wp-content/uploads/2024/05/pix-qrcode.webp" title="Ajude a manter este projeto com uma doação." width="150"/>

**Chave**: `b1839493-2afe-484d-9272-82a3e402b36f`

---

## Extra

### Erros

Se ao executar o código for exibido o alerta:

```bash
qt.qpa.plugin: Could not find the Qt platform plugin "wayland" in ""
```

instale o pacote `qt6-wayland` na sua distribuição Linux.

### Qt

- [Blog](https://www.qt.io/blog).
- [Documentação Qt](https://doc.qt.io/).
- [Documentação Qt for Python](https://doc.qt.io/qtforpython-6/).

### KDE

- [Site oficial](https://kde.org/).
- [Blogs](https://blogs.kde.org/).
- [Adventures in Linux and KDE](https://pointieststick.com/).
- [KDE Human Interface Guidelines (HIG)](https://develop.kde.org/hig/).

### Ícones

- [Cuttlefish](https://develop.kde.org/docs/features/icons/). O Cuttlefish pode ser instalado através do pacote plasma-sdk.
- [Breeze (CDN)](https://cdn.kde.org/breeze-icons/icons.html).

### RADs

- [Qt Designer](https://doc.qt.io/qt-6/qtdesigner-manual.html).

### IDEs

- [https://www.qt.io/product/development-tools](https://www.qt.io/product/development-tools).

### Design

- [Qt Design Studio](https://www.qt.io/product/ui-design-tools).

---
