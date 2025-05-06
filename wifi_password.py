import subprocess

# Get all Wi-Fi profiles
meta_data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles'])

data = meta_data.decode('utf-8', errors="backslashreplace")
data = data.split('\n')

profiles = []

for i in data:
    if "All User Profile" in i:
        # Extract the profile name
        profile = i.split(":")[1].strip()
        profiles.append(profile)

print("{:<30}| {:<}".format("WiFi Name", "Password"))
print("-" * 50)

# For each profile, get the password
for profile in profiles:
    try:
        # Run the command to get profile details including the key
        result = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', profile, 'key=clear'])
        result = result.decode('utf-8', errors="backslashreplace")
        Z
        # Search for the password
        password_line = [line for line in result.split('\n') if "Key Content" in line]
        
        if password_line:
            password = password_line[0].split(":")[1].strip()
        else:
            password = "N/A"
        
        print("{:<30}| {:<}".format(profile, password))
    except subprocess.CalledProcessError:
        print("{:<30}| {:<}".format(profile, "Error retrieving password"))


