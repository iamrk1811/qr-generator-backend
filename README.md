# QR Generator

Help us to generate QR with given URL for our spaces

## Getting Started

Follow these instructions to set up the project locally.

### Prerequisites

- **Python 3.11**: Ensure Python is installed on your system. You can download it from [python.org](https://www.python.org/).
- **Git**: Used for version control. Install it from [git-scm.com](https://git-scm.com/).

### Installation

1. **Clone the repository**:
   ```bash
   git clone git@github.com:iamrk1811/qr-generator-backend.git
   cd your-repo-name
2. **Create virtualenv and run the application**
    ```
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    pip install -r requirements.txt
    pre-commit install
    uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
