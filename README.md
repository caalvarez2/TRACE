# TRACE

TRACE (Targeted Reconnaissance for Advanced Content Exploitation) is a tool designed to support the Department of Defense (DoD) in ensuring the security and resilience of their technological systems. Developed for penetration testers in the Cyber Experimentation & Analysis Division (CEAD), TRACE automates critical steps in security testing, helping analysts identify vulnerabilities and assess risks efficiently. Its features include project collaboration, server-client architecture, user-role management, HTTP operations, and web tree navigation.


## Authors

- [@Cadena, Kevin](https://www.github.com/Peaches04)
- [@Peltshog, Deki](https://www.github.com/dekkip)
- [@Rojas, Sabas A](https://www.github.com/SabasRojas)
- [@Romero, Danilo](https://www.github.com/LinkXotica)
- [@Robles, Alan A](https://www.github.com/alanrobles02)
- [@Alvarez, Cesar A](https://www.github.com/caalvarez2)
- [@Donritchie, Ewane](https://www.github.com/Donritchie-E)



## Run Locally

Clone the project

```bash
  git clone https://github.com/caalvarez2/TRACE.git
```

Go to the project directory

```bash
  cd TRACE
```

Install dependencies

```bash
  Install npm
    On Windows (using Chocolatey): choco install nodejs
    On macOS (using Homebrew): brew install node
    For Linux (Debian/Ubuntu): sudo apt update && sudo apt install nodejs npm

  After installation, you can verify npm is installed by typing: npm -v
```
```bash
  Install python
    On Windows (using Chocolatey): choco install python
    On macOS (using Homebrew): brew install python
    For Linux (Debian/Ubuntu): sudo apt update && sudo apt install python3
```
```bash
  npm install svelte
```

Start the server
```bash
  Inside backend folder, uvicorn main:app --reload
```
```bash
  Inside the Trace-svelte, run npm run dev
```