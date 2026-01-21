# Install
```
pip install poetry
```

```
pip install requirements.txt
```

# Run
```
fastapi dev src/main.py
```

## Run with Uvicorn
```
poetry run uvicorn src.main:app --reload
```

# Test
```
poetry run pytest
```