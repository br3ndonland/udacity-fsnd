# Udacity

## Full-Stack Web Developer nanodegree (FSND)
The Full-Stack Web Developer nanodegree was co-created by Udacity, Amazon, GitHub, AT&T, and Google. The program teaches skills including Python programming, JavaScript and AJAX for front-end development, back-end databases, and Linux server deployment.

I am logging my code and progress with Jupyter notebook files.

Setup: for more, see [br3ndonland_computing_setup.mdown](https://github.com/br3ndonland/general/blob/master/br3ndonland_computing_setup.mdown)

* [Anaconda](https://docs.anaconda.com/anaconda/install/)
    - jupyter notebook
        + [jupyter-themes](https://github.com/dunovank/jupyter-themes)
            * `pip install jupyterthemes`
            * mods: `jt -t chesterish -f ubuntu -fs 14 -altp -tfs 16 -nf sourcesans -nfs 16 -ofs 12 -cellw 88% -T`
            * shutdown jupyter notebook kernel, clear browser cache, restart browser, restart jupyter notebook
        + [jupyter version control with nbdime](http://nbdime.readthedocs.io/en/latest/)
            * terminal: `pip install nbdime` (may already be installed through anaconda. to check, enter `conda list` at the command line).
            * `nbdime config-git --enable --global` (can also enable for individual repositories)
            * Add [jupyter .gitignore](https://github.com/jupyter/notebook/blob/master/.gitignore) to directory (or to $HOME/.config/git/ignore for global configuration), to avoid recognizing notebook checkpoint files.
