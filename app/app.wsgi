import os
import sys

sys.path.append(os.path.dirname(__file__))

from debtsapi import app

if __name__ == "__main__":
    app.run(debug=True)
