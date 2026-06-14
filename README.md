# fluxcomatfluxcoarse

Overview of the FLUXCOM Exercise for FLUXCOARSE

This exercise is based on work by Anya Fries:

- <https://github.com/anyafries/FLUXtrapolation>
- <https://arxiv.org/abs/2605.19812>


# Setup and Installation

If you are already familiar with python, you can set up the Python environment and run the code in any way you like. The required packages are listed in the `pixi.toml` file.

I recommend using `pixi`, as it should make the setup process easier, particularly if you are new to python.

## Install `pixi`
---

First, install `pixi`. Quick installation instructions for each operating system are below. Full installation instructions are available [here](https://pixi.prefix.dev/latest/installation/#__tabbed_1_1).

#### Linux and macOS

To install `pixi`, run the following command in your terminal:

```sh
curl -fsSL https://pixi.sh/install.sh | sh
```

If your system does not have `curl`, you can use `wget` instead:

```sh
wget -qO- https://pixi.sh/install.sh | sh
```

#### Windows

Download and run the [Windows installer](https://github.com/prefix-dev/pixi/releases/latest/download/pixi-x86_64-pc-windows-msvc.msi).

Alternatively, you can install `pixi` from PowerShell with:

```sh
powershell -ExecutionPolicy Bypass -c "irm -useb https://pixi.sh/install.ps1 | iex"
```


## Set Up the Environment
---

Once `pixi` is installed, open a terminal and [clone](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository?tool=webui&platform=windows) this repository to your local machine:

```sh
git clone https://github.com/jnelson18/fluxcomatfluxcoarse.git
```

and navigate to the project directory:

```sh
cd fluxcomatfluxcoarse
```

Once in the project directory, install the environment with:

```sh
pixi install
```

## Download Data
---

There is a simple script to download all the example site data.

From the project directory, run:

```sh
pixi run python download_data.py
```

This may take a few minutes, but will put all the files exactly where they need to go. If your download gets interupted, just restart it and the script will skip any files that already exist.

Alternatively, you can download the data directly from [here](https://nextcloud.bgc-jena.mpg.de/s/wjZzy8BCE7KagEQ).

If downloading manually, place all `.csv` files in the following directory:

```text
data/sites/
```

The example scripts expect the site data to be in this location.

## Running the Notebook
---

The environment should now be ready and you can run the exercise.

From the project directory, launch the notebook with:

```sh
pixi run jupyter lab exercise.ipynb
```

Jupyter Lab should open in your default web browser ready to go. You may need to pull the latest changes on the day of the course, but this will not affect the environment or data downloads.















