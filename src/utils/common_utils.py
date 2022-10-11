from genericpath import exists
from operator import index
import yaml
import os
import shutil
import logging
import json

def read_params(config_path: str):
    with open(config_path) as yaml_file:
        config = yaml.safe_load(yaml_file)
    logging.info(f"read parameters")

    return config

def clean_prev_dirs_if_exists(dir_path: str):
    if os.path.isdir(dir_path):
        shutil.rmtree(dir_path)
    logging.info(f"cleaned existing artifacts directory at {dir_path}")
    

def create_dir(dirs: list):
    for dir_path in dirs:
        os.makedirs(dir_path, exist_ok=True)
    logging.info(f"created directory at {dir_path}")
    

def save_local_df(df, df_path, header=False):
    if header:
        new_cols = [col.replace(" ", "_") for col in df.columns]
        df.to_csv(df_path, index=False, header=new_cols)
        logging.info(f"dataframe saved at the at {df_path} with new headers")
    else:
        df.to_csv(df_path, index=False)
        logging.info(f"dataframe saved at the at {df_path}")

def save_reports(file_path: str, report: dict):
    with open(file_path, "w") as f:
        json.dump(report, f, indent=4)
    logging.info(f"dreports saved at  at {file_path}")

    
    