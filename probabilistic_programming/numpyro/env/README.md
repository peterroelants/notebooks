# Python Environment

## Local conda environment

The Miniconda environment can be build and activated locally if you have conda installed by:
```
conda env create --file ./env/conda_env.yml
conda activate numpyro
```

And can be cleaned up afterwards with:
```
conda deactivate && conda remove --name numpyro --all
```


### Updating

To list outdated packages you can use `pip list --outdated` and `conda update --all --dry-run --channel conda-forge` in the activated environment.
