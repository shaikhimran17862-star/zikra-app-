[app]
title = Zikra AI
package.name = zikra
package.domain = org.zikra.ai
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json,wav,mp3
version = 1.0.0

# Requirements
requirements = python3,kivy,requests,urllib3,certifi,pyjnius,google-generativeai

# Permissions required for Zikra
android.permissions = INTERNET,SYSTEM_ALERT_WINDOW,FOREGROUND_SERVICE,BIND_ACCESSIBILITY_SERVICE,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE,RECORD_AUDIO,CALL_PHONE,CAMERA,POST_NOTIFICATIONS

# Target API levels for Realme C25
android.api = 33
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a, armeabi-v7a

# Foreground service setup
android.services = ZikraService:service.py
