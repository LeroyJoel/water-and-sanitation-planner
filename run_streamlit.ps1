# Run Streamlit with the repo `src` folder added to PYTHONPATH so imports from
# the local package (src\water_sanitation_crew) work without installing the
# package. Use a proper virtual environment when possible, or run `python -m pip install -e .`

# Resolve absolute path to ./src
$src = Resolve-Path -Path "./src"

# Prepend src to PYTHONPATH for this process (PowerShell uses ; on Windows)
$env:PYTHONPATH = "$($src.Path)$([System.IO.Path]::PathSeparator)$env:PYTHONPATH"

Write-Host "Using PYTHONPATH: $env:PYTHONPATH"

# Launch Streamlit app
streamlit run "${src.Path}\water_sanitation_crew\streamlit_app.py"
