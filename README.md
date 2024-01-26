# LAN Repo Manager

LAN Repo Manager is a command-line tool designed to help manage repositories and categories within a local area network (LAN).

## Prerequisites

- Python 3.x installed on your system
- `.repo_variables.json` file located in your home directory (`~/`)

## Setting Up Environment

1. **Environment Variables:**
   
   - Ensure that the `.repo_variables.json` file is located in your home directory (`~/`). This file contains configuration variables used by the program.
   
   - Example of `.repo_variables.json`
     
     ```json
     {
         PARENT_FOLDER: /path/to/parent/folder,
         IP_OR_HOSTNAME: server_hostname.local,
         USER: your_username,
         FOLDER_NAME: repos
     }
     ```

2. **Python Virtual Environment:**
   
   - Create a Python virtual environment to isolate dependencies:
     
     ```bash
     python3 -m venv env
     ```
   
   - Activate the virtual environment:
     
     ```bash
     . env/bin/activate
     ```

## Installing Dependencies

Install the required dependencies using pip:

```bash
pip install -r requirements.txt
```

## Building Executable

To build the executable file using PyInstaller, run the following command:

```bash
pip install pyinstaller
pyinstaller --onefile -n lan-repo-manager main.py
```

## SSH Public Key Setup

To add your SSH public key to the server computer in the LAN network, use the following command:

```bash
cat .ssh/id.pub | ssh <username>@<hostname> 'cat >> ~/.ssh/authorized_keys'
```

Replace `<username>` and `<hostname>` with your actual username and hostname.

## Git Configuration

On the server machine, set the default branch name to `main` using the following Git command:

```bash
git config --global init.defaultBranch main
```

## Usage Examples

### Git Global Setup

```bash
git config --global user.name 'Your Name' 
git config --global user.email 'your.email@example.com'
```

### Create a New Repository

```bash
git clone <username>@<hostname>:<parent_folder>/<folder_name>/test/test.git cd test git switch --create main touch README.md 
git add README.md git commit -m 'add README' 
git push --set-upstream origin main
```

### Push an Existing Folder

```bash
cd existing_folder 
git init --initial-branch=main 
git remote add origin <username>@<hostname>:<parent_folder>/<folder_name>/test/test.git 
git add . 
git commit -m 'Initial commit' 
git push --set-upstream origin main
```

### Push an Existing Git Repository

```bash
cd existing_repo 
git remote rename origin old-origin 
git remote add origin <username>@<hostname>:<parent_folder>/<folder_name>/test/test.git 
git push --set-upstream origin --all 
git push --set-upstream origin --tags
```

## License

This project is licensed under the GNU General Public License v3.0 (GPL-3.0).
