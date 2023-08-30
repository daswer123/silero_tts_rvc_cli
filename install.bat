@echo off

python -m venv venv
call venv/scripts/activate

pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
pip install -r requerments.txt

python dowload_rvc_base.py