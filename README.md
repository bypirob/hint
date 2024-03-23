# Hint ✨

Code suggestions from the terminal using AI (LLMs).

![hint cover image](https://github.com/bypirob/hint/blob/main/docs/cover.png?raw=true)

## Why I created Hint ✨ ?

Sometimes I need to run some CLI command that I don't remember exactly, because I don't use it too often to remember all the details.

Because of that, I have to go to the browser and find the documentation, so I lost time and focus.

Using `hint` command will speed your development workflow: just describe what you need in human language and you'll get an AI generated command suggestion.

> Remember that AI can generate errors or wrong commands, so if you are unsure, remember to always check the command.

## Installation

The installation process is a bit rudimentary, but we can improve it in the future!

### Setting up the tool

First, clone the repository and install the dependencies:

```
git clone git@github.com:bypirob/hint.git
python3 -m pip install pipenv
pipenv install
```

### Adding Anthropic API KEY

Create a `.env` file and add a `ANTHROPIC_API_KEY=your_api_key`.

[Anthropic API Key docs.](https://docs.anthropic.com/claude/docs/getting-access-to-claude#step-3-generate-an-api-key)


### Creating an alias

Edit your `.bashrc` or `.zshrc` file and add an alias to use it from anywhere:

```
alias hint="pipenv run python3 /path/to/hint/main.py"
```

### Examples

```
$ hint show the pods of a kubectl namespace
> command: kubectl get pods -n <namespace>

$ hint search in history the commands that start with ls
> command: history | grep ^ls

$ hint list the files from an aws s3 bucket called test
> command: aws s3 ls s3://test
```

## About Hint ✨

Because of this tool is for myself, I wanted something simple and cross-platform, so I've chosen Python because almost every developer system has it installed. I'm open to use any other language in the future if needed.

### Why open source?

I've created this tool for myself, but I think it can help others. I like privacy and I usually don't trust many tools, in particular those related to terminal where sensitive information is used, so I want a tool that is transparent.

### Models

Right now I've just implemented one LLM model: Haiku from Anthropic. I find it very powerful, it's fast, realiable and cheap ($0.25 for every million input tokens and $1.25 for every million output tokens).

I'll probably add support for local models using Ollama and OpenAI models like GPT-3.5-turbo, for testing purposes.