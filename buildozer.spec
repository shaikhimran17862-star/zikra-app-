[app]
title = Zikra AI
package.name = zikra
package.domain = org.zikra.ai
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json,wav,mp3
version = 1.0.0

# Requirements
requirements = python3,kivy,requests,urllib3,certifi,pyjnius,google-generativeai,plyer

# Permissions required for Zikra
android.permissions = INTERNET,CAMERA,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE,RECORD_AUDIO,SYSTEM_ALERT_WINDOW,FOREGROUND_SERVICE,BIND_ACCESSIBILITY_SERVICE

# Target API levels for Realme C25
android.api = 33
android.minapi = 21
android.ndk = 25b
android.build_tools_version = 33.0.2
android.archs = arm64-v8a
android.accept_sdk_licenses = True

# Foreground service setup
android.services = ZikraService:service.py
