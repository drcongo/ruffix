# Ruffix

An extremely simple Sublime Text plugin to run `ruff --fix` on the current view.

I'll probably add deeper functionality in future like a sidebar context menu to fix an entire folder or project.

## Installation

Just use Package Control - `ctrl-shift-p`, select `Package Control: Install Package`, search for `ruffix`.

Note, this plugin does *not* install or maintain Ruff for you, you need to [do that yourself](https://docs.astral.sh/ruff/installation/) and ensure that `ruff` is on your `$PATH`. If you're able to run `ruff --fix some_file.py` on the command line, then this plugin should work.

## Usage

Open a Python file, open the command palette, type `ruffix` and hit return, or hit `super-option-r`.


## Disclaimer

I'm not affiliated with [Ruff](https://docs.astral.sh/ruff/), just a very enthusiastic user.


