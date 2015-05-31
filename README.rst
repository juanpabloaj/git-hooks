=========
git-hooks
=========

Show useful hooks by language and hook name.

Install
=======

::

    pip install git-hooks

Usage
=====

List hooks availables for some language

::

    git hooks node


Show hook

::

    git hooks node pre-commit


Install hook

::

    git hooks node pre-commit > .git/hooks
    chmod u+x .git/hooks/pre-commit

Contribute
==========

Add hooks to `githook/hooks` directory.

