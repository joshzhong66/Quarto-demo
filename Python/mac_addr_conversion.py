# 输入的 MAC 地址列表
mac_addresses = [
    "00-14-22-01-23-45",
    "00:14:22:01:23:45"
]

# MAC 地址转换逻辑
def convert_mac_address(mac_address):
    cleaned_mac = mac_address.replace("-", "").replace(":", "")
    format1 = cleaned_mac[:2] + "-" + cleaned_mac[2:4] + "-" + cleaned_mac[4:6] + "-" + cleaned_mac[6:8] + "-" + cleaned_mac[8:10] + "-" + cleaned_mac[10:12]
    format2 = cleaned_mac[:2] + ":" + cleaned_mac[2:4] + ":" + cleaned_mac[4:6] + ":" + cleaned_mac[6:8] + ":" + cleaned_mac[8:10] + ":" + cleaned_mac[10:12]
    format3 = cleaned_mac[:2] + cleaned_mac[2:4] + "-" + cleaned_mac[4:8] + "-" + cleaned_mac[8:12]
    format4 = cleaned_mac.upper()
    return format1, format2, format3, format4

# 运行转换并显示结果
results = [convert_mac_address(mac) for mac in mac_addresses]

# 输出转换结果
for result in results:
    print(result)
