# ThreatGraph Inspector: Code & Config Vulnerability Visualizer

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![AI Generated](https://img.shields.io/badge/Content-AI_Generated-brightgreen.svg?style=flat&labelColor=0078D4)

## Architecture Overview & Problem Statement

### The Challenge
Modern software systems are complex, integrating vast quantities of code, diverse configuration files, and numerous third-party dependencies. Traditional security scanning tools often produce fragmented, textual reports that, while comprehensive in data, fail to provide the contextual visualization necessary to understand the intricate relationships between identified vulnerabilities. This leads to analysis paralysis, inefficient prioritization, and slower remediation cycles, leaving organizations exposed to unaddressed risks stemming from secrets, misconfigurations, and known CVEs buried deep within their codebase and operational configurations.

### The Solution: ThreatGraph Inspector
ThreatGraph Inspector addresses this critical gap by providing an elite, enterprise-grade graphical interface for comprehensive vulnerability visualization. It employs a sophisticated multi-engine analysis pipeline capable of parsing and interpreting both application source code and a wide array of configuration files (e.g., YAML, JSON, INI, `.env`).

At its core, ThreatGraph Inspector constructs a dynamic **dependency and data flow graph**, illuminating the propagation pathways of vulnerabilities. This visual representation transcends static reports, allowing security professionals to intuitively grasp the impact of a compromised secret, the cascading effect of a misconfiguration, or the blast radius of a known CVE across the entire project ecosystem. The Python-based backend performs deep static analysis, while the interactive Tkinter GUI frontend serves as a "single pane of glass," offering an intuitive platform for threat intelligence, risk assessment, and accelerated remediation.

## Features

*   **Comprehensive Multi-Source Scanning**: Automatically detects secrets (e.g., API keys, credentials), identifies critical misconfigurations (e.g., exposed services, insecure defaults), and maps known CVEs within both application source code and diverse configuration files (YAML, JSON, XML, INI, .env, etc.).
*   **Interactive Visual Graphing**: Generates dynamic dependency and data flow graphs that illustrate the interconnectedness of files, components, and identified vulnerabilities, enabling intuitive risk pathway analysis and impact assessment.
*   **Contextual Risk Dashboards**: Presents high-level risk summaries, vulnerability density maps, and trend analysis, offering actionable insights for strategic security posture management and resource allocation.
*   **Granular Visual Diffing**: Provides side-by-side visual diffs highlighting vulnerable code/config sections, changes over time, and the precise location of identified issues, accelerating root cause analysis.
*   **Intelligent Remediation Suggestions**: Offers context-aware, actionable remediation guidance and best practices directly within the interface, accelerating the vulnerability resolution process and improving developer efficiency.
*   **Deep Dive File Explorer**: An integrated, interactive file explorer facilitates seamless navigation through project directories, allowing users to select and analyze specific files, directories, or entire repositories with drag-and-drop simplicity.

## Quick Start

Get ThreatGraph Inspector up and running on your local machine.

### Prerequisites

*   Python 3.8+
*   `git` command-line tool

### Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-org/ThreatGraph-Inspector.git
    cd ThreatGraph-Inspector
    ```

2.  **Create and activate a virtual environment (recommended):**
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows: .venv\Scripts\activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

### Usage

Once installed, launch the graphical application:

```bash
python gui_app.py
```

## Example Telemetry Output

Upon successful launch, the console will display:

```
Launched visual GUI application window [Tkinter]
```

This indicates the ThreatGraph Inspector's interactive GUI application window is now active and ready for use.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.