import subprocess

subprocess.run(["python", "generate_data.py"])
subprocess.run(["python", "train_model.py"])
subprocess.run(["python", "predict.py"])
