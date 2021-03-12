#!/bin/bash

function pythonScieszka
{
  python3 -c "import sys; print(sys.executable)"
}

pwd
#src_venv
"$(pythonScieszka)" zlecenieWykonaniaBadania.py
#evince zlecenie.pdf
