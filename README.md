# DeepTrack SW Skills

Central repository for reusable skills and CLI tooling.

## Installation with npx

The expected workflow is to install skills from a remote GitLab repository directly into the local repository where you want to use them.

Base command:

```bash
npx skills add <gitlab-repository>
```

If you want to install a specific skill:

```bash
npx skills add <gitlab-repository> --skill <skill-name>
```

Example:

```bash
npx skills add https://gitlab.com/deeptrack1/sw/tools/deeptrack-sw-skills.git
```

Example installing a single skill:

```bash
npx skills add https://gitlab.com/deeptrack1/sw/tools/deeptrack-sw-skills.git --skill update-changelog
```

## Installation destination

By default, skills are installed in:

```text
.agents/skills/
```

Example result:

```text
my-local-repo/
└── .agents/
    └── skills/
        ├── update-changelog/
        └── manage_documentation/
```


## Requirements

- Node.js 18 or higher
- Access to the remote GitLab repository

### Installing Node.js

Using **nvm** (recommended):

```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.1/install.sh | bash
source ~/.bashrc
nvm install 18
nvm use 18
```

Verify the installation:

```bash
node --version
```
