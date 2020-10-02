LIST_CMD = "/System/Library/PrivateFrameworks/Apple80211.framework/Versions/A/Resources/airport scan"
IS_WIFI_OFF = "/System/Library/PrivateFrameworks/Apple80211.framework/Versions/A/Resources/airport -I"

TURN_WIFI_ON = "networksetup -setairportpower {port} on"
TURN_WIFI_OFF = "networksetup -setairportpower {port} off"

GET_WIFI_PORT = "networksetup -listallhardwareports"
CONNECT_TO_NETWORK = "networksetup -setairportnetwork {port} {ssid} {password}"

NETWORK_STATUS = "/System/Library/PrivateFrameworks/Apple80211.framework/Versions/A/Resources/airport -I"
