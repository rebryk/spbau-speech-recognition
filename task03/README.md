# Instruction

1. `docker build -f Dockerfile -t ctc:last`
2. Run a container from the built image
2. Upload VCTK-Corpus to `/workspace/data/`
3. Put `gen.py` to `/workspace/data/` and run it with `python gen.py`
4. Start to train the model by executing the next command <br> ```python deepspeech.pytorch/train.py --train-manifest data/train.csv --val-manifest data/val.csv```

For more information visit [deepspeech.pytorch](https://github.com/SeanNaren/deepspeech.pytorch)
