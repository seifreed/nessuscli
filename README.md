<p align="center">
  <img src="https://img.shields.io/badge/nessuscli-Nessus%20REST%20CLI-blue?style=for-the-badge" alt="nessuscli">
</p>

<h1 align="center">nessuscli</h1>

<p align="center">
  <strong>Python client and CLI for Nessus Professional's REST API</strong>
</p>

<p align="center">
  <a href="https://github.com/seifreed/nessuscli"><img src="https://img.shields.io/badge/python-3.14%2B-blue?style=flat-square&logo=python&logoColor=white" alt="Python 3.14+"></a>
  <img src="https://img.shields.io/badge/license-MIT-green?style=flat-square" alt="MIT License">
  <a href="https://github.com/seifreed/nessuscli/stargazers"><img src="https://img.shields.io/github/stars/seifreed/nessuscli?style=flat-square" alt="GitHub Stars"></a>
  <a href="https://github.com/seifreed/nessuscli/issues"><img src="https://img.shields.io/github/issues/seifreed/nessuscli?style=flat-square" alt="GitHub Issues"></a>
</p>

---

## Overview

**nessuscli** is a Python library and command-line client for Nessus Professional's REST API. It uses a bundled API contract to expose 166 operations across 25 resources through both a dynamic client and generated typed wrappers.

### Key Features

| Feature | Description |
|---------|-------------|
| **Complete catalog CLI** | 25 Nessus resources and 166 catalog operations exposed as hierarchical commands |
| **Contract-driven** | API paths, methods, parameters, and generated wrappers come from `api_spec.json` |
| **Typed library** | Generated client classes with explicit operation signatures and docstrings |
| **Authentication** | Nessus API access/secret keys or a Nessus session token |
| **Request handling** | Path, query, JSON payload, raw body, multipart upload, and download support |
| **Cross-platform** | Python 3.14 on Windows, Linux, and macOS, including x64 and ARM |
| **Configuration** | TOML, environment variables, and command-line settings with predictable precedence |
| **Tested** | Real local HTTP integration tests, 100% test coverage, and static/security checks |

### Supported Data

```text
API responses       JSON, text, and bytes
File transfers      Multipart uploads and downloaded files
Configuration       TOML, environment variables, and CLI options
API surface         166 operations across 25 resources
```

---

## Installation

### From Source

```bash
git clone https://github.com/seifreed/nessuscli.git
cd nessuscli
python3.14 -m venv venv

# Linux/macOS
source venv/bin/activate

# Windows PowerShell
# .\venv\Scripts\Activate.ps1

pip install -e .
```

### Development Tools

```bash
pip install -e ".[dev]"
```

The runtime package has no third-party dependencies. Development dependencies are declared in the single `pyproject.toml` file.

---

## Quick Start

Configure Nessus Professional with API keys issued by Nessus:

```toml
[nessus]
base_url = "https://localhost:8834"
access_key = "your-access-key"
secret_key = "your-secret-key"
timeout = 30
verify_ssl = true
```

Then inspect the available resources and call an operation:

```bash
nessus --help
nessus resources
nessus scans --help
nessus scans details --scan-id 1
nessus scans list --folder-id 1
nessus scans create --uuid template-uuid --settings '{"name": "Example"}'
nessus policies export --policy-id 1 --output policy.pdf
nessus file upload --file policy.nessus
```

---

## Configuration

Configuration sources are evaluated in this order:

```text
Command-line options > environment variables > TOML file
```

The default configuration path is platform-specific. On Linux it is `~/.config/nessuscli/config.toml`; set `NESSUS_CONFIG` or use `--config` to choose another file.

| Setting | Environment variable | CLI option | Description |
|---------|----------------------|------------|-------------|
| `base_url` | `NESSUS_BASE_URL` | `--base-url` | Nessus server URL |
| `access_key` | `NESSUS_ACCESS_KEY` | `--access-key` | Nessus API access key |
| `secret_key` | `NESSUS_SECRET_KEY` | `--secret-key` | Nessus API secret key |
| `token` | `NESSUS_TOKEN` | `--token` | Nessus session token |
| `timeout` | `NESSUS_TIMEOUT` | `--timeout` | HTTP timeout in seconds |
| `verify_ssl` | `NESSUS_VERIFY_SSL` | `--insecure` | Disable TLS certificate verification when explicitly requested |
| Config file | `NESSUS_CONFIG` | `--config` | TOML configuration path |

Use `--insecure` only when the Nessus endpoint and network are trusted.

---

## Usage

### Command Line Interface

The root command accepts connection settings and exposes both the catalog and resource commands:

```console
nessus [OPTIONS] COMMAND
```

| Command | Description |
|---------|-------------|
| `nessus resources` | List all resources and their operations |
| `nessus <resource> --help` | List operations for one resource |
| `nessus <resource> <operation>` | Call an operation directly |
| `nessus call <resource> <operation>` | Call an operation using the generic compatibility command |

The available resource commands are `agent-groups`, `agents`, `editor`, `file`, `folders`, `groups`, `mail`, `migration`, `permissions`, `plugin-rules`, `plugins`, `policies`, `profiles`, `proxy`, `reports`, `scanners`, `scans`, `server`, `session`, `settings`, `software-update`, `terrascan`, `tokens`, `users`, and `was`.

Every operation supports these common arguments:

| Option | Description |
|--------|-------------|
| `--path JSON` | Path parameters as a JSON object |
| `--query JSON` | Query parameters as a JSON object |
| `--payload JSON` | JSON request payload |
| `--body JSON` | Raw JSON request body |
| `--file FILE` | File to upload |
| `--output FILE` | Destination for a downloaded response |
| `--arg NAME=VALUE` | Named parameter; JSON values are parsed automatically |
| `--help` | Show operation-specific options |

Parameters declared by the API contract are also available as named options. For example:

```bash
# Grouped parameters
nessus call scans list --query '{"folder_id": 1}'

# Named parameters and a download destination
nessus scans export-download --scan-id 1 --file-id 2 --output report.pdf

# Compatibility syntax for a path parameter
nessus call scans details --arg scan_id=1
```

### API Coverage

The bundled `src/nessuscli/api_spec.json` contract contains the complete catalog currently supported by the project: 166 operations in 25 resources. Run `nessus resources` to print the catalog, and use `<resource> --help` or `<resource> <operation> --help` to inspect exact parameters for any operation.

---

## Python Library

### Basic Usage

```python
from nessuscli import Settings, create_client

settings = Settings.from_sources()
client = create_client(settings)

scans = client.scans.list()
details = client.scans.details(scan_id=1)
```

The dynamic client also supports explicit resource and operation names:

```python
result = client.call("scans", "details", scan_id=1)
```

### Typed Client

Use the generated client when explicit signatures and operation docstrings are useful:

```python
from nessuscli import Settings, create_typed_client

settings = Settings.from_sources()
client = create_typed_client(settings)
details = client.scans.details(scan_id=1)
```

Downloads return bytes by default. Use the CLI `--output` option or the library's output path support to persist a downloaded response.

---

## Development and Quality

Run the project quality gates from the repository root:

```bash
black --check .
ruff check .
mypy .
pytest --cov=nessuscli --cov-report=term-missing --cov-fail-under=100
bandit -r src
pip-audit
```

The test suite uses real local HTTP integration paths and does not require Nessus credentials.

---

## PyPI Publishing (OIDC)

The repository publishes distributions through PyPI Trusted Publishing. The workflow uses GitHub Actions OIDC and does not require a `PYPI_API_TOKEN` secret.

Before the first release, add this trusted publisher in the PyPI project settings:

| Field | Value |
|-------|-------|
| Owner | `seifreed` |
| Repository | `nessuscli` |
| Workflow | `publish.yml` |
| Environment | `pypi` |

Update the version in `pyproject.toml`, create a GitHub release, and mark it as published. The `publish.yml` workflow builds the wheel and source distribution, then uploads both to PyPI using the OIDC identity.

---

## Requirements

- Python 3.14 or newer
- Nessus Professional with API access keys or a session token for live requests
- Runtime dependencies: none beyond the Python standard library
- Development tooling: available through the `dev` optional dependency in `pyproject.toml`

---

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/your-change`)
3. Run the complete quality gate locally
4. Commit your changes (`git commit -m 'Describe the change'`)
5. Push the branch (`git push origin feature/your-change`)
6. Open a Pull Request

---

## License

This project is licensed under the MIT license as declared in `pyproject.toml`.

**Repository:** [github.com/seifreed/nessuscli](https://github.com/seifreed/nessuscli)

---

<p align="center">
  <sub>Built for Nessus API automation and security workflows</sub>
</p>
