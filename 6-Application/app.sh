#!/bin/bash

# Creates Streamlit configuration and launches app on port 8888
# Create Streamlit config directory
mkdir -p ~/.streamlit

# Create Streamlit configuration file
cat << EOF > ~/.streamlit/config.toml
[browser]
gatherUsageStats = false

[server]
port = 8888
enableCORS = false
enableXsrfProtection = false
address = "0.0.0.0"
headless = true

[theme]
primaryColor = "#2176AE"
backgroundColor = "#FFFFFF"
secondaryBackgroundColor = "#F0F2F6"
textColor = "#262730"
font = "sans serif"

[logger]
level = "info"
EOF

# Launch Streamlit app
cd "$(dirname "$0")"
streamlit run app.py
