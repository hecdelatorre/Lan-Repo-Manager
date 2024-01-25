# LAN Repo Manager

LAN Repo Manager is a Python-based tool that simplifies the management of repositories on a local area network (LAN). It provides an easy-to-use interface to create project categories, repositories, list repositories, and manage categories.

## Prerequisites

- Python 3.x
- `repo_variables.json` file in the user's home directory (e.g., `~/repo_variables.json`). The file should be structured as follows:

```json
{
  PARENT_FOLDER: /path/to/parent/folder,
  IP_OR_HOSTNAME: server_hostname.local,
  USER: your_username,
  FOLDER_NAME: repos
}
```

**Note**: Ensure that the `repo_variables.json` file is located in the home directory.

## Installation

Install the required dependencies using the following command:

```bash
pip install -r requirements.txt
```

To generate a standalone executable, install PyInstaller:

```bash
pip install pyinstaller
```

Build the executable:

```bash
pyinstaller --onefile -n lan-repo-manager main.py
```

## Usage

1. Fill in the `repo_variables.json` file in your home directory with the appropriate values.

2. Run the main program:

```bash
./lan-repo-manager
```

3. Follow the on-screen instructions to create categories, repositories, list repositories, and manage categories.

## SSH Key Setup

To enable secure communication with the server, make sure you have an SSH key pair. If not, generate one using the following command:

```bash
ssh-keygen -t rsa -b 2048
```

Follow the prompts to generate the key pair. Once generated, copy the public key (`~/.ssh/id_rsa.pub`) and send it to the server administrator for authentication.

Add the public key to the server's authorized keys:

```bash
cat ~/.ssh/id_rsa.pub | ssh your_username@server_hostname.local 'cat >> ~/.ssh/authorized_keys'
```

**Note**: Replace `your_username` and `server_hostname.local` with your actual username and server hostname.

## Important Notes

- Ensure that the `repo_variables.json` file is correctly filled in with the appropriate values.
- The program manages repositories in the specified parent folder on the server, allowing users to organize and version control their projects easily.

This project is licensed under the GNU General Public License v3.0 (GPL-3.0). See the [LICENSE](LICENSE) file for details.
