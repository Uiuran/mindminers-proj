# Test Project for Mind-Miners

## Installation

```python 
git clone https://github.com/Uiuran/mindminers-proj.git
cd ~/path/to/dir/mindminers-proj/
conda create --name calculadora python=3.6
conda activate calculadora
pip install . --use-feature=2020-resolver
```

## Usage

```python
import mmcalculadora as calc

calculadora=calc.IRCalculadora('data.csv')
calculadora=calculadora()

print(calculadora.summary)

calculadora.load_dataset('another_data.csv')
calculadora=calculadora()

print(calculadora.summary)
```

or in the notebooks folder:

```bash
jupyter-notebook rendimento-absoluto.ipynb
```

## Status

03-09-2020  Alpha - (Parte1 - Calculadora)

## TODO

Visualizações
