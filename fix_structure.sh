#!/usr/bin/env bash
set -e

# 1. Ensure we’re in the repo root:
#    this folder must contain your sportai_suite/ directory.
echo "Working directory: $(pwd)"

# 2. Move ai_modules into sportai_suite/ if it isn’t there already
if [ ! -d "sportai_suite/ai_modules" ] && [ -d "ai_modules" ]; then
  mv ai_modules sportai_suite/
  echo "➜ Moved ai_modules → sportai_suite/ai_modules"
fi

# 3. Add __init__.py files so Python treats them as packages
touch sportai_suite/__init__.py
touch sportai_suite/ai_modules/__init__.py
echo "➜ Created __init__.py in sportai_suite/ and ai_modules/"

# 4. Normalize your main app filename
#    Rename any file starting with "main" to main_app.py
for f in sportai_suite/main*.py; do
  if [[ "$f" != "sportai_suite/main_app.py" ]]; then
    mv "$f" sportai_suite/main_app.py
    echo "➜ Renamed $f → sportai_suite/main_app.py"
    break
  fi
done

# 5. Inject the “path hack” at top of main_app.py so ai_modules is on PYTHONPATH
MAIN=​sportai_suite/main_app.py
if ! grep -q "BASE_DIR" "$MAIN"; then
  sed -i '1i\
import os, sys\n\
# ensure this directory is on Python’s import path\n\
BASE_DIR = os.path.dirname(__file__)\n\
if BASE_DIR not in sys.path:\n\
    sys.path.insert(0, BASE_DIR)\n' "$MAIN"
  echo "➜ Injected import-path hack into main_app.py"
fi

# 6. Verify imports line up
#    (Quick check—no action needed if these lines exist:)
grep -q "from ai_modules.demand_forecasting import DemandForecaster" "$MAIN" \
  && echo "✔ demand_forecasting import OK" \
  || echo "⚠ missing demand_forecasting import"

# 7. Install requirements (adjust path if your requirements.txt is elsewhere)
pip install -r sportai_suite/requirements.txt

echo "✅ Structure fixed! Now run:"
echo "   cd $(pwd) && streamlit run sportai_suite/main_app.py"
