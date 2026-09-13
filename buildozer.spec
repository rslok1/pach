[app]
title = Капучинатор
package.name = capuchinator
package.domain = org.fixiki
source.dir = .
source.include_exts = py,png,jpg,jpeg,mp3,wav
version = 0.1
requirements = python3,pygame
orientation = landscape
fullscreen = 1

[buildozer]
log_level = 2
warn_on_root = 1

[android]
fullscreen = 1
android.archs = arm64-v8a
android.api = 33
android.minapi = 21
android.accept_sdk_license = True

# Жёстко задаем проверенные пути GitHub Runner, чтобы Buildozer не искал несуществующие папки
android.sdk_path = /usr/local/lib/android/sdk
android.ndk_path = /usr/local/lib/android/sdk/ndk/25.2.9519653
