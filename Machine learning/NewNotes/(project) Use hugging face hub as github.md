- Make sure your hugging face cli package is updated:
```python
pip install --upgrade huggingface_hub
```

- Login HF
```python
python -m pip install huggingface_hub
huggingface-cli login --token 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
```

- Create the model/dataset/space repo on [[Hugging face hub]] website. Add files in it on webpage or on terminal. 

- Set up
	- Enable larger than 5GB files. 
```python
git lfs install
huggingface-cli lfs-enable-largefiles .
```

- Cloning HF repo 
```shell
git clone https://huggingface.co/<your-username>/<your-model-name>
cd <your-model-id>
```

- Push files
```shell
git add .
git commit -m "First model version"  # You can choose any descriptive message
git push
```


