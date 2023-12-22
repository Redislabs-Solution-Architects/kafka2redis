#! /bin/bash
python app/make_index.py
python app/ingest_data.py
flask run -p 5050 --host=0.0.0.0
