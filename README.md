# BambooBotでバッテリーの残り容量を表示するレポジトリ

### インストール方法
```
git clone git@github.com:rb-sapiens/bamboobot_battery_display.git

sudo cp bamboobot_battery_display/display.service /etc/systemd/system/display.service
sudo systemctl daemon-reload
sudo systemctl enable display.service

sudo cp NotoSansMono-Bold.ttf /usr/share/fonts/truetype/noto/
```

### display.serviceの修正
User、Environment、ExecStartは環境に合わせて修正してください。
