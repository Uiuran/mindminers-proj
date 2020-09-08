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
calculadora()

# Sumário mensal de renda e impostos
print(calculadora.summary)

# Evolução de operações, lucros e prejuízos
print(calculadora.serie)

# Outros dados
calculadora.load_dataset('another_data.csv')
calculadora()
...
```

or in the notebooks folder:

```bash
jupyter-notebook rendimento-absoluto.ipynb
```

## Demonstrative scripts, output data(.csv) and plots(.png)

See the notebook folder for that. The demonstrative script is a jupyter notebook since it allows for hover interativity with Plotly.

## Status

08-09-2020  Beta - (Projeto Concluído/Funcional)

03-09-2020  Alpha - (Parte1 - Calculadora)

## TODO
