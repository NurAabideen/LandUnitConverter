#!/usr/bin/env bash

# Copyright (c) 2021-2024 tteck
# Author: tteck (tteckster)
# License: MIT
# https://github.com/tteck/Proxmox/raw/main/LICENSE

source /dev/stdin <<< "$FUNCTIONS_FILE_PATH"
color
verb_ip6
catch_errors
setting_up_container
network_check
update_os

msg_info "Installing Dependencies"
$STD apt-get install -y curl
$STD apt-get install -y sudo
$STD apt-get install -y mc
$STD apt-get install -y ca-certificates
$STD apt-get install -y gnupg
msg_ok "Installed Dependencies"

msg_info "Setting up Node.js Repository"
mkdir -p /etc/apt/keyrings
curl -fsSL https://deb.nodesource.com/gpgkey/nodesource-repo.gpg.key | gpg --dearmor -o /etc/apt/keyrings/nodesource.gpg
echo "deb [signed-by=/etc/apt/keyrings/nodesource.gpg] https://deb.nodesource.com/node_20.x nodistro main" >/etc/apt/sources.list.d/nodesource.list
msg_ok "Set up Node.js Repository"

msg_info "Installing Node.js"
$STD apt-get update
$STD apt-get install -y nodejs
msg_ok "Installed Node.js"

msg_info "Installing n8n (Patience)"
$STD npm install --global patch-package
$STD npm install --global n8n
msg_ok "Installed n8n"

msg_info "Creating Service"
cat <<EOF >/etc/systemd/system/n8n.service
[Unit]
Description=n8n

[Service]
Type=simple
Environment=N8N_SECURE_COOKIE=false
Environment=WEBHOOK_URL=http://n8n.cybernur.com
Environment=N8N_HOST=n8n.cybernur.com
ExecStart=n8n start
[Install]
WantedBy=multi-user.target
EOF
$STD systemctl enable --now n8n
msg_ok "Created Service"

motd_ssh
customize

msg_info "Cleaning up"
$STD apt-get -y autoremove
$STD apt-get -y autoclean
msg_ok "Cleaned"
